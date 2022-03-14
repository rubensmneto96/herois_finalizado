# -*- coding: utf-8 -*-

from OFS import SimpleItem
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.ZSQLMethods.SQL import SQL
from Globals import package_home
import os

global product_path
product_path = os.path.join(package_home(globals())) + '/'

class Herois(SimpleItem.SimpleItem):
    """Classe Heroi com suas configuracoes"""
    
    meta_type = "cadastro de Herois"
    
    manage_options = (
        {'label': 'View', 'action': 'index_html',},
    )
    
    # Paginas
    index = PageTemplateFile('Main/index_html', globals())
    cadHerois = PageTemplateFile('Cadastro/cad', globals())
    cadSuccess = PageTemplateFile('Cadastro/cadSuccess', globals())
    editHerois = PageTemplateFile('Cadastro/edit', globals())
    editSuccess = PageTemplateFile('Cadastro/editSuccess', globals())
    deleteHerois = PageTemplateFile('Cadastro/delete', globals())
    delSuccess = PageTemplateFile('Cadastro/deleteSuccess', globals())
    listHerois = PageTemplateFile('Cadastro/list', globals())
    
    # Macros
    nav = PageTemplateFile('templates/nav', globals())
    foot = PageTemplateFile('templates/foot', globals())
    
    # CSS
    style = PageTemplateFile('css/style.css', globals())
    
    # SQL
    
    insert_heroi = SQL(
        id='insert_heroi', title='', connection_id='herois_connection',
        arguments='nome\nidade\npoder', template=open(
            product_path + 'sql/insert_heroi.sql').read()
    )
    
    select_herois = SQL(
        id='select_herois', title='', connection_id='herois_connection',
        arguments='', template=open(
            product_path + 'sql/select_herois.sql').read()
    )
    
    edit_heroi = SQL(
        id='edit_heroi', title='', connection_id='herois_connection',
        arguments='id_heroi\nnome\nidade\npoder', template=open(
            product_path + 'sql/edit_heroi.sql').read()
    )
    
    delete_heroi = SQL(
        id='delete_heroi', title='', connection_id='herois_connection',
        arguments='id_heroi', template=open(
            product_path + 'sql/delete_heroi.sql').read()
    )
    
    selectSpecific = SQL(
        id='selectSpecific', title='', connection_id='herois_connection',
        arguments='id_heroi', template=open(
            product_path + 'sql/selectSpecific.sql').read()
    )
    
    
    def __init__(self, id, herois_connection):
        """Inicializa Heroi"""
        self.id = id
        self.herois_connection = herois_connection
    
    # Redirecionamento para paginas
    
    def index_html(self):
        """Redireciona para pagina index_html com informacoes do heroi"""
        return self.index()
    
    def cadastrar(self):
        """Redireciona para a pagina de cadastro de herois"""
        return self.cadHerois()
    
    
    def editar(self):
        """Redireciona para a pagina para editar informacoes do heroi"""
        return self.editHerois()
    
    def listar(self):
        """Redireciona para a pagina que lista os herois cadastrados"""
        return self.listHerois()
    
    def deletar(self):
        """Redireciona para a pagina que deleta o heroi"""
        return self.deleteHerois()
    
    # Funcoes para o banco de dados
    
    def insert(self, nome, idade, poder):
        """Insere dados dos herois"""
        
        self.insert_heroi(
            nome=nome, idade=idade, poder=poder
        )
        
        msg = nome + " cadastrado com sucesso"
        
        return self.cadSuccess(msg=msg)
    
    def select(self):
        """Mostra todos os herois cadastrados"""

        return self.select_herois()
    
    def selSpecific(self):
        """Seleciona um heroi especifico"""
        
        return self.selectSpecific()
    
    def edit(self, id_heroi, nome, idade, poder):
        """Edita heroi"""
        
        self.edit_heroi(
            id_heroi=id_heroi, nome=nome, idade=idade, poder=poder
        )
        
        msgEdit = nome + ' editado com sucesso.'
        
        return self.editSuccess(msgEdit=msgEdit)
    
    def delete(self, id_heroi):
        """Deleta heroi"""
        
        self.delete_heroi(
            id_heroi=id_heroi
        )
        
        msgDelete = "Heroi deletado com sucesso"
        
        return self.delSuccess(msgDelete=msgDelete)
    
    
def manage_addHeroisSite(self, id, herois_connection='herois_connection', RESPONSE=None):
    """Adiciona Herois em uma pasta"""
    conexao = getattr(self, herois_connection)
    self._setObject(id, Herois(id, conexao))
    RESPONSE.redirect(id + '/index_html')
    

manage_addHeroisSiteForm = PageTemplateFile('Main/add_site_id', globals())


nav = PageTemplateFile('templates/nav', globals())
foot = PageTemplateFile('templates/foot', globals())