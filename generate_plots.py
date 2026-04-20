"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""
# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.
import numpy as np


def generate_data(seed):
    """Generate synthetic sensor readings and timestamps.

    Parameters
    ----------
    seed : int
        Seed used to initialize NumPy's random number generator for
        reproducible output.

    Returns
    -------
    tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]
        A 3-item tuple containing:
        - sensor_a: Normally distributed samples with mean 25.0 and standard
          deviation 3.0.
        - sensor_b: Normally distributed samples with mean 27.0 and standard
          deviation 4.5.
        - timestamps: Sorted uniform samples from 0.0 to 10.0 seconds.
        All arrays have shape ``(200,)``.
    """
    rng = np.random.default_rng(seed=seed)
    n = 200
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=n)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=n)
    timestamps = np.sort(rng.uniform(low=0.0, high=10.0, size=n))
    return sensor_a, sensor_b, timestamps
