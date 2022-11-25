from flask import Blueprint, render_template, request, redirect, url_for
from models.contatos import Contatos
from db import db

main = Blueprint('routes', __name__)

@main.route("/")
def home():
    return render_template("index.html")

@main.route("/who")
def who():
    return render_template("who.html")

@main.route("/contato", methods=["GET", "POST"])
def cont():
    if request.method == "POST":
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['comment']

        insert = Contatos(
            email = email,
            assunto = assunto,
            descricao = descricao
        )

        db.session.add(insert)
        db.session.commit()
        return redirect(url_for('routes.list'))
    return render_template("contato.html")


@main.route('/list')
def list(): 
    data = Contatos.query.all()
    return render_template('list.html', data=data)