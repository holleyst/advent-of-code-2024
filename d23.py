#!/usr/bin/env python3

# Advent of Code 2024
# Day 23: LAN Party
# https://adventofcode.com/2024/day/23

import networkx as nx

input_file = "d23input.txt"
with open(input_file, "r") as f:
    data = f.read().strip()
    lines = data.split("\n")

conn_pairs = [tuple(l.strip().split("-")) for l in lines]


# part 1: how many contain at least one computer with a name that starts with t?
G = nx.Graph()
G.add_edges_from(conn_pairs)
cliques = list(nx.enumerate_all_cliques(G))
conn_trios = [c for c in cliques if len(c) == 3]
t_trios = [c for c in conn_trios if any(e.startswith('t') for e in c)]
print("sets contain at least one t-computer (part 1):", len(t_trios))


# part 2: what is the password to get into the LAN party?
print("LAN party password (part 2):", ",".join(sorted(max(cliques, key=len))))

