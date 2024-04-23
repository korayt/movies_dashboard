import streamlit as st
import pandas as pd
import plotly.express as px

# load data
df = pd.read_csv('./data/raw/movies.csv')

# session state variables
if "chosen_director" not in st.session_state:
    st.session_state["chosen_director"] = "Christopher Nolan"
if "chosen_start_year" not in st.session_state:
    st.session_state["chosen_start_year"] = 1998
if "chosen_end_year" not in st.session_state:
    st.session_state["chosen_end_year"] = 2020
if "start_year" not in st.session_state:
    st.session_state["start_year"] = 1998
if "end_year" not in st.session_state:
    st.session_state["end_year"] = 2020
if "chosen_df" not in st.session_state:
    st.session_state["chosen_df"] = df[
        (df.director == st.session_state.chosen_director) & (df.year >= st.session_state.chosen_start_year) & (
                df.year <= st.session_state.chosen_end_year)]

# operations

directors = df.groupby('director').sum()['votes'].sort_values(ascending=False).keys()


# callbacks
def change_director_handler():
    st.session_state["start_year"] = df[(df.director == st.session_state.chosen_director)]["year"].min()
    st.session_state["end_year"] = df[(df.director == st.session_state.chosen_director)]["year"].max()
    st.session_state["chosen_start_year"] = st.session_state["start_year"]
    st.session_state["chosen_end_year"] = st.session_state["end_year"]
    st.session_state["chosen_df"] = df[
        (df.director == st.session_state.chosen_director) & (df.year >= st.session_state.chosen_start_year) & (
                df.year <= st.session_state.chosen_end_year)]


def change_year_handler():
    st.session_state["chosen_start_year"] = st.session_state.chosen_years[0]
    st.session_state["chosen_end_year"] = st.session_state.chosen_years[1]
    st.session_state["chosen_df"] = df[
        (df.director == st.session_state.chosen_director) & (df.year >= st.session_state.chosen_start_year) & (
                df.year <= st.session_state.chosen_end_year)]


main = st.container()
with main:
    st.title('Director Dashboard')
    st.write('One way stop to get insights on directors.')
    st.selectbox(label="Select a director!", options=directors, on_change=change_director_handler,
                 key='chosen_director')
    st.slider(label="Select years to analyze!", min_value=st.session_state["start_year"],
              max_value=st.session_state["end_year"],
              value=(st.session_state["start_year"], st.session_state["end_year"]), step=1,
              on_change=change_year_handler, key='chosen_years')
    st.write('Director selected:', st.session_state.chosen_director)
    st.write('Start year:', st.session_state.chosen_start_year, 'End year:', st.session_state.chosen_end_year)

    fig_popular_movies = px.bar(st.session_state["chosen_df"].sort_values(by='votes', ascending=False), x="name",
                                y="votes", title=f"Movies of {st.session_state['chosen_director']}"
                                                 f" between {st.session_state['chosen_start_year']} and "
                                                 f"{st.session_state['chosen_end_year']} sorted by popularity")

    fig_genre = px.histogram(st.session_state["chosen_df"], x='genre',
                             title=f"Genre of the movies by {st.session_state['chosen_director']}")
    st.plotly_chart(fig_popular_movies)
    st.plotly_chart(fig_genre)
