# post functions
from flask import render_template, request, flash, url_for
from werkzeug.utils import redirect

from . import login_manager, models, forms, db
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime
from app.models import User, Customer

def index():
    customer = models.Customer.query.all()
    super_customer = models.Customer.query.filter_by(is_boom_news=True).first()
    return render_template("index.html", customer=customer, super_customer=super_customer)

@login_required
def customer_create():
    form = forms.CustomerForm()
    if request.method == "POST":
        if form.validate_on_submit():
            name = request.form.get('name')
            phone_number = request.form.get('phone_number')
            item = request.form.get('item')
            quantity = request.form.get('quantity')
            price = request.form.get('price')
            new_customer = models.Customer(name=name,phone_number=phone_number,item=item, quantity=quantity, price=price)
            db.session.add(new_customer)
            db.session.commit()
            flash("ВЫ ЗАРЕг")
            return redirect(url_for("index"))
        elif form.errors:
            for errors in form.errors.values():
                for error in errors:
                    flash(error, category="danger")
        return render_template("customer_create.html", form=form)


def customer_detail(customer_id):
    customer = Customer.query.filter_by(id=customer_id).first()
    if customer:
        return render_template("customer_detail.html", customer=customer)
    else:
        flash("Клиент не найден", category="danger")
        return render_template(url_for("index"))

@login_required
def customer_delete(customer_id):
    customer = Customer.query.filter_by(id=customer_id).first()
    if customer:
        if request.method == "POST":
            db.session.delete(customer)
            db.session.commit()
            flash("Клиент удален", category="success")
            return redirect(url_for("customer"))
        else:
            form = forms.CustomerForm()
            return render_template("customer_delete.html", customer=customer, form=form)
    else:
        flash("Клиент не найден", category="danger")
        return redirect(url_for("customer"))

@login_required
def customer_update(customer_id):
    customer = Customer.query.filter_by(id=customer_id).fisrt()
    if customer:
        form = forms.CustomerForm(obj=customer)
        if request.method == "POST":
            if form.validate_on_submit():
                name = request.form.get('name')
                phone_number = request.form.get("phone_number")
                item = request.form.get("item")
                quantity = request.form.get("quantity")
                price = request.form.get("price")
                user = request.form.get("user")
                customer.name = name
                customer.phone_number = phone_number
                customer.item = item
                customer.quantity = quantity
                customer.price = price
                customer.user = user
                db.session.commit()
                return redirect(url_for("customer"))
            if form.errors:
                for errors in form.errors.values():
                    for error in errors:
                        flash(error, category="danger")
        return render_template("customer_update.html", form=form, customer=customer)
    else:
        flash("Клиент не найден", category="danger")
        return redirect(url_for("customer"))









# user functions

def register():
    user_form = forms.UserForm()
    if request.method == "POST":
        if user_form.validate_on_submit():
            username = request.form.get("username")
            password = request.form.get("password")
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash("Пользователь успешно зарегистрировался", category="success")
            return redirect(url_for("login"))
        if user_form.errors:
            for errors in user_form.errors.values():
                for error in errors:
                    flash(error, category="danger")
    return render_template("register.html", form=user_form)


def login():
    user_form = forms.UserForm()
    if request.method == "POST":
        if user_form.validate_on_submit():
            username = request.form.get("username")
            password = request.form.get("password")
            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                login_user(user)
                flash("Вы успешно зашли в систему", category="success")
                return redirect(url_for("customer"))
            else:
                flash("Неверный логин или пароль", category="danger")
                return render_template("login.html", form=user_form)
        if user_form.errors:
            for errors in user_form.errors.values():
                for error in errors:
                    flash(error, category="danger")
    return render_template("login.html", form=user_form)

def logout():
    logout_user()
    flash('Вы успешно вышли из системы', category='success')
    return redirect(url_for('login'))
