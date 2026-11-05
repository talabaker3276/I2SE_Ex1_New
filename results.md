# Experiment Results

## Dataset
- Input: MRHead_1.nrrd
- Plane definitions: planes.csv
- 10 planes defined by 3 points
- 1 plane defined by 4 points

## Results
- Total frames: 11
- Projection time: 0.0075 seconds
- Projection FPS: 1460.66
- Output video: output.mp4
- Video successfully generated and visually inspected.

## Conclusion
The initial experiment successfully generated an MP4 video containing 11 MRI projections.

The FPS measurement includes projection and image normalization, but excludes video encoding. Performance on a 500×500×500 volume has not yet been verified.

## 500x500x500 Benchmark

- Volume dimensions: 500x500x500
- Data type: uint8
- Test data: all zeros (synthetic)
- Total frames: 11
- Projection time: 0.0089 seconds
- Projection FPS: 1240.74
- Video: benchmark_output.mp4
- Video generation: successful

This benchmark measures projection and normalization,
excluding video encoding. It uses synthetic zero-valued
data and does not establish performance for all MRI inputs.