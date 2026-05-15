from config import conectar
from models import paralelo_model, estudiante_model, materia_model

class InscritoModel:
    tabla = "inscrito"
    
    @staticmethod
    def listar():
        with conectar() as conn:
            with conn.cursor() as cur:
                sql = f"""
                    SELECT 
                        i.id_ins,
                        m.sigla || ' - ' || m.descrip || ' - ' || p.let_pa || '',
                        e.nombre || ' ' || e.apellido,
                        i.nota,
                        i.estado,
                        i.id_par,
                        i.id_est
                    FROM {InscritoModel.tabla} i
                    JOIN {estudiante_model.EstudianteModel.tabla} e ON i.id_est = e.id_est
                    JOIN {paralelo_model.ParaleloModel.tabla} p ON i.id_par = p.id_par
                    JOIN {materia_model.MateriaModel.tabla} m ON p.id_mat = m.id_mat
                    ORDER BY i.id_ins ASC
                """
                cur.execute(sql) 
                return cur.fetchall()

    @staticmethod
    def insertar(id_par, id_est, nota):
        with conectar() as conn:
            with conn.cursor() as cur:
                sql = f"INSERT INTO {InscritoModel.tabla} (id_par, id_est, nota) VALUES (%s, %s, %s)"
                cur.execute(sql, (id_par, id_est, nota))
            conn.commit()

    @staticmethod
    def obtener_por_id(id_ins, id_par, id_est):
        with conectar() as conn:
            with conn.cursor() as cur:
                sql = f"SELECT * FROM {InscritoModel.tabla} WHERE id_ins = %s AND id_par = %s AND id_est = %s"
                cur.execute(sql, (id_ins, id_par, id_est,))
                return cur.fetchone()
            
    @staticmethod
    def actualizar(id_ins, id_par, id_est, nota):
        with conectar() as conn:
            with conn.cursor() as cur:
                sql = f"""
                    UPDATE {InscritoModel.tabla} 
                    SET id_par = %s, id_est = %s, nota = %s
                    WHERE id_ins = %s
                """
                cur.execute(sql, (id_par, id_est, nota, id_ins))
            conn.commit()
    
    @staticmethod
    def eliminar(id_ins, id_par, id_est):
        with conectar() as conn:
            with conn.cursor() as cur:
                sql = f"DELETE FROM {InscritoModel.tabla} WHERE id_ins = %s AND id_par = %s AND id_est = %s"
                cur.execute(sql, (id_ins, id_par, id_est))
            conn.commit()