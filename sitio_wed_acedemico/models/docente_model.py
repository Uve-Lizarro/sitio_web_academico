from config import conectar

class DocenteModel:
    tabla = "docente"
    
    @staticmethod
    def listar():
        with conectar() as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM {DocenteModel.tabla} ORDER BY id_doc ASC")
                return cur.fetchall()

    @staticmethod
    def insertar(nombre, apellido, ci, sexo, fecha_nac):
        with conectar() as conn:
            with conn.cursor() as cur:
                sql = f"INSERT INTO {DocenteModel.tabla} (nombre, apellido, ci, sexo, fecha_nac) VALUES (%s, %s, %s, %s, %s)"
                cur.execute(sql, (nombre, apellido, ci, sexo, fecha_nac))
            conn.commit()

    @staticmethod
    def obtener_por_id(id_doc):
        with conectar() as conn:
            with conn.cursor() as cur:
                sql = f"SELECT * FROM {DocenteModel.tabla} WHERE id_doc = %s"
                cur.execute(sql, (id_doc,))
                return cur.fetchone()
            
    @staticmethod
    def actualizar(id_doc, nombre, apellido, sexo, fecha_nac):
        with conectar() as conn:
            with conn.cursor() as cur:
                sql = f"""
                    UPDATE {DocenteModel.tabla} 
                    SET nombre = %s, apellido = %s, sexo = %s, fecha_nac = %s
                    WHERE id_doc = %s
                """
                cur.execute(sql, (nombre, apellido, sexo, fecha_nac, id_doc))
            conn.commit()
    
    @staticmethod
    def eliminar(id_doc):
        with conectar() as conn:
            with conn.cursor() as cur:
                sql = f"DELETE FROM {DocenteModel.tabla} WHERE id_doc = %s"
                cur.execute(sql, (id_doc,))
            conn.commit()