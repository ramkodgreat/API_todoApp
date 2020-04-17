from app import *

class Task(db.Model):
    id =  db.Column(db.Integer, primary_key = True)
    content =  db.Column(db.Text(200), nullable = False)
    date_created =  db.Column(db.DateTime, default = datetime.utcnow)

    def __Init__(self, content):
        self.content = content   

# object serialization/deserialization 
class TodoSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "content", "date_created")
        
# for viewing a single object
todo_schema = TodoSchema()
# for viewing a single object
todos_schema = TodoSchema(many=True)
        