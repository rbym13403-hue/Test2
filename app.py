from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body { font-family: Arial; text-align: center; margin-top: 50px; }
            </style>
        </head>
        <body>
            <h1>✅ التطبيق يعمل بنجاح</h1>
            <p>تم حل مشكلة وضع الشاشة</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
