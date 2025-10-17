import csv
import json
# ===== File paths =====
# Path to the CSV file exported from ImageJ (containing centroid coordinates of set ROIs)
csv_file_path = 'PATH\Results.csv'
# Path where the new JSON configuration file will be saved
json_file_path = 'PATH\config.json'

# ===== Initialize the JSON structure =====
# 'dishes' will store position data for each ROI (centroids)
# 'dish_setup' may define layout parameters (e.g., number of rows and columns)
data = {
    "dishes": [],
    "dish_setup": [5, 5] # example layout: 5x5 grid of dishes
}

# ===== Read the centroid coordinates from the CSV file =====
with open(csv_file_path, 'r') as csv_file:
    reader = csv.DictReader(csv_file)  # reads CSV rows as dictionaries using header names
    for i, row in enumerate(reader):
        # Convert centroid X and Y positions (strings) to integers
        x = int(row['X'])
        y = int(row['Y'])
        # Append each coordinate and a fixed radius (50) as a list
        # Format example: [[[x, y], 50], ...]
        data["dishes"].append([[x, y], 50])
# ===== Write the structured data into a JSON file =====
with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file)
# ===== Confirmation message =====
print("CSV to JSON conversion complete.")
