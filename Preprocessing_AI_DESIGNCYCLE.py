from PIL import Image, ImageEnhance

# Load the image
image_path = r'C:\Users\HP\Pictures\Saved Pictures\TEMPLE_PUNE.jpg'  # Replace with the path to your image
image = Image.open(image_path)

# Choose adjustment type: 'brightness' or 'contrast'
adjustment_type = input("Type 'brightness' or 'contrast': ").strip().lower()

# Choose the enhancement factor
# 1.0 means original, <1.0 means decrease, >1.0 means increase
factor = float(input("Enter enhancement factor (e.g., 1.2 for 20% increase): "))

# Apply enhancement
if adjustment_type == 'brightness':
    enhancer = ImageEnhance.Brightness(image)
    enhanced_image = enhancer.enhance(factor)
elif adjustment_type == 'contrast':
    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(factor)
else:
    print("Invalid adjustment type!")
    exit()

# Save the result
output_path = 'enhanced_image_1.jpg'
enhanced_image.save(output_path)
print(f"{adjustment_type.capitalize()} adjusted image saved as {output_path}")


