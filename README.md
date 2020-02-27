# pitching_dash
## Dashboard to evaluate pitchers

In order to run the file, you must have the following files in the same folder:
* ibp_dash.py
* ibp_pitcher.csv
* phillies_logo.png

### Streamlit Installation
Once all files are located in the same folder, open your terminal and run the following command:
`pip install streamlit`

If you encounter an error at this step, try the following command:
`conda install -c conda-forge watchdog`

Then:
`pip install streamlit`

### Running the Dashboard
Once streamlit has been installed, make sure that you are operating your terminal in the directory that contains the folder with the files for the Dashboard.

Once you have the directory (cd) with the folder open, run the following command:
`streamlit run ibp_dash.py`

Streamlit should then run the dashboard in your default browser using a local server.

### Usage
With the Dashboard open, you can use the sidebar on the left-hand side of the page to toggle which pitcher's stats you would like to view. On the center portion of the page, you can view the raw data in the DataFrame by checking the "Show Data" checkbox. Underneath, you may view different charts to visualize the pitchers' data. By clicking the selection box, you can decide which charts to look into. For some of the charts, you may check boxes for stats before/after the All-Star Break or select specific batter handedness. Enjoy!
