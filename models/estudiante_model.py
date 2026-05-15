from config import conectar

class EstudianteModel:
    tabla = "estudiante"
    
    @staticmethod
    def listar():
        with conectar() as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM {EstudianteModel.tabla} ORDER BY id_est ASC")
                return cur.fetchall()

    @staticmethod
    def insertar(nombre, apellido, ci, sexo, fecha_nac):
        with conectar() as conn:
            with conn.cursor() as cur:
                sql = f"INSERT INTO {EstudianteModel.tabla} (nombre, apellido, ci, sexo, fecha_nac) VALUES (%s, %s, %s, %s, %s)"
                cur.execute(sql, (nombre, apellido, ci, sexo, fecha_nac))
            conn.commit()

    @staticmethod
    def obtener_por_id(id_est):
        with conectar() as conn:
            with conn.cursor() as cur:
                sql = f"SELECT * FROM {EstudianteModel.tabla} WHERE id_est = %s"
                cur.execute(sql, (id_est,))
                return cur.fetchone()
            
    @staticmethod
    def actualizar(id_est, nombre, apellido, sexo, fecha_nac):
        with conectar() as conn:
            with conn.cursor() as cur:
                sql = f"""
                    UPDATE {EstudianteModel.tabla} 
                    SET nombre = %s, apellido = %s, sexo = %s, fecha_nac = %s
                    WHERE id_est = %s
                """
                cur.execute(sql, (nombre, apellido, sexo, fecha_nac, id_est))
            conn.commit()
    
    @staticmethod
    def eliminar(id_est):
        with conectar() as conn:
            with conn.cursor() as cur:
                sql = f"DELETE FROM {EstudianteModel.tabla} WHERE id_est = %s"
                cur.execute(sql, (id_est,))
            conn.commit()