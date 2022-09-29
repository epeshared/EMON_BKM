import pandas as pd

excel = 'aggregate.xlsx'
excel_sheet_name = 'Sheet1'
column_name = 'metrics'

df = pd.read_excel(excel, sheet_name=excel_sheet_name, index_col=0)
cut_values = df[df[column_name].str.contains('metric_Load_L2_Miss_Latency_using_ORO_events(ns)|metric_CHA % cyles Fast asserted|metric_CHA RxC IRQ latency (ns)|UNC_CHA_RxC_IRQ1_REJECT.PA_MATCH|UNC_CHA_RxC_OCCUPANCY.IRQ|UNC_CHA_RxC_INSERTS.IRQ|UNC_CHA_DISTRESS_ASSERTED.VERT|UNC_CHA_CLOCKTICKS')]
cut_values = cut_values.set_index('metrics')
print(cut_values)
cut_values.loc['% CHA cycles where physical address match (PA_MATCH) rejects happen'] = cut_values.loc['UNC_CHA_RxC_IRQ1_REJECT.PA_MATCH'] / cut_values.loc['UNC_CHA_CLOCKTICKS']
cut_values.loc['Average IRQ Latency in uncore cycles'] = cut_values.loc['UNC_CHA_RxC_OCCUPANCY.IRQ'] / cut_values.loc['UNC_CHA_RxC_INSERTS.IRQ']
cut_values.loc['% cycles FaST signal is asserted to throttle all the cores'] = cut_values.loc['UNC_CHA_DISTRESS_ASSERTED.VERT'] / cut_values.loc['UNC_CHA_CLOCKTICKS']
print(cut_values)

cut_values.to_excel("lock_contension_analysis.xlsx")
