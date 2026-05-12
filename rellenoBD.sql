CREATE TABLE tipo_usuario(
    id_tipo_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE estado(
    id_estado INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE usuarios(
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    id_tipo_usuario INT,
    id_estado INT,

    FOREIGN KEY (id_tipo_usuario) REFERENCES tipo_usuario(id_tipo_usuario),
    FOREIGN KEY (id_estado) REFERENCES estado(id_estado)

);

INSERT INTO tipo_usuario (nombre) VALUES ('Vendedor'), ('Supervisor');
INSERT INTO estado (nombre) VALUES ('Habilitado'), ('Deshabilitado');