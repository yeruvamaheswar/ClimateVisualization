from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd

# ////////
# Bermuda
# ////////

bermuda = make_subplots(
    rows = 2,
    cols = 1,
    subplot_titles = ("<b>pH</b>", "<b>pCO2</b>"))

# Pull Data
ber = pd.read_csv('./Ocean Data/bermuda.csv')

# Figure 1 
bermuda.append_trace(go.Scatter(
    x = ber['Bermuda Year'],
    y = ber['Bermuda pH'],
    name = "pH"
), row = 1, col = 1)

# Figure 2
bermuda.append_trace(go.Scatter(
    x = ber['Bermuda Year'],
    y = ber['Bermuda pCO2'],
    name = "pCO2"
), row = 2, col = 1)

# Rename the Axes
bermuda.update_xaxes(title_text = "<b>Year</b>")
bermuda.update_yaxes(title_text = "<b>pH</b>", row = 1, col = 1)
bermuda.update_yaxes(title_text = "<b>pCO2</b>", row = 2, col = 1)

# Name the graph overall 
bermuda.update_layout(height = 800, width = 800, title_text = "<b>Bermuda</b>")
bermuda.show()

# ///////////////
# Canary Islands
# ///////////////

canary = make_subplots(
    rows=2,
    cols=1,
    subplot_titles = ("<b>pH</b>", "<b>pCO2</b>"))

# Pull Data
can = pd.read_csv('./Ocean Data/canaryislands.csv')

# Figure 1 
canary.append_trace(go.Scatter(
    x = can['Canary Islands Year'],
    y = can['Canary Islands pH'],
    name = "pH"
), row = 1, col = 1)

# Figure 2
canary.append_trace(go.Scatter(
    x = can['Canary Islands Year'],
    y = can['Canary Islands pCO2'],
    name = "pCO2"
), row = 2, col = 1)

# Rename the Axes
canary.update_xaxes(title_text = "<b>Year</b>")
canary.update_yaxes(title_text = "<b>pH</b>", row = 1, col = 1)
canary.update_yaxes(title_text = "<b>pCO2</b>", row = 2, col = 1)

# Name the graph overall 
canary.update_layout(height = 800, width = 800, title_text = "<b>Canary Islands</b>")
canary.show()

# ///////
# Hawaii
# //////

hawaii = make_subplots(
    rows=2,
    cols=1,
    subplot_titles = ("<b>pH</b>", "<b>pCO2</b>"))

# Pull Data
haw = pd.read_csv('./Ocean Data/hawaii.csv')

# Figure 1 
hawaii.append_trace(go.Scatter(
    x = haw['Hawaii Year'],
    y = haw['Hawaii pH'],
    name = "pH"
), row = 1, col = 1)

# Figure 2
hawaii.append_trace(go.Scatter(
    x = haw['Hawaii Year'],
    y = haw['Hawaii pCO2'],
    name = "pCO2"
), row = 2, col = 1)

# Rename the Axes
hawaii.update_xaxes(title_text = "<b>Year</b>")
hawaii.update_yaxes(title_text = "<b>pH</b>", row = 1, col = 1)
hawaii.update_yaxes(title_text = "<b>pCO2</b>", row = 2, col = 1)

# Name the graph overall 
hawaii.update_layout(height = 800, width = 800, title_text = "<b>Hawaii</b>")
hawaii.show()