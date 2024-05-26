from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from aws_keyspace_conn import DataExtraction  # Assuming this file contains your database connection code
from cross_traders import sendCrossBorderMail
from mail import sendMail
from market_snapshots import sendMarketSnapshotMail
from psp import sendPSPMail  # Assuming this file contains your email sending function

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests, if needed

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_marketsnapshot', methods=['POST'])
def send_market_snapshot():
    try:
        sendMarketSnapshotMail()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})
    
@app.route('/send_psp', methods=['POST'])
def send_psp():
    try:
        sendPSPMail()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})
    
@app.route('/send_crossborder', methods=['POST'])
def send_crossborder():
    try:
        sendCrossBorderMail()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=False)
