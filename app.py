from flask import Flask, jsonify
import os
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head><title>Scalingo Test</title></head>
        <body style="font-family: Arial; text-align: center; margin-top: 50px;">
            <h1>🚀 التطبيق يعمل على Scalingo!</h1>
            <p>تم النشر بنجاح</p>
            <p>الوقت الحالي: {}</p>
            <hr>
            <p>بيئة التشغيل: {}</p>
        </body>
    </html>
    '''.format(datetime.datetime.now(), os.getenv('ENVIRONMENT', 'development'))

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.datetime.now().isoformat()
    })

@app.route('/api/info')
def info():
    return jsonify({
        'app': 'Scalingo Test App',
        'version': '1.0.0',
        'port': int(os.getenv('PORT', 5000))
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
