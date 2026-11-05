# Plane Projection Algorithm

## 1. Goal
Extract a 2D image from a 3D NRRD volume using a plane defined by 3 or 4 points.

## 2. Three-Point Plane
Given points `a, b, c` forming an isosceles triangle:

1. Validate `|dist(a,b) - dist(a,c)| < 0.001`.
2. Calculate `Dab = dist(a,b)` and `Dbc = dist(b,c)`.
3. Compute normalized vectors from `a` to `b` and `a` to `c`.
4. Create a 2D output matrix of size `Dab × Dbc`.
5. Move along both triangle sides, row by row.
6. Sample voxel values between the two sides.
7. Center each sampled row in the output matrix.
8. Assign zero to out-of-bounds samples.

## 3. Four-Point Plane
Given points `a1, a2, b, c` forming an isosceles trapezoid:

1. Validate equal-length sides within `EPS = 0.001`.
2. Verify `dist(a1,a2) <= dist(b,c)` and coplanarity.
3. Move along the two equal-length sides.
4. Sample voxel values between corresponding points.
5. Store the samples in a 2D output matrix.

## 4. Output
Each plane produces one 2D image. The images are combined into an MP4 video in CSV order.

## 5. Efficiency
Use NumPy vectorized operations to minimize Python loops and improve processing speed.
