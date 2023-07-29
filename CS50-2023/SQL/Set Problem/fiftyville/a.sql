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
        