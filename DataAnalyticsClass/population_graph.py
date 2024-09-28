# make graphics

import streamlit as st
import pandas as pd

# define figure title
st.title('Population Plot')

# Read the CSV file
url = "https://github.com/AbhishekSingh1909/population_graph_streamlit/blob/main/DataAnalyticsClass/population.csv"
df = pd.read_csv(url)

# Drop unnecessary columns if any (e.g., 'Unnamed: 0')
if 'Unnamed: 0' in df.columns:
    df = df.drop(columns='Unnamed: 0')

# Pivot the DataFrame to have years as rows and countries as columns
df_population = df.pivot(index='year', columns='country', values='pop')


# Reset index to have 'year' as a column
df_population = df_population.reset_index()

# Rename columns to remove multi-level headers (i.e., remove 'country' label)
# This removes the 'country' name from the columns
df_population.columns.name = None

countries = df['country'].unique().tolist()

# define selectors(column to draw)

column = st.multiselect('Countries', countries)
# plot the line chart
st.line_chart(df_population, x='year', y=column,
              x_label='year', y_label='Population')
