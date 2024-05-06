import streamlit as st
import leafmap.foliumap as leafmap

# Set page layout
st.set_page_config(layout="wide")

# About section markdown
markdown = """
A Streamlit map template
<https://github.com/Younguz/steamlit_template>
"""

# Sidebar
st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

# Main title
st.title("Customizable Split-panel Map")

# Function to create split-panel map
def create_split_panel_map(left_layer, right_layer):
    m = leafmap.Map()
    m.split_map(left_layer=left_layer, right_layer=right_layer)
    m.add_legend(title="ESA Land Cover", builtin_legend="ESA_WorldCover")
    return m

# Select layers for split-panel map
left_layer = st.sidebar.selectbox("Select left layer", ["ESA WorldCover 2020 S2 FCC", "Other Layer 1"])
right_layer = st.sidebar.selectbox("Select right layer", ["ESA WorldCover 2020", "Other Layer 2"])

# Create split-panel map
split_map = create_split_panel_map(left_layer, right_layer)

# Display split-panel map
st.write(split_map.to_streamlit(height=700))

# Show/hide source code
with st.expander("See source code"):
    with st.echo():
        create_split_panel_map(left_layer, right_layer)
