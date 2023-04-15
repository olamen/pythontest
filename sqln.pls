
CREATE SEQUENCE facture_numfacture_seq
   start with 1
  INCREMENT by 1;

CREATE SEQUENCE hotel_numhotel_seq
  start with 1
  INCREMENT by 1;

CREATE SEQUENCE reservation_numresa_seq
  start with 1
  INCREMENT by 1;

CREATE SEQUENCE occupation_numoccup_seq
  start with 1
  INCREMENT by 1;

-- Creation des tables

CREATE TABLE hotel
(
  numhotel integer ,
  nom varchar(30) NOT NULL,
  ville varchar(20) NOT NULL,
  etoiles integer, -- Nombre d'etoiles
  CONSTRAINT cp_numhotel PRIMARY KEY (numhotel)
);

CREATE TABLE client
(
  numclient integer,
  nom varchar(20) NOT NULL,
  prenom varchar(20),
  CONSTRAINT cp_numclient PRIMARY KEY (numclient)
);

CREATE TABLE chambre
(
  numchambre Integer NOT NULL,
  numhotel integer NOT NULL,
  etage integer,
  "type" varchar(15), -- domaine
  prixnuitht integer NOT NULL, -- Prix par nuit, hors taxes
  CONSTRAINT cp_chambre PRIMARY KEY (numchambre, numhotel),
  CONSTRAINT fk_chambre_hotel FOREIGN KEY (numhotel)
      REFERENCES hotel(numhotel) ON DELETE CASCADE,
  CONSTRAINT cv_typechambre CHECK ( "type" in ( 'simple', 'double','triple','suite','autre'))
) ;


CREATE TABLE occupation
(
  numclient integer NOT NULL,
  numhotel integer NOT NULL,
  numchambre integer NOT NULL,
  datedepart date, -- NULL si inconnue
  datearrivee date NOT NULL,
  numoccup integer ,
  CONSTRAINT cp_occupation PRIMARY KEY (numoccup),
  CONSTRAINT fk_occupation_chambre FOREIGN KEY (numchambre, numhotel)
      REFERENCES chambre (numchambre, numhotel),
  CONSTRAINT fk_occupation_client FOREIGN KEY (numclient)
      REFERENCES client (numclient) ON DELETE CASCADE,
  CONSTRAINT fk_occupation_hotel FOREIGN KEY (numhotel)
      REFERENCES hotel (numhotel) ON DELETE CASCADE ,
  CONSTRAINT occupation_check CHECK (datearrivee < datedepart)
);

CREATE TABLE reservation 
(
  numresa integer,
  numclient integer NOT NULL,
  numchambre integer NOT NULL,
  numhotel integer NOT NULL,
  datearrivee date NOT NULL,
  datedepart date NOT NULL,
  CONSTRAINT cp_resa PRIMARY KEY (numresa),
  CONSTRAINT fk_resa_chambre FOREIGN KEY (numchambre, numhotel)
      REFERENCES chambre(numchambre, numhotel) ON DELETE CASCADE,
  CONSTRAINT fk_resa_client FOREIGN KEY (numclient)
      REFERENCES client(numclient)
ON DELETE CASCADE,
  CONSTRAINT fk_resa_hotel FOREIGN KEY (numhotel)
      REFERENCES hotel (numhotel) 
ON DELETE CASCADE,
  CONSTRAINT reservation_check CHECK (datearrivee < datedepart)
) ;



