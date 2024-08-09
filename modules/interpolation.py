import numpy as np

from modules.colormaps import lerp


def create_custom_colormatrix_2D(cmap_length: int = 600, verbose: bool = True):
    """
    Remake of Christophe Hurter's javascript implementation
    of the interpolation between <n> colors (two or more).

    Parameters
    ----------
    cmap_length: int
        Size of the colormap (HaReBaD_color_matrix_upper.shape[0]).

    Returns
    -------
    colormatrix: list or 2D numpy array
        This is the color matrix that can be used to created a color map.

    Note
    -----
    HaReBaD_color_matrix_upper.shape[1] (shape=3) represents the (r,g,b) values.
    """

    clientWidth = cmap_length

    # Gradient 1D

    # Defines colors
    color1 = {"r": 220, "g": 220, "b": 220}
    color2 = {"r": 255, "g": 255, "b": 255}

    colormatrix = []

    # Manually set the first 0-20 values (from mid-light gray gray to black)
    decrease_step = 10  # 0.1 for illustration purposes, 10 otherwise
    decrease_i = 10  # 0.1 for illustration purposes, 10 otherwise
    rgb_start = 200
    for i in range(20):  # 70
        decrease_i = decrease_step * i
        colormatrix.append(
            np.array(
                [
                    rgb_start - decrease_i,
                    rgb_start - decrease_i,
                    rgb_start - decrease_i,
                    1,
                ]
            )
            / 255
        )
        colormatrix[-1][-1] = 1  # Force alpha to 1

    # Manually set the 20-40 values (from black to mid-light gray)
    increase_step = 10
    increase_i = 10
    rgb_start = 0
    i = 0
    for j in range(20, 40):  # (120,140)
        increase_i = increase_step * i
        colormatrix.append(
            np.array(
                [
                    rgb_start + increase_i,
                    rgb_start + increase_i,
                    rgb_start + increase_i,
                    1,
                ]
            )
            / 255
        )
        colormatrix[-1][-1] = 1  # Force alpha to 1
        i += 1

    # Use interpolation to create a colormap between light gray and high-light gray
    for x in range(0, clientWidth):
        t = x / clientWidth
        colormatrix.append(
            [
                lerp(t, color2["r"], color1["r"]) / 255,
                lerp(t, color2["g"], color1["g"]) / 255,
                lerp(t, color2["b"], color1["b"]) / 255,
                1,
            ]
        )

    colormatrix = np.array(colormatrix)

    if verbose:
        print(
            f"Created an image (gray-black-gray-white) with shape: {colormatrix.shape}."
        )

    return colormatrix
