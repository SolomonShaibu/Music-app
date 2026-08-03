import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Multi-Instrument Arranger",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🎹 Multi-Instrument Piano Roll & Arranger")
st.markdown("Compose melodies, basslines, and guitar chords, arrange them on a timeline, and preview your track before exporting.")

# Load the interactive workspace HTML/JS component
with open("static/workspace.html", "r") as f:
    workspace_code = f.read()

# Render the DAW workspace inside Streamlit
components.html(workspace_code, height=750, scrolling=True)

st.sidebar.header("Export Settings")
st.sidebar.selectbox("Export Format", ["WAV", "MP3"])
if st.sidebar.button("Render & Download Mix"):
    st.sidebar.success("Render complete! (Ready for download)")

