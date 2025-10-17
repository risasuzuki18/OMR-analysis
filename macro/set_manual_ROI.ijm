// ===== Initialize ROI Manager and measurement settings =====

// Open the ROI Manager window (ensures it's available)
run("ROI Manager...");

// Load a saved ROI set (zip) from disk (kept commented as in your script)
roiManager("Open", "PATH/RoiSet.zip");

// Ensure pixel-based units (no spatial calibration)
run("Set Scale...", "distance=0 known=0 unit=pixel");

// Configure measurements to record the centroid (X, Y) of each ROI; integers (decimal=0)
run("Set Measurements...", "centroid redirect=None decimal=0");

// Show all ROIs overlaid on the image with labels (helps visual verification)
// Align the circle with the petridish
roiManager("show all with labels");

// Pause execution until the user clicks "OK" (useful for checking ROI placement)
waitForUser;
// Deselect any selected ROI(s) so subsequent commands apply as intended
roiManager("deselect");
// Measure all ROIs currently in the ROI Manager according to Set Measurements (centroid here)
roiManager("Measure");
// Save the Results table (centroid measurements) as a CSV to the given path
saveAs("Results", "PATH/Results.csv");

// Close all open image windows (the current image and any others)
close("*");
run("Close All");
