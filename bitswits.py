from flask import Flask, render_template, request
from openai import OpenAI  

app = Flask(__name__)


OPENAI_API_KEY = 'YOUR-API-KEY-HERE'



def get_chat(prompt):
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content  


@app.route("/bitswits/", methods=["GET", "POST"])
def bitswits():
    if request.method == 'POST':
        user_prompt = request.form['prompt']
        print("User Prompt is:", user_prompt)
        reply = get_chat(user_prompt)
        return render_template('bitswits_output.html', prompt=user_prompt, reply=reply)
    else:
        return render_template('bitswits.html')

if __name__ == "__main__":
    app.run()







