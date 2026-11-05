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



## 6. Test Execution Status

| Test | Status | Notes |
|---|---|---|
| Load valid NRRD | Passed | MRHead_1.nrrd loaded successfully |
| Valid 3-point planes | Passed (demo) | 10 planes processed |
| Valid 4-point plane | Passed (demo) | 1 plane processed |
| Invalid plane definitions | Not yet tested | Requires negative test cases |
| Out-of-bounds coordinates | Not yet tested | Requires boundary tests |
| Image dimensions and pixel values | Not yet verified | Requires comparison with expected values |
| Video frame count | Passed | 11 frames generated |
| Video frame order | Not yet verified | Requires frame-by-frame comparison |
| Performance on 500x500x500 | Not yet tested | Required benchmark |

## 7. Demo Execution

Command:

`python3 Ex0.py MRHead_1.nrrd planes.csv output.mp4`

Latest observed results:

- Projection time: 0.0074 seconds
- Projection FPS: 1490.41
- Total frames: 11
- MP4 video generated successfully

The FPS measurement excludes video encoding.
The reported FPS is specific to this experiment and
does not establish performance on a 500x500x500 volume.
