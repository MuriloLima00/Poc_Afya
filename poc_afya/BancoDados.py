import pyodbc

server = 'Servert2csql.eastus.cloudapp.azure.com'
database = 'ApoioT2C' 
username = 'usrApoioT2C' 
password = '@PwdT2cuyr5763bG'

def FilaBanco():

    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password+'')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tbl_PLConsolidada WHERE Situacao='Aguardando'")
    #cursor.execute("SELECT * FROM tbl_PLConsolidada")
    result = cursor.fetchall()

    '''
    print('')
    for linha in result:
        print(linha[1]+', '+linha[8])
    print('')
    '''

    conn.close()

    return result

def attFila(situacao,ies,coligada,filial):
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password+'')
    cursor = conn.cursor()

    cursor.execute("UPDATE tbl_PLConsolidada SET Situacao='"+situacao+"' WHERE IES='"+ies+"' AND COLIGADA='"+coligada+"' AND FILIAL='"+filial+"'")
    cursor.commit()

    conn.close()
