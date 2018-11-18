#---------------CREATE
CREATE TABLE bands(name VARCHAR, 
		foundation_year DATE,  
		is_active BOOLEAN );

CREATE TABLE bands(name VARCHAR UNIQUE, 
		foundation_year DATE NOT NULL,  
		Is_active BOOLEAN );


#---------------INSERT

INSERT INTO bands (name, foundation_year, is_active)
		(‘Bon Jovi’, ‘1983-01-01’, True), 

INSERT INTO bands VALUES (‘Owl City’, ‘2002-01-01’, True), 
		    (Disturbed, 1994,True);

INSERT INTO bands VALUES(‘Anathema,’ 1990 True),
		(‘Olvi’, ‘2001-01-01’, False),
		(‘DDT’, ‘1980-01-01’,  True);



#----------SELECT

SELCT * FROM bands;

SELECT name, is_active FROM bands;

SELECT max(foundation_year) FROM bands;

SELECT * FROM bands WHERE foundation_year < ‘1995-01-01’;

SELECT * FROM bands WHERE foundation_year BETWEEN ‘1990-01-01’ AND ‘1995-01-01’;

SELECT * FROM bands WHERE foundation_year NOT BETWEEN ‘1990-01-01’ AND ‘1995-01-01’;

SELECT * FROM bands WHERE foundation_year IN (‘1990-01-01’, ‘1994-01-01’);

SELECT * FROM bands WHERE foundation_year NOT IN (‘1990-01-01’, ‘1994-01-01’);


#---JOIN
SELECT * FROM bands LEFT OUTER JOIN songs ON (bands.name = songs.band);

SELECT * FROM bands RIGHT OUTER JOIN songs ON (bands.name = songs.band);

SELECT * FROM bands FULL OUTER JOIN songs ON (bands.name = songs.band);

