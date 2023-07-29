select * from bakery_security_logs where day = 28 and month = 07 and year = 2021 and hour = 10 order by minute;




select name from people as pp 
    join bank_accounts as ba on pp.id = ba.person_id
    join atm_transactions as at on ba.account_number = at.account_number
    where at.day = 28
    and at.month = 07
    and at.year = 2021
    and at.transaction_type = 'withdraw';

select * from passengers limit 1;


select name from people where phone_number in (
            select caller from phone_calls where day = 28 and month = 07 and year = 2021 and duration < 60);

select * from passengers limit 1;


            select name from people where license_plate in(
            select license_plate from bakery_security_logs where activity = 'exit' and day = 28 and month = 07 and year = 2021 and hour = 10 and minute between 15 and 35);