import numpy as np
import pandas as pd
# read the excel file
df1 = pd.read_excel('C:/Users/abc/PycharmProjects/FirstPythonProject/swaraschedule_new.xlsx', header=1)
# create data data frame and filter three columns
data = pd.DataFrame(df1[['Story', 'Label', 'DesignSect','As']][1:])

# find unique value from story and label column and make its list
df_Story = data['Story'].unique()
df_Label = data['Label'].unique()
new_data = pd.DataFrame()
# select each number from story column in descending order and find the corresponding label only if label df_label is not empty
# for i in df_Story:
#     if len(df_Label) > 0:
#         print(i)
#         # Programme begin for height based clustering
#         list1 = set(data[data['Story'] == i]['Label'].unique())
#         list_intersected = list(list1 & set(df_Label))
#         if list_intersected != []:
#             #print(list_intersected)
#             data_slice = data[data['Label'].isin(list_intersected)]
#             data_slice.reset_index(drop=True,inplace=True)
#             #print(data_slice)
#             height_list = pd.DataFrame([i] * len(data_slice), columns=['height_cluster'])
#             #print(height_list)
#             df_column_merged = data_slice.join(height_list)
#             #print(df_column_merged)
#             new_data = pd.concat([new_data, df_column_merged])
#             #print(new_data)
#             del data_slice,height_list, df_column_merged
#             df_Label = set(df_Label) - set(list_intersected)
#             #print(df_Label)
# new_data.reset_index(drop=True,inplace=True)
# new_data.to_excel('new_data.xlsx')
# section based floor wise clustering
g_label = data.groupby('Label')
clean_data_2 = []
for p,q in g_label:
    print(p)
    r = q.groupby('Story')
    for s,t in r:
        u = t.max()
        clean_data_2.append(u)
    #print(clean_data_2)
clean_data = pd.DataFrame(clean_data_2)
#print(clean_data.info())
#print(clean_data)
clean_data.to_excel('clean_data.xlsx')
clean_data_new = clean_data[['Story','Label','DesignSect']]
clean_data_pivoted = clean_data_new.pivot(index='Story',columns='Label')
clean_data_pivoted.fillna("0",inplace=True)
clean_data_pivoted.to_excel('clean_data_pivoted.xlsx')
h = clean_data_pivoted.columns
for j in range(len(h)):
    print(h(j))
    # for k in range(len(h)) :
    #     if all(clean_data_pivoted[('DesignSect',h[j])] == clean_data_pivoted[('DesignSect',h(k))]) == True:
    #         print('yes')