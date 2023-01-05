CREATE TABLE "client" (
	"id_client"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"nom"	TEXT NOT NULL,
	"prenom"	TEXT NOT NULL
);

CREATE TABLE "chambres" (
	"id_chambre"	INTEGER NOT NULL UNIQUE,
	"capacité"	INTEGER NOT NULL,
	"tarif"	INTEGER NOT NULL,
	PRIMARY KEY("id_chambre")
);

CREATE TABLE "reservation" (
	"id_reservation"	INTEGER NOT NULL UNIQUE,
	"id_client"	INTEGER NOT NULL UNIQUE,
	"id_chambre"	INTEGER NOT NULL UNIQUE,
	"date_debut"	TEXT NOT NULL,
	"date_fin"	TEXT NOT NULL,
	FOREIGN KEY("id_chambre") REFERENCES "chambres"("id_chambre"),
	PRIMARY KEY("id_reservation"),
	FOREIGN KEY("id_client") REFERENCES "client"("id_client")
);

INSERT INTO client VALUES(1, "Dupont", "Jean")
INSERT INTO chambres VALUES(1, 3, 70)

INSERT INTO "main"."reservation"
("id_reservation", "id_client", "id_chambre", "date_debut", "date_fin")
VALUES (1, 4, 42, '2022-10-13', '2022-10-16');