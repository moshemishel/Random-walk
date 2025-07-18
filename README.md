# Random Walk Simulation

A comprehensive multi-dimensional random walk simulator with advanced visualization capabilities and support for multiple simultaneous walkers.

## Overview

This project implements a sophisticated random walk simulation that can operate in any number of dimensions. Random walks are fundamental stochastic processes used across physics, finance, biology, and computer science to model phenomena ranging from particle diffusion to stock price movements.

**Key Innovation**: Unlike basic random walk implementations, this simulator provides intelligent visualization that automatically adapts to the dimensionality of your data, supporting everything from simple 1D time series to complex high-dimensional explorations.

## Features

### 🚀 **Multi-Dimensional Support**
- **1D**: Time-series visualization of position evolution
- **2D**: Beautiful trajectory plots in the plane
- **3D**: Interactive 3D path visualization with rotation and zoom
- **4D+**: Comprehensive tabular analysis with all dimensional data

### 👥 **Multiple Walker Support**
- Simulate multiple independent walkers simultaneously
- Compare different random walk instances
- Analyze statistical properties across multiple realizations

### 📊 **Intelligent Visualization**
- Automatic format selection based on dimensionality
- High-quality matplotlib graphics
- Interactive 3D plots with full camera control
- Clean, professional data tables for high-dimensional analysis

### ⚙️ **Flexible Configuration**
- Configurable number of walkers, dimensions, and steps
- Robust input validation with clear error messages
- Extensible architecture for custom walk types

## Installation

### Prerequisites
```bash
python >= 3.10
```

### Dependencies
```bash
pip install matplotlib pandas numpy
```

### Quick Start
```bash
git clone <repository-url>
cd random-walk-simulation
python random_walk.py
```

## Usage Guide

### Basic Usage
```bash
python random_walk.py
```

The program will prompt you for three parameters:
1. **Number of walkers** (≥1): How many independent random walks to simulate
2. **Number of dimensions** (≥1): The dimensionality of the space
3. **Number of steps** (≥1): Length of each random walk

### Example Scenarios

#### 📈 **1D Random Walk - Stock Price Model**
```
Please enter number of walkers: 5
Please enter number of dims: 1
Please enter number of steps: 252
```
*Simulates 5 different "stock price" paths over a trading year (252 days)*

#### 🗺️ **2D Random Walk - Particle Diffusion**
```
Please enter number of walkers: 3
Please enter number of dims: 2
Please enter number of steps: 1000
```
*Models 3 particles diffusing in a 2D medium*

#### 🌐 **3D Random Walk - Molecular Motion**
```
Please enter number of walkers: 1
Please enter number of dims: 3
Please enter number of steps: 500
```
*Visualizes molecular Brownian motion in 3D space*

#### 📊 **High-Dimensional Analysis**
```
Please enter number of walkers: 2
Please enter number of dims: 6
Please enter number of steps: 100
```
*Explores random walks in 6D space with tabular output*

## Algorithm Details

### Core Random Walk Process
1. **Initialization**: All walkers start at the origin (0 in all dimensions)
2. **Step Generation**: At each time step:
   - Randomly select one dimension from available dimensions
   - Randomly choose direction: +1 (forward) or -1 (backward)
   - Move exactly one unit in the chosen direction
3. **Path Recording**: Complete trajectory is stored for analysis and visualization

### Mathematical Properties
- **Step Size**: Fixed unit steps (±1)
- **Dimension Selection**: Uniform random selection
- **Direction Selection**: Uniform random ±1
- **Expected Displacement**: 0 (unbiased random walk)
- **Variance**: Grows linearly with number of steps

## Code Architecture

### 🏗️ **Main Components**

#### `random_walk(walkers, dims, steps)`
- **Purpose**: Main orchestration function
- **Input**: Configuration parameters
- **Output**: Complete simulation with visualization
- **Features**: Input validation, coordinate initialization, walker management

#### `make_random_steps(coordinates, walker)`
- **Purpose**: Executes random walk algorithm for a single walker
- **Algorithm**: Iterative step generation with random dimension/direction selection
- **Efficiency**: O(steps × dimensions) time complexity

#### `display_coordinates(coordinates)`
- **Purpose**: Intelligent visualization dispatcher
- **Logic**: Automatic format selection based on dimensionality
- **Outputs**: 
  - 1D: `plt.plot()` time series
  - 2D: `plt.plot()` trajectory paths
  - 3D: `plt.axes(projection='3d')` interactive plots
  - 4D+: `pandas.DataFrame` formatted tables

### 🔧 **Technical Implementation**

#### Data Structure
```python
coordinates = [
    [  # Walker 0
        [x0, x1, x2, ...],  # Dimension 0 over time
        [y0, y1, y2, ...],  # Dimension 1 over time
        # ... more dimensions
    ],
    # ... more walkers
]
```

#### Memory Efficiency
- **Space Complexity**: O(walkers × dimensions × steps)
- **Pre-allocation**: All arrays initialized to optimal size
- **No Dynamic Resizing**: Eliminates memory fragmentation

## Applications & Use Cases

### 🔬 **Scientific Research**
- **Physics**: Brownian motion, diffusion processes, particle transport
- **Chemistry**: Molecular dynamics, reaction kinetics
- **Biology**: Animal foraging patterns, cell migration, epidemiology

### 💰 **Financial Modeling**
- **Stock Prices**: Simple random walk models
- **Interest Rates**: Term structure modeling
- **Risk Analysis**: Monte Carlo simulations

### 🤖 **Computer Science**
- **Algorithm Design**: Randomized search algorithms
- **Machine Learning**: Random sampling methods
- **Network Analysis**: Random graph traversal

### 📚 **Educational Applications**
- **Probability Theory**: Stochastic process demonstrations
- **Statistics**: Central limit theorem illustrations
- **Data Science**: Monte Carlo method examples

## Performance Characteristics

### Computational Complexity
- **Time**: O(walkers × steps × dimensions)
- **Space**: O(walkers × dimensions × steps)
- **Scalability**: Linear in all parameters

### Recommended Limits
- **Interactive Use**: ≤10 walkers, ≤1000 steps
- **Batch Analysis**: ≤100 walkers, ≤10,000 steps
- **Memory Considerations**: Monitor usage for high-dimensional cases

## Advanced Features & Extensions

### 🚀 **Potential Enhancements**
- **Biased Random Walks**: Add drift parameters
- **Lévy Flights**: Heavy-tailed step distributions
- **Boundary Conditions**: Reflecting or absorbing boundaries
- **Correlated Steps**: Add memory to the process
- **Custom Step Distributions**: Non-uniform step sizes

### 📁 **Data Export Options**
- **CSV Output**: For external analysis
- **JSON Format**: For web applications
- **HDF5**: For large-scale data storage
- **Image Export**: High-resolution plot saving

### 📊 **Statistical Analysis**
- **Displacement Statistics**: Mean, variance, higher moments
- **Path Analysis**: Tortuosity, fractal dimension
- **Ensemble Averaging**: Multi-walker statistics
- **Correlation Analysis**: Step-to-step dependencies

## Troubleshooting

### Common Issues
1. **Import Errors**: Ensure all dependencies are installed
2. **Memory Issues**: Reduce walkers/steps for large simulations
3. **Visualization Problems**: Check matplotlib backend configuration
4. **Performance**: Consider reducing parameters for slow systems

### Error Messages
- `"Number of walkers must be positive"`: Enter values ≥ 1
- `"Number of dims must be positive"`: Enter values ≥ 1
- `"Number of steps must be positive"`: Enter values ≥ 1

## Contributing

This project welcomes contributions! Areas for improvement:
- Additional visualization options
- Performance optimizations
- New random walk variants
- Statistical analysis tools
- Documentation enhancements

## License

This project is open source. Please check the LICENSE file for specific terms.

## References

- Berg, H.C. (1993). *Random Walks in Biology*. Princeton University Press.
- Metzler, R., & Klafter, J. (2000). The random walk's guide to anomalous diffusion. *Physics Reports*, 339(1), 1-77.
- Redner, S. (2001). *A Guide to First-Passage Processes*. Cambridge University Press.

---

**Version**: 1.0  
**Python Compatibility**: 3.10+  
**Last Updated**: 2025
