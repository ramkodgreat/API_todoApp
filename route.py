from app import *
from model import *

# Get all content
@app.route('/')
def get_contents():
    all_todo = Task.query.all()
    result = todos_schema.dump(all_todo)
    return jsonify(result)

# Get a sinlge content
@app.route('/content/<int:id>')
def get_content(id):
    one_todo = Task.query.get(id)
    result = todo_schema.dump(one_todo)
    return jsonify(result)

#Post a content
@app.route('/addtodo', methods=["POST"])
def postTask(): 
    if request.method == "POST":
        request_content = request.json['content'] # geting content from client
        if request_content == " ":  # client cannot post empty task
            return jsonify({ "message": "content must not be empty please" })
        else:
            new_item =Task(content=request_content) # maping content from client to our bd

            db.session.add(new_item) # adding the client content to db
            db.session.commit() # commiting client content
            return jsonify({ "message": "content added succesful" })

# Updating a content from todo list
@app.route('/updatetodo/<int:id>', methods = ["PUT"])
def update(id):
    get_todo = Task.query.get(id) #fetch from db by id
    request_content = request.json['content'] # content field getting from client
    get_todo.content = request_content # matching content with edited content
    if request_content == " ":
        return jsonify({ "message": "content must not be empty please" })
    else:
        db.session.commit() # commiting client content
    return todo_schema.jsonify(get_todo)

# Deleting a content from todo list
@app.route('/deletetodo/<id>', methods = ["DELETE"])
def delete(id):
    try:
        content_to_delete = Task.query.get(id)
        db.session.delete(content_to_delete)
        db.session.commit()
        return jsonify({ "message": "content deleted successfully!" })
    except:   
        # No content with the  id or error in the cod
        return jsonify({ "message": "no content with such id", "status_code":404 })

#This will  handle  errors like unfound url
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Record not found for : ' + request.url + ' please refer to API documentation' 
         }
    return (message)
