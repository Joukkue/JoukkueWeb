# JoukkueWeb
A web page to be used with JoukkueBot

CREATE DATABASE joukkue;
 
CREATE USER joukkue WITH PASSWORD 'joukkue';
 
ALTER ROLE cat SET client_encoding TO 'utf8';
 
ALTER ROLE cat SET timezone TO 'Europe/Helsinki';
 
GRANT ALL PRIVILEGES ON DATABASE joukkue TO joukkue;
 
ALTER ROLE joukkue CREATEDB;