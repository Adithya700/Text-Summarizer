from flask import Flask, request, jsonify 
from summarizer import summarize_text 
 
app = Flask(__name__) 
 
@app.route("/summarize", methods=["POST"]) 
def summarize(): 
 
    data = request.json 
 
    result = summarize_text( 
        data["text"] 
    ) 
 
    return jsonify({ 
        "summary": result 
    }) 
 
if __name__ == "__main__": 
    app.run(debug=True) 