import itertools
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
#define the directory where the images are stored
image_directory = os.path.join(os.path.dirname(__file__), 'color_ball')

#define the colors and corresponding images fliename

color_images = {
    'red': os.path.join(os.path.dirname(__file__), 'color_ball/red_ball.png'),
    #'blue': os.path.join(os.path.dirname(__file__), 'color_ball/blue_ball.png'),
    #'green': os.path.join(os.path.dirname(__file__), 'color_ball/green_ball.png'),
    'yellow': os.path.join(os.path.dirname(__file__), 'color_ball/yellow_ball.png')

}

#generate all possible combinations of colors
colors = list(color_images.keys())
permutations = list(itertools.permutations(colors))

#Function to plot a permutation of images
def plot_permutation(perm, index, ax):
    for i, color in enumerate(perm):
        img = mpimg.imread(color_images[color])
        ax[i].imshow(img)
        ax[i].axis('off')
        ax[i].set_title(color)
    ax[0].set_ylabel(f'Permutation {index+1}', fontsize=16)

# Adjust the loop to plot two permutations side by side
fig, axs = plt.subplots(len(permutations)//2, len(colors), figsize=(20, len(permutations)*3))
for index, perm in enumerate(permutations):
    if index % 2 == 0:  # Even index, new row
        plot_permutation(perm, index, axs[index//2])
    else:  # Odd index, same row as previous
        plot_permutation(perm, index, axs[index//2, len(colors):])

plt.tight_layout()
plt.show()