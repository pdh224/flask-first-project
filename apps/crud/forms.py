from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,DateField,IntegerField
from wtforms.validators import DataRequired
#wtforms.validators:유효성 검증 관련 모듈
#DataRequired:이 필드는 반드시 값을 써야 하는 필드
#Email:이메일 형식을 반드시 지켜야 하는 필드
#length:입력한 값의 길이 관련
class UserForm(FlaskForm):
    days=DateField(
        "날짜",
        validators=[
            DataRequired(message="날짜 입력은 필수입니다."),
        ],
    )
    amWeather=StringField(
        "오전 날씨",
        validators=[
            DataRequired(message="오전 날씨는 필수입니다."),
        ],
    )
    pmWeather=StringField(
        "오후 날씨",
        validators=[
            DataRequired(message="오후 날씨는 필수입니다."),
        ],
    )
    temmin=IntegerField(
        "최저 기온",
        validators=[
            DataRequired(message="최저 기온은 필수입니다."),
        ],
    )
    temmax=IntegerField(
        "최고 기온",
        validators=[
            DataRequired(message="최고 기온은 필수입니다."),
        ],
    )
    submit = SubmitField("신규 등록")