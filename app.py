from flask import Flask # type: ignore
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Chemin du fichier dans le volume
    file_path = '/data/visites.log'
    
    # Écriture d’un log à chaque visite
    with open(file_path, 'a') as f:
        f.write('Une visite a eu lieu.\n')
    
    return 'Bonjour, Kubernetes de Flask !'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
