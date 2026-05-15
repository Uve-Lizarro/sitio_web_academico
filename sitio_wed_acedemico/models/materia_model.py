from config import conectar

class MateriaModel:
    tabla = "materia"
    
    @staticmethod
    def listar():
        with conectar() as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM {MateriaModel.tabla} ORDER BY id_mat ASC")
                return cur.fetchall()

    @staticmethod
    def insertar(sigla, descrip, nro_semestral):
        with conectar() as conn:
            with conn.cursor() as cur:
                sql = f"INSERT INTO {MateriaModel.tabla} (sigla, descrip, nro_semestral) VALUES (%s, %s, %s)"
                cur.execute(sql, (sigla, descrip, nro_semestral))
            conn.commit()

    @staticmethod
    def obtener_por_id(id_mat):
        with conectar() as conn:
            with conn.cursor() as cur:
                sql = f"SELECT * FROM {MateriaModel.tabla} WHERE id_mat = %s"
                cur.execute(sql, (id_mat,))
                return cur.fetchone()
            
    @staticmethod
    def actualizar(id_mat, sigla, decripcion, nro_semestral):
        with conectar() as conn:
            with conn.cursor() as cur:
                sql = f"""
                    UPDATE {MateriaModel.tabla} 
                    SET sigla = %s, descrip = %s, nro_semestral = %s
                    WHERE id_mat = %s
                """
                cur.execute(sql, (sigla, decripcion, nro_semestral, id_mat))
            conn.commit()
    
    @staticmethod
    def eliminar(id_mat):
        with conectar() as conn:
            with conn.cursor() as cur:
                sql = f"DELETE FROM {MateriaModel.tabla} WHERE id_mat = %s"
                cur.execute(sql, (id_mat,))
            conn.commit()