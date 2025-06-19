import cv2
import numpy as np
import os
import matplotlib.pyplot as plt


def noise_image(image, noise_level, noise_type):
    if noise_type == "gaussian":
        noise = np.random.normal(0, noise_level, image.shape)
        return image + noise
    elif noise_type == "uniform":
        noise = np.random.uniform(-noise_level, noise_level, image.shape)
        return image + noise
    elif noise_type == "salt_and_pepper":
        noise = np.random.randint(0, 2, image.shape)
        return image * noise
    elif noise_type == "poisson":
        noise = np.random.poisson(noise_level, image.shape)
        return image + noise
    else:
        raise ValueError("Invalid noise type")

def display_images_side_by_side():
    fig, axes = plt.subplots(1, 4, figsize=(20, 5))
    
    base_path = "data/5_base_Race_ethnicity.jpg" #create plot to show difference in noise
    noisy_paths = [
        "noisy/5_base_Race_ethnicity_e2.jpg",
        "noisy/5_base_Race_ethnicity_e3.jpg",
        "noisy/5_base_Race_ethnicity_e4.jpg"
    ]
    
    original = cv2.imread(base_path)
    original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
    
    axes[0].imshow(original)
    axes[0].set_title('Original')
    axes[0].axis('off')
    
    for idx, path in enumerate(noisy_paths, 1):
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        axes[idx].imshow(img)
        axes[idx].set_title(f'Noise Level e{idx+1}')
        axes[idx].axis('off')
    
    plt.tight_layout()
    plt.show()

def main():
    directory = "data"
    os.makedirs("noisy", exist_ok=True)
    for file in os.listdir(directory):
        image = cv2.imread(os.path.join(directory, file))
        noisy_image_e2 = noise_image(image, 1e2, "gaussian")
        noisy_image_e3 = noise_image(image, 1e3, "gaussian")
        noisy_image_e4 = noise_image(image, 1e4, "gaussian")
        cv2.imwrite(os.path.join("noisy", file.replace(".jpg", "_e2.jpg")), noisy_image_e2)
        cv2.imwrite(os.path.join("noisy", file.replace(".jpg", "_e3.jpg")), noisy_image_e3)
        cv2.imwrite(os.path.join("noisy", file.replace(".jpg", "_e4.jpg")), noisy_image_e4)
    
    display_images_side_by_side()

if __name__ == "__main__":
    main()
