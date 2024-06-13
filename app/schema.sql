DROP TABLE IF EXISTS admins;
DROP TABLE IF EXISTS influencers;
DROP TABLE IF EXISTS campaigner;
DROP TABLE IF EXISTS ad_requests;
DROP TABLE IF EXISTS campains;


CREATE TABLE admins(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE influencers(
    influ_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    reach INTEGER NOT NULL,
    niche TEXT NOT NULL
);

CREATE TABLE campaigner(
    camp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE ad_requests(
    ad_id INTEGER PRIMARY KEY AUTOINCREMENT,
    influ_id INTEGER NOT NULL,
    camp_id INTEGER NOT NULL,
    requirements TEXT NOT NULL,
    pay_amt REAL NOT NULL,
    status TEXT UNIQUE NOT NULL
);

CREATE TABLE campains(
    ad_id INTEGER PRIMARY KEY AUTOINCREMENT,
    camp_id INTEGER NOT NULL,
    requirements TEXT NOT NULL,
    budget REAL NOT NULL,
    status TEXT UNIQUE NOT NULL
);