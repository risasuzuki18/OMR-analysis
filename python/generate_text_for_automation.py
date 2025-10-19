# add the paths to folders with tif siles to PATH_1, PATH_2...

import os

# Function to generate a single script for all paths
def generate_script(folder_paths, output_file="script_output.txt"):
    # Determine the directory where the current Python script is located
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Set the output file path to the same directory as the script
    output_file_path = os.path.join(script_directory, output_file)

    base_script = """cd cOMR
cd rrs-fish-detector
workon comr
python detect.py {path}
python detections_to_csv.py {path} --fields time relative_theta --angle_unit deg --angle_positive
python PATH\\rename_detections_file.py {path}\n\n"""

    # Open the output file to write the content
    with open(output_file_path, 'w') as script_file:
        # Loop over each folder path in the list
        for folder_path in folder_paths:
            # Replace the placeholder with the actual folder path
            script_content = base_script.format(path=folder_path)
            # Write the script content to the file
            script_file.write(script_content)
        
    print(f"Generated single script file: {output_file}")

# Add full paths to folders containing TIFF files below.
# Each path should point to a folder you want to run the detection pipeline on.
# Example: r"C:\Users\YourName\Documents\fish_data\experiment_1"
folder_paths = [
r"PATH_1",
r"PATH_2"
# Add more paths as needed
]

generate_script(folder_paths, "combined_script_output.txt")
