CREATE DATABASE IF NOT EXISTS airports_db;
-- CREATE USER 'passnfly'@'localhost' IDENTIFIED BY 'pass1234';
-- GRANT ALL PRIVILEGES ON airports_db . * TO 'passnfly'@'localhost';
USE airports_db;

CREATE TABLE airports (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(150),
    city VARCHAR(50),
    country VARCHAR(20),
    iata VARCHAR(10),
    icao VARCHAR(10),
    latitude FLOAT,
    longitude FLOAT,
    altitude FLOAT,
    timezone FLOAT,
    dst VARCHAR(10),
    tz VARCHAR(50),
    type VARCHAR(20),
    source VARCHAR(20),
    created_at DATETIME,
    updated_at DATETIME,
    deleted BOOLEAN,

    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1;