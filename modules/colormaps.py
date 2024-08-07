import math
import numpy as np
import pandas as pd

def getRandomInt(max: int):
    return math.floor(np.random.random() * max)

def getRandomIntHex(max: int):
    return hex(math.floor(np.random.random() * max))[2:]

def lerp(inter: float, v0: float, v1: float):
    return math.floor(inter*v0 + (1-inter)*v1)

def dist(p1: list, p2: list):
    return np.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def create_custom_colormatrix_3D(n_cmaps: int=100, cmap_length: int=256, power: int=5):
    clientHeight = cmap_length
    clientWidth = n_cmaps

    # Read positions from CSV
    pos_df = pd.read_csv('config/pos.csv')
    pos = pos_df.to_dict(orient='records')

    # Read colors from CSV
    colors_df = pd.read_csv('config/colors.csv')
    colors = colors_df.to_dict(orient='records')

    n_colors = len(pos)
    HaReBaD_color_matrix_upper = []

    for y in range(0, clientHeight):
        HaReBaD_color_matrix_upper.append([])
        for x in range(0, clientWidth):
            p = (x / clientWidth, y / clientHeight)
            d = [0] * len(pos)
            colShepard = {"r": 0, "g": 0, "b": 0}

            for i in range(n_colors):
                d[i] = dist(p, [pos[i]["x"], pos[i]["y"]])**power

            sumDist = sum(1/d_i for d_i in d if d_i != 0)

            for i in range(n_colors):
                if d[i] == 0:
                    colShepard["r"] = colors[i]["r"]
                    colShepard["g"] = colors[i]["g"]
                    colShepard["b"] = colors[i]["b"]
                else:
                    colShepard["r"] += 1/d[i] * colors[i]["r"] / sumDist
                    colShepard["g"] += 1/d[i] * colors[i]["g"] / sumDist
                    colShepard["b"] += 1/d[i] * colors[i]["b"] / sumDist

            inter = {"r": 0, "g": 0, "b": 0}
            inter["r"] = lerp(y / clientHeight, 255, colShepard["r"])
            inter["g"] = lerp(y / clientHeight, 255, colShepard["g"])
            inter["b"] = lerp(y / clientHeight, 255, colShepard["b"])

            inter["r"] = min(inter["r"], 255)
            inter["g"] = min(inter["g"], 255)
            inter["b"] = min(inter["b"], 255)

            col = [inter["r"] / 255, inter["g"] / 255, inter["b"] / 255, 1]
            HaReBaD_color_matrix_upper[-1].append(col)

    HaReBaD_color_matrix_upper = np.array(HaReBaD_color_matrix_upper)
    print(f"There are {HaReBaD_color_matrix_upper.shape[1]} color matrices of shape ({HaReBaD_color_matrix_upper.shape[0]},{HaReBaD_color_matrix_upper.shape[2]})")

    return HaReBaD_color_matrix_upper