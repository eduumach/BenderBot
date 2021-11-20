import json
import requests

fileLocal = '/home/dudu/Projetos/Python/BenderBot/'


def salva(mensagem, file_id=None):
    localImagem = None
    if file_id is not None:
        request = requests.get(
            'https://api.telegram.org/bot' + '2077508467:AAFEKBfWZdV-hog1497QBjaFTGx5ljmwjCI' + '/getFile?file_id=' + str(
                file_id))
        pegaId = json.loads(request.content)
        arquivoUrl = 'https://api.telegram.org/file/bot' + '2077508467:AAFEKBfWZdV-hog1497QBjaFTGx5ljmwjCI' + '/' + \
                     pegaId['result']['file_path']
        localImagem = fileLocal + 'eventos/imagens/' + str(len(getArquivos())) + '.png'
        imagem = requests.get(arquivoUrl)
        arquivo = open(localImagem, 'wb')
        arquivo.write(imagem.content)

    pegaDados = open(fileLocal + 'eventos/dadosEventos.json', 'r')
    dados = json.load(pegaDados)
    separarLinhas = mensagem.splitlines()
    mensagem = {"nome": separarLinhas[1][6:], "data": separarLinhas[2][6:],
                "link": separarLinhas[3][6:], "img": localImagem}
    dados['eventos'].append(mensagem)

    arquivo = open(fileLocal + 'eventos/dadosEventos.json', 'w+')
    json.dump(dados, arquivo, indent=4)


def getArquivos():
    with open(fileLocal + 'eventos/dadosEventos.json', 'r') as dadosJson:
        dados = json.load(dadosJson)
        return dados['eventos']
