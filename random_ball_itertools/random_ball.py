import itertools
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import pandas as pd
#define the directory where the images are stored
image_directory = os.path.join(os.path.dirname(__file__), 'color_ball')

#define the colors and corresponding images fliename

color_images = {
    'red': os.path.join(os.path.dirname(__file__), 'color_ball/red_ball.png'),
    'blue': os.path.join(os.path.dirname(__file__), 'color_ball/blue_ball.png'),
    'green': os.path.join(os.path.dirname(__file__), 'color_ball/green_ball.png'),
    'yellow': os.path.join(os.path.dirname(__file__), 'color_ball/yellow_ball.png'),
    'orange': os.path.join(os.path.dirname(__file__), 'color_ball/orange_ball.png'),
    'purple': os.path.join(os.path.dirname(__file__), 'color_ball/purple_ball.png'),

}

#generate all possible combinations of colors
colors = list(color_images.keys())
permutations = list(itertools.permutations(colors))

#Function to plot a permutation of images
def plot_permutation(perm,index):
    fig, ax = plt.subplots(1, len(perm), figsize=(12, 3))
    for i, color in enumerate(perm):
        img = mpimg.imread(color_images[color])
        ax[i].imshow(img)
        ax[i].axis('off')
        ax[i].set_title(color)
    plt.suptitle(f'Permutation {index+1}', fontsize=16)
    plt.show()

for index, perm in enumerate(permutations):
    plot_permutation(perm, index)
# Convert permutations to a DataFrame for easier CSV export
df_permutations = pd.DataFrame(permutations, columns=[f'Color {i+1}' for i in range(len(colors))])

# Define the CSV file path
csv_file_path = os.path.join(os.path.dirname(__file__), 'permutation.csv')

# Export the DataFrame to a CSV file
df_permutations.to_csv(csv_file_path, index=False)

print(f'Permutations have been saved to {csv_file_path}')