from flask import Flask,render_template

directors=[
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


app=Flask(__name__)
@app.route('/directors')
def web_home():
    return render_template("index.html",directors=directors)



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002)