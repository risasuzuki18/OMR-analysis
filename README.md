# 👀 OMR-analysis
R, python and Fiji macro scripts for OMR experiment analysis and plotting

- Prepare ROI files (manually set) for use in detection software
- Extract mean gray values from videos to retrieve timing information
- Organize detection data and timestamp data
- Format and integrate metadata for analysis
- Automate behavioral response analysis and statistical testing
- Generate plots 

## 📁 Folder Structure
```
OMR_analysis/
│
├── macros/              # Macros for ROI selection, gray-value extraction, etc
│   ├── time_stamp.ijm           # Calculate frame-wise mean gray value differences
│   ├── camera_source_id.ijm     # Identify whether TIFF stack is from the left or right camera
│   └── set_manual_ROI.ijm       # Select ROI manually and save as CSV
│
├── python/              # Helper scripts for pre-processing and organizing input data
│   ├── ROI_to_config_json.py     # Convert ROI CSV to config.json format for detect.py
│   ├── generate_text_for_automation.py # Create automation script for batch detection
│   ├── run_automation.py         # Execute batch detection automation
│   ├── extract_metadata.py       # Extract metadata from OMR_record.xlsx and combine into CSV
│   ├── rename_detection_files.py # Rename detections.csv files by appending experiment ID
│   └── rename_timestamp_csv.py   # Standardize filenames from time_stamp.ijm outputs
│   
├── R/                   # R scripts for data processing and analysis
│   ├── OMR_analysis_stripe_width.Rmd  # R script for stripe width sensitivity test analysis
│   ├── OMR_analysis_color_vision.Rmd  # R script for color vision test analysis
│   └── calculate_response_values.Rmd  # Compute response values used in above scripts
│
├── examples/            # Example CSV files (metadata, parameters)
│   ├── RoiSet.zip                # Example ROI set for 5×5 setup (used in time_stamp.ijm)
│   ├── camera_check.roi          # ROI preset used in camera_source_id.ijm
│   ├── OMR_record.xlsx           # Example Excel file of the metadata for experiments
│   ├── #combined_sheet_metadata.csv  # Sample output file from extract_metadata.py
│   ├── L_262_detections_reduced.csv  # Example CSV file output from detect.py
│   ├── CvGr2_int.csv             # Stripe parameters used in OMR_analysis_color_vision.Rmd
│   └── p1-6_int.csv              # Stripe parameters used in OMR_analysis_stripe_width.Rmd
│
└── README.md                     # Documentation and usage instructions
```

## 🔗 Code Availability

- **Stripe Generator** → https://github.com/dkalsan/rotating-radial-stripes
- **Detection Software** → https://github.com/dkalsan/rrs-fish-detector
- **This Repository** → Contains all macros, Python scripts, and R notebooks used for running the detection software, organizing metadata, and performing downstream behavioral analysis and plotting

## 🧭 How to Use

1. **Perform the OMR experiment** and prepare the metadata sheet (`OMR_record.xlsx`).
2. **Run `separate_videos.py`** (from the detection software) to split video into left/right `.tif` stacks.
3. *(Optional)* Use `set_manual_ROI.ijm` to manually set ROIs for each video.
4. *(Optional)* Convert `results.csv` (generated in set_manual_ROI.ijm) to `config.json` using `ROI_to_config_json.py`, then move the file to the corresponding video folder.
5. *(Optional)* Run `preview.py` (from the detection software) to visually confirm the manually set ROI.
6. *(Optional)* Generate batch automation text with `generate_text_for_automation.py`.
7. *(Optional)* Run `run_automation.py` to execute batch processing (this automates steps 8-11).
8. **Run `detect.py`** (from the detection software) to generate `detections.json`.
9. **Convert `detections.json` to CSV** using `detections_to_csv.py`.
10. **Identify camera side** (left/right) using `camera_source_id.ijm`.
11. **Rename detection files** with experiment ID using `rename_detection_files.py`.
12. **Extract time information** by running `time_stamp.ijm`.
13. **Standardize time-stamp filenames** using `rename_timestamp_csv.py`.
14. **Format metadata** by running `extract_metadata.py`.
15. **Run R scripts** to calculate response metrics, generate visualizations, and perform statistical tests.



