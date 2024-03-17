import PIL.Image

# Define the ASCII characters to use
#ASCII_CHARS = ['@', 'J', 'D', '%', '*', 'P', '+', 'Y', '$', ',', '.']
ASCII_CHARS = ' .,:;i1tfLCG08@'

def pixel_to_ascii(pixel):
    """Convert a pixel to an ASCII character."""
    return ASCII_CHARS[pixel // 25]


image_path = 'C:\\Users\\carte\\OneDrive\\Pictures\\20220509_071429.jpg'

def image_to_ascii(image_path):
    """Convert an image to ASCII art."""
    # Load the image
    try:
        with PIL.Image.open(image_path) as image:
            # Resize the image
            new_width = 120
            width, height = image.size
            aspect_ratio = height / width
            new_height = aspect_ratio * new_width * 0.55
            image = image.resize((new_width, int(new_height)))

            # Convert the image to grayscale
            image = image.convert('L')

            # Convert the pixels to ASCII characters
            pixels = image.getdata()
            ascii_chars = [pixel_to_ascii(pixel) for pixel in pixels]
            ascii_chars = ''.join(ascii_chars)

            # Split the ASCII characters into lines
            lines = [ascii_chars[index:index + new_width] for index in range(0, len(ascii_chars), new_width)]
            ascii_art = '\n'.join(lines)

            # Print the ASCII art to the console
            print(ascii_art)
    except FileNotFoundError:
        print(f"Error: Could not find file '{image_path}'")

image_to_ascii(image_path)
