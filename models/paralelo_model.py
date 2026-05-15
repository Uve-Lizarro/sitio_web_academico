from config import conectar
from models import materia_model, docente_model

class ParaleloModel:
    tabla = "paralelo"
    
    @staticmethod
    def listar():
        with conectar() as conn:
            with conn.cursor() as cur:
                sql = f"""
                    SELECT 
                        p.id_par, 
                        m.sigla, 
                        m.descrip, 
                        d.nombre || ' ' || d.apellido,
                        p.let_pa,
                        p.id_mat,
                        p.id_doc
                    FROM {ParaleloModel.tabla} p
                    JOIN {materia_model.MateriaModel.tabla} m ON p.id_mat = m.id_mat
                    JOIN {docente_model.DocenteModel.tabla} d ON p.id_doc = d.id_doc
                    ORDER BY p.id_par ASC
                """
                cur.execute(sql) 
                return cur.fetchall()

    @staticmethod
    def insertar(id_mat, id_doc, let_pa):
        with conectar() as conn:
            with conn.cursor() as cur:
                sql = f"INSERT INTO {ParaleloModel.tabla} (id_mat, id_doc, let_pa) VALUES (%s, %s, %s)"
                cur.execute(sql, (id_mat, id_doc, let_pa))
            conn.commit()

    @staticmethod
    def obtener_por_id(id_par, id_mat, id_doc):
        with conectar() as conn:
            with conn.cursor() as cur:
                sql = f"SELECT * FROM {ParaleloModel.tabla} WHERE id_par = %s AND id_mat = %s AND id_doc = %s"
                cur.execute(sql, (id_par, id_mat, id_doc,))
                return cur.fetchone()
            
    @staticmethod
    def actualizar(id_par, id_mat, id_doc, let_pa):
        with conectar() as conn:
            with conn.cursor() as cur:
                sql = f"""
                    UPDATE {ParaleloModel.tabla} 
                    SET id_mat = %s, id_doc = %s, let_pa = %s
                    WHERE id_par = %s
                """
                cur.execute(sql, (id_mat, id_doc, let_pa, id_par))
            conn.commit()
    
    @staticmethod
    def eliminar(id_par, id_mat, id_doc):
        with conectar() as conn:
            with conn.cursor() as cur:
                sql = f"DELETE FROM {ParaleloModel.tabla} WHERE id_par = %s AND id_mat = %s AND id_doc = %s"
                cur.execute(sql, (id_par, id_mat, id_doc))
            conn.commit()