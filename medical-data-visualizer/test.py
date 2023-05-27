import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('test.csv')

#change values
"""
#all the changes in the csv
for index, row in df.iterrows():

    #creating overweight column
    calc = round(row['weight'] / (row['height'] ** 2 / 10000),2)
    df.loc[index, 'overweight'] = 1 if calc > 25 else 0
    #changing to boolean all the gluc values
    df.loc[index, 'gluc'] = 1 if row['gluc'] > 1 else 0
    #changing to boolean all the cholesterol values
    df.loc[index, 'cholesterol'] = 1 if row['cholesterol'] > 1 else 0

df['overweight'] = df['overweight'].astype('int64')

df.to_csv('test.csv')
"""
#barplot exercise
df = df.drop(['id','age','height','weight','sex','ap_hi','ap_lo'], axis=1)
print(df.head())
df2 = pd.DataFrame()
i = 0
for index in df.columns:
    df2.loc[i,'variable'] = index
    df2.loc[i,'total'] = len(df[(df['cardio'] == 0) & (df[index] == 0)])
    df2.loc[i,'value'] = 0
    df2.loc[i,'cardio'] = 0
    i=i+1
    df2.loc[i,'variable'] = index
    df2.loc[i,'total'] = len(df[(df['cardio'] == 0) & (df[index] == 1)])
    df2.loc[i,'value'] = 1
    df2.loc[i,'cardio'] = 0
    i=i+1
    df2.loc[i,'variable'] = index
    df2.loc[i,'total'] = len(df[(df['cardio'] == 1) & (df[index] == 0)])
    df2.loc[i,'value'] = 0
    df2.loc[i,'cardio'] = 1
    i=i+1
    df2.loc[i,'variable'] = index
    df2.loc[i,'total'] = len(df[(df['cardio'] == 1) & (df[index] == 1)])
    df2.loc[i,'value'] = 1
    df2.loc[i,'cardio'] = 1
    i=i+1

df2.drop([20,21,22,23], axis=0, inplace=True)

#changing variable type of all columns to integer
df2['total'] = df2['total'].astype('int64')
df2['value'] = df2['value'].astype('int64')
df2['cardio'] = df2['cardio'].astype('int64')
df2 = df2.sort_values('variable', ascending=True).reset_index().drop('index', axis=1)

sns.catplot(kind='bar',data=df2, x='variable', y='total', hue='value', col='cardio')

plt.savefig('plot.png')
plt.show()
#heatplot exercise
"""
df = df[df['ap_lo'] <= df['ap_hi']]
df = df[df['height'] >= df['height'].quantile(0.025)]
df = df[df['height'] <= df['height'].quantile(0.975)]
df = df[df['weight'] >= df['weight'].quantile(0.025)]
df = df[df['weight'] <= df['weight'].quantile(0.975)]
matrix = df.corr()
matrix2 = np.triu(matrix)


plt.figure(figsize=(9,9), dpi=100)



sns.heatmap(data=matrix,
            annot=True,
            mask=matrix2,
            fmt='.1f',
            cmap='icefire',
            linewidths=1,
            center=0,
            vmin=-0.15,
            vmax=0.30,
            square=True,
            cbar_kws={'shrink': 0.4, 'ticks': [.24,.16,.08,.00,-.08]},
            annot_kws={"size": 8}
)

plt.show()
"""