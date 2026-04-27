import streamlit as st
from banner import show_banner
from src.data_utils import load_data, prepare_habits, prepare_habit_builder_data
from src.sidebar import render_sidebar
from src.tabs.tickets import render_tickets_tab
from src.tabs.habits import render_habits_tab
from src.tabs.habit_builder import render_habit_builder_tab
from src.tabs.overview import render_overview_tab

# Page configuration
#--------------------------------------------------------------------------------
show_banner()
st.set_page_config(page_title="Ticket & Habit Tracker", layout="wide")


# Data path
#--------------------------------------------------------------------------------
FILE_PATH = "Dashboard_sheet.xlsx"


# Sidebar
#--------------------------------------------------------------------------------
render_sidebar(FILE_PATH)


# Data loading
#--------------------------------------------------------------------------------
df_tickets, df_habits, df_hb, error = load_data(FILE_PATH)

if error:
    st.error(f"Error loading data: {error}")
    st.stop()

if df_tickets is None or df_habits is None or df_hb is None:
    st.warning("No data found in the expected sheets.")
    st.stop()


# Main Application
#--------------------------------------------------------------------------------
tab_ov, tab1, tab2, tab3 = st.tabs(["Overview", "Tickets", "Habits", "Habit Builder"])

# --- Tab 0: Overview ---
with tab_ov:
    render_overview_tab(df_tickets, df_habits, df_hb)

# --- Tab 1: Tickets ---
with tab1:
    render_tickets_tab(df_tickets)

# --- Tab 2: Habits ---
with tab2:
    melted_habits = prepare_habits(df_habits)
    render_habits_tab(df_habits, melted_habits)

# --- Tab 3: Habit Builder ---
with tab3:
    df_hb_melted = prepare_habit_builder_data(df_hb)
    if df_hb_melted is not None:
        render_habit_builder_tab(df_hb, df_hb_melted)
    else:
        st.error("Could not process Habit Builder data.")
