from collections import Counter
from flask import Flask, render_template, url_for, request, redirect, Response, session, escape
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
app.secret_key = '(G+KbPeShVmYq3t6w9z$C&E)H@McQfTjWnZr4u7x!A%D*G-JaNdRgUkXp2s5v8y/'

# Models
class Quiz(db.Model):
    quiz_id = db.Column(db.Integer, primary_key=True)
    quiz_name = db.Column(db.String(200), nullable=False)
    questions = db.relationship("Question")
    user = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    def __str__(self):
        return '<Quiz ' + str(self.quiz_id) + ', ' + str(self.quiz_name) + '>'

    def __repr__(self):
        return '<Quiz ' + str(self.quiz_id) + ', ' + str(self.quiz_name) + '>'

class Question(db.Model):
    question_id = db.Column(db.Integer, primary_key=True)
    question_name = db.Column(db.String(200), nullable=False)
    answers = db.relationship("Answer")
    quiz = db.Column(db.Integer, db.ForeignKey('quiz.quiz_id'))

    def __str__(self):
        return '<Question ' + str(self.question_id) + ', ' + str(self.question_name) + '>'

    def __repr__(self):
        return '<Question ' + str(self.question_id) + ', ' + str(self.question_name) + '>'

class Answer(db.Model):
    answer_id = db.Column(db.Integer, primary_key=True)
    answer_name = db.Column(db.String(200), nullable=False)
    result = db.Column(db.String(200), nullable=False)
    question = db.Column(db.Integer, db.ForeignKey('question.question_id'))

    def __str__(self):
        return '<Answer ' + str(self.answer_id) + ', ' + str(self.answer_name) + '>'

    def __repr__(self):
        return '<Answer ' + str(self.answer_id) + ', ' + str(self.answer_name) + '>'

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    quiz = db.relationship("Quiz")

    def __str__(self):
        return '<User ' + str(self.user_id) + ', ' + str(self.username) + '>'

    def __repr__(self):
        return '<User ' + str(self.user_id) + ', ' + str(self.username) + '>'

# Web Views
@app.route('/')
def index():
    print(session)
    return render_template('index.html')

@app.route('/create/quiz', methods=['POST', 'GET'])
def create_quiz():
    if request.method == 'POST':
        try: 
            # get input
            quiz_name = request.form.get('quizTitle', None)

            # check if unique
            count = Quiz.query.filter_by(quiz_name=quiz_name).count()
            if count > 0:
                return render_template('create_quiz.html', message="Quiz creation failed. The quiz name is taken.")

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
            quiz = Quiz(quiz_name=quiz_name, user=session['user_id'])
            db.session.add(quiz)
            db.session.commit()

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
            quiz.questions.append(question_one)
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
            quiz.questions.append(question_two)
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
            quiz.questions.append(question_three)
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
            quiz.questions.append(question_four)
            db.session.commit()
            
        except Exception as e:
            return render_template('create_quiz.html', message="The quiz could not be created.")
        return redirect('/view/all/quizzes')
    else:
        return render_template('create_quiz.html')

    
@app.route('/take/quiz/<int:id>', methods=['POST', 'GET'])
def take_quiz(id):
    quiz_object = Quiz.query.filter_by(quiz_id=id).first_or_404()
    results = []
    if request.method == "POST":
        for question in quiz_object.questions:
            result = request.form.get(str(question.question_id), -5)
            results.append(result)
        final_result = Counter(results).most_common(1)[0][0]
        url = "/take/quiz/" + str(id)
        return render_template("result.html", result=final_result, url=url)
    return render_template('take_quiz.html', quiz=quiz_object)

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/view/all/quizzes')
def view_all_quizzes():
    quiz_objects = Quiz.query.order_by(Quiz.quiz_id).all()
    return render_template('view_all_quizzes.html', quiz= quiz_objects)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        session.pop('username', None)
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        count = User.query.filter_by(username=username).count()
        if count > 0:
            print(username)
            print(password)
            user_object = User.query.filter_by(username=username).first_or_404()
            if password == user_object.password:
                session['username'] = username
                session['user_id'] = user_object.user_id
                return redirect(url_for('index'))
            else:
                return render_template('login_register.html', message="Login failed.")
        else:
            return render_template('login_register.html', message="Login failed.")
    return render_template('login_register.html')

@app.route('/logout')
def logout():
    if session['username']:
        session.pop('username', None)
        session.pop('user_id', None)
    return redirect(url_for('index'))

@app.route('/edit/quiz/<int:id>', methods=['POST', 'GET'])
def edit_quiz(id):
    quiz_object = Quiz.query.filter_by(quiz_id=id).first_or_404()
    if request.method == "POST":
        quiz_name = request.form.get('quizTitle', None)
        result_one = request.form.get('resultOne', None)
        result_two = request.form.get('resultTwo', None)
        result_three = request.form.get('resultThree', None)
        result_four = request.form.get('resultFour', None)

        question_one = request.form.get('question_1', None)
        question_one_answer_one = request.form.get('questionAnswer_1_1', None)
        question_one_answer_two = request.form.get('questionAnswer_1_2', None)
        question_one_answer_three = request.form.get('questionAnswer_1_3', None)
        question_one_answer_four = request.form.get('questionAnswer_1_4', None) 

        question_two = request.form.get('question_2', None)
        question_two_answer_one = request.form.get('questionAnswer_2_1', None)
        question_two_answer_two = request.form.get('questionAnswer_2_2', None)
        question_two_answer_three = request.form.get('questionAnswer_2_3', None)
        question_two_answer_four = request.form.get('questionAnswer_2_4', None)

        question_three = request.form.get('question_3', None)
        question_three_answer_one = request.form.get('questionAnswer_3_1', None)
        question_three_answer_two = request.form.get('questionAnswer_3_2', None)
        question_three_answer_three = request.form.get('questionAnswer_3_3', None)
        question_three_answer_four = request.form.get('questionAnswer_3_4', None)
         
        question_four = request.form.get('question_4', None)
        question_four_answer_one = request.form.get('questionAnswer_4_1', None)
        question_four_answer_two = request.form.get('questionAnswer_4_2', None)
        question_four_answer_three = request.form.get('questionAnswer_4_3', None)
        question_four_answer_four = request.form.get('questionAnswer_4_4', None)
        
        quiz_object.quiz_name = quiz_name
        for x, question in enumerate(quiz_object.questions): 
            if x == 0:
                question.question_name = question_one
                for y, answer in enumerate(question.answers):
                    if y == 0:
                        answer.answer_name = question_one_answer_one
                    elif y == 1:
                        answer.answer_name = question_one_answer_two
                    elif y == 2:
                        answer.answer_name = question_one_answer_three
                    else:
                        answer.answer_name = question_one_answer_four
                db.session.commit()
            elif x == 1:
                question.question_name = question_two
                for y, answer in enumerate(question.answers):
                    if y == 0:
                        answer.answer_name = question_two_answer_one
                    elif y == 1:
                        answer.answer_name = question_two_answer_two
                    elif y == 2:
                        answer.answer_name = question_two_answer_three
                    else:
                        answer.answer_name = question_two_answer_four
                db.session.commit()
            elif x == 2:
                question.question_name = question_three
                for y, answer in enumerate(question.answers):
                    if y == 0:
                        answer.answer_name = question_three_answer_one
                    elif y == 1:
                        answer.answer_name = question_three_answer_two
                    elif y == 2:
                        answer.answer_name = question_three_answer_three
                    else:
                        answer.answer_name = question_three_answer_four
                db.session.commit()
            else:
                question.question_name = question_four
                for y, answer in enumerate(question.answers):
                    if y == 0:
                        answer.answer_name = question_four_answer_one
                    elif y == 1:
                        answer.answer_name = question_four_answer_two
                    elif y == 2:
                        answer.answer_name = question_four_answer_three
                    else:
                        answer.answer_name = question_four_answer_four
                db.session.commit()
            print(question.question_name)
            db.session.commit()
        return render_template("edit_page.html", quiz=quiz_object, message="The quiz has been updated.")
    return render_template('edit_page.html', quiz=quiz_object)

@app.route('/account/<int:id>')
def account(id):
    quiz_object = Quiz.query.filter_by(user=id)
    return render_template('account_page.html', quiz=quiz_object)

@app.route('/delete/<int:id>')
def delete(id):
    quizzes = Quiz.query.filter_by(user=id)
    for quiz in quizzes:
        for question in quiz.questions:
            for answer in question.answers:
                db.session.delete(answer)
            db.session.delete(question)
        db.session.delete(quiz)
    user = User.query.filter_by(user_id=id).first_or_404()
    db.session.delete(user)
    db.session.commit()
    if session['username']:
        session.pop('username', None)
        session.pop('user_id', None)
    return redirect(url_for('index'))

    
@app.route('/delete/quiz/<int:id>')
def delete_quiz(id):
    url = '/account/' + str(session['user_id'])
    quiz = Quiz.query.filter_by(quiz_id=id).first_or_404()
    for question in quiz.questions:
        for answer in question.answers:
            db.session.delete(answer)
        db.session.delete(question)
    db.session.delete(quiz)
    db.session.commit()
    return redirect(url)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        username = request.form.get('new_username', None)
        password = request.form.get('new_password', None)
        count = User.query.filter_by(username=username).count()
        if count > 0:
            return render_template('login_register.html', message="Registration failed. The username is already taken.")
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return render_template('login_register.html', message="Registration complete. Please login with your new account.")
    return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(debug=True)

