from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
import os
import time

app = Flask(__name__)
app.config['UPLOAD_PATH'] = os.path.dirname(os.path.abspath(__file__)) + '/uploads'


@app.route('/')
def index():
    return render_template('index.html', titulo="Analisador de Mudas por meio de CNN", imagem="capa_padrao.jpg")


@app.route('/analize', methods=['POST', 'GET'])
def analize():
    if request.method == 'POST':
        print(request.files['arquivo'])
        arquivo = request.files['arquivo']
        upload_path = app.config['UPLOAD_PATH']
        timestamp = time.time()
        arquivo.save(f'{upload_path}/seed-{timestamp}.jpg')
        print(f'{upload_path}/seed-{timestamp}.jpg')
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
