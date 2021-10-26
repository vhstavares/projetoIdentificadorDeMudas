from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
import os
import time
import loadModel as lM

app = Flask(__name__)
app.config['UPLOAD_PATH'] = os.path.dirname(os.path.abspath(__file__)) + '/uploads'

titulo = "Analisador de Mudas"

@app.route('/')
def index():
    return render_template('index.html', titulo=titulo, retorno='', imagem = "homeSeed.png")


@app.route('/analize', methods=['POST', 'GET'])
def analize():
    if request.method == 'POST':
        try:
            print(request.files['arquivo'])
            arquivo = request.files['arquivo']
            upload_path = app.config['UPLOAD_PATH']
            timestamp = time.time()
            imagem = f'{upload_path}/seed-{timestamp}.jpg'
            arquivo.save(imagem)
            retornImagem = lM.analise(imagem)
            print(retornImagem)
            return render_template(
                'index.html',
                titulo=titulo,
                retorno=retornImagem,
                imagem = "homeSeed.png"
            )
        except Exception as e:
            print(e)
            return render_template(
                'index.html',
                titulo=titulo,
                retorno=str(e),
                imagem="homeSeed.png"
            )
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
