# %%
import csv
import json
from typing import Iterator

import numpy as np
from utils.types import Row, Winner
import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle

FILE = "../src/analyzes-complete-final-final.csv"

# %%


def read_file(path: str) -> Iterator[Row]:
    with open(path) as f:
        reader = csv.DictReader(f)
        reader.fieldnames = (
            [f.strip() for f in reader.fieldnames] if reader.fieldnames else None
        )

        yield from (Row.create(row) for row in reader)


def write_sus_json(sus: list[Row], not_sus: list[Row]) -> None:
    with open("sus.json", "w") as s:
        json.dump([r.model_dump(mode="json") for r in sus], s)
    with open("not_sus.json", "w") as n:
        json.dump([r.model_dump(mode="json") for r in not_sus], n)


def write_sus_csv(sus: list[Row], not_sus: list[Row]) -> None:
    with open("sus.csv", "w") as s:
        s.write("\n".join([r.to_csv() for r in sus]))
    with open("not_sus.csv", "w") as n:
        n.write("\n".join([r.to_csv() for r in not_sus]))


def separar_suspeitas() -> tuple[list[Row], list[Row]]:
    count = 0
    sus: list[Row] = []
    not_sus: list[Row] = []

    for row in read_file(FILE):
        if row.winner == Winner.DRAW:
            continue
        winner_rating = (
            row.white_rating if row.winner == Winner.WHITE else row.black_rating
        )
        loser_rating = (
            row.black_rating if row.winner == Winner.WHITE else row.white_rating
        )

        if winner_rating < loser_rating - 500:
            sus.append(row)
        else:
            not_sus.append(row)
        count += 1
    return sus, not_sus


def group_by_winner(rows: list[Row]) -> dict[str, list[Row]]:
    grouped: dict[str, list[Row]] = {}
    for row in rows:
        if row.winner in grouped:
            grouped[row.winner_id].append(row)
        else:
            grouped[row.winner_id] = [row]
    return grouped


def make_graph(rows: list[Row], min_x: int = 0, max_x: int = 300) -> None:
    x = []
    y = []

    count_x = 0
    count_y = 0

    max_len = 0
    for row in rows:
        count_x = 0
        max_len = max(max_len, len(row.winner_jogadas))
        for jog in row.winner_jogadas:
            if jog and max_x >= count_x >= min_x:
                x.append(count_x)
                y.append(count_y)
            count_x += 1
        count_y += 1

    plt.scatter(x, y, marker=MarkerStyle("|"))
    plt.xticks(range(min_x, max_len))
    plt.yticks(range(len(rows)))  # , [f"{i}" for i in range(0, len(rows), 20)])
    plt.yscale("linear")
    plt.xscale("linear")
    plt.show()


def main():
    MIN_PARTIDAS = 2
    MIN_JOGADAS = 40
    MAX_JOGADAS = 300

    sus, not_sus = separar_suspeitas()
    print("Comprimentos ao carregar: ", len(sus), len(not_sus))

    # sus = [s for s in sus if MAX_JOGADAS >= len(s.jogadas_all)]  # >= MIN_JOGADAS]
    # not_sus = [n for n in not_sus if MAX_JOGADAS >= len(n.jogadas_all)]  # >= MIN_JOGADAS]

    print("Comprimentos ao filtrar por número de jogadas: ", len(sus), len(not_sus))

    sus_grouped = group_by_winner(sus)
    not_sus_grouped = group_by_winner(not_sus)

    print("Número de jogadores: ", len(sus_grouped.keys()), len(not_sus_grouped.keys()))

    print("Comprimentos ao filtrar por número de jogos: ", len(sus), len(not_sus))

    make_graph(sus[:200], 20, 200)
    make_graph(not_sus[:200], 20, 200)
    # write_sus_csv(sus, not_sus)


# %%
def make_ratio_graph(line1: list[float], line2: list[float]) -> None:
    line1_x = [i * 1 for i in range(len(line1))]
    not_line2_x = [i * 1 for i in range(len(line2))]

    plt.plot(line1_x, line1, "go")
    plt.plot(not_line2_x, line2, "rx")

    plt.show()


# %%
def make_ratio_bar(line1: list[float], line2: list[float]) -> None:
    win_counts = {
        "Ganhou": np.array(line1),
        "Perdeu": np.array(line2),
    }
    width = 0.6  # the width of the bars: can also be len(x) sequence

    fig, ax = plt.subplots()
    bottom = np.zeros(len(line1))

    for label, win_count in win_counts.items():
        p = ax.bar(
            [f"{i}" for i in range(len(line1))],
            win_count,
            width,
            label=label,
        )

        ax.bar_label(p, label_type="center")

    ax.legend()

    plt.show()


# %%

rows = [
    row
    for row in read_file(FILE)
    if row.winner != Winner.DRAW and len(row.jogadas_all) > 20
]
size = 10
winners_ratio = [
    r.winner_jogadas.count(True) / len(r.winner_jogadas) for r in rows[:size]
]
losers_ratio = [r.loser_jogadas.count(True) / len(r.loser_jogadas) for r in rows[:size]]
make_ratio_graph(winners_ratio, losers_ratio)
# make_ratio_bar(winners_ratio, losers_ratio)

# %%
