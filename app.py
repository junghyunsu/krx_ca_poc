from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 데이터베이스 모델 정의
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    start = db.Column(db.String(100))
    end = db.Column(db.String(100))

# 데이터베이스 초기화
@app.before_first_request
def create_tables():
    db.create_all()

# 메인 페이지
@app.route('/')
def index():
    return render_template('index.html')

# 이벤트 가져오기
@app.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    events = [{"id": event.id, "title": event.title, "start": event.start, "end": event.end} for event in events]
    return jsonify(events)

# 이벤트 추가
@app.route('/add_event', methods=['POST'])
def add_event():
    title = request.form.get('title')
    start = request.form.get('start')
    end = request.form.get('end')
    event = Event(title=title, start=start, end=end)
    db.session.add(event)
    db.session.commit()
    return jsonify({"id": event.id})

# 이벤트 삭제
@app.route('/delete_event/<int:id>', methods=['POST'])
def delete_event(id):
    event = Event.query.get(id)
    db.session.delete(event)
    db.session.commit()
    return jsonify({"status": "deleted"})

if __name__ == '__main__':
    app.run(debug=True)

