import os
from dotenv import load_dotenv

load_dotenv()

def calculate_triangle_area(width, height):
    try:
        return 0.5 * width * height
    except:
        return -1

if __name__ == "__main__":
    width = os.getenv("ENV_WIDTH")
    height = os.getenv("ENV_HEIGHT")

    area_of_triangle = calculate_triangle_area(float(width), float(height))

    print(area_of_triangle)
