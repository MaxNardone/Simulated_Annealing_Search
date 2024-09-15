# Simulated_Annealing_Search
The goal of this project is to minimize an objective function by using the probabilistic optimization approach known as simulated annealing. By using a "cooling" strategy, the method searches a large solution space before eventually convergently arriving at the best solution.

## Table of Contents

- Features
- Installation
- Usage
- Optimization Process
- Visualization
- Acknowledgements

##  Features

- **Simulated Annealing Algorithm**: A robust optimization method for finding global minima in complex functions.
- **Visualization of the Optimization Path**: Visual tracking of the solution search process in 3D plot.

##  Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/Simulated_Annealing_Optimization.git
   cd Simulated_Annealing_Optimization
   ```

2. **Create a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**

   ```bash
   pip install -r requirements.txt
   ```

##  Usage

### Running the Python Script

```bash
python simulated_annealing.py
```

### Using the Jupyter Notebook

Launch the notebook using this command:

```bash
jupyter notebook Simulated_Annealing_search.ipynb
```

##  Optimization Process

In order to investigate potential solutions, the Simulated Annealing method progressively lowers randomness, or temperature, which results in a more focused search later on.

##  Visualization

The 3D visualizations provided in the notebook show the progression of the search across the solution space, allowing users to observe how the algorithm explores and converges on the optimal solution.

##  Acknowledgements
- **Jason Brownlee** for the core annealing code displayed in the .py file, available on “Machine Learning Mastery”.
- **Matplotlib** for enabling detailed 3D visualizations.
- **University of Surrey** for providing academic guidance on optimization techniques.
