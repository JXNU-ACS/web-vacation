#coding=utf-8
from flask import Flask,request,json,jsonify,abort
from functools import wraps

app = Flask(__name__)

students = [
    {
        'id': 1,
        'name': u'William',
        
    },
    {
        'id': 2,
        'name': u'Tom',

    }
]

@app.errorhandler(404)
def not_found(error):
	message = {
		'status':404,
		'text':'the url:'+request.url+' Not Found'
	}
	response = jsonify(message)
	response.status_code = 404
	return response

@app.route('/',methods=['GET'])
def index():
	return jsonify({'students' : students})

@app.route('/students/<int:id>',methods=['GET'])
def get_student(id):
    student = filter(lambda t: t['id'] == id ,students)
    return jsonify({'students': student})

@app.route('/messages',methods = ['POST'])
def api_message():
	if request.headers['Content-Type'] == 'text/plain':
		return 'text:'+request.data
	elif request.headers['Content-Type']  == 'application/json':
		return 'JSON:'+json.dumps(request.json)
	elif request.headers['Content-Type']  == 'application/octet-stream':
		with open('demo.txt','wb') as f:
			f.write(request.data)
		return 'a demo.txt has been written!'
	else:
		return 	'unsupported media type'

@app.route('/students',methods = ['POST'])
def create_student():
	if not request.json or not 'name' in request.json:
		abort(400)
	student = {
		'id' : students[-1]['id']+1,
		'name': request.json['name']
	}
	students.append(student)
	return jsonify({'students': student})

@app.route('/students/<int:id>',methods=['DELETE'])
def delete_students(id):
	student = filter(lambda t:t['id']==id,students)
	if len(student) == 0:
		abort(404)
	students.remove(student[0])
	return jsonify({'students': student})

@app.route('/students/<int:id>',methods=['PUT'])
def update_students(id):
	student = filter(lambda t:t['id']==id,students)
	if len(student) == 0:
		abort(404)
	if not request.json:
		abort(400)
	if 'name' in request.json and type(request.json['name']) != unicode:
		abort(400)
	student[0]['name'] = request.json.get('name',student[0]['name'])
	return jsonify({'students':student[0]['name']})

#test basic auth
def check_auth(username,password):
	return username == 'admin' and password == 'admin'

def no_authenticate():
	message = {'message':'Authenticate.'}
	response = jsonify(message)
	response.status_code = 401
	response.headers['WWW-Authenticate'] = 'Basic '
	return response

def required_auth(f):
	@wraps(f)
	def decorated(*args,**kwargs):
		auth = request.authorization
		if not auth or not check_auth(auth.username,auth.password):
			return no_authenticate()
		return f(*args,**kwargs)
	return decorated

@app.route('/secrets')
@required_auth
def secretes():
	return 'you have auth'


if __name__ == '__main__':
	app.run()