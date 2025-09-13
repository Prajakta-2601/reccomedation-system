import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the fertilizer data
df = pd.read_csv("kaggle_fertilizer_prediction.csv")

# Create fertilizer recommendation analysis by crop type
# Group by crop type and fertilizer to get counts
fert_crop_counts = df.groupby(['Crop Type', 'Fertilizer Name']).size().reset_index(name='Count')

# Get top 8 crop types by frequency to reduce clutter
top_crops = df['Crop Type'].value_counts().head(8).index.tolist()
fert_crop_filtered = fert_crop_counts[fert_crop_counts['Crop Type'].isin(top_crops)]

# Get top 6 fertilizers by frequency to reduce legend clutter
top_fertilizers = df['Fertilizer Name'].value_counts().head(6).index.tolist()

# Filter for top fertilizers and group others
fert_crop_filtered['Fertilizer Clean'] = fert_crop_filtered['Fertilizer Name'].apply(
    lambda x: x if x in top_fertilizers else 'Other'
)

# Re-aggregate after grouping others
fert_final = fert_crop_filtered.groupby(['Crop Type', 'Fertilizer Clean']).agg({'Count': 'sum'}).reset_index()

# Shorten fertilizer names to meet 15 character limit
fert_name_map = {
    'Ferrous Sulphate': 'Ferrous Sul',
    'Calcium Nitrate': 'Calcium Nit',
    'NPK': 'NPK',
    'DAP': 'DAP', 
    'Urea': 'Urea',
    'Potash': 'Potash',
    'Other': 'Other'
}

fert_final['Fertilizer Short'] = fert_final['Fertilizer Clean'].map(fert_name_map).fillna(fert_final['Fertilizer Clean'])

# Create stacked bar chart with agricultural colors (greens, browns, blues)
agricultural_colors = ['#2E8B57', '#8B4513', '#4682B4', '#228B22', '#CD853F', '#5F9EA0', '#8FBC8F']

fig = px.bar(
    fert_final,
    x='Crop Type',
    y='Count',
    color='Fertilizer Short',
    title='Fertilizer Recommendations by Crop',
    color_discrete_sequence=agricultural_colors
)

# Update layout for better readability
fig.update_layout(
    xaxis_title='Crop Type',
    yaxis_title='Count',
    legend_title='Fertilizer'
)

# Update traces and axis formatting
fig.update_traces(cliponaxis=False)
fig.update_xaxes(tickangle=45)

# Center legend since we have 7 or fewer items
unique_fertilizers = fert_final['Fertilizer Short'].nunique()
if unique_fertilizers <= 5:
    fig.update_layout(legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5))

# Save the chart
fig.write_image("fertilizer_analysis.png")
print("Single stacked bar chart saved successfully!")
print(f"Chart shows {len(top_crops)} crop types and {unique_fertilizers} fertilizer categories")