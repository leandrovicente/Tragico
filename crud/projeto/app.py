from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)


class Pessoa(db.Model):
    __tablename__ = 'cliente'
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    valor = db.Column(db.String)
    codigo = db.Column(db.String)
    email = db.Column(db.String)

    def __init__(self, nome, valor, codigo, email):
        self.nome = nome
        self.valor = telefone
        self.codigo = cpf
        self.email = email


db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        valor = request.form.get('telefone')
        codigo = request.form.get('cpf')
        email = request.form.get('email')

        if nome and valor and codigo and email:
            p = Pessoa(nome, valor, codigo, email)
            db.session.add(p)
            db.session.commit()
    return redirect(url_for('index'))


@app.route('/lista')
def lista():
    listaPessoas = Pessoa.query.all()
    return render_template('lista.html', pessoas=listaPessoas)


@app.route('/deletar/<int:id>')
def deletar(id):
    pessoa = Pessoa.query.filter_by(_id=id).first()
    db.session.delete(pessoa)
    db.session.commit()

    listaPessoas = Pessoa.query.all()
    return render_template('lista.html', pessoas=listaPessoas)


@app.route('/atualizar/<int:id>', methods=['GET', 'POST'])
def atualizar(id):
    pessoa = Pessoa.query.filter_by(_id=id).first()

    if request.method == 'POST':
        nome = request.form.get('nome')
        valor = request.form.get('valor')
        codigo = request.form.get('codigo')
        email = request.form.get('email')

        if nome and telefone and cpf and email:
            pessoa.nome = nome
            pessoa.valor = valor
            pessoa.codigo = codigo
            pessoa.email = email

            db.session.commit()
            return redirect(url_for('lista'))
    return render_template('atualizar.html', pessoa=pessoa)


if __name__ == '__main__':
    app.run()
