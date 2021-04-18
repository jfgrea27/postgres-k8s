-- Setting up DB for Testing

CREATE TABLE "Accounts" (
	"id"	SERIAL,
	"first_name"	TEXT NOT NULL,
	"last_name"	TEXT NOT NULL,
	"email"	TEXT,
	"gender"	TEXT NOT NULL,
	"account_number"	TEXT NOT NULL UNIQUE,
	"crncy"	TEXT NOT NULL,
	"balance"	REAL NOT NULL,
	PRIMARY KEY("account_number")
);

COPY "Accounts" FROM '/usr/src/data.csv' WITH (FORMAT csv);