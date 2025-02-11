from flask import Flask, render_template, request
from unidecode import unidecode

app = Flask(__name__)

# Base de dados dos produtos
produtos = [
    {"CÓDIGO": 1096, "PRODUTO": "BEIJINHO"},
    {"CÓDIGO": 17834, "PRODUTO": "BISCOITO CACETINHO"},
    {"CÓDIGO": 5913, "PRODUTO": "BISCOITO CHAMPAGNE"},
    {"CÓDIGO": 3056, "PRODUTO": "BOLACHA CAMELO"},
    {"CÓDIGO": 7481, "PRODUTO": "BOLACHA DE COCO"},
    {"CÓDIGO": 7207, "PRODUTO": "BOLACHA MIMOSA"},
    {"CÓDIGO": 2566, "PRODUTO": "BOLACHA REG INTEGRAL"},
    {"CÓDIGO": 7214, "PRODUTO": "BOLACHA REGALIA"},
    {"CÓDIGO": 7153, "PRODUTO": "BOLACHA ROSQUINHA"},
    {"CÓDIGO": 9300, "PRODUTO": "BOLINHO DE BACALHAU"},
    {"CÓDIGO": 7788, "PRODUTO": "BOLINHO DE CAMARÃO"},
    {"CÓDIGO": 9324, "PRODUTO": "BOLINHO DE CHARQUE"},
    {"CÓDIGO": 7788, "PRODUTO": "BOLINHO DE GOMA"},
    {"CÓDIGO": 4724, "PRODUTO": "BOLINHO DE PIZZA"},
    {"CÓDIGO": 9331, "PRODUTO": "BOLINHO DE QUEIJO"},
    {"CÓDIGO": 17874, "PRODUTO": "BOLO AIPIM KG"},
    {"CÓDIGO": 73309, "PRODUTO": "BOLO BACIA C/1 UN"},
    {"CÓDIGO": 73305, "PRODUTO": "BOLO BACIA C/4 UN"},
    {"CÓDIGO": 17870, "PRODUTO": "BOLO CAÇAROLA C/QUEIJO"},
    {"CÓDIGO": 1427, "PRODUTO": "BOLO CENOURA"},
    {"CÓDIGO": 17320, "PRODUTO": "BOLO CENOURA SIMPLES"},
    {"CÓDIGO": 17295, "PRODUTO": "BOLO CHOC CREMOSO"},
    {"CÓDIGO": 6927, "PRODUTO": "BOLO COM LARANJA"},
    {"CÓDIGO": 1001, "PRODUTO": "BOLO COM PASSAS"},
    {"CÓDIGO": 9751, "PRODUTO": "BOLO DE ABACAXI"},
    {"CÓDIGO": 7085, "PRODUTO": "BOLO DE AMENDOIM"},
    {"CÓDIGO": 9492, "PRODUTO": "BOLO DE BANANA"},
    {"CÓDIGO": 7450, "PRODUTO": "BOLO DE CHOCOLATE"},
    {"CÓDIGO": 7016, "PRODUTO": "BOLO DE COCADA"},
    {"CÓDIGO": 3674, "PRODUTO": "BOLO DE FRUTAS VERMELHAS"},
    {"CÓDIGO": 6293, "PRODUTO": "BOLO DE MACAXEIRA"},
    {"CÓDIGO": 6347, "PRODUTO": "BOLO DE MASSA PUBA"},
    {"CÓDIGO": 6361, "PRODUTO": "BOLO DE MILHO"},
    {"CÓDIGO": 6198, "PRODUTO": "BOLO FORMIGUEIRO"},
    {"CÓDIGO": 6149, "PRODUTO": "BOLO GOIABADA"},
    {"CÓDIGO": 2300, "PRODUTO": "BOLO INDIANO"},
    {"CÓDIGO": 6217, "PRODUTO": "BOLO INGLES"},
    {"CÓDIGO": 6316, "PRODUTO": "BOLO MAIZENA"},
    {"CÓDIGO": 6088, "PRODUTO": "BOLO MASSA PUBA"},
    {"CÓDIGO": 7177, "PRODUTO": "BOLO MESCLADO"},
    {"CÓDIGO": 7108, "PRODUTO": "BOLO PÉ DE MOLEQUE PAÇOCA"},
    {"CÓDIGO": 3063, "PRODUTO": "BRASILEIRA"},
    {"CÓDIGO": 1070, "PRODUTO": "BRIGADEIRO"},
    {"CÓDIGO": 4121, "PRODUTO": "BRIOCHE COM CÔCO"},
    {"CÓDIGO": 6095, "PRODUTO": "BRIOCHE COM CREME"},
    {"CÓDIGO": 4145, "PRODUTO": "BRIOCHE COM FRUTAS"},
    {"CÓDIGO": 6095, "PRODUTO": "BRIOCHE CREME CHOC"},
    {"CÓDIGO": 6514, "PRODUTO": "BROA DA CASA"},
    {"CÓDIGO": 6514, "PRODUTO": "BROA DA CASA"},
    {"CÓDIGO": 8174, "PRODUTO": "CAROLINA"},
    {"CÓDIGO": 9851, "PRODUTO": "COXINHA CATUPIRY"},
    {"CÓDIGO": 5227, "PRODUTO": "COXINHA DE CARNE"},
    {"CÓDIGO": 9837, "PRODUTO": "COXINHA DE FRANGO"},
    {"CÓDIGO": 953, "PRODUTO": "CROISSANT SABORES"},
    {"CÓDIGO": 1695, "PRODUTO": "DELICIA DE ABACAXI"},
    {"CÓDIGO": 6000, "PRODUTO": "DIPLOMATA"},
    {"CÓDIGO": 1020, "PRODUTO": "DOCE MARIA MOLE"},
    {"CÓDIGO": 3410, "PRODUTO": "DOCINHO"},
    {"CÓDIGO": 998949, "PRODUTO": "EMPADA"},
    {"CÓDIGO": 8419, "PRODUTO": "ENROLADINHO"},
    {"CÓDIGO": 6613, "PRODUTO": "FARINHA DE ROSCA"},
    {"CÓDIGO": 1823, "PRODUTO": "FOCACCIA"},
    {"CÓDIGO": 9913, "PRODUTO": "FOLHADO DE FRANGO"},
    {"CÓDIGO": 6965, "PRODUTO": "GALETO"},
    {"CÓDIGO": 596, "PRODUTO": "KIELZ"},
    {"CÓDIGO": 6615, "PRODUTO": "MINI COXINHA"},
    {"CÓDIGO": 953, "PRODUTO": "MINI CROISSANT"},
    {"CÓDIGO": 1631, "PRODUTO": "MOUSSE DE CHOCOLATE"},
    {"CÓDIGO": 1488, "PRODUTO": "MOUSSE DE MARACUJA"},
    {"CÓDIGO": 3346, "PRODUTO": "MOUSSE DE MORANGO"},
    {"CÓDIGO": 4144, "PRODUTO": "PAINETTOME CINCO LATE"},
    {"CÓDIGO": 6873, "PRODUTO": "PÃO BAGUETE"},
    {"CÓDIGO": 9690, "PRODUTO": "PÃO BATATA"},
    {"CÓDIGO": 7078, "PRODUTO": "PÃO BOLACHÃO"},
    {"CÓDIGO": 17864, "PRODUTO": "PÃO BRIOCHE"},
    {"CÓDIGO": 20139, "PRODUTO": "PÃO DE ALHO"},
    {"CÓDIGO": 7030, "PRODUTO": "PÃO DE FORMA"},
    {"CÓDIGO": 21933, "PRODUTO": "PÃO DE LEITE"},
    {"CÓDIGO": 34083, "PRODUTO": "PÃO DE MILHO COQU"},
    {"CÓDIGO": 7115, "PRODUTO": "PÃO DE QUEIJO"},
    {"CÓDIGO": 7496, "PRODUTO": "PÃO DELICIA"},
    {"CÓDIGO": 949, "PRODUTO": "PÃO DOCE"},
    {"CÓDIGO": 4251, "PRODUTO": "PÃO FRANCÊS"},
    {"CÓDIGO": 3822, "PRODUTO": "PÃO HAMBÚRGUER"},
    {"CÓDIGO": 3073, "PRODUTO": "PÃO HAMBÚRGUER GERGELIM"},
    {"CÓDIGO": 3957, "PRODUTO": "PÃO HOT DOG RECHEADO"},
    {"CÓDIGO": 7092, "PRODUTO": "PÃO INTEGRAL"},
    {"CÓDIGO": 6835, "PRODUTO": "PÃO ITALIANO"},
    {"CÓDIGO": 6316, "PRODUTO": "PÃO MANTEIGA"},
    {"CÓDIGO": 21931, "PRODUTO": "PÃO PORTUGUÊS"},
    {"CÓDIGO": 7122, "PRODUTO": "PÃO RECIFE"},
    {"CÓDIGO": 9317, "PRODUTO": "PÃO SALADA RUSSA"},
    {"CÓDIGO": 1984, "PRODUTO": "PASTEL DE PORNAS"},
    {"CÓDIGO": 9713, "PRODUTO": "PETIT-FOUR DE COMBA"},
    {"CÓDIGO": 4985, "PRODUTO": "PIZZA SABORES"},
    {"CÓDIGO": 7061, "PRODUTO": "PUDIM"},
    {"CÓDIGO": 9157, "PRODUTO": "ROCAMBOLE"},
    {"CÓDIGO": 6989, "PRODUTO": "SALGADINHO DE QUEIJO"},
    {"CÓDIGO": 1023, "PRODUTO": "SANDUICHE NATURAL"},
    {"CÓDIGO": 408, "PRODUTO": "SOBREMESA"},
    {"CÓDIGO": 7893, "PRODUTO": "SUSPINO"},
    {"CÓDIGO": 8648, "PRODUTO": "TORRADA DE BOLO"},
    {"CÓDIGO": 6781, "PRODUTO": "TORRADA SIMPLES"},
    {"CÓDIGO": 1441, "PRODUTO": "TORTA DE ABACAXI"},
    {"CÓDIGO": 7160, "PRODUTO": "TORTA DE BANANA"},
    {"CÓDIGO": 7054, "PRODUTO": "TORTA DE CHOCOLATE"},
    {"CÓDIGO": 1821, "PRODUTO": "TORTA DE MARACUJA"},
    {"CÓDIGO": 6491, "PRODUTO": "TORTA DE MORANGO"},
    {"CÓDIGO": 1907, "PRODUTO": "TORTA DOCE DE LEITE"},
    {"CÓDIGO": 1785, "PRODUTO": "TORTA HOLANDESA"},
    {"CÓDIGO": 6422, "PRODUTO": "TORTA LEITE CONDENS"},
    {"CÓDIGO": 1549, "PRODUTO": "TORTA MOUSSE DE LIMAO"},
    {"CÓDIGO": 69231, "PRODUTO": "TORTA SABORES"},
    {"CÓDIGO": 5104, "PRODUTO": "TORTA SALGADA"},
    {"CÓDIGO": 8485, "PRODUTO": "TORTILETE"},
    {"CÓDIGO": 34096, "PRODUTO": "TORTILLE"}
]

def normalizar_texto(texto):
    return unidecode(texto).lower()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    nome_produto = request.form['nome_produto']
    resultados = []
    nome_normalizado = normalizar_texto(nome_produto)
    for produto in produtos:
        produto_normalizado = normalizar_texto(produto["PRODUTO"])
        if nome_normalizado in produto_normalizado:
            resultados.append(produto)
    return render_template('resultados.html', resultados=resultados)

if __name__ == '__main__':
    app.run(debug=True)