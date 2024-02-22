from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators
from flask_bootstrap import Bootstrap5


class LoginForm(FlaskForm):
    username = StringField(label="UserName:", validators=[
        validators.length(min=6, message="At least 6 characters"),
        validators.data_required(message="Please Enter the field")])
    password = PasswordField("Password: ", validators=[validators.data_required(message="please fill out")])
    submit = SubmitField("Sign Up")


app = Flask(__name__)
app.config["SECRET_KEY"] = "Mojtaba"
# app.secret_key = "Mojtaba"
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == "mojtaba" and form.password.data == "Tekken66":
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template("login_alt.html", form=form)


@app.route("/denied")
def denied():
    return render_template("denied.html")


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
