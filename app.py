from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Ruta principal - Menú
@app.route("/")
def index():
    return render_template("index.html")

# Ruta para el formulario de inscripción
@app.route("/inscripcionCurso", methods=['GET', 'POST'])
def inscripcion():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellidos = request.form.get('apellidos')
        curso = request.form.get('curso')
        return redirect(url_for('index'))
    return render_template("inscripcionCurso.html")

# Ruta para el registro de usuarios
@app.route("/registroUsuarios", methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellidos = request.form.get('apellidos')
        email = request.form.get('email')
        password = request.form.get('password')
        # Aquí puedes agregar la lógica para procesar los datos
        return redirect(url_for('index'))
    return render_template("registroUsuarios.html")

# Ruta para el registro de productos
@app.route("/registroProductos", methods=['GET', 'POST'])
def productos():
    if request.method == 'POST':
        producto = request.form.get('producto')
        categoria = request.form.get('categoria')
        existencia = request.form.get('existencia')
        precio = request.form.get('precio')
        # Aquí puedes agregar la lógica para procesar los datos
        return redirect(url_for('index'))
    return render_template("registroProductos.html")

# Ruta para el registro de libros
@app.route("/registroLibros", methods=['GET', 'POST'])
def libros():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        autor = request.form.get('autor')
        resumen = request.form.get('resumen')
        medio = request.form.get('medio')
        # Aquí puedes agregar la lógica para procesar los datos
        return redirect(url_for('index'))
    return render_template("registroLibros.html")

if __name__ == "__main__":
    app.run(debug=True)