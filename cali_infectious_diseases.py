import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
pio.templates.default = "plotly_white"
import seaborn as sns
df= pd.read_csv (r'C:\Users\Tombra\Infectious-diseases-in-California\california infectious disease.csv')
df_filled = df.fillna(df.mean(numeric_only=True))
disease_county_grouped = df_filled.groupby(['Disease', 'County'])['Cases'].sum().reset_index()

df_filtered = df_filled[~df_filled['Disease'].isin(['Yellow Fever', 'Anthrax', 'Domoic Acid Poisoning'])]

