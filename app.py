from flask import Flask, request

app = Flask(__name__)

@app.route('/notify', methods=['POST'])
def notify():
    print("✅ success")
    return "Received", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
