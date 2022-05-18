## Vammos criar a classe de comunicação com o banco de dados e as
# manipulações de registros ##

import pymysql

conn= pymysql.connect(db='cadastro',user='python',passwd='Python@123')

class Tabela_cadastro():
    def __init__(self,id=0,nome="",sobrenome="",cpf=""):
        self.id= id
        self.nome= nome
        self.sobrenome= sobrenome
        self.cpf= cpf
        
    
    def insere_user(self):
        cursor=conn.cursor()
        cursor.execute("insert into cadastro_clientes(nome,sobrenome,cpf) values ('"+self.nome+"','"+self.sobrenome+"','"+self.cpf+"')")
        conn.commit()
        cursor.close()
        
    def selectusuario(self,id):
        cursor= conn.cursor()
        cursor.execute("select * from cadastro_clientes where id ="+id+"")
        
        for regs in cursor:
            self.id= regs[0]
            self.nome= regs[1]
            self.sobrenome= regs[2]
            self.cpf= regs[3]
            
        cursor.close()
    