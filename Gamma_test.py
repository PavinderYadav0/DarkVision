import cv2
import os
import numpy as np
import argparse

def adjust_gamma(image, gamma):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)

def main(input_image_path):
    img = cv2.imread(input_image_path)  # BGR

    gamma_values = [0.3, 0.5, 1.5, 2.0]
    processed_images = [img]
    for gamma in gamma_values[1:]:
        # Apply addWeighted for contrast and brightness adjustments
        contrast_img = cv2.addWeighted(img, 3, img, 0, 10)

        # Apply gamma correction
        gamma_corrected_img = adjust_gamma(contrast_img, gamma)

        # Normalize the image
        normalized_img = cv2.normalize(gamma_corrected_img, None, 20, 150, cv2.NORM_MINMAX)

        # Apply Gaussian blur
        blurred_img = cv2.GaussianBlur(normalized_img, (3, 3), 0)

        # Append the processed image to the list
        processed_images.append(blurred_img)

    # Concatenate the processed images horizontally
    combined_images = np.hstack(processed_images)

    # Write gamma values on each image
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 2
    color = (255, 255, 255)
    thickness = 2
    offset_x = 50
    offset_y = 100
    for i, gamma in enumerate(gamma_values[1:], start=1):  # Start from the second image
        gamma_text = f"Gamma: {gamma:.2f}"
        cv2.putText(combined_images, gamma_text, (i * img.shape[1] + offset_x, offset_y),
                    font, font_scale, color, thickness, cv2.LINE_AA)

    # Write label on the first image
    input_image_label = "Input Image"
    cv2.putText(combined_images, input_image_label, (offset_x, offset_y),
                font, font_scale, color, thickness, cv2.LINE_AA)

    # Create a directory named 'results' if it doesn't exist
    output_folder = 'results'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Save the combined image in the 'results' folder
    output_image_path = os.path.join(output_folder, 'Tested.jpg')
    cv2.imwrite(output_image_path, combined_images)

    # Show the combined image
    #cv2.imshow("Combined Images", combined_images)

    # Wait for a key press and then close the window
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process images and save results in a folder')
    parser.add_argument('input_image_path', type=str, help='Path to the input image')
    args = parser.parse_args()

    main(args.input_image_path)
