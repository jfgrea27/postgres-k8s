-- Setting up DB for Testing
-- (1) Creation of DATABASE & TABLE(s)
-- (2) Import of data into TABLE(s)

-- (1) Creation of DATABASE & TABLE(s)
CREATE DATABASE "BANK";

CREATE TABLE "Accounts" (
	"id"	INTEGER NOT NULL,
	"first_name"	TEXT NOT NULL,
	"last_name"	TEXT NOT NULL,
	"email"	TEXT,
	"gender"	TEXT NOT NULL,
	"account_number"	TEXT NOT NULL UNIQUE,
	"crncy"	TEXT NOT NULL,
	"balance"	REAL NOT NULL,
	PRIMARY KEY("account_number")
);

-- (2) Import of data into TABLE(s)
COPY "Accounts" FROM '/usr/src/data.csv' WITH (FORMAT csv);