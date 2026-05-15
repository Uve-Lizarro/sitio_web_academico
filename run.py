from flask import Flask, render_template, request, redirect, url_for
from models.estudiante_model import EstudianteModel
from models.docente_model import DocenteModel
from models.materia_model import MateriaModel
from models.paralelo_model import ParaleloModel
from models.inscrito_model import InscritoModel

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', 
                           estudiantes=EstudianteModel.listar(),
                           docentes=DocenteModel.listar(),
                           materias=MateriaModel.listar(),
                           paralelos=ParaleloModel.listar(),
                           inscritos=InscritoModel.listar()
                           )

@app.route('/estudiante/agregar', methods=['POST'])
def agregar_estudiante():
    EstudianteModel.insertar(
        request.form['atri_1_L_E'],
        request.form['atri_2_L_E'],
        request.form['atri_3_L_E'],
        request.form['atri_4_L_E'],
        request.form['atri_5_L_E']
    )
    return redirect(url_for('index'))

@app.route('/estudiante/modificar/<id>', methods=['GET', 'POST'])
def modificar_estudiante(id):
    if request.method == 'POST':
        EstudianteModel.actualizar(
            id,
            request.form['atri_1_M_E'],
            request.form['atri_2_M_E'],
            request.form['atri_3_M_E'],
            request.form['atri_4_M_E']
        )
        return redirect(url_for('index'))
    
    est = EstudianteModel.obtener_por_id(id)
    return render_template('estudiante/modificar.html', estudiante=est)

@app.route('/estudiante/eliminar/<id>', methods=['GET'])
def eliminar_estudiante(id):
    EstudianteModel.eliminar(id)
    return redirect(url_for('index'))

# Funciones para tabla docente

@app.route('/docente/agregar', methods=['POST'])
def agregar_docente():
    DocenteModel.insertar(
        request.form['atri_1_L_D'],
        request.form['atri_2_L_D'],
        request.form['atri_3_L_D'],
        request.form['atri_4_L_D'],
        request.form['atri_5_L_D']
    )
    return redirect(url_for('index'))

@app.route('/docente/modificar/<id>', methods=['GET', 'POST'])
def modificar_docente(id):
    if request.method == 'POST':
        DocenteModel.actualizar(
            id,
            request.form['atri_1_M_D'],
            request.form['atri_2_M_D'],
            request.form['atri_3_M_D'],
            request.form['atri_4_M_D']
        )
        return redirect(url_for('index'))
    
    doc = DocenteModel.obtener_por_id(id)
    return render_template('docente/modificar.html', docente=doc)

@app.route('/docente/eliminar/<id>', methods=['GET'])
def eliminar_docente(id):
    DocenteModel.eliminar(id)
    return redirect(url_for('index'))

# Funciones para tabla materia

@app.route('/materia/agregar', methods=['POST'])
def agregar_materia():
    MateriaModel.insertar(
        request.form['atri_1_L_M'],
        request.form['atri_2_L_M'],
        request.form['atri_3_L_M']
    )
    return redirect(url_for('index'))

@app.route('/materia/modificar/<id>', methods=['GET', 'POST'])
def modificar_materia(id):
    if request.method == 'POST':
        MateriaModel.actualizar(
            id,
            request.form['atri_1_M_M'],
            request.form['atri_2_M_M'],
            request.form['atri_3_M_M']
        )
        return redirect(url_for('index'))
    
    mat = MateriaModel.obtener_por_id(id)
    return render_template('materia/modificar.html', materia=mat)

@app.route('/materia/eliminar/<id>', methods=['GET'])
def eliminar_materia(id):
    MateriaModel.eliminar(id)
    return redirect(url_for('index'))

# Funciones para tabla paralelo

@app.route('/paralelo/agregar', methods=['POST'])
def agregar_paralelo():
    ParaleloModel.insertar(
        request.form['atri_1_L_P'],
        request.form['atri_2_L_P'],
        request.form['atri_3_L_P']
    )
    return redirect(url_for('index'))

@app.route('/paralelo/modificar/<id>/<id_mat>/<id_doc>', methods=['GET', 'POST'])
def modificar_paralelo(id, id_mat, id_doc):
    if request.method == 'POST':
        ParaleloModel.actualizar(
            id,
            request.form['atri_1_M_P'],
            request.form['atri_2_M_P'],
            request.form['atri_3_M_P']
        )
        return redirect(url_for('index'))
    
    par = ParaleloModel.obtener_por_id(id, id_mat, id_doc)
    mats = MateriaModel.listar()
    docs = DocenteModel.listar()
    
    return render_template('paralelo/modificar.html', paralelo=par, materias=mats, docentes=docs)

@app.route('/paralelo/eliminar/<id>/<id_mat>/<id_doc>', methods=['GET'])
def eliminar_paralelo(id, id_mat, id_doc):
    ParaleloModel.eliminar(id, id_mat, id_doc)
    return redirect(url_for('index'))

# Funciones para tabla inscrito

@app.route('/inscrito/agregar', methods=['POST'])
def agregar_inscrito():
    InscritoModel.insertar(
        request.form['atri_1_L_I'],
        request.form['atri_2_L_I'],
        request.form['atri_3_L_I']
    )
    return redirect(url_for('index'))

@app.route('/inscrito/modificar/<id>/<id_par>/<id_est>', methods=['GET', 'POST'])
def modificar_inscrito(id, id_par, id_est):
    if request.method == 'POST':
        InscritoModel.actualizar(
            id,
            request.form['atri_1_M_I'],
            request.form['atri_2_M_I'],
            request.form['atri_3_M_I']
        )
        return redirect(url_for('index'))
    
    ins = InscritoModel.obtener_por_id(id, id_par, id_est)
    par = ParaleloModel.listar()
    est = EstudianteModel.listar()
    
    return render_template('inscrito/modificar.html', inscrito=ins, paralelos=par, estudiantes=est)

@app.route('/inscrito/eliminar/<id>/<id_par>/<id_est>', methods=['GET'])
def eliminar_inscrito(id, id_par, id_est):
    InscritoModel.eliminar(id, id_par, id_est)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=3000, debug=True)