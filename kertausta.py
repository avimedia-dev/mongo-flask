from mongo_connection import *
client = connect()
db = client['taskDB']
col = client['task_collection']

document = {
    "name": "Taitotalo",
    "adress": "Valimotie 8",
    "phone": 2312312312,

}

