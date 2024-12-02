# -*- coding: utf-8 -*-

import pandas as pd

"""File Information
@file_name: day_1.py
@author: Dylan "dyl-m" Monfret
Advent of Code 2024 - Day 1
"""

RAW_DATA = pd.read_table('../data/day_1.txt',
                         sep=' ',
                         header=None).dropna(axis=1, how='all').reset_index(drop=True)

"Functions"


def compute_part_1(raw_data: pd.DataFrame) -> (int, pd.DataFrame):
    """Compute Day 1 - Part 1 answer.
    :param raw_data: input data
    :return: sum of distances
    """
    data = pd.DataFrame({'v1': raw_data.iloc[:, 0].sort_values().tolist(),
                         'v2': raw_data.iloc[:, 1].sort_values().tolist()})
    data['dist'] = abs(data.v1 - data.v2)
    return data.dist.sum(), data


def compute_part_2(raw_data: pd.DataFrame) -> int:
    """Compute Day 1 - Part 2 answer.
    :param raw_data: input data
    :return: sum of similarities
    """
    # Compute Part 1
    _, data = compute_part_1(raw_data)

    # Part 2
    data['count_v1_in_v2'] = data.v1.apply(lambda x: data.v2.tolist().count(x))
    data['sim'] = data.count_v1_in_v2 * data.v1
    return data.sim.sum()


"Main"

if __name__ == "__main__":
    # Part 1
    part_1, _ = compute_part_1(RAW_DATA)

    # Part 2
    part_2 = compute_part_2(RAW_DATA)
