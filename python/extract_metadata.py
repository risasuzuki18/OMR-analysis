# ================================================================
# Script to extract and merge experiment metadata from Excel sheets
# ================================================================

from pathlib import Path, PosixPath
import pandas as pd

def save_df_as_csv(df, file_path):
    """
    Save a pandas DataFrame as a CSV file with consistent formatting.
    """
    df.to_csv(
        path_or_buf=file_path,
        sep=',',
        header=True,
        index=None,
        index_label=None,
        mode='w',
        decimal='.',
        na_rep='NaN',
        encoding='utf-8-sig'
    )
    print(file_path.name + ' has been saved at: ' + str(file_path))


# ===== Define input and output paths =====
excel_file = Path('Path_metadata.xlsx')   # Path to input Excel file
output_dir = Path('Path_output')          # Directory to save output CSV files


# ===== Import all sheets from the Excel file =====
# Read all sheets as a dictionary of DataFrames
# - sheet_name=None → reads all sheets
# - header=None → first row is not treated as header
# - usecols='A:D' → reads only columns A to D
excel_sheets = pd.read_excel(io=excel_file, sheet_name=None, header=None, usecols='A:D')


# ===== Keep only sheets with 'RS_' or 'BW_' in their names =====
# Keeping these sheets that contains experiments
excel_sheets = {
    sheet_name: sheet
    for (sheet_name, sheet) in excel_sheets.items()
    if any(experimenter in sheet_name for experimenter in ['RS_', 'BW_'])
}


# ===== Split and merge metadata and well info from each sheet =====
for sheet in excel_sheets:
    df = excel_sheets[sheet]

    # Find the split marker '#######' — separates experiment info (top) and well info (bottom)
    split_pos = df[df[0] == '#######'].index[0]

    # --- df1: experiment-level metadata ---
    df1 = df.iloc[:split_pos, 0:2].reset_index(drop=True)

    # --- df2: well-level metadata ---
    df2 = df.iloc[split_pos + 2:].reset_index(drop=True)
    df2.columns = df2.iloc[0]  # Set first row as column headers
    df2 = df2.drop(0).reset_index(drop=True)

    # --- Merge df1 and df2 ---
    # Each key-value pair in df1 becomes a new constant column in df2
    df2[df1[0]] = pd.DataFrame([df1[1]], index=df2.index)

    # Update dictionary with the merged DataFrame
    excel_sheets[sheet] = df2


# ===== Save each processed sheet as an individual CSV =====
for sheet in excel_sheets:
    filename = output_dir.joinpath(f'{sheet}_metadata.csv')
    save_df_as_csv(excel_sheets[sheet], filename)


# ===== Combine all processed sheets into one DataFrame =====
metadata_sheets_df = pd.concat(excel_sheets, axis=0).reset_index(drop=True)

# Save the combined metadata file
filename = output_dir.joinpath('#combined_sheet_metadata.csv')
save_df_as_csv(metadata_sheets_df, filename)


# ===== Print or return the final combined DataFrame (optional) =====
print(metadata_sheets_df)
