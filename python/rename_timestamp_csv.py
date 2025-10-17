import os
import re


# ================================================================
# Function 1: rename_files()
# ================================================================
# This function renames files that follow a specific pattern:
# e.g., "20250117_RS_12_some_text_3.csv" → "RS_12_3.csv"
# Extracts:
#   - RS number (xxx)
#   - last numeric part before ".csv" (y)
# Pattern explained:
#   ^\d{8}_RS_(\d+)_.*_(\d+)\.csv$
#   └── 8 digits at start (date)
#         _RS_ then one or more digits (group 1)
#                some text (.*)
#                        underscore + digits (group 2)
#                                    .csv end
# ================================================================
def rename_files(folder_path):
    pattern = re.compile(r'^\d{8}_RS_(\d+)_.*_(\d+)\.csv$')

    for filename in os.listdir(folder_path):
        old_path = os.path.join(folder_path, filename)
        
        # Check if filename matches the pattern
        match = pattern.match(filename)
        if match:
            xxx = match.group(1)  # Extract RS number
            y = match.group(2)    # Extract trailing number before .csv
            
            # Construct new simplified name
            new_filename = f"RS_{xxx}_{y}.csv"
            new_path = os.path.join(folder_path, new_filename)
            
            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed '{filename}' to '{new_filename}'")
        else:
            print(f"Skipped '{filename}' as it doesn't match the pattern.")



# ================================================================
# Function 2: rename_files_2()
# ================================================================
# This function renames files that match a simpler pattern:
# e.g., "20250117_RS_45_sometext.csv" → "RS_45.csv"
# Extracts only:
#   - RS number (xxx)
# Pattern explained:
#   ^\d{8}_RS_(\d+)_.*\.csv$
#   └── 8 digits + '_RS_' + digits (group 1) + '_' + anything + '.csv'
# ================================================================
def rename_files_2(folder_path):
    pattern = re.compile(r'^\d{8}_RS_(\d+)_.*\.csv$')

    for filename in os.listdir(folder_path):
        old_path = os.path.join(folder_path, filename)
        
        match = pattern.match(filename)
        if match:
            xxx = match.group(1)  # Extract RS number
            
            # Construct new filename: RS_<number>.csv
            new_filename = f"RS_{xxx}.csv"
            new_path = os.path.join(folder_path, new_filename)
            
            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed '{filename}' to '{new_filename}'")
        else:
            print(f"Skipped '{filename}' as it doesn't match the pattern.")



# ================================================================
# Example usage
# ================================================================
# Replace the path below with the folder containing your CSV files created by time_stamp.ijm
# Both rename functions are run in sequence to handle two filename styles:
#   1. Files ending with a number before .csv (rename_files)
#   2. Files without that trailing number (rename_files_2)
# ================================================================
folder_path = '/PATH/Time_stamps'

rename_files(folder_path)
rename_files_2(folder_path)
