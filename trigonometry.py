import math

def calculate_trigonometric_functions(angle_radians):
    cos_value = math.cos(angle_radians)
    sin_value = math.sin(angle_radians)
    tan_value = math.tan(angle_radians)

    return cos_value, sin_value, tan_value

# Example usage
angle_radians = math.radians(45)  # Convert 45 degrees to radians
cos_val, sin_val, tan_val = calculate_trigonometric_functions(angle_radians)

print(f"cos(45°) = {cos_val}")
print(f"sin(45°) = {sin_val}")
print(f"tan(45°) = {tan_val}")