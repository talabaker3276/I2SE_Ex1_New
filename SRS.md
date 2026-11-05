# Software Requirements Specification (SRS)

## 1. Purpose
Develop an efficient Python application that extracts 2D plane projections from 3D NRRD volumetric data.

## 2. Functional Requirements
- Load a 3D NRRD file containing unsigned 8, 16, or 32-bit values.
- Read plane coordinates from a CSV file.
- Support planes defined by 3 or 4 points.
- **3 points:** An isosceles triangle satisfying `|dist(a,b) - dist(a,c)| < 0.001`.
- **4 points:** An isosceles trapezoid with equal-length sides, `dist(a1,a2) <= dist(b,c)`, and coplanar points.
- Generate a 2D image for each plane.
- Assign zero to samples outside the volume.
- Export an MP4 video containing one frame per plane, in CSV order.

## 3. Non-Functional Requirements
- Correct and stable execution.
- Minimum performance requirement: 30 FPS.
- Target performance: 100 FPS for a 500×500×500 byte volume.
- Clear, modular, and maintainable code.

## 4. Input and Output
**Input:** A 3D NRRD file and a CSV file containing plane coordinates.

**Output:** An MP4 video containing the generated 2D projections.

## 5. Execution
```bash
python Ex0.py file.nrrd file.csv file.mp4
```


## 6. Input Validation and Error Handling

- Validate that each CSV row contains exactly 9 or 12 numeric values.
- Verify that 3-point planes form valid isosceles triangles.
- Verify that 4-point planes form valid isosceles trapezoids with parallel bases, equal-length sides, and coplanar points.
- Reject invalid plane definitions with a clear error message.
- Reject input volumes that are not three-dimensional.

## 7. Performance Verification

The implementation should achieve at least 30 FPS, with a target of 100 FPS on a 500x500x500 byte volume.

The current experiment demonstrates successful execution on the provided MRI dataset. Performance on a 500x500x500 volume has not yet been verified.
