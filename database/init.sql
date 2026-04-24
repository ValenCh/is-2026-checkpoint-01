CREATE TABLE IF NOT EXISTS members (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    legajo VARCHAR(20),
    feature VARCHAR(50),
    servicio VARCHAR(50),
    estado VARCHAR(20)
);