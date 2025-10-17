// ===== Set the input/output folders and list their contents =====

// Show a message prompting the user to select the folder containing folders of videos (.tif) to analyze
	showMessage("Select Open Folder"); 
	openDir = getDirectory("Choose a Directory"); 
  
// Show a message prompting the user to select the folder where .csv results will be saved
	showMessage("Select Save Folder");
	saveDir = getDirectory("Choose a Directory"); 

// Get a list of all files or subfolders in the selected input directory
	list = getFileList(openDir);

// ===== Loop over each item (e.g., subfolder) in the selected directory =====
for (i=0; i<list.length; i++){
	
	openDir_2 = openDir + list[i];   // Path to the current subfolder
	list_2 = getFileList(openDir_2); // List of files within that subfolder

    setBatchMode("hide");          // Run in batch mode (no GUI updates) to speed up processing
    	
  // ===== Loop through files in the subfolder =====
	for (l=0; l<list_2.length; l++){
    //check if the file is a .tif file
       if (endsWith(list_2[l], ".tif")) {
		//Open the .tif stacks in the folder
		open(openDir_2+list_2[l]);
    // Run the defined operation on the opened image stack
		    operation();
	}
   }
}


// ===== Define the processing operation applied to each .tif stack =====
function operation(){
File_name = getTitle();         // Get current image name
Save_name = replace(File_name, ".ome.tif", ".csv");    // Create output filename by replacing extension

selectWindow(File_name);
numSlices = nSlices;           // Get total number of slices in the stack
numSlices_2 = numSlices - 1;   // One less for the shifted duplicate
duplicateRange = "duplicate range=2-" + numSlices;  // Range for 2..N
duplicateRange_2 = "duplicate range=1-" + numSlices_2; // Range for 1..N-1

// Duplicate slices 2..N to create Stack-1
selectWindow(File_name);
run("Duplicate...", duplicateRange);
rename("Stack-1");

// Duplicate slices 1..N-1 to create Stack-2
selectWindow(File_name);
run("Duplicate...", duplicateRange_2);
rename("Stack-2");

// Subtract Stack-2 from Stack-1 to compute frame-to-frame intensity differences 
imageCalculator("Subtract create stack", "Stack-1","Stack-2");

// Configure measurement options: mean gray values, 3 decimal places   
run("Set Measurements...", "mean redirect=None decimal=3");

// Select the subtraction result stack for measurement
selectWindow("Result of Stack-1");
run("Select All");      // Measure whole-frame mean for each slice

// Loop through all slices of the result stack and measure mean intensity
for (n = 1; n <= nSlices(); n++){
setSlice(n);
run("Measure");
}

// Save the Results table as a .csv file in the chosen output directory
saveAs("Results", saveDir + Save_name );

// Close the Results window and all image windows to prepare for next file
selectWindow("Results");
run("Close");
close("*");

}
