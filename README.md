# 3D Volume Plane Projection — Ex1

## Project Overview
This project implements an efficient algorithm for extracting 2D images from 3D NRRD medical imaging data.

## Plane Representation
The algorithm supports two types of planes:

- **3 points (a, b, c):** An isosceles triangle where `|dist(a,b) - dist(a,c)| < 0.001`.
- **4 points (a1, a2, b, c):** An isosceles trapezoid with equal-length sides, a shorter or equal starting edge, and coplanar points.

## Implementation
The project is implemented in Python and supports NRRD input, CSV plane definitions, and MP4 video output.

## Execution
```bash
python Ex0.py file.nrrd file.csv file.mp4
```

Each plane in the CSV generates one video frame, preserving the original order.

## Performance
The required minimum is 30 FPS, with a target of 100 FPS.

## Project Goal
Develop a correct, robust, and efficient plane projection algorithm with documented design, testing, and experimental results.
