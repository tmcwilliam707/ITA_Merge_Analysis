# Define valid municipalities
VALID_MUNICIPALITIES = ["Municipality1", "Municipality2", "Municipality3"]

def check_non_null(value, field_name):
    if value is None:
        return f"{field_name} cannot be null."
    return None

def check_valid_municipality(municipality):
    if municipality not in VALID_MUNICIPALITIES:
        return f"Invalid municipality: {municipality}."
    return None

def check_valid_coordinates(lat, lon):
    if not (-90 <= lat <= 90):
        return f"Latitude {lat} out of range (-90 to 90)."
    if not (-180 <= lon <= 180):
        return f"Longitude {lon} out of range (-180 to 180)."
    return None

def validate_address_point(address_point):
    errors = []
    errors.append(check_non_null(address_point.get("address"), "Address"))
    errors.append(check_non_null(address_point.get("municipality"), "Municipality"))
    errors.append(check_valid_municipality(address_point.get("municipality")))
    errors.append(check_valid_coordinates(address_point.get("latitude"), address_point.get("longitude")))
    return [error for error in errors if error is not None]

# Example usage
address_points = [
    {"address": "123 Main St", "municipality": "Municipality1", "latitude": 45.0, "longitude": -75.0},
    {"address": None, "municipality": "Municipality4", "latitude": 95.0, "longitude": -75.0},
]

for address_point in address_points:
    validation_errors = validate_address_point(address_point)
    if validation_errors:
        print(f"Validation errors for {address_point}: {validation_errors}")
    else:
        print(f"Address point {address_point} is valid.")