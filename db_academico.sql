---CREATE DATABASE db_academico

CREATE TABLE estudiante (
    id_est VARCHAR(10) NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    ci VARCHAR(10) UNIQUE NOT NULL,
    sexo CHAR(1) NOT NULL,
    fecha_nac DATE NOT NULL,
    edad INTEGER NOT NULL,
    PRIMARY KEY (id_est)
);

CREATE TABLE docente (
    id_doc VARCHAR(10) NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    ci VARCHAR(10) UNIQUE NOT NULL,
    sexo CHAR(1) NOT NULL,
    fecha_nac DATE NOT NULL,
    edad INTEGER NOT NULL,
    PRIMARY KEY (id_doc)
);

CREATE TABLE materia (
    id_mat VARCHAR(8) NOT NULL,
    sigla VARCHAR(8) NOT NULL,
    descrip VARCHAR(50) NOT NULL,
    nro_semestral INTEGER NOT NULL,
    PRIMARY KEY (id_mat)
);

CREATE TABLE paralelo (
    id_par VARCHAR(6) NOT NULL,
    id_mat VARCHAR(8) NOT NULL,
    id_doc VARCHAR(10) NOT NULL,
    let_pa VARCHAR(1) NOT NULL,
    PRIMARY KEY (id_par),
    UNIQUE(id_mat, let_pa),
    FOREIGN KEY (id_mat) REFERENCES materia(id_mat),
    FOREIGN KEY (id_doc) REFERENCES docente(id_doc)
);

CREATE TABLE inscrito (
    id_ins VARCHAR(6) NOT NULL,
    id_par VARCHAR(6) NOT NULL,
    id_est VARCHAR(10) NOT NULL,
    nota NUMERIC(5,2),
    estado VARCHAR(10) NOT NULL,
    PRIMARY KEY (id_ins),
    FOREIGN KEY (id_par) REFERENCES paralelo(id_par),
    FOREIGN KEY (id_est) REFERENCES estudiante(id_est)
);

--- Función y Trigger para calcular la edad

CREATE OR REPLACE FUNCTION funcion_calcular_edad()
RETURNS TRIGGER AS $$
BEGIN
    NEW.edad := EXTRACT(YEAR FROM age(NEW.fecha_nac));
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER tr_calcular_edad_estudiante
BEFORE INSERT OR UPDATE ON estudiante
FOR EACH ROW
EXECUTE FUNCTION funcion_calcular_edad();

CREATE TRIGGER tr_calcular_edad_docente
BEFORE INSERT OR UPDATE ON docente
FOR EACH ROW
EXECUTE FUNCTION funcion_calcular_edad();

--- Funciones y Triggers para generar los IDs

CREATE OR REPLACE FUNCTION funcion_generar_id_estudiante()
RETURNS TRIGGER AS $$
BEGIN
    NEW.id_est := 'est_' || LEFT(NEW.ci, 4) || LOWER(LEFT(NEW.nombre, 2));
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER tr_generar_id_estudiante
BEFORE INSERT ON estudiante
FOR EACH ROW
EXECUTE FUNCTION funcion_generar_id_estudiante();

CREATE OR REPLACE FUNCTION funcion_generar_id_docente()
RETURNS TRIGGER AS $$
BEGIN
    NEW.id_doc := 'doc_' || LEFT(NEW.ci, 4) || LOWER(LEFT(NEW.nombre, 2));
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER tr_generar_id_docente
BEFORE INSERT ON docente
FOR EACH ROW
EXECUTE FUNCTION funcion_generar_id_docente();

CREATE OR REPLACE FUNCTION funcion_generar_id_materia()
RETURNS TRIGGER AS $$
BEGIN
    
    NEW.id_mat := 'ma_' || UPPER(RIGHT(NEW.sigla, 3)) || '_' || NEW.nro_semestral::text;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER tr_generar_id_materia
BEFORE INSERT OR UPDATE ON materia
FOR EACH ROW
EXECUTE FUNCTION funcion_generar_id_materia();

CREATE OR REPLACE FUNCTION funcion_generar_id_paralelo()
RETURNS TRIGGER AS $$
DECLARE
    parte_mat TEXT;
    parte_doc TEXT;
BEGIN
    parte_mat := SUBSTRING(NEW.id_mat FROM 5 FOR 2);

    parte_doc := SUBSTRING(NEW.id_doc FROM 7 FOR 2);

    NEW.id_par := 'p_' || parte_mat || parte_doc;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER tr_generar_id_paralelo
BEFORE INSERT OR UPDATE ON paralelo
FOR EACH ROW
EXECUTE FUNCTION funcion_generar_id_paralelo();

CREATE OR REPLACE FUNCTION funcion_generar_id_inscrito()
RETURNS TRIGGER AS $$
DECLARE
    parte_est TEXT;
    parte_par TEXT;
BEGIN
    parte_est := SUBSTRING(NEW.id_est FROM 5 FOR 2);

    parte_par := SUBSTRING(NEW.id_par FROM 3 FOR 2);

    NEW.id_ins := 'i_' || parte_est || parte_par;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER tr_generar_id_inscrito
BEFORE INSERT OR UPDATE ON inscrito
FOR EACH ROW
EXECUTE FUNCTION funcion_generar_id_inscrito();

--- Función y Trigger para redondear la nota y definir el estado

CREATE OR REPLACE FUNCTION funcion_redondear_nota()
RETURNS TRIGGER AS $$
BEGIN
    NEW.nota := ROUND(NEW.nota::numeric);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER tr_redondear_nota
BEFORE INSERT OR UPDATE ON inscrito
FOR EACH ROW
EXECUTE FUNCTION funcion_redondear_nota();

CREATE OR REPLACE FUNCTION funcion_estado_nota()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.nota = 0 THEN
        NEW.estado := 'Abandono';
        
    ELSIF NEW.nota >= 51.00 THEN
        NEW.estado := 'Aprobado';
        
    ELSE
        NEW.estado := 'Reprobado';
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER tr_estado_nota
BEFORE INSERT OR UPDATE ON inscrito
FOR EACH ROW
EXECUTE FUNCTION funcion_estado_nota();

--- Datos de prueba

INSERT INTO estudiante (nombre, apellido, ci, sexo, fecha_nac) VALUES
('Guillermo Diaz', 'Perez Velasco', '10041599', 'M', '2000-01-15'),
('Flor Elizabeht', 'Torrez Felipez', '14083227', 'F', '2006-05-20'),
('Laura Nataly', 'Navarro Zapata', '15521001', 'F', '2003-09-08'),
('Juan Pablo', 'Torrez Vasquez', '10098893', 'M', '2002-12-25');

SELECT * FROM estudiante;

INSERT INTO docente (nombre, apellido, ci, sexo, fecha_nac) VALUES
('Carlos Ramiro', 'Vasquez Camargo', '5545476', 'M', '1980-03-10'),
('Natalia Alejandra', 'Jimenez Loza', '6844125', 'F', '1985-07-25'),
('Rafael', 'Flores Alanoca', '5264110', 'M', '1975-12-05');

SELECT * FROM docente;

INSERT INTO materia (sigla, descrip, nro_semestral) VALUES
('INF 111', 'Programación I', 1),
('INF 121', 'Programación II', 2),
('INF 131', 'Programación III', 3),
('INF 113', 'Programación Web I', 1),
('INF 122', 'Programación Web II', 2),
('INF 133', 'Programación Web III', 3);

SELECT * FROM materia;

INSERT INTO paralelo (id_mat, id_doc, let_pa) VALUES
('ma_111_1', 'doc_5545ca', 'A'),
('ma_121_2', 'doc_6844na', 'B'),
('ma_131_3', 'doc_5545ca', 'C');

SELECT * FROM paralelo;

INSERT INTO inscrito (id_par, id_est, nota) VALUES
('p_1145', 'est_1004gu', '68.7'),
('p_1145', 'est_1408fl', '72.4'),
('p_2144', 'est_1552la', '65.2'),
('p_2144', 'est_1009ju', '52.1');

SELECT * FROM inscrito;

