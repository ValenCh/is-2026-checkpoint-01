CREATE TABLE IF NOT EXISTS members (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    legajo VARCHAR(20),
    feature VARCHAR(50),
    servicio VARCHAR(50),
    estado VARCHAR(20)
);

INSERT INTO members (nombre, apellido, legajo, feature, servicio, estado) VALUES
('Valentino', 'Chiappini', '33072', 'Feature 01', 'Coordinador', 'Activo'),
('Sergio Adrian', 'Maldonado', '21352', 'Feature 02', 'Frontend', 'Activo'),
('Juan Ignacio', 'Wilt', '33151', 'Feature 03', 'Backend', 'Activo'),
('Alvaro', 'Marini', '33133', 'Feature 04', 'Database', 'Activo'),
('Valentino', 'Chiappini', '33072', 'Feature 05', 'Portainer', 'Activo');