
from apps.app import db
from apps.auth.forms import SignUpForm, LoginForm
from apps.crud.models import Acount
from flask import Blueprint,render_template,flash,url_for,redirect,request
from flask_login import login_user, logout_user


auth=Blueprint(
    "auth",
    __name__,
    template_folder="templates",
    static_folder="static"
)
@auth.route("/")
def index():
    users=Acount.query.all()
    return render_template("auth/index.html",users=users)

@auth.route("/signup",methods=["GET","POST"])
def signup():
    form=SignUpForm()
    if form.validate_on_submit():
        user=Acount(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        if user.is_duplicate_email():
            flash("지정 이메일 주소는 이미 등록되어 있습니다")
            return redirect(url_for("auth.signup"))
        db.session.add(user)
        db.session.commit()
        login_user(user)
        next_=request.args.get("next")
        if next_ is None or not next_.startswith("/"):
            next_=url_for("crud.users")
        return redirect(next_)
    return render_template("auth/signup.html", form=form)

@auth.route("/login", methods=["GET","POST"])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user=Acount.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for("crud.index"))
        flash("메일 주소 또는 비밀번호가 일치하지 않습니다")

    return render_template("auth/login.html",form=form)

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("crud.index"))

# @auth.route("/users")
# def users():
#     users=Acount.query.all()
#     return render_template("auth/index.html")

@auth.route("/<user_id>",methods=["GET","POST"])
def edit_user(user_id):
    form=SignUpForm()
    user=Acount.query.filter_by(id=user_id).first()
    if form.validate_on_submit():
        user.username=form.username.data
        user.email=form.email.data
        user.password=form.password.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("crud.index"))
    return render_template("auth/edit.html",user=user, form= form)

@auth.route("/<user_id>/delete", methods=["POST"])
def delete_user(user_id):
    user=Acount.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("auth.index"))



