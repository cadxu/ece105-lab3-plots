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
import matplotlib.pyplot as plt
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

# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.
def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Plot sensor readings against timestamps on a provided axes.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Sensor A readings to plot on the y-axis.
    sensor_b : numpy.ndarray
        Sensor B readings to plot on the y-axis.
    timestamps : numpy.ndarray
        Time values in seconds to plot on the x-axis.
    ax : matplotlib.axes.Axes
        Existing Matplotlib axes to modify in place.

    Returns
    -------
    None
        This function modifies ``ax`` in place and does not return a value.
    """
    ax.scatter(timestamps, sensor_a, color="tab:blue", alpha=0.75, s=20, label="Sensor A")
    ax.scatter(timestamps, sensor_b, color="tab:orange", alpha=0.75, s=20, label="Sensor B")
    ax.set_title("Sensor Readings Over Time")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Temperature (°C)")
    ax.legend()
    return None

# Create plot_histogram (sensor_a, sensor_b, timestamps, ax) that draws
# the histogram plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.
def plot_histogram(sensor_a, sensor_b, timestamps, ax):
    """Plot overlaid histograms for Sensor A and Sensor B.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Sensor A temperature readings.
    sensor_b : numpy.ndarray
        Sensor B temperature readings.
    timestamps : numpy.ndarray
        Timestamp array included for API consistency with other plotting
        functions; not used by this histogram.
    ax : matplotlib.axes.Axes
        Existing Matplotlib axes to modify in place.

    Returns
    -------
    None
        This function modifies ``ax`` in place and does not return a value.
    """
    ax.hist(sensor_a, bins=30, alpha=0.5, color="tab:blue", label="Sensor A")
    ax.hist(sensor_b, bins=30, alpha=0.5, color="tab:orange", label="Sensor B")

    mean_a = np.mean(sensor_a)
    mean_b = np.mean(sensor_b)
    ax.axvline(
        mean_a,
        color="tab:blue",
        linestyle="--",
        linewidth=2,
        label=f"Sensor A mean: {mean_a:.2f} C",
    )
    ax.axvline(
        mean_b,
        color="tab:orange",
        linestyle="--",
        linewidth=2,
        label=f"Sensor B mean: {mean_b:.2f} C",
    )

    ax.set_xlabel("Temperature (C)")
    ax.set_ylabel("Count")
    ax.set_title("Temperature Distributions for Sensor A and Sensor B")
    ax.legend()
    return None
# Create plot_boxplot (sensor_a, sensor_b, timestamps, ax) that draws
# the box plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.
def plot_boxplot(sensor_a, sensor_b, timestamps, ax):
    """Plot side-by-side box plots for Sensor A and Sensor B.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Sensor A temperature readings.
    sensor_b : numpy.ndarray
        Sensor B temperature readings.
    timestamps : numpy.ndarray
        Timestamp array included for API consistency with other plotting
        functions; not used by this box plot.
    ax : matplotlib.axes.Axes
        Existing Matplotlib axes to modify in place.

    Returns
    -------
    None
        This function modifies ``ax`` in place and does not return a value.
    """
    ax.boxplot([sensor_a, sensor_b], labels=["Sensor A", "Sensor B"])

    overall_mean = np.mean(np.concatenate([sensor_a, sensor_b]))
    ax.axhline(
        overall_mean,
        color="gray",
        linestyle="--",
        linewidth=1.8,
        label=f"Overall mean: {overall_mean:.2f} deg C",
    )

    ax.set_xlabel("Sensor")
    ax.set_ylabel("Temperature (deg C)")
    ax.set_title("Sensor Temperature Distributions (Box Plot)")
    ax.legend()
    return None

# Create main() that generates data, creates a 1x3 subplot figure,
# calls each plot function, adjusts layout, and saves as sensor_analysis.png
# at 150 DPI with tight bounding box.
def main():
    """Generate data, create plots, and save the analysis figure.

    Parameters
    ----------
    None
        This function does not take any parameters.

    Returns
    -------
    None
        This function saves ``sensor_analysis.png`` and does not return a value.
    """
    seed = 3376
    sensor_a, sensor_b, timestamps = generate_data(seed=seed)

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    plot_scatter(sensor_a, sensor_b, timestamps, axes[0, 0])
    plot_histogram(sensor_a, sensor_b, timestamps, axes[0, 1])
    plot_boxplot(sensor_a, sensor_b, timestamps, axes[1, 0])
    axes[1, 1].axis("off")  

    fig.tight_layout()
    fig.savefig("sensor_analysis.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
