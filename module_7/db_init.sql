-- drop user if exists
DROP USER IF EXISTS 'user'@'localhost';

-- create user and grant them all privileges to the pysports database
CREATE USER 'user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Everythinghaschanged27';

-- grant all privileges to the pysports database to user on localhost
GRANT ALL PRIVILEGES ON pysports.* TO'user'@'localhost';

-- drop tables if they are present
DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS team;

-- create the team table
CREATE TABLE team (
    team_id     INT             NOT NULL        AUTO_INCREMENT,
    team_name   VARCHAR(75)     NOT NULL,
    mascot      VARCHAR(75)     NOT NULL,
    PRIMARY KEY(team_id)
);

-- create the player table and set the foreign key
CREATE TABLE player (
    player_id   INT             NOT NULL        AUTO_INCREMENT,
    first_name  VARCHAR(75)     NOT NULL,
    last_name   VARCHAR(75)     NOT NULL,
    team_id     INT             NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team
    FOREIGN KEY(team_id)
        REFERENCES team(team_id)
);

-- insert team records
INSERT INTO team(team_id, team_name, mascot)
    VALUES('1','Team Gandalf', 'White Wizards');

INSERT INTO team(team_id, team_name, mascot)
    VALUES('2','Team Sauron', 'Orcs');

-- insert player records
INSERT INTO player(player_id, first_name, last_name, team_id)
    VALUES('1', 'Thorin', 'Oakenshield','1');

INSERT INTO player(player_id, first_name, last_name, team_id)
    VALUES('2', 'Bilbo', 'Baggins','1');

INSERT INTO player(player_id, first_name, last_name, team_id)
    VALUES('3', 'Frodo', 'Baggins','1');

INSERT INTO player(player_id, first_name, last_name, team_id)
    VALUES('4', 'Saruman', 'The White','2');

INSERT INTO player(player_id, first_name, last_name, team_id)
    VALUES('5', 'Angmar', 'Witch-king','2');

INSERT INTO player(player_id, first_name, last_name, team_id)
    VALUES('6', 'Azog', 'The Defiler','2');

