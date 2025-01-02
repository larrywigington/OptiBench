# **OptiBench**  
*A Benchmark Repository for Mathematical Optimization Problems*

## **Overview**  
Welcome to **OptiBench**, an open repository for benchmarking mathematical optimization algorithms. This repository provides a standardized collection of operations research problems, datasets, and baseline solutions. It also features a leaderboard for comparing algorithmic performance across various hardware configurations.  

Whether you're a researcher, student, or practitioner, **OptiBench** offers a platform to develop, test, and showcase optimization techniques.

---

## **Key Features**
- **Standardized Problem Sets**: Includes classical operations research problems like linear programming, integer programming, and combinatorial optimization.
- **Datasets**: A library of real-world and synthetic datasets for benchmarking.
- **Baseline Algorithms**: Implementations of well-known algorithms for comparison.
- **Leaderboard**: Submit your solutions and compare their performance on our dynamic leaderboard.
- **Community Contributions**: Open to contributions from researchers and developers.

---

## **Repository Structure**

```plaintext
OptiBench/
│
├── optibench/                        # Core Python package logic
│   ├── __init__.py                    # Initialization of package
│   ├── datasets/                      # Dataset generation tools
│   │   ├── __init__.py
│   │   ├── generate.py                # Logic for generating datasets
│   │   ├── lp/                        # Linear Programming datasets and problem generation
│   │   ├── nlp/                       # Nonlinear Programming datasets and problem generation
│   │   ├── cp/                        # Combinatorial Programming datasets and problem generation
│   │   └── ip/                        # Integer Programming datasets and problem generation
│   │
│   ├── problems/                      # Problem definitions (e.g., problem1.md)
│   │   ├── lp/                        # Problem definitions for LP
│   │   ├── nlp/                       # Problem definitions for NLP
│   │   ├── cp/                        # Problem definitions for CP
│   │   └── ip/                        # Problem definitions for IP
│   │
│   ├── baselines/
│   │   ├── lp.py                      # Simplex/Interior Point Method
│   │   ├── nlp.py                     # Gradient Descent, etc.
│   │   ├── cp.py                      # Backtracking, Branch & Bound, etc.
│   │   └──ip.py                      # Mixed-Integer Programming solvers
│   │
│   ├── leaderboard/                   # Interaction with GitHub leaderboard
│   │   ├── __init__.py
│   │   ├── leaderboard.py             # Logic for submitting results to GitHub leaderboard
│   │   ├── fetch_leaderboard.py       # Logic for fetching leaderboard data
│   │   └── authenticate.py            # GitHub authentication tools (via GitHub API)
│   │
│   ├── submissions/                   # User-submitted solutions
│   │   ├── __init__.py
│   │   └── submit_solution.py         # Logic for submitting solutions to the repo
│   │   
│   ├── tests/
│   │   ├── test_generate_datasets.py   # Unit tests for dataset generation tools.
│   │   ├── test_baselines.py           # Tests for baseline algorithms.
│   │   └──test_leaderboard.py         # Tests GitHub interaction and leaderboard API.
│   │   
│   └──cli.py                         # Command line interface for dataset generation & submission
│
├── datasets/                          # Predefined large datasets for benchmarking (large storage)
├── submissions/                       # Directory for user submissions (files will be managed by script)
├── README.md                          # Main README with repo instructions
├── setup.py                           # Packaging details for the PyPI package
├── requirements.txt                   # Python package dependencies
└── LICENSE                            # License file
```

---

## **Getting Started**
### **1. Clone the Repository**
```bash
git clone https://github.com/larrywigington/OptiBench.git
cd OptiBench
```

### **2. Explore the Problems**
Navigate to the `problems/` directory to explore available problems and their descriptions.

### **3. Test Your Algorithm**
- Select a problem and dataset.
- Use the baseline algorithms in `baselines/` as a starting point.
- Implement your algorithm following the submission guidelines in `CONTRIBUTING.md`.

### **4. Submit Your Results**
Submit your solution, performance metrics, and hardware details to `submissions/`. Your results will be validated and added to the leaderboard.

---

## **Example Problem**
### Linear Programming: Transportation Problem
- **Description**: Minimize the cost of transporting goods from suppliers to consumers.
- **Input**: Supply vector, demand vector, and cost matrix.
- **Output**: Optimal transportation plan and cost.
- **Baseline**: Simplex Method.

---

## **Contributing**
We welcome contributions! To contribute:
1. Fork this repository.
2. Add new problems, datasets, or solutions.
3. Submit a pull request.

Refer to `CONTRIBUTING.md` for detailed guidelines.

---

## **Leaderboard**
The leaderboard ranks submissions based on:
- Solution quality.
- Runtime performance.
- Hardware efficiency.

Stay competitive by submitting optimized solutions!

---

## **License**
This repository is licensed under the MIT License. See `LICENSE` for details.

---

## **Acknowledgments**
Thanks to the optimization and operations research community for their invaluable contributions and feedback.  

---

Feel free to modify this as needed. Would you like me to prepare any additional files, such as `CONTRIBUTING.md` or `LICENSE`?
