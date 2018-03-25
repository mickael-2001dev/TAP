from setuptools import setup

setup(
    name="tapifsul",
    version="1.0.0.0.0",
    description="Pacote da matéria de TAP",
    author="Silvio",
    author_email="silviogomez@ifsul.edu.br",
    url="www.ifsul.edu.br",
    packages=["tap_ifsul_functions", "tap_ifsul_functions.messages"]
)


# Comando para geração do arquivo distribuivel
# no mesmo diretório do arquivo setup.py executar o seguinte comando
# python setup.py sdist
# Será gerado o arquivo ../dist/tapifsul-1.0.0.0.0.tar.gz
#entrar em /dist
# pip3 install tapifsul-1.0.0.0.0.tar.gz
# Removendo o pacote
# pip3 uninstall tapifsul