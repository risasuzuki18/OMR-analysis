// ===== Load ROI Manager and predefined ROI set =====
// Open the ROI Manager window (ensures it's active)
run("ROI Manager...");
// Load a predefined ROI file that contains one or more regions of interest
// In this case, the ROI is positioned on the RIGHT EDGE of each image.
// This region is chosen because:
// - When the camera is from the LEFT side, prisms and black/white stripes appear in this area,
//   resulting in higher mean gray values.
// - When the camera is from the RIGHT side, that region is dark (almost black),
//   so the mean gray values are close to zero.
roiManager("Open", "PATH/camera_check.roi");

// ===== Set up directory and file handling =====
// Ask the user to select the folder containing folders with videos for analysis
showMessage("Select Open Folder"); 
openDir = getDirectory("Choose a Directory"); 
// Get a list of all items (subfolders or files) inside the selected directory
list = getFileList(openDir);

// ===== Loop over each subfolder in the selected directory =====
for (i = 0; i < list.length; i++) {
    // Build full path for each subfolder
    openDir_2 = openDir + list[i];
    // Get a list of files inside that subfolder
    list_2 = getFileList(openDir_2);
    // Run in batch mode (faster and without GUI updates)
    setBatchMode("hide");
        
    // ===== Process each .tif file within the subfolder =====
    for (l = 0; l < list_2.length; l++) {
        // Check if the file is a .tif file
        if (endsWith(list_2[l], "_14.ome.tif")) { //open one specific .tif file
            // Open the .tif stacks in the folder
            open(openDir_2 + list_2[l]);
            operation(openDir_2); // Pass the current folder path to the operation function
        }
    }
}

// ===== Define the measurement and classification function =====
function operation(currentDir) {
    File_name = getTitle(); // Get the name of the currently opened image
    // Configure measurement settings: measure mean gray value with 3 decimal places
    run("Set Measurements...", "mean redirect=None decimal=3");
    // Measure the mean gray value for the ROI(s) loaded in the ROI Manager
    roiManager("Measure");
    // Retrieve the measured "Mean" value from the last row of the Results table
    Mean = getResult("Mean", nResults - 1); 

    // ===== Classify and name output file based on the Mean value =====
    // If mean gray value is greater than 20 → label as "Camera_L"
    // Otherwise → label as "Camera_R"
    if (Mean > 20) {
        Save_name = "Camera_L.csv";
    } else {
        Save_name = "Camera_R.csv";
    }

    // Save the Results table as a CSV file in the same folder as the image
    saveAs("Results", currentDir + Save_name);

    // Close the Results table to avoid duplication
    close("Results");

    // Close the current image
    close("*");
}
