import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the data
df = pd.read_csv('western_maharashtra_crop_fertilizer.csv')

# Calculate total production by district
district_production = df.groupby('District')['Production_Tonnes'].sum().reset_index()
district_production = district_production.sort_values('Production_Tonnes', ascending=True)

# Get all districts (there are only 7 unique districts in the data)
all_districts = district_production.copy()

# Convert production to thousands for better readability  
all_districts.loc[:, 'Production_k'] = all_districts['Production_Tonnes'] / 1000

# Create horizontal bar chart
fig = go.Figure()

fig.add_trace(go.Bar(
    y=all_districts['District'],
    x=all_districts['Production_k'],
    orientation='h',
    marker_color='#2E8B57',  # Sea green color for Maharashtra theme
    text=[f'{x:.0f}k' for x in all_districts['Production_k']],
    textposition='outside',
    hovertemplate='<b>%{y}</b><br>Production: %{x:.1f}k tonnes<extra></extra>'
))

# Update layout
fig.update_layout(
    title='Districts by Total Production',
    xaxis_title='Production (k)',
    yaxis_title='District',
    showlegend=False
)

# Update traces for better appearance
fig.update_traces(cliponaxis=False)

# Save the chart
fig.write_image('maharashtra_districts.png')

print("Chart saved successfully!")
print(f"All {len(all_districts)} districts by production:")
for idx, row in all_districts.iterrows():
    print(f"{row['District']}: {row['Production_Tonnes']:,.0f} tonnes")