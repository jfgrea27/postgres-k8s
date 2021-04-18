-- Setting up DB for Testing

CREATE TABLE "Accounts" (
	"id"	SERIAL,
	"first_name"	TEXT NOT NULL,
	"last_name"	TEXT NOT NULL,
	"email"	TEXT,
	"gender"	TEXT NOT NULL,
	"iban"	TEXT NOT NULL UNIQUE,
	"crncy"	TEXT NOT NULL,
	"balance"	REAL NOT NULL,
	PRIMARY KEY("iban")
);

COPY "Accounts" FROM '/usr/src/data.csv' WITH (FORMAT csv);