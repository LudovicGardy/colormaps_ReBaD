import numpy as np
from matplotlib.colors import ListedColormap

from modules.interpolation import create_custom_colormatrix_2D

def create_cmap(cmatrix_dict: dict, combine_two_cmaps: bool=True):
    '''
    Create a unique color matrix and color map using two
    concatenated 2D (shape = [cmap_length, rgb]) color maps.

    Parameters
    ----------
    r: list of floats:
        Red value, between 0 and 1
    g: list of floats:
        Green value, between 0 and 1
    b: list of floats
        Blue value, between 0 and 1

    Returns:
    color_matrix: numpy 2D array
        Contains all the rgb values for a given colormap
    color_map: matplotlib object
        The color_matrix transformed into an object that matplotlib can use on figures
    '''

    ### Init rgba matrix
    if combine_two_cmaps:
        cmatrix_2D = create_custom_colormatrix_2D(cmap_length=600, verbose=False)
        cmatrix_2D_length = len(cmatrix_2D)
        color_matrix = np.empty([len(cmatrix_dict["r"])+cmatrix_2D_length, 4])
        color_matrix.fill(0)
        color_matrix[0:cmatrix_2D_length] = cmatrix_2D

        ### Fill our empty matrix with our r,g,b values
        color_matrix[cmatrix_2D_length:, 0] = cmatrix_dict["r"]
        color_matrix[cmatrix_2D_length:, 1] = cmatrix_dict["g"]
        color_matrix[cmatrix_2D_length:, 2] = cmatrix_dict["b"]
        color_matrix[cmatrix_2D_length:, 3] = np.repeat(1, len(cmatrix_dict["b"]))  # alpha channel
    else:
        color_matrix = np.empty([len(cmatrix_dict["r"]), 4])
        color_matrix.fill(0)

        ### Fill our empty matrix with our r,g,b values
        color_matrix[:, 0] = cmatrix_dict["r"]
        color_matrix[:, 1] = cmatrix_dict["g"]
        color_matrix[:, 2] = cmatrix_dict["b"]
        color_matrix[:, 3] = np.repeat(1, len(cmatrix_dict["b"]))  # alpha channel

    color_map = ListedColormap(color_matrix)

    return(color_matrix, color_map)


def get_all_cmaps(HaReBaD_color_matrix_upper: np.ndarray):
    '''
    Given a list of 3D colormatrices (cmap_length, n_cmaps, rgba), extract the top row (highest values/colors)
    and store them to a 2D list (cmap_length, rgba) to use these colors as a colorbar with all the possible colors
    in the 3D list/array.
    '''
    rgb_max_all_cmaps = []
    for i in range(HaReBaD_color_matrix_upper[1, :, 1].shape[0]):
        rgb_max_all_cmaps.append(HaReBaD_color_matrix_upper[1, i, :])
    all_colormaps = ListedColormap(rgb_max_all_cmaps)

    return(all_colormaps)

def create_image():
    '''
    Create some random image on which we will apply the colormap.
    Any other image could replace this one.
    '''

    dx, dy = 0.015, 0.05
    x = np.arange(-4.0, 4.0, dx)
    y = np.arange(-4.0, 4.0, dy)
    X, Y = np.meshgrid(x, y)

    def z_fun(x, y):
        return (1 - x / 2 + x**5 + y**6) * np.exp(-(x**2 + y**2))

    Z2 = z_fun(X, Y)
    return(Z2)
