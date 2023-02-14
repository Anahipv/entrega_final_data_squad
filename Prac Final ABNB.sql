--Visualizamos y exploramos tabla ppal

SELECT *
from "airbnb_KC"."0213_airbnb_madrid_clean" amc 
order by amc.id 
limit 20


SELECT count(*)
from "airbnb_KC"."0213_airbnb_madrid_clean" amc 




-- creamos schema particular para el DER

create schema prac_final_abnb authorization yputqhxb;


--Creacion Tablas, Constraints y Populación de Datos 

--Creacion tabla Host

create table "prac_final_abnb".Host (
	Host_id int, --PK
	Host_name varchar(500),
	constraint Host_PK primary key (Host_id)
);


INSERT INTO "prac_final_abnb".host  (Host_id, Host_name)
SELECT distinct "Host ID", "Host Name" 
FROM "airbnb_KC"."0213_airbnb_madrid_clean"  amc ;

select *
from "prac_final_abnb".host


--creacion tabla features
create table "prac_final_abnb".features (
	id_features serial not null, --PK
	feature_name varchar(500) not null,
	constraint features_pk primary key (id_features)
);
	

INSERT INTO "prac_final_abnb".features (feature_name) values ('Host Is Superhost');
INSERT INTO "prac_final_abnb".features (feature_name) values ('Host Identity Verified');


select *
from "prac_final_abnb".features



--Creacion Tabla Host-Feat y  Keys
create table "prac_final_abnb".host_features (
	id_features int, --FK, PK
	Host_id int --FK, PK
);


alter table "prac_final_abnb".host_features 
add constraint host_features_pk primary key(id_features, Host_id);


alter table "prac_final_abnb".host_features 
add constraint host_features_fk1 foreign key (id_features)
references "prac_final_abnb".features(id_features); 

alter table "prac_final_abnb".host_features 
add constraint host_features_fk2 foreign key (Host_id)
references "prac_final_abnb".host (Host_id); 
	

--creacion tabla amenities
create table "prac_final_abnb".amenities (
	id_amenities serial not null, --PK
	amenities_name varchar(500) not null,
	constraint amenities_idpk primary key (id_amenities)
);


-- popoulacion amenities
INSERT INTO "prac_final_abnb".amenities (amenities_name) values ('kitchen');
INSERT INTO "prac_final_abnb".amenities (amenities_name) values ('internet');
INSERT INTO "prac_final_abnb".amenities (amenities_name) values ('Air conditioning');
INSERT INTO "prac_final_abnb".amenities (amenities_name) values ('heating');
INSERT INTO "prac_final_abnb".amenities (amenities_name) values ('washer');
INSERT INTO "prac_final_abnb".amenities (amenities_name) values ('dryer');
INSERT INTO "prac_final_abnb".amenities (amenities_name) values ('elevator');
INSERT INTO "prac_final_abnb".amenities (amenities_name) values ('Pets allowed');
INSERT INTO "prac_final_abnb".amenities (amenities_name) values ('Wheelchair accessible');
INSERT INTO "prac_final_abnb".amenities (amenities_name) values ('Smoking allowed');
INSERT INTO "prac_final_abnb".amenities (amenities_name) values ('tv');
INSERT INTO "prac_final_abnb".amenities (amenities_name) values ('pool');
INSERT INTO "prac_final_abnb".amenities (amenities_name) values ('Pets live on this property');
INSERT INTO "prac_final_abnb".amenities (amenities_name) values ('Free parking on premises');
INSERT INTO "prac_final_abnb".amenities (amenities_name) values ('24-hour check-in');
INSERT INTO "prac_final_abnb".amenities (amenities_name) values ('breakfast');

select *
from "prac_final_abnb".amenities a 




--Creacion Tabla Amenities_Prop y Keys  
create table "prac_final_abnb".Amenities_Property (
	id_amenities int, --FK, PK
	id_property int --FK, PK
);


alter table "prac_final_abnb".Amenities_Property 
add constraint Amenities_Property_pk primary key(id_amenities, id_property);


alter table "prac_final_abnb".Amenities_Property 
add constraint Amenities_Property_fk1 foreign key (id_amenities)
references "prac_final_abnb".amenities(id_amenities); 

alter table "prac_final_abnb".Amenities_Property 
add constraint Amenities_Property_fk2 foreign key (id_property)
references "prac_final_abnb".property (id); 




--Creación tabla Room type
create table "prac_final_abnb".room_type (
	id_room_type serial not null, --PK
	name_room_type varchar(500) not null,
	constraint room_type_pk primary key (id_room_type)
);

--Populado tabla Room Type
INSERT INTO "prac_final_abnb".room_type  (name_room_type)
SELECT distinct "Room Type" 
FROM "airbnb_KC"."0213_airbnb_madrid_clean" amc;


--Creación tabla Property type
CREATE TABLE "prac_final_abnb".property_type(
	id_property_type serial NOT NULL, --PK
	name_property_type varchar(500) NOT NULL,
	CONSTRAINT property_type_pk PRIMARY KEY (id_property_type)
);

--Populado tabla Property type
INSERT INTO "prac_final_abnb".property_type (name_property_type)
SELECT distinct "Property Type"
FROM "airbnb_KC"."0213_airbnb_madrid_clean";

--Creación tabla Bed type
CREATE TABLE "prac_final_abnb".bed_type(
	id_bed_type serial NOT NULL, --PK
	name_bed_type varchar(500) NOT NULL,
	CONSTRAINT bed_type_pk PRIMARY KEY (id_bed_type)
);

--Populado tabla Bed type
INSERT INTO "prac_final_abnb".bed_type (name_bed_type)
SELECT distinct "Bed Type"
FROM "airbnb_KC"."0213_airbnb_madrid_clean";


--Creación tabla Cancellation Policy
CREATE TABLE "prac_final_abnb".cancellation_policy(
	id_cancellation_policy serial NOT NULL, --PK
	cancellation_policy varchar(500) NOT NULL,
	CONSTRAINT cancallation_policy_pk PRIMARY KEY (id_cancellation_policy)
);

--Populado tabla Cancellation Policy
INSERT INTO "prac_final_abnb".cancellation_policy (cancellation_policy)
SELECT distinct "Cancellation Policy"
FROM "airbnb_KC"."0213_airbnb_madrid_clean";


--Creación tabla Country
CREATE TABLE "prac_final_abnb".country(
	id_country_code serial NOT NULL, --PK
	name_country varchar(500) NOT NULL,
	CONSTRAINT country_pk PRIMARY KEY (id_country_code)
);

--Populado tabla Country
INSERT INTO "prac_final_abnb".country (name_country)
SELECT distinct "country"
FROM "airbnb_KC"."0213_airbnb_madrid_clean";
	

-- Creación y populado tabla state
--Consulta para unir el id del country con el estado y se guardo en una tabla

CREATE TABLE "prac_final_abnb".state  
AS
SELECT DISTINCT amc.state, c.id_country_code
FROM "airbnb_KC"."0213_airbnb_madrid_clean" amc , "prac_final_abnb".country c 
WHERE amc.country = c.name_country

--Se cambia el nombre de columna para coincidir con la definición en E-R
ALTER table "prac_final_abnb".state
RENAME COLUMN state TO name_state;

--Se agrega la PK con serial
ALTER TABLE "prac_final_abnb".state  
ADD COLUMN id_state serial PRIMARY KEY;

--Se modifica la columna a FK
ALTER TABLE "prac_final_abnb".state
ADD CONSTRAINT state_fk FOREIGN KEY (id_country_code)  
REFERENCES "prac_final_abnb".country (id_country_code);



--Se define que la FK no puede ser null
ALTER TABLE "prac_final_abnb".state 
ALTER COLUMN id_country_code SET NOT NULL;


-- Creación y populado tabla City
CREATE TABLE "prac_final_abnb".city  
AS
SELECT DISTINCT amc.city, s.id_state 
FROM "airbnb_KC"."0213_airbnb_madrid_clean" amc , "prac_final_abnb".state s 
WHERE amc.state = s.name_state 

--Se cambia el nombre de columna para coincidir con la definición en E-R
ALTER table "prac_final_abnb".city
RENAME COLUMN city TO name_city;

--Se agrega la PK con serial
ALTER TABLE "prac_final_abnb".city  
ADD COLUMN id_city serial PRIMARY KEY NOT NULL;

--Se modifica la columna a FK
ALTER TABLE "prac_final_abnb".city
ADD CONSTRAINT city_fk FOREIGN KEY (id_state)  
REFERENCES "prac_final_abnb".state (id_state);

--Se define que la FK no puede ser null
ALTER TABLE "prac_final_abnb".city 
ALTER COLUMN id_state SET NOT NULL;




-- Creación y populado tabla Neighbourhood group sin Zipcode
CREATE TABLE "prac_final_abnb".neighbourhood_group  
AS
SELECT DISTINCT amc."Neighbourhood Group Cleansed", c.id_city
FROM "airbnb_KC"."0213_airbnb_madrid_clean" amc , "prac_final_abnb".city c  
WHERE amc.city = c.name_city




--Se cambia el nombre de columna para coincidir con la definición en E-R
ALTER table "prac_final_abnb".neighbourhood_group
RENAME COLUMN "Neighbourhood Group Cleansed" TO name_neighbourhood_group;


--Se agrega la PK con serial
ALTER TABLE "prac_final_abnb".neighbourhood_group  
ADD COLUMN id_neighbourhood_group serial PRIMARY KEY NOT NULL;

--Se modifica la columna a FK
ALTER TABLE "prac_final_abnb".neighbourhood_group 
ADD CONSTRAINT neighbourhood_group_fk FOREIGN KEY (id_city)  REFERENCES "prac_final_abnb".city (id_city);

--Se define que la FK no puede ser null   
ALTER TABLE "prac_final_abnb".neighbourhood_group 
ALTER COLUMN id_neighbourhood_group SET NOT NULL;

select *
from "prac_final_abnb".neighbourhood_group ng 

select *
from "prac_final_abnb".state s 

select *
from "prac_final_abnb".city c  


-- Creación y populado tabla Neighbourhood 
CREATE TABLE "prac_final_abnb".neighbourhood  
AS
SELECT DISTINCT amc."Neighbourhood Cleansed", ng.id_neighbourhood_group 
FROM "airbnb_KC"."0213_airbnb_madrid_clean" amc , "prac_final_abnb".neighbourhood_group ng 
WHERE amc."Neighbourhood Group Cleansed" = ng.name_neighbourhood_group 

--Se cambia el nombre de columna para coincidir con la definición en E-R
ALTER table "prac_final_abnb".neighbourhood
RENAME COLUMN "Neighbourhood Cleansed" TO name_neighbourhood;

--Se agrega la PK con serial
ALTER TABLE "prac_final_abnb".neighbourhood  
ADD COLUMN id_neighbourhood serial PRIMARY KEY NOT NULL;

--Se modifica la columna a FK   
ALTER TABLE "prac_final_abnb".neighbourhood 
ADD CONSTRAINT neighbourhood_fk FOREIGN KEY (id_neighbourhood_group)  REFERENCES "prac_final_abnb".neighbourhood_group (id_neighbourhood_group);

--Se define que la FK no puede ser null
ALTER TABLE "prac_final_abnb".neighbourhood 
ALTER COLUMN id_neighbourhood SET NOT NULL;



select *
from "prac_final_abnb".neighbourhood n 


-- creacion tabla property y Populacion


CREATE TABLE "prac_final_abnb".property
AS
SELECT DISTINCT amc.id, amc."Host ID", pt.id_property_type , rt.id_room_type, bt.id_bed_type, cp.id_cancellation_policy, n.id_neighbourhood ,amc.accommodates, amc.bathrooms , amc.bedrooms, amc.beds , amc.price , amc."Security Deposit" , amc."Cleaning Fee" , amc."Guests Included" , amc."Review Scores Rating" , amc.latitude , amc.longitude , amc."Number of Reviews"  
FROM "airbnb_KC"."0213_airbnb_madrid_clean" amc  , "prac_final_abnb".property_type pt , "prac_final_abnb".room_type rt , "prac_final_abnb".bed_type bt , "prac_final_abnb".cancellation_policy cp , "prac_final_abnb".neighbourhood n 
WHERE amc."Property Type" = pt.name_property_type and amc."Room Type" = rt.name_room_type and amc."Bed Type" = bt.name_bed_type and amc."Cancellation Policy" = cp.cancellation_policy and amc."Neighbourhood Cleansed" = n.name_neighbourhood 

select count(*)
from "prac_final_abnb".property	



--Creacion PK y FKs

ALTER TABLE "prac_final_abnb".property  
ADD CONSTRAINT prop_pk PRIMARY key (id)

-- FK
alter table "prac_final_abnb".property
add constraint property_fk1 foreign key (id_property_type)
references "prac_final_abnb".property_type (id_property_type); 

alter table "prac_final_abnb".property
add constraint property_fk2 foreign key (id_room_type)
references "prac_final_abnb".room_type (id_room_type);

alter table "prac_final_abnb".property
add constraint property_fk3 foreign key (id_bed_type)
references "prac_final_abnb".bed_type (id_bed_type);

alter table "prac_final_abnb".property
add constraint property_fk4 foreign key ("Host ID")
references "prac_final_abnb".host (Host_id);


alter table "prac_final_abnb".property
add constraint property_fk5 foreign key (id_cancellation_policy)
references "prac_final_abnb".cancellation_policy (id_cancellation_policy);


alter table "prac_final_abnb".property 
add constraint property_fk6 foreign key (id_neighbourhood)
references "prac_final_abnb".neighbourhood (id_neighbourhood);



select count(*)
from "prac_final_abnb".property p	
	
select *
from "prac_final_abnb".property p	
order by id 
limit 20






