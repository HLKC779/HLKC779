from flask import Flask, render_template, request, flash, jsonify
from summarizer import summarize_text
import os

app = Flask(__name__)
app.secret_key = 'my_api_key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form.get('text')
    
    if not text or len(text) > 500:  # Character limit
        flash('Please enter text (max 500 characters).', 'error')
        return jsonify({'error': 'Invalid input'}), 400

    summary = summarize_text(text)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)