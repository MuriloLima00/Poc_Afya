from datetime import datetime
import os

hoje = datetime.now()
hoje = hoje.strftime('%d%m%Y')

base_path = 'C:/Csc/IES RPA/Adiantamento/Consolidação/Legado'

def createBase():
    base_hoje = base_path+'/Exportacao_'+hoje
    if(os.path.exists(base_hoje) == False):
        os.makedirs(base_hoje)

    return base_hoje

def createPaths(coligada, filial, ies):
    coligada = coligada.rjust(2,'0')
    filial = filial.rjust(2,'0')

    base_hoje = createBase()
    path_filial = base_hoje+'/'+coligada+filial+' - '+ies
    
    if(os.path.exists(path_filial) == False):
        os.makedirs(path_filial)

    return path_filial

def renameFile(path, ies, coligada, filial):
    new_nameFile = path+'/Planilha_Fies_Legado_'+ies+'_'+coligada.rjust(2,'0')+'_'+filial.rjust(2,'0')+'.xls'

    if(os.path.exists(path+'/pesquisa-aditamentos.xls') == True):
        os.rename(path+'/pesquisa-aditamentos.xls', new_nameFile)

# renameFile('C:/Csc/IES RPA/Adiantamento/Consolidação/Legado/Exportacao_15122022/0201 - UNITPAC ARAGUAINA')