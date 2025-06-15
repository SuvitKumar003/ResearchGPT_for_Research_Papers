from flask import Flask, request, jsonify, render_template
from vectorstore.query_index import search_query

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # assuming you have a frontend template

@app.route("/query", methods=["POST"])
def handle_query():
    data = request.get_json()
    query = data.get("query", "")
    
    try:
        results = search_query(query)
        return jsonify({"results": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
