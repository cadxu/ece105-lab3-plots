# ECE 105 Lab 3 Sensor Plots

Generate synthetic temperature sensor data and produce a single analysis figure containing scatter, histogram, and box-plot visualizations.

## Installation

Activate your `ece105` conda environment, then install dependencies with either conda or mamba:

```bash
conda activate ece105
conda install numpy matplotlib
```

Or:

```bash
conda activate ece105
mamba install numpy matplotlib
```

## Usage

Run the script from the project directory:

```bash
python generate_plots.py
```

## Example output

The script writes one PNG file:

- `sensor_analysis.png` (150 DPI, tight bounding box), containing three side-by-side plots:
  - **Scatter plot:** Sensor A and Sensor B readings versus timestamps.
  - **Histogram:** Overlaid distributions for both sensors with dashed mean lines.
  - **Box plot:** Side-by-side sensor distributions with a dashed overall-mean reference line.

## AI tools used and disclosure

This program was written with Copilot.
