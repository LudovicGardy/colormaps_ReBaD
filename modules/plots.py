import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable, axes_size
from matplotlib.colors import ListedColormap

from modules.plot_utils import create_image

def show_all_available_colormaps(HaReBaD_color_matrix_upper, all_colormaps):
    ### Plot color matrices list
    f, ax = plt.subplots(figsize= (5,5))

    img = ax.imshow(HaReBaD_color_matrix_upper, cmap =all_colormaps, alpha = 0.7, 
            interpolation ='bilinear', aspect = "auto")
    ax.set_yticks([])
    ax.set_xticks([])
    ax.set_title(f"\nThere are {HaReBaD_color_matrix_upper.shape[1]} color maps of shape ({HaReBaD_color_matrix_upper.shape[0]},{HaReBaD_color_matrix_upper.shape[2]}).\n")
    ax.set_xlabel(f"Color maps (from i=0 to i=n={HaReBaD_color_matrix_upper.shape[1]})")
    ax.set_ylabel(f"Color map <i> length (size = {HaReBaD_color_matrix_upper.shape[0]})")

    #- Create colorbar
    aspect = 20
    pad_fraction = 0.5
    divider = make_axes_locatable(ax)
    height = axes_size.AxesX(ax, aspect=2/100)
    pad = axes_size.Fraction(0.5, height)
    cax = divider.append_axes("right", size=height, pad=pad)
    cax.tick_params(axis='both', which='major')
    plt.colorbar(img, cax=cax, orientation="vertical")
    cax.set_yticks([])
    cax.set_xticks([]) 

# Fonction pour afficher un exemple individuel
def show_individual_example(HaReBaD_color_matrix_upper, color_map_i, ax):
    color_map = ListedColormap(HaReBaD_color_matrix_upper[:, color_map_i, :][::-1])

    #- Create image
    custom_image_shape = create_image()
    img = ax.imshow(custom_image_shape, cmap=color_map, alpha=0.7, 
                    interpolation='bilinear', aspect="auto")

    #- Create colorbar
    aspect = 20
    pad_fraction = 0.5
    divider = make_axes_locatable(ax)
    height = axes_size.AxesX(ax, aspect=2/100)
    pad = axes_size.Fraction(0.5, height)
    cax = divider.append_axes("right", size=height, pad=pad)
    cax.tick_params(axis='both', which='major')
    plt.colorbar(img, cax=cax, orientation="vertical")

    return color_map

def show_multiple_examples(HaReBaD_color_matrix_upper):
    f, ax = plt.subplots(4, 4, figsize=(10,10))
    for i in range(4):
        for j in range(4):
            color_map_i = i*4+j
            color_map = show_individual_example(HaReBaD_color_matrix_upper, color_map_i, ax)
            ax[i,j].set_title(f"Color map {color_map_i}")
            ax[i,j].set_yticks([])
            ax[i,j].set_xticks([])

    plt.tight_layout()
    plt.show()