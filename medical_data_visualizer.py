import pandas as pd 
import seaborn as sns 
import numpy as np 
import matplotlib.pyplot as plt 

df = pd.read_csv(r"PYTHON_PROJECT/medical.csv")
print(df.head(3))

df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

def draw_cat_plot():
    df_cat = pd.melt(df, 
                     id_vars=['cardio'], 
                     value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    fig = sns.catplot(x="variable", y="total", hue="value", col="cardio",
                      data=df_cat, kind="bar").fig

    fig.savefig('catplot.png')
    plt.show()
    
    return fig

def draw_heat_map():
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    corr = df_heat.corr()

    mask = np.triu(np.ones_like(corr, dtype=bool))

    fig, ax = plt.subplots(figsize=(12, 10))

    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', center=0, square=True, linewidths=0.5, cbar_kws={"shrink": .45})

    fig.savefig('heatmap.png')
    plt.show()
    return fig

draw_cat_plot()
draw_heat_map()
