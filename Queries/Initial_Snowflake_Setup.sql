use role sysadmin;
Create database HACKOVERFLOW;
use role accountadmin;
show users;

CREATE OR REPLACE USER Srikant PASSWORD = 'Srikant' LOGIN_NAME = 'SRIKANT' DISPLAY_NAME = 'SRIKANT' MUST_CHANGE_PASSWORD = FALSE;
CREATE OR REPLACE USER Srikant PASSWORD = 'Darshith' LOGIN_NAME = 'Darshith' DISPLAY_NAME = 'Darshith' MUST_CHANGE_PASSWORD = FALSE;
CREATE OR REPLACE USER Srikant PASSWORD = 'Abhishek' LOGIN_NAME = 'Abhishek' DISPLAY_NAME = 'Abhishek' MUST_CHANGE_PASSWORD = FALSE;
CREATE OR REPLACE USER Srikant PASSWORD = 'Akash' LOGIN_NAME = 'Akash' DISPLAY_NAME = 'Akash' MUST_CHANGE_PASSWORD = FALSE;
CREATE OR REPLACE USER Srikant PASSWORD = 'Ishwar' LOGIN_NAME = 'Ishwar' DISPLAY_NAME = 'Ishwar' MUST_CHANGE_PASSWORD = FALSE;

grant role accountadmin to user Srikant;

create schema Srikant;
create schema Akash;
create schema Darshith;
create schema Abhishek;
create schema Ishwar;


GRANT USAGE, OPERATE, MONITOR ON WAREHOUSE COMPUTE_WH TO ROLE accountadmin;

alter user ISHWAR  SET DEFAULT_ROLE = 'ACCOUNTADMIN';
alter user PRINCE  SET DEFAULT_ROLE = 'ACCOUNTADMIN';
alter user AKASH  SET DEFAULT_ROLE = 'ACCOUNTADMIN';
alter user DARSHITH  SET DEFAULT_ROLE = 'ACCOUNTADMIN';
alter user SRIKANT  SET DEFAULT_ROLE = 'ACCOUNTADMIN';
