from flask import Flask, render_template, request
import os

print("APP LOADED")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
   if request.method == 'POST':
      namaDepan = request.form['namaDepan']
      namaBelakang = request.form['namaBelakang']

      nama = '%s %s' % (namaDepan, namaBelakang)

      p = nama
      C = ''
      k = 3

      for i in range(len(p)):
         c = chr(ord(p[i]) + k)
         C = C + c

      return render_template('response.html', nama=C)

   return render_template('form.html')

if __name__ == '__main__':
   port = int(os.environ.get("PORT", 5000))
   app.run(host='0.0.0.0', port=port)
