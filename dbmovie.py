from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:<password>@cluster0.mvesofx.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

user = db.movies.find_one({'title':'가버나움'})
print(movie['star'])