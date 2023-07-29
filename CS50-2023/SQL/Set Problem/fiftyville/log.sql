-- checks occurrences on the day and address of the incident
select * from crime_scene_reports where day = 28 and month = 07 and year = 2021 and street = 'Humphrey Street';

    -- result: 
        --Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time - each of their interview transcripts mentions the bakery.


-- checks interviws that mention bakery
select * from interviews where transcript like '%bakery%';

    -- result:
        --161|Ruth|2021|7|28|Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.
        --162|Eugene|2021|7|28|I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.
        --163|Raymond|2021|7|28|As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket.


-- check security footage
select * from bakery_security_logs where day = 28 and month = 07 and year = 2021 and hour = 10 and minute > 24;

    --result:
        --268|2021|7|28|10|35|exit|1106N58


-- return thief name 
select name from people where passport_number in (
            select passport_number from passengers as ps 
            join flights as fl on ps.flight_id = fl.id 
            where fl.id is (
                select id from flights 
                where day = 29 
                and month = 07 
                and year = 2021   
                and origin_airport_id is(
                select id from airports 
                where city = 'Fiftyville' 
                ) order by hour limit 1)) 
        and phone_number in (
            select caller from phone_calls 
            where day = 28 
            and month = 07 
            and year = 2021 
            and duration < 60)
        and name in (
            select name from people 
            where license_plate in(
                select license_plate from bakery_security_logs 
                where activity = 'exit' 
                and day = 28 
                and month = 07 
                and year = 2021 
                and hour = 10 
                and minute between 15 and 25))        
        and name in (
            select name from people as pp 
            join bank_accounts as ba on pp.id = ba.person_id
            join atm_transactions as at on ba.account_number = at.account_number
            where at.day = 28
            and at.month = 07
            and at.year = 2021
            and at.transaction_type = 'withdraw'
        );    
        


--return airport destination
select city from airports as ar join flights as fl on ar.id = fl.destination_airport_id where fl.id is (
    select flight_id from passengers where passport_number is (  
    select passport_number from people where passport_number in (
        select passport_number from passengers as ps 
        join flights as fl on ps.flight_id = fl.id where fl.id is (
        select id from flights where day = 29 and month = 07 and year = 2021 order by hour limit 1)
    ) 
        and phone_number in (
            select receiver from phone_calls where day = 28 and month = 07 and year = 2021 and duration < 60)
    
));


--return accomplice name
select name from people where phone_number is (
    select caller from phone_calls where day = 28 and month = 07 and year = 2021 and receiver is (
    select phone_number from people where passport_number in (
        select passport_number from passengers as ps 
        join flights as fl on ps.flight_id = fl.id where fl.id is (
        select id from flights where day = 29 and month = 07 and year = 2021 order by hour limit 1)
    ) 
        and phone_number in (
            select receiver from phone_calls where day = 28 and month = 07 and year = 2021 and duration < 60)
    )
    );
