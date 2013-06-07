import urllib.request

response = urllib.request.urlopen('http://ichart.finance.yahoo.com/table.csv?s=AAPL')
html = response.readlines()[1:21]
resp = [str(linha[:-1],'utf-8').split(',') for linha in html]
print(resp)