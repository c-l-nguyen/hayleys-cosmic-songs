#!/usr/bin/env python
# coding: utf-8

import pandas as pd

decade_df = pd.read_csv("../data/raw/billboard_hot_100_by_decade.csv")
decade_df["decade"] = decade_df["decade"].astype("int64")

# sort and keep top 100 songs for each decade
sorted_decade = decade_df.sort_values(["decade","count"], ascending=False).reset_index(drop=True)
top_100_songs_by_decade = sorted_decade.groupby("decade").head(100)

# save to CSV
top_100_songs_by_decade.to_csv("../data/clean/decades/billboard_top_100_by_decade.csv", index=False)
