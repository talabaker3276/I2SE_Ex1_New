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


## 6. Detailed Implementation

The algorithm processes each plane independently.

1. Read the plane coordinates from the CSV file.
2. Validate the plane geometry using EPS = 0.001.
3. For a triangle, start both sides at point `a`.
4. For a trapezoid, start the sides at points `a1` and `a2`.
5. Calculate the output height from the length of the equal sides.
6. Calculate the output width from the maximum base length.
7. For each output row, calculate the interpolation parameter:
   `t = (y + 0.5) / height`.
8. Interpolate the left and right endpoints of the row.
9. Calculate the row width and center it in the output image.
10. Generate sample positions using NumPy vectorization.
11. Round each 3D sample position to the nearest voxel using
    `floor(position + 0.5)`.
12. Copy valid voxel values into the 2D image.
13. Leave out-of-bounds samples as zero.
14. Normalize the image to 8-bit grayscale.
15. Add the image as a frame to the MP4 video.

### Trapezoid Validation

For four points, the implementation checks:
- Equal-length sides within EPS.
- The starting base is not longer than the ending base.
- The two bases are parallel.
- All four points are coplanar.
- The geometry is not degenerate.

### Performance Measurement

Projection FPS is calculated as:

`FPS = number_of_frames / projection_elapsed_time`

The measurement includes projection and image normalization,
but excludes MP4 video encoding.

The current experiment does not verify performance on a
500x500x500 volume.
