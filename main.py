from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import validators

openai.api_key = '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'

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins for all routes

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    user_input = data.get('input', '')

    print('User input:', user_input)

    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=f"only return a url from this prompt - {user_input}\nURL:",
      temperature=0.5,
      max_tokens=100
    )

    predicted_website = response.choices[0].text.strip()  # Process this as required

    # Check if predicted_website is a valid URL

    print(predicted_website)
    if validators.url(predicted_website):
        url = predicted_website
    else:
        url = "Invalid URL"

    return jsonify({'url': url})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
