import sys
import csv
import numpy as np
import nrrd
import cv2
import time


def load_volume(filename):
    """Load a 3D NRRD volume."""
    volume, header = nrrd.read(filename)

    if volume.ndim != 3:
        raise ValueError("Input must be a 3D volume")

    return volume


def load_planes(filename):
    """Read planes defined by 3 or 4 points."""
    planes = []

    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            if not row:
                continue

            values = [float(value) for value in row]

            if len(values) not in (9, 12):
                raise ValueError(
                    "Each plane must contain 9 or 12 coordinates"
                )

            points = np.array(values).reshape(-1, 3)
            planes.append(points)

    return planes


def distance(a, b):
    """Calculate Euclidean distance."""
    return np.linalg.norm(a - b)


def validate_plane(points):
    """Validate a triangle or trapezoid."""
    eps = 0.001

    if len(points) == 3:
        a, b, c = points

        if abs(distance(a, b) - distance(a, c)) >= eps:
            raise ValueError("Triangle must be isosceles")

    elif len(points) == 4:
        a1, a2, b, c = points

        if abs(distance(a1, b) - distance(a2, c)) >= eps:
            raise ValueError("Trapezoid sides must be equal")

        if distance(a1, a2) > distance(b, c):
            raise ValueError("Invalid trapezoid dimensions")

        base1 = a2 - a1
        base2 = c - b

        if np.linalg.norm(np.cross(base1, base2)) > eps * np.linalg.norm(base1) * np.linalg.norm(base2):
            raise ValueError("Trapezoid bases must be parallel")

        normal = np.cross(a2 - a1, b - a1)
        if np.linalg.norm(normal) < 1e-10:
            raise ValueError("Degenerate trapezoid")

        coplanarity = abs(np.dot(normal, c - a1))
        if coplanarity / np.linalg.norm(normal) >= eps:
            raise ValueError("Trapezoid points must be coplanar")

    else:
        raise ValueError("A plane requires 3 or 4 points")


def project_plane(volume, points):
    """Extract a 2D image from a 3D volume."""
    validate_plane(points)

    if len(points) == 3:
        a, b, c = points
        start_left = a
        start_right = a
    else:
        a1, a2, b, c = points
        start_left = a1
        start_right = a2

    height = max(1, int(np.ceil(distance(start_left, b))))
    width = max(
        1,
        int(np.ceil(max(
            distance(start_left, start_right),
            distance(b, c)
        )))
    )

    image = np.zeros((height, width), dtype=volume.dtype)

    for y in range(height):
        t = (y + 0.5) / height

        left = start_left + t * (b - start_left)
        right = start_right + t * (c - start_right)

        row_width = min(width, max(1, int(np.ceil(distance(left, right)))))
        x_start = (width - row_width) // 2

        s = (np.arange(row_width) + 0.5) / row_width
        positions = left + s[:, None] * (right - left)

        indices = np.floor(positions + 0.5).astype(np.int64)

        valid = np.all(
            (indices >= 0) &
            (indices < np.array(volume.shape)),
            axis=1
        )

        valid_indices = indices[valid]
        image[y, x_start + np.flatnonzero(valid)] = volume[
            valid_indices[:, 0],
            valid_indices[:, 1],
            valid_indices[:, 2]
        ]

    return image


def normalize_image(image):
    """Convert a projection into an 8-bit image."""
    image = image.astype(np.float32)

    min_value = image.min()
    max_value = image.max()

    if max_value > min_value:
        image = (image - min_value) * 255.0 / (
            max_value - min_value
        )
    else:
        image = np.zeros_like(image)

    return image.astype(np.uint8)


def main():
    if len(sys.argv) != 4:
        print("Usage: python Ex0.py file.nrrd file.csv file.mp4")
        sys.exit(1)

    nrrd_file = sys.argv[1]
    csv_file = sys.argv[2]
    output_file = sys.argv[3]

    volume = load_volume(nrrd_file)
    planes = load_planes(csv_file)

    if not planes:
        raise ValueError("CSV file contains no planes")

    start_time = time.perf_counter()
    frames = []

    for points in planes:
        image = project_plane(volume, points)
        frame = normalize_image(image)
        frames.append(frame)

    elapsed = time.perf_counter() - start_time
    fps = len(frames) / elapsed
    print(f"Projection time: {elapsed:.4f} seconds")
    print(f"Projection FPS: {fps:.2f}")


    video_width = max(frame.shape[1] for frame in frames)
    video_height = max(frame.shape[0] for frame in frames)

    video_width += video_width % 2
    video_height += video_height % 2

    writer = cv2.VideoWriter(
        output_file,
        cv2.VideoWriter_fourcc(*"mp4v"),
        1,
        (video_width, video_height),
        isColor=True
    )

    if not writer.isOpened():
        raise RuntimeError("Could not create MP4 video")

    try:
        for frame in frames:
            canvas = np.zeros(
                (video_height, video_width),
                dtype=np.uint8
            )

            h, w = frame.shape
            y = (video_height - h) // 2
            x = (video_width - w) // 2

            canvas[y:y+h, x:x+w] = frame

            writer.write(
                cv2.cvtColor(canvas, cv2.COLOR_GRAY2BGR)
            )
    finally:
        writer.release()

    print(f"Video created: {output_file}")
    print(f"Total frames: {len(frames)}")


if __name__ == "__main__":
    main()
