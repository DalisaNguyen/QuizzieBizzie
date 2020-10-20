from flask import Flask, render_template, url_for, request, redirect, Response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# Many-to-many fields
ans = db.Table('ans',
    db.Column('question_id', db.Integer, db.ForeignKey('question.question_id'), primary_key=True),
    db.Column('answer_id', db.Integer, db.ForeignKey('answer.answer_id'), primary_key=True)
)

ques = db.Table('ques',
    db.Column('quiz_id', db.Integer, db.ForeignKey('quiz.quiz_id'), primary_key=True),
    db.Column('question_id', db.Integer, db.ForeignKey('question.question_id'), primary_key=True)
)

# Models
class Quiz(db.Model):
    quiz_id = db.Column(db.Integer, primary_key=True)
    quiz_name = db.Column(db.String(200), nullable=False)
    questions = db.relationship("Question", secondary=ques, backref=db.backref("questions", lazy="dynamic"))

    def __str__(self):
        return '<Quiz ' + str(self.quiz_id) + ', ' + str(self.quiz_name) + '>'

    def __repr__(self):
        return '<Quiz ' + str(self.quiz_id) + ', ' + str(self.quiz_name) + '>'

class Question(db.Model):
    question_id = db.Column(db.Integer, primary_key=True)
    question_name = db.Column(db.String(200), nullable=False)
    answers = db.relationship("Answer", secondary=ans, backref=db.backref("answers", lazy="dynamic"))

    def __str__(self):
        return '<Question ' + str(self.question_id) + ', ' + str(self.question_name) + '>'

    def __repr__(self):
        return '<Question ' + str(self.question_id) + ', ' + str(self.question_name) + '>'

class Answer(db.Model):
    answer_id = db.Column(db.Integer, primary_key=True)
    answer_name = db.Column(db.String(200), nullable=False)
    result = db.Column(db.String(200), nullable=False)

    def __str__(self):
        return '<Answer ' + str(self.answer_id) + ', ' + str(self.answer_name) + '>'

    def __repr__(self):
        return '<Answer ' + str(self.answer_id) + ', ' + str(self.answer_name) + '>'



# Web Views
@app.route('/')
def index():
    # example - will be removed at the end
    quiz_object = Quiz.query.filter_by(quiz_name="What fruit should you eat?").first_or_404()
    # example terminal print statements
    print(quiz_object) # models are objects
    print(quiz_object.quiz_name)
    # to access the objects, either use a loop or first_or_404 with a filter
    for question in quiz_object.questions:
        print(question.question_name)
        print(question.answers) # the question model uses answers to connect to answer objects
        for answer in question.answers: 
            print("Answer: " + str(answer.answer_name) + "\t Result: " + str(answer.result))
        print('\n')
    return render_template('index.html', quiz=quiz_object)

@app.route('/create/quiz', methods=['POST', 'GET'])
def create_quiz():
    if request.method == 'POST':
        try: 
            # get input
            quiz_name = request.form.get('quizTitle', None)
            result_one = request.form.get('resultOne', None)
            result_two = request.form.get('resultTwo', None)
            result_three = request.form.get('resultThree', None)
            result_four = request.form.get('resultFour', None)

            question_one = request.form.get('questionOne', None)
            question_one_answer_one = request.form.get('questionOneAnswerOne', None)
            question_one_answer_two = request.form.get('questionOneAnswerTwo', None)
            question_one_answer_three = request.form.get('questionOneAnswerThree', None)
            question_one_answer_four = request.form.get('questionOneAnswerFour', None)

            question_two = request.form.get('questionTwo', None)
            question_two_answer_one = request.form.get('questionTwoAnswerOne', None)
            question_two_answer_two = request.form.get('questionTwoAnswerTwo', None)
            question_two_answer_three = request.form.get('questionTwoAnswerThree', None)
            question_two_answer_four = request.form.get('questionTwoAnswerFour', None)

            question_three = request.form.get('questionThree', None)
            question_three_answer_one = request.form.get('questionThreeAnswerOne', None)
            question_three_answer_two = request.form.get('questionThreeAnswerTwo', None)
            question_three_answer_three = request.form.get('questionThreeAnswerThree', None)
            question_three_answer_four = request.form.get('questionThreeAnswerFour', None)

            question_four = request.form.get('questionFour', None)
            question_four_answer_one = request.form.get('questionFourAnswerOne', None)
            question_four_answer_two = request.form.get('questionFourAnswerTwo', None)
            question_four_answer_three = request.form.get('questionFourAnswerThree', None)
            question_four_answer_four = request.form.get('questionFourAnswerFour', None)

            # create objects and link them
            question_one = Question(question_name=question_one)
            db.session.add(question_one)
            db.session.commit()
            answer_one = Answer(answer_name=question_one_answer_one, result=result_one)
            answer_two = Answer(answer_name=question_one_answer_two, result=result_two)
            answer_three = Answer(answer_name=question_one_answer_three, result=result_three)
            answer_four = Answer(answer_name=question_one_answer_four, result=result_four)
            db.session.add(answer_one)
            db.session.add(answer_two)
            db.session.add(answer_three)
            db.session.add(answer_four)
            db.session.commit()
            question_one.answers.append(answer_one)
            question_one.answers.append(answer_two)
            question_one.answers.append(answer_three)
            question_one.answers.append(answer_four)
            db.session.commit()

            question_two = Question(question_name=question_two)
            db.session.add(question_two)
            db.session.commit()
            answer_one = Answer(answer_name=question_two_answer_one, result=result_one)
            answer_two = Answer(answer_name=question_two_answer_two, result=result_two)
            answer_three = Answer(answer_name=question_two_answer_three, result=result_three)
            answer_four = Answer(answer_name=question_two_answer_four, result=result_four)
            db.session.add(answer_one)
            db.session.add(answer_two)
            db.session.add(answer_three)
            db.session.add(answer_four)
            db.session.commit()
            question_two.answers.append(answer_one)
            question_two.answers.append(answer_two)
            question_two.answers.append(answer_three)
            question_two.answers.append(answer_four)
            db.session.commit()

            question_three = Question(question_name=question_three)
            db.session.add(question_three)
            db.session.commit()
            answer_one = Answer(answer_name=question_three_answer_one, result=result_one)
            answer_two = Answer(answer_name=question_three_answer_two, result=result_two)
            answer_three = Answer(answer_name=question_three_answer_three, result=result_three)
            answer_four = Answer(answer_name=question_three_answer_four, result=result_four)
            db.session.add(answer_one)
            db.session.add(answer_two)
            db.session.add(answer_three)
            db.session.add(answer_four)
            db.session.commit()
            question_three.answers.append(answer_one)
            question_three.answers.append(answer_two)
            question_three.answers.append(answer_three)
            question_three.answers.append(answer_four)
            db.session.commit()
            
            question_four = Question(question_name=question_four)
            db.session.add(question_four)
            db.session.commit()
            answer_one = Answer(answer_name=question_four_answer_one, result=result_one)
            answer_two = Answer(answer_name=question_four_answer_two, result=result_two)
            answer_three = Answer(answer_name=question_four_answer_three, result=result_three)
            answer_four = Answer(answer_name=question_four_answer_four, result=result_four)
            db.session.add(answer_one)
            db.session.add(answer_two)
            db.session.add(answer_three)
            db.session.add(answer_four)
            db.session.commit()
            question_four.answers.append(answer_one)
            question_four.answers.append(answer_two)
            question_four.answers.append(answer_three)
            question_four.answers.append(answer_four)
            db.session.commit()

            quiz = Quiz(quiz_name=quiz_name)
            db.session.add(quiz)
            db.session.commit()
            quiz.questions.append(question_one)
            quiz.questions.append(question_two)
            quiz.questions.append(question_three)
            quiz.questions.append(question_four)
            db.session.commit()
        except Exception as e:
            print(e)
        return redirect('/create/quiz')
    else:
        # test for quizzes
        quizzes = Quiz.query.all()
        for q in quizzes:
            print('Quiz: ' + str(q.quiz_name))
            for qu in q.questions:
                print(qu.question_name)
                for a in qu.answers:
                    print(a.answer_name)
                print('\n')


        return render_template('create_quiz.html')

    
@app.route('/take/quiz')
def take_quiz():
    return render_template('take_quiz.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/view/all/quizzes')
def view_all_quizzes():
    return render_template('view_all_quizzes.html')

if __name__ == "__main__":
    app.run(debug=True)

