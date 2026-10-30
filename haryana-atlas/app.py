from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Haryana Grid Atlas",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Keep the supplied reference UI intact and display it inside a Streamlit app.
# The original HTML already opens on the login screen (page 0).
APP_DIR = Path(__file__).parent
html_path = APP_DIR / "haryana-grid-atlas.html"
html = html_path.read_text(encoding="utf-8")

st.markdown(
    """
    <style>
      html, body, [data-testid="stApp"], [data-testid="stAppViewContainer"],
      [data-testid="stMain"], [data-testid="stMainBlockContainer"] {
        margin: 0 !important;
        padding: 0 !important;
        max-width: 100% !important;
        overflow: hidden !important;
      }
      [data-testid="stHeader"], [data-testid="stToolbar"],
      [data-testid="stDecoration"], [data-testid="stStatusWidget"],
      [data-testid="stSidebar"], footer {
        display: none !important;
      }
      .block-container {
        padding: 0 !important;
        max-width: 100% !important;
      }
      [data-testid="stIFrame"] {
        width: 100% !important;
        height: 100vh !important;
        min-height: 100vh !important;
        border: 0 !important;
      }
      [data-testid="stIFrame"] iframe {
        width: 100% !important;
        height: 100vh !important;
        min-height: 100vh !important;
        border: 0 !important;
        display: block !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

components.html(html, height=950, scrolling=False)
