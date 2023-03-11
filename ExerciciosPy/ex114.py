import urllib
import urllib.request
try:
    site=urllib.request.urlopen('https://filmestorrentdownload.com.br/')
except:
    print('O site não esta acessível no momento!')
else:
    print('Consegui acessar o site com sucesso...')
    print(site.read()) # mostra o codico todo o codigo do site