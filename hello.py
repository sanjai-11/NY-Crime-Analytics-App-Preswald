import pandas as pd
import plotly.express as px
from preswald import get_df, plotly, table, text, slider, selectbox

# Title
text("# NY Crime Analytics App")
text("""
This dashboard presents crime statistics for all counties in New York State from 1990 to the present. The dataset is sourced from the Division of Criminal Justice Services (DCJS), which compiles official crime reports submitted by over 500 police and sheriff departments. 

It includes counts and rates (per 100,000 residents) for violent crimes (murder, rape, robbery, aggravated assault), property crimes (burglary, larceny, motor vehicle theft), and firearm-related incidents. Users can explore trends over time, compare counties, and analyze specific crime categories interactively.

This Crime dataset was downloaded from data.gov (https://catalog.data.gov/dataset/index-violent-property-and-firearm-rates-by-county-beginning-1990)""")

# loading dataset
df = get_df("data/crime_data.csv") 

text("## Table of Crime Records")
table(df)

text("")

df["Year"] = pd.to_numeric(df["Year"])
df["County"] = df["County"].astype(str)

# adding filter bars
year = slider("Select Year", min_val=int(df["Year"].min()), max_val=int(df["Year"].max()), default=int(df["Year"].max()))
county = selectbox("Select County", options=sorted(df["County"].unique().tolist()))

# adding filter options for year & county
filtered = df[(df["Year"] == year) & (df["County"] == county)]

text(f"## {county} County Crime Summary ({year})")

if not filtered.empty:
    table(filtered[[
        "Population", "Index Count", "Index Rate",
        "Violent Count", "Violent Rate",
        "Property Count", "Property Rate",
        "Firearm Count", "Firearm Rate"
    ]])

    total_crimes = int(filtered["Index Count"].values[0])
    text(f"### Total Reported Crimes: {total_crimes}")
else:
    text("No data found for this year and county.")

# bar chart for crime breakdonw
if not filtered.empty:
    bar_df = pd.DataFrame({
        "Category": ["Violent", "Property", "Firearm"],
        "Rate per 100K": [
            filtered["Violent Rate"].values[0],
            filtered["Property Rate"].values[0],
            filtered["Firearm Rate"].values[0],
        ]
    })
    fig_bar = px.bar(bar_df, x="Category", y="Rate per 100K", color="Category", title="Crime Rate Breakdown")
    plotly(fig_bar)

# county-level crime trend 
trend_df = df[df["County"] == county]
text("## Crime Trends Over Time")
fig_line = px.line(
    trend_df,
    x="Year",
    y=["Violent Rate", "Property Rate", "Firearm Rate"],
    title=f"{county} Crime Rate Trends (1990–{df['Year'].max()})"
)
plotly(fig_line)

# distribution across counties (for same year)
text("## Violent Crime Distribution by County")
year_df = df[df["Year"] == year]
fig_hist = px.histogram(
    year_df,
    x="Violent Rate",
    nbins=30,
    title=f"Distribution of Violent Crime Rates Across Counties ({year})"
)
plotly(fig_hist)

# data table filtered
text("## Data Table (Filtered)")
table(year_df[["County", "Violent Rate", "Property Rate", "Firearm Rate"]].sort_values(by="Violent Rate", ascending=False).head(10))
