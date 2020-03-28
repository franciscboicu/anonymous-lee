CREATE TABLE messages (
	id SERIAL NOT NULL,
	msg text NOT NULL,
	code varchar(16) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE users (
	id SERIAL NOT NULL,
	username varchar(16) NOT NULL,
	password varchar(32) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE messages_passwords (
	message_id int NOT NULL,
	password varchar(16) NOT NULL,
	FOREIGN KEY (message_id) REFERENCES messages(id)
);