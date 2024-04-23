# movies_dashboard

## Motivation
Target audience: Agents of directors
Our motivation for this dashboard is to create a simple dashboard that agents can use to evaluate their clients and explore new potential clients.
Our dashboard will allow for agents to filter by directors and will create interactive plots to explore their past. 
You can also filter by the start and end year to deep dive into a specific time period.
Our main feature is to allow our users to search for a directors movies. It is very easy to evaluate you favourite director and see their movies' popularity by efficient plots that we sorted just for you!
You will also be able to look at which genre is preferred by the director and how many movies they have made in that genre.

## Description




## Installation

Cd into the project root

```bash
cd /path/to/movies_dashboard
```

Create a conda environment

```bash
conda env create -f environment.yml
```

Activate the conda environment

```bash
conda activate director-dashboard
```

Run the app

```bash
streamlit run src/app.py
```