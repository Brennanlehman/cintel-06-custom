# --------------------------------------------
# Imports at the top - PyShiny EXPRESS VERSION
# --------------------------------------------

# From shiny, import just reactive and render
from shiny import reactive, render

# From shiny.express, import just ui and inputs if needed
from shiny.express import ui

import random
from datetime import datetime
from collections import deque
import pandas as pd
import plotly.express as px
from shinywidgets import render_plotly
from scipy import stats
import seaborn as sns

# --------------------------------------------




DEQUE_SIZE: int = 5
reactive_value_wrapper = reactive.value(deque(maxlen=DEQUE_SIZE))

MAX_DEQUE_SIZE = 20
# --------------------------------------------
# Initialize a REACTIVE CALC that all display components can call
# to get the latest data and display it.
# The calculation is invalidated every UPDATE_INTERVAL_SECS
# to trigger updates.
# It returns a tuple with everything needed to display the data.
# Very easy to expand or modify.
# --------------------------------------------

impaired_df = pd.read_csv("C:/Users/blehman/Projects/cintel-06-custom/dashboard/impaired.csv")



@reactive.calc()
def reactive_calc_combined():


    # Data generation logic
    deaths = round(random.uniform(0, 8), 1)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_dictionary_entry = {"deaths":deaths, "timestamp":timestamp}

    # get the deque and append the new entry
    reactive_value_wrapper.get().append(new_dictionary_entry)

    # Get a snapshot of the current deque for any further processing
    deque_snapshot = reactive_value_wrapper.get()

    # For Display: Convert deque to DataFrame for display
    df = impaired_df

    # For Display: Get the latest dictionary entry
    latest_dictionary_entry = new_dictionary_entry

    # Return a tuple with everything we need
    # Every time we call this function, we'll get all these values
    return deque_snapshot, df, latest_dictionary_entry




# Define the Shiny UI Page layout
# Call the ui.page_opts() function
# Set title to a string in quotes that will appear at the top
# Set fillable to True to use the whole page width for the UI
ui.page_opts(title="Impaired Driving Deaths - Blehman", fillable=True)

# Sidebar is typically used for user interaction/information
# Note the with statement to create the sidebar followed by a colon
# Everything in the sidebar is indented consistently
with ui.sidebar(open="open"):


    ui.h1("Impaired Driving Death Rates", class_="text-center", style="color:blue")
    ui.p(
        "by Age and Gender, 2012 & 2014, All States.",
        class_="text-center", style="color:green",
    )
    ui.hr()

    ui.h2("Sidebar")
    ui.input_date_range("daterange", "Date range", start="2011-01-01", end="2014-12-31")
    
    ui.input_checkbox_group(  
    "State",
    "select state",  
    ["Kentucky", "Alabama", "Ohio"],
    inline=True,
)

    ui.hr()

    ui.h3("Links:", style="text-decoration: underline")
    ui.a(
        "CDC Data - Impaired Driving Death Rates",
        href="https://data.cdc.gov/Motor-Vehicle/Impaired-Driving-Death-Rate-by-Age-and-Gender-2012/ebbj-sh54/about_data",
        target="_blank",
    )
    ui.a(
        "GitHub App - Lehman",
        href="https://brennanlehman.github.io/cintel-05-cintel/",
        target="_blank",

    )
# In Shiny Express, everything not in the sidebar is in the main panel

with ui.layout_columns():
    with ui.value_box(
        theme= """
            bg-primary
            text-light
            border-primary""",
    ):

        "Impaired Driving Death Rates"

        @render.text
        def display_temp():
            """Get the latest reading and return a death string"""
            deque_snapshot, df, latest_dictionary_entry = reactive_calc_combined()
            return f"{latest_dictionary_entry['deaths']}"

      



#with ui.card(full_screen=True, min_height="100%"):
with ui.card(full_screen=True, style="background-color: lightgray;", height=350):
    ui.card_header("Impaired Deaths Data Frame")

    @render.data_frame
    def display_df():
        """Get the latest reading and return a dataframe with current readings"""
        deque_snapshot, df, latest_dictionary_entry = reactive_calc_combined()
        pd.set_option('display.width', None)        # Use maximum width
        return render.DataGrid(df, width="100%", height="100%")


with ui.card(full_screen=True, style="background-color: lightgray;", height=350):
        ui.card_header("State Seaborn historgram")

        @render.plot(alt="A Seaborn histogram on Death Rates.")  
        def plot():  
            ax = sns.histplot(data=impaired_df, x="Female, 2012", y="State")  
            ax.set_title("Female Death Rates, 2012")
            ax.set_xlabel("Count")
            ax.set_ylabel("null")
            return ax 
