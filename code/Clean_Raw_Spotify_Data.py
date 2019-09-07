#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import ast

def literal_return(val):
	"""
	Evaluate strings to lists in UTF-8 format
	"""
    try:
        return ast.literal_eval(val)
    except (ValueError, SyntaxError) as e:
        return val

spotify_df = pd.read_csv("../data/billboard_2000_2018_spotify.csv")
spotify_df["genre"] = spotify_df["genre"].apply(literal_return)

# filter out 2018 since year is incomplete
spotify_df = spotify_df.query("year != 2018").sort_values("year").reset_index(drop=True)

# save to CSV
spotify_df.to_csv("../data/billboard_2000_2018_spotify_clean.csv", index=False)
