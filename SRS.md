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
