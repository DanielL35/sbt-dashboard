import pandas as pdexcel_url = 'https://sciencebasedtargets.org/resources/files/SBTiProgressReport2021AppendixData.xlsx'df = pd.read_excel(excel_url, sheet_name=1)#%%df = df.drop(0)