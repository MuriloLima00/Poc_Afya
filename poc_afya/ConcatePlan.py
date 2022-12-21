import pandas as pd
import xlrd
import os

def ConcatenarPlanilhas(pasta_base):
    listaPastas = os.listdir(pasta_base)
    planilhas = []
    names = []
    for pasta in listaPastas:
        if(os.path.isdir(pasta_base+'\\'+pasta) == True):
            arquivo = os.listdir(pasta_base+'\\'+pasta)
            path = pasta_base+'/'+pasta+'/'+arquivo[0]
            name = path.replace(pasta_base+'/','')
            name = name.replace('/'+arquivo[0],'')
            planXlrd = xlrd.open_workbook(path, ignore_workbook_corruption=True)
            plan = pd.read_excel(planXlrd, skiprows=12)
            planilhas+=[plan]
            names+=[name]

    consolidada = pd.concat(planilhas, keys=names)
    consolidada.to_excel(pasta_base+'/PlanilhaConsolidada.xlsx')
