from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# class Question(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     question_name = db.Column(db.String(200), nullable=False)

#     # def __repr__(self):
#     #     return '<Task %r>' % self.id   

# class Answer(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     answer_name = db.Column(db.String(200), nullable=False)

# tags = db.Table('tags',
#     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
#     db.Column('page_id', db.Integer, db.ForeignKey('page.id'), primary_key=True)
# )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create/quiz')
def create_quiz():
    return render_template('create_quiz.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/view/all/quizzes')
def view_all_quizzes():
    return render_template('view_all_quizzes.html')

@app.route('/view/quiz')
def view_quiz():
    return render_template('view_quiz.html')


if __name__ == "__main__":
    app.run(debug=True)
