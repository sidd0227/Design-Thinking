

from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

csv_file = 'dt.csv'
df = pd.read_csv(csv_file)

df['ph'] = df['ph'].astype(float)
df['temp'] = df['temp'].astype(float)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    input_data = [None] * 5  
    if request.method == 'POST':
        input_data[0] = request.form['N']
        input_data[1] = request.form['P']
        input_data[2] = request.form['K']
        input_data[3] = request.form['temp']
        input_data[4] = request.form['ph']
        

        result = find_output(input_data)

    return render_template('search_csv.html', input_data=input_data, result=result)

def find_output(input_data):
    try:
        result = df[(df['N'] == int(input_data[0])) & (df['P'] == int(input_data[1])) & 
                    (df['K'] == int(input_data[2])) & (round(df['ph'],2) == round(float(input_data[4]),2)) & (df['temp'] == float(input_data[3]))]['label'].iloc[0]
        return result
    except IndexError:
        return 'No matching data found.'

if __name__ == '__main__':
    app.run(debug=True)
