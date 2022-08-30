#pip3 install xlrd==1.2.0

import pandas as pd

excel = 'sprE3_vs_icx8368.bak.xlsx'
excel_sheet_name = 'emon diff'
column_name = 'metrics'

df = pd.read_excel(excel, sheet_name=excel_sheet_name, index_col=0)
snoop_values = df[df[column_name].str.contains('snoop|SNOOP')]
print(snoop_values)

snoop_values.to_excel("snoop.xlsx")
