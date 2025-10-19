# OMR-analysis
R, python and Fiji macro scripts for OMR experiment analysis and plotting

OMR_analysis/
│
├── macros/              # Macros for ROI selection, gray-value extraction, etc
│   ├── time_stamp.ijm            # Calculate frame-wise mean gray value differences
│   ├── camera_source_id.ijm      # Identify whether TIFF stack is from the left or right camera
│   └── set_manual_ROI.ijm        # Select ROI manually and save as CSV
│
├── python/              # Helper scripts for pre-processing and organizing input data
│   ├── ROI_to_config_json.py     # Convert ROI CSV to config.json format for detect.py
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
│   └── p1-6_int.csv              # Stripe parameters used in OMR_analysis_stripe_width.Rmd
│
└── README.md                     # Documentation and usage instructions
