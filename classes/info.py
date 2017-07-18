# coding: utf-8

class Info:
    """ Classe responsável por armazenar as informações inseridas no formulário """
    def __init__(self):
        self.montante = None
        self.taxa_juros = None
        self.parcelas = None
        self.amortizacao = None
        self.nome_arquivo = None
        self.diretorio = None

    @property
    def montante(self):
        """ Quantia a ser emprestada """
        return self.montante

    @property
    def taxa_juros(self):
        """ Taxa de juros anual que será cobrada """
        return self.taxa_juros

    @property
    def parcelas(self):
        """ Quantidade de parcelas para a dívida ser paga """
        return self.parcelas

    @property
    def amortizacao(self):
        """ Tipo de amortização utilizada (SAC, Price ou Americano) """
        return self.amortizacao

    @property
    def nome_arquivo(self):
        """ Nome do arquivo """
        return self.nome_arquivo

    @property
    def diretorio(self):
        """ Local para armazenar o arquivo """
        return self.diretorio
