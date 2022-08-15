#pip3 install xlrd==1.2.0

import pandas as pd

#the following data (excel_1, excel_2, TPS_1 and TPS_2) must be put by yourself
excel_1 = 'summary_spr.xlsx'
excel_2 = 'summary_icx.xlsx'
TPS_1 = 59748
TPS_2 = 33694


df_sheet1 = pd.read_excel(excel_1, sheet_name='system view', index_col=0)
df1 = df_sheet1.iloc[:,[0]]
print(df1);


df_sheet2 = pd.read_excel(excel_2, sheet_name='system view', index_col=0)
df2 = df_sheet2.iloc[:,[0]]
print(df2);

df_join = df1.join(df2, rsuffix='_right')
print(df_join)

df_join = df_join.rename(columns={'aggregated': excel_1, 'aggregated_right': excel_2})
retired_any_1 = df_join.loc['INST_RETIRED.ANY',excel_1]
retired_any_2 = df_join.loc['INST_RETIRED.ANY',excel_2]

df_join = df_join.reset_index()
df_join = df_join.rename(columns={df_join.columns[0]: 'metrics'})

tps_row = pd.DataFrame({'metrics':'TPS', excel_1:TPS_1, excel_2:TPS_2}, index=[0])
df_join = pd.concat([tps_row,df_join.loc[:]]).reset_index(drop=True)

path_lane_1 = retired_any_1/TPS_1
path_lane_2 = retired_any_2/TPS_2
path_lane_row = pd.DataFrame({'metrics':'path_lane', excel_1:path_lane_1, excel_2:path_lane_2}, index=[0])
df_join = pd.concat([path_lane_row,df_join.loc[:]]).reset_index(drop=True)

df_join['diff'] =  df_join[excel_1]/df_join[excel_2]
df_join['diff'] = df_join['diff'].apply(lambda x: format(x, '.2'))
print(df_join)

df_join.to_excel("aggregate.xlsx")
