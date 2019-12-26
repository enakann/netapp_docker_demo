from flask import Flask,request,jsonify,render_template
from flask_restful import Api,Resource
import redis
import copy
import redis

app=Flask(__name__)

api=Api(app)
r = redis.Redis(host='redis-server', port=6379, db=0)
count=0
r.set('count',count)
storecontents=[
    {
        "director":"QuentinTorantino",
        "movies":[
            {
                "name":"Django Unchained",
                "lead":"Jamie Foxx"
            },
            {
                "name":"kill bill",
                "lead":"uma thurma"
            },
        ]
    },
{
        "director":"David fincher",
        "movies":[
            {
                "name":"Fight club",
                "lead":"Brad pitt"
            }
        ]
    }
]

def geturl_fordata(ls):
    copy_ls=copy.deepcopy(ls)
    newcontent=[]
    for item in copy_ls:
        item["url"]="http://127.0.0.1:5000/directors/{}".format(item["director"])
        newcontent.append(item)
    return newcontent

@app.route("/")
def home():
    return render_template("index.html")


class Store(Resource):
    def get(self):
        count=int(r.get('count'))
        count+=1
        r.set('count',count)
        new_storecontents = geturl_fordata(storecontents)
        new_storecontents.append({'count':count})
        return jsonify({"storecontents":new_storecontents})

    def post(self):
        data=request.get_json()
        new_director={
            "name":data['director'],
            "movies":[]
        }
        storecontents.append(new_director)
        return {"status":200,"store":new_director}


class Item(Resource):

    def get(self,name):
        store = [x for x in storecontents if x["director"] == name][0]
        return jsonify({"stauts":200,"store":store})

    def post(self,name):
        item=request.get_json()
        for store in storecontents:
            if store["director"]==name:
                store["movies"].append(item)
                return jsonify({"status":200})





api.add_resource(Store,'/directors')

api.add_resource(Item,"/director/<string:name>")


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)
