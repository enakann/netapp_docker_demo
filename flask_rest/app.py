from flask import Flask,request,jsonify,render_template
from flask_restful import Api,Resource
import copy


app=Flask(__name__)

api=Api(app)


storecontents=[
    {
        "director":"QuentinTorantino",
        "movies":[
            {
                "name":"Django Unchained",
                "lead":"Jamie Foxx"
            }
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
        item["url"]="http://127.0.0.1:5000/director/{}".format(item["director"])
        newcontent.append(item)
    return newcontent

@app.route("/")
def home():
    return render_template("index.html")


class Store(Resource):
    def get(self):
        new_storecontents = geturl_fordata(storecontents)
        return jsonify({"storecontents":new_storecontents})

    def post(self):
        data=request.get_json()
        new_director={
            "name":data['director'],
            "movies":[]
        }
        storecontents.append(new_director)
        return {"status":200,"store":new_store}


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





api.add_resource(Store,'/director')

api.add_resource(Item,"/director/<string:name>")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
