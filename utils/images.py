import os
import random
import matplotlib.pyplot as plt


def visualize_images(path: str = '../data/train', num_images: int = 5) -> None:
    """Displays a random selection of images from a specified directory.
    
    This function selects a given number of random images from the provided directory and displays them in a single row using matplotlib.

    Args:
        path (str): The directory path containing images. Defaults to '../data/train'.
        num_images (int): The number of images to display. Defaults to 5.

    Raises:
        ValueError: If no images are found in the specified path.
    """
    
    # Get a list of image filenames
    image_filenames = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

    if not image_filenames:
        raise ValueError("No images found in the specified path")

    # Select random images
    selected_images = random.sample(image_filenames, min(num_images, len(image_filenames)))

    # Create a figure and axes
    fig, axes = plt.subplots(1, num_images, figsize=(15, 3), facecolor='white')

    # Display each image
    for i, image_filename in enumerate(selected_images):
        # Load image
        image_path = os.path.join(path, image_filename)
        image = plt.imread(image_path)

        # Display image
        axes[i].imshow(image)
        axes[i].axis('off')
        axes[i].set_title(image_filename)  # Set image filename as title

    # Adjust layout and display
    plt.tight_layout()
    plt.show()
