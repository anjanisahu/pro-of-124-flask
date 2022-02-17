#get method 
#The most common method. A GET message is send, and the server returns data


# and post method
#Used to send HTML form data to the server. The data received by the POST method is not cached by the server.

#put method 
# Used to create new data or replace existing data at the specified resource.


# and delete method
#Used to delele existing data at the specified resource.


from flask import Flask , jsonify, request
app=Flask(__name__)
tasks=[
    {
        'id': 1, 
        'title': 'Buy groceries', 
        'description': 'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
    
        'id': 2, 
        'title':'Learn Python', 
        'description': 'Need to find a good Python tutorial on the web', 
        'done': False 
        
    }
]
@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please give data"
        
        },400)
    task = { 
        'id': tasks[-1]['id'] + 1, 
        'title': request.json['title'], 
        'description': request.json.get('description', ""), 
        'done': False 
        } 
    tasks.append(task)
    return jsonify({
        "status":"sucess",
        "message":"task added"
    })

@app.route("/get-data") 
def get_task(): 
    return jsonify({ 
        "data" : tasks 
        }
        )
    

        
if __name__ == '__main__':
    app.run(debug=True)




