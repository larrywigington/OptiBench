# CONTRIBUTING.md

# **Contributing to OptiBench**

Thank you for your interest in contributing to **OptiBench**! We welcome contributions of all kinds, including bug fixes, new features, documentation improvements, code refactoring, and new benchmark datasets or algorithms.

To make the contribution process smooth and efficient, please follow these guidelines.

---

## **Getting Started**

### **Step 1: Prerequisites**

Ensure you have the following installed on your system:
- **Python 3.7 or later** (we recommend the latest version).
- **pip**: Python's package installer.
- **Git** for version control.

### **Step 2: Fork and Clone Repository**
1. Fork the repository on GitHub.
2. Clone your forked repository locally:
   ```bash
   git clone https://github.com/larrywigington/OptiBench.git
   ```
3. Navigate into the project directory:
   ```bash
   cd OptiBench
   ```

---

## **Development Workflow**

### **Step 1: Set Up Your Environment**
1. Install dependencies for the project:
   ```bash
   pip install -r requirements.txt
   ```
2. Install OptiBench locally in editable mode:
   ```bash
   pip install -e .
   ```

### **Step 2: Create a New Branch**
Create a new branch for your feature or fix:
```bash
git checkout -b your-feature-branch
```

Make sure you name your branch descriptively (e.g., `fix-issue-42` or `add-transportation-dataset`).

### **Step 3: Make Your Changes**
Modify the relevant files and add tests (if applicable). Follow these guidelines:
- Maintain the structure outlined by the **repository's file organization**.
- Write clear, clean, and efficient code.
- Add docstrings for all new functions or classes following Python’s **PEP 257**.
- Follow **PEP 8** for style (e.g., use `black` to auto-format your code).

### **Step 4: Test Your Changes**
Run the test suite to ensure your changes do not break existing functionality:
```bash
pytest
```
If you introduce new features, include relevant tests under the `tests/` folder.

### **Step 5: Commit Your Changes**
1. Stage your modified files:
   ```bash
   git add .
   ```
2. Commit your changes with a clear and concise commit message:
   ```bash
   git commit -m "Add [your feature description]"
   ```

### **Step 6: Push Your Branch**
Push your branch to your fork:
```bash
git push origin your-feature-branch
```

### **Step 7: Create a Pull Request**
1. Go to the **original repository** on GitHub.
2. Click on `Pull Requests`, then `New Pull Request`.
3. Ensure your branch is selected as the source, and create the pull request.
4. Provide a clear and descriptive summary of what the PR does.

---

## **Code of Conduct**
By contributing to this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

---

## **Adding New Problems or Datasets**

If you are adding a new optimization problem (e.g., Linear Programming, Integer Programming) or a dataset, please follow these conventions:
1. Problems:
    - Add problem definitions to the appropriate folder under `optibench/problems/`.
    - Ensure problem definitions are well-documented (e.g., mathematical formulation, description, input format).
    - Include small test datasets for the problem in the `datasets/` folder.

2. Dataset Generation:
    - Add new dataset generation scripts to the `optibench/datasets` module.
    - Ensure the script is callable by users through the package (e.g., via `optibench.datasets.new_dataset_function`).
    - Outputs should be serialized in a reusable format like JSON.

3. Tests:
    - Add unit tests to validate that dataset generation scripts produce datasets in the correct format.
    - Include edge cases (minimum inputs, sparsity levels, etc.).

---

## **Writing Documentation**
All major contributions (new features, problems, datasets, etc.) must be documented:
1. Add relevant examples to the **README.md**, if applicable.
2. For Python modules, write docstrings in support of tools like **Sphinx**:
   ```python
   def example_function(arg1: int) -> str:
       """
       Example function to demonstrate docstring style.

       Args:
           arg1 (int): A sample integer argument.

       Returns:
           str: A sample string output.
       """
       return str(arg1)
   ```

3. Include guidance on how the feature interacts with existing functionality.

---

## **Testing Changes**
All contributions must be accompanied by relevant tests in the `tests/` directory:
1. Add unit tests for new functions in `tests/`.
2. Run tests via `pytest` and ensure they all pass:
   ```bash
   pytest
   ```

---

## **Style Guide**
1. Code must follow **PEP 8** (use linters like `flake8` or formatters like `black`).
2. Docstrings must follow **PEP 257** style for consistency.
3. Use **type annotations** to improve code readability and quality.

Here’s an example:
```python
def generate_example_dataset(size: int, seed: int = 42) -> dict:
    """
    Generate an example dataset for testing purposes.

    Args:
        size (int): Size of the dataset to generate.
        seed (int, optional): Random seed. Defaults to 42.

    Returns:
        dict: A dictionary representing the generated dataset.
    """
    pass
```

---

## **Submitting Bug Reports**

If you encounter a bug, we would appreciate a detailed bug report:
1. Open an issue on [GitHub](https://github.com/YourUsername/OptiBench/issues).
2. Include the following:
    - A clear and descriptive title.
    - Steps to reproduce the issue.
    - Expected behavior and actual behavior.
    - Versions of Python and OptiBench.
    - Any relevant error messages or tracebacks.

---

## **Getting Help**
If you need guidance or have questions about contributing, feel free to:
1. Open a discussion on the **GitHub Discussions** tab.
2. Reach out through an issue or pull request.

---

We appreciate your time and contributions to improving **OptiBench**! Your involvement makes this tool better for everyone in the optimization community.