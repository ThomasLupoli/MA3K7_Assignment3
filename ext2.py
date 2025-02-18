import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as mp
import time
import random
from tqdm import tqdm
from collections import defaultdict

start = time.time()



def game(i):
    hat = list(range(1, i + 1))
    index_map = defaultdict(list)

    for idx, val in enumerate(hat):
        index_map[val].append(idx)

    while len(hat) > 1:
        a, b = random.sample(hat, 2)
        new = abs(a - b)

        if a in index_map and index_map[a]:
            a_index = index_map[a].pop()
            if not index_map[a]:
                del index_map[a]

            if a_index < len(hat) - 1:
                last_value = hat[-1]
                hat[a_index] = last_value

                if len(hat) - 1 in index_map[last_value]:
                    index_map[last_value].remove(len(hat) - 1)

                index_map[last_value].append(a_index)

            hat.pop()

        if b in index_map and index_map[b]:
            b_index = index_map[b].pop()
            if not index_map[b]:
                del index_map[b]

            if b_index < len(hat) - 1:
                last_value = hat[-1]
                hat[b_index] = last_value

                if len(hat) - 1 in index_map[last_value]:
                    index_map[last_value].remove(len(hat) - 1)

                index_map[last_value].append(b_index)

            hat.pop()

        hat.append(new)
        index_map[new].append(len(hat) - 1)

    return hat[0]

def run_simulations(num_games, i):
    counter = mp.Value("i", 0)
    with mp.Pool(mp.cpu_count()) as pool:
        results = list(tqdm(pool.imap(game, [i] * num_games), total=num_games))
    return results

if __name__ == "__main__":
    mp.freeze_support()

    num_games = 1000
    i = 18_000
    print("🚀 Running simulations...")

    results = run_simulations(num_games, i)
    mean = np.mean((np.array(results)))
    print(mean)

    print(f"✅ Done! Saved {num_games} results.")
