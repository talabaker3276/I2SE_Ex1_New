# Testing Strategy

## 1. Objective
Verify the correctness, stability, and performance of the 3D plane projection algorithm.

## 2. Test Cases
- **Test 1:** Load a valid 3D NRRD file.
- **Test 2:** Project a valid 3-point isosceles triangle.
- **Test 3:** Project a valid 4-point isosceles trapezoid.
- **Test 4:** Reject invalid plane definitions.
- **Test 5:** Return zero for coordinates outside the volume.
- **Test 6:** Verify output image dimensions and pixel values.
- **Test 7:** Verify one video frame per CSV row, preserving order.
- **Test 8:** Measure processing time and FPS.

## 3. Performance Requirements
- Minimum: 30 FPS.
- Target: 100 FPS for a 500×500×500 byte volume.

## 4. Experiment
Run the program using an NRRD dataset and a CSV file containing both 3-point and 4-point planes.

Record the execution time, FPS, and generated MP4 output.

## 5. Expected Result
The program should generate correct 2D projections and a valid MP4 video without errors.
