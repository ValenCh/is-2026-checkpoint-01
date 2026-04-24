CREATE TABLE IF NOT EXISTS members (
    id       SERIAL PRIMARY KEY,
    nombre   VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    legajo   VARCHAR(20) UNIQUE NOT NULL,
    estado   VARCHAR(20) CHECK (estado IN ('Activo', 'Inactivo'))
);

CREATE TABLE IF NOT EXISTS features (
    id         SERIAL PRIMARY KEY,
    member_id  INT REFERENCES members(id),
    feature    VARCHAR(50),
    servicio   VARCHAR(50)
);

INSERT INTO members (nombre, apellido, legajo, estado) VALUES
    ('Valentino',     'Chiappini', '33072', 'Activo'),
    ('Sergio Adrian', 'Maldonado', '21352', 'Activo'),
    ('Juan Ignacio',  'Wilt',      '33151', 'Activo'),
    ('Alvaro',        'Marini',    '33133', 'Activo');

INSERT INTO features (member_id, feature, servicio) VALUES
    (1, 'Feature 01', 'Coordinador'),
    (1, 'Feature 05', 'Portainer'),
    (2, 'Feature 02', 'Frontend'),
    (3, 'Feature 03', 'Backend'),
    (4, 'Feature 04', 'Database');