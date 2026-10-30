# Haryana Grid Atlas — Streamlit version (reference UI preserved)

This version keeps the supplied `haryana-grid-atlas.html` interface intact and runs it inside a Streamlit application.

**Important:** The earlier conversion recreated the interface with different Streamlit layouts. This corrected version does not redesign the dashboard. It uses the original reference file so the fonts, colours, page transitions, navigation, map, charts, wording, and login design remain as supplied.

## Run on Windows

1. Extract this ZIP file.
2. Open the extracted `haryana_grid_atlas_streamlit_exact` folder.
3. Open Command Prompt or PowerShell in that folder.
4. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

5. Activate it:

   **Command Prompt**
   ```bash
   .venv\Scripts\activate
   ```

   **PowerShell**
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

6. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

7. Start the app:

   ```bash
   python -m streamlit run app.py
   ```

8. Open the local URL shown in the terminal, usually `http://localhost:8501`.

## Demo login

- Username: any non-empty username
- Password: any password with at least 4 characters

## Notes

- The login page is the first screen, as in the supplied reference.
- The original HTML is included as the UI asset and is not redesigned by Streamlit.
- The interactive map uses internet map tiles and requests district boundaries from OpenStreetMap/Nominatim. An internet connection is needed for those map layers and boundary lookups.
- The dashboard data is illustrative, as described in the original reference.
