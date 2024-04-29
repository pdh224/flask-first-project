from flask import Blueprint, render_template,redirect, url_for
from apps.crud.forms import UserForm
from apps.app import db
from apps.crud.models import User


crud= Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@crud.route("/")
def index():
    return render_template("crud/index.html")

@crud.route("/new", methods=["GET","POST"])
def create_user():
    form=UserForm()
    if form.validate_on_submit():
        user=User(
            days=form.days.data,
            amWeather=form.amWeather.data,
            pmWeather=form.pmWeather.data,
            temmin=form.temmin.data,
            temmax=form.temmax.data,
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("crud.users"))
    return render_template("crud/create.html", form=form)

@crud.route("/inf")
def users():
    users=User.query.all()
    return render_template("crud/inf.html",users=users)

@crud.route("/inf/<user_id>/delete", methods=["POST"])
def delete_user(user_id):
    user=User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("crud.users"))

@crud.route("/inf/<user_id>", methods=["GET"]) 
def users_result(user_id):
    print(user_id)
    user_src = None
    users=User.query.filter_by(id=user_id).first()
    if not users :
        return "데이터가 없어요"
    if users.amWeather=="맑음":
        user_src1="맑음.png"
    if users.amWeather=="구름":
        user_src1="구름.png"
    if users.amWeather=="흐림":
        user_src1="구름.png"
    if users.amWeather=="비":
        user_src1="비.png"
    if users.pmWeather=="맑음":
        user_src2="맑음.png"
    if users.pmWeather=="비":
        user_src2="비.png"
    if users.pmWeather=="구름":
        user_src2="구름.png"       
  
    return render_template("crud/result.html",user=users, user_src1=user_src1, user_src2=user_src2)