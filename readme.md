# Monte Carlo Simulation for Semi-Circle Point Distribution

This repository contains a Python implementation of a Monte Carlo simulation to estimate the probability that a set of random points, generated inside a unit circle, are concentrated on the same side (semi-circle).

## Description

The simulation generates a given number of random points within the unit circle, calculates their polar angles, and checks whether the points are concentrated on the same half of the circle. The simulation is repeated multiple times, and the average probability of this happening is computed.

### Functions:
- **_points_is_one_side(points)**: Simulates whether a set of random points in the unit circle are concentrated on the same side (semi-circle). 
- **monto_carlo_points(num_iter, points)**: Runs the Monte Carlo simulation for `num_iter` iterations, each time generating `points` random points. It prints the average probability of the points being concentrated on one side.

## Installation

To run this simulation, you'll need Python (version 3.x recommended) and the following dependencies:

- **numpy**: For numerical operations.

You can install the required dependencies using `pip`:

```bash
pip install numpy
```

## Usage

To run the simulation, use the `monto_carlo_points` function. It takes two parameters:
- `num_iter`: The number of iterations for the Monte Carlo simulation.
- `points`: The number of random points generated in each iteration.

Example usage:

```python
monto_carlo_points(100000, 4)
```

This will run the simulation 100,000 times, each time generating 4 random points, and print the average probability of those points being concentrated on the same semi-circle.

## Output

The output of the function is the average probability that the points, after being randomly placed within the unit circle, are concentrated on one side of the circle.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

