import os
import sys

def rename_detections_file(path):
    # ===== File naming setup =====
    # The script looks for 'detections.csv' created by detect.py
    # and renames it depending on which camera file (L or R) is present.
    # camera file is created by camera_source_id.ijm
    target_filename = "detections.csv"
    camera_r_file = "Camera_R.csv"
    camera_l_file = "Camera_L.csv"
    
    # ===== Step 1: Check if detections.csv exists =====
    if target_filename not in os.listdir(path):
        print(f"Error: '{target_filename}' does not exist in the specified directory.")
        return
    
    # ===== Step 2: Extract experiment identifier from folder name =====
    # Example folder naming pattern: something_like_123_more
    # This extracts the "123" part (index 2 after splitting by '_')
    # Determine the 'nnn' part of the new filename from the directory name
    directory_name = os.path.basename(path)
    try:
        nnn = directory_name.split('_')[2]
    except IndexError:
        print("Error: The directory name does not follow the expected pattern (e.g., contains '_').")
        return

    # ===== Step 3: Determine which camera was used =====
    # Uses presence of 'Camera_R.csv' or 'Camera_L.csv' to decide prefix
    if camera_r_file in os.listdir(path):
        new_filename = f"R_{nnn}_detections.csv"  # Right camera
    elif camera_l_file in os.listdir(path):
        new_filename = f"L_{nnn}_detections.csv"  # Left camera
    else:
        print(f"Error: Neither '{camera_r_file}' nor '{camera_l_file}' found in the directory.")
        return
    
    # ===== Step 4: Rename detections.csv accordingly =====
    try:
        os.rename(
            os.path.join(path, target_filename),
            os.path.join(path, new_filename)
        )
        print(f"File renamed to: {new_filename}")
    except Exception as e:
        print(f"Error renaming file: {e}")

# ===== Main program entry =====
if __name__ == "__main__":
    # Expect exactly one argument: the path to the experiment directory
    if len(sys.argv) != 2:
        print("Usage: python script.py /path/to/directory")
    else:
        rename_detections_file(sys.argv[1])
