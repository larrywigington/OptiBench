import numpy as np
import json
from scipy.sparse import random as sparse_random


def generate_transportation_dataset(
        num_suppliers: int,
        num_consumers: int,
        total_supply_demand: int = 1000000,
        sparsity: float = 0.1,
        seed: int = 42,
        output_file: str = None
):
    """
    Generate a large-scale transportation problem dataset.

    Args:
        num_suppliers (int): Number of suppliers.
        num_consumers (int): Number of consumers.
        total_supply_demand (int): Total supply and demand (balanced problem).
        sparsity (float): Fraction of entries in the cost matrix that are non-zero (0 to 1).
        seed (int): Random seed for reproducibility.
        output_file (str): Path to save the dataset in JSON format.
                          If None, the dataset is returned as a Python dictionary.

    Returns:
        dict: If output_file is None, returns the dataset as a dictionary.
    """
    # Set random seed for reproducibility
    np.random.seed(seed)

    # Generate supply vector (randomly distributed)
    supply = np.random.randint(1, total_supply_demand // num_suppliers, size=num_suppliers)
    supply = (supply / supply.sum()) * (total_supply_demand // 2)
    supply = np.round(supply).astype(int)

    # Generate demand vector (randomly distributed)
    demand = np.random.randint(1, total_supply_demand // num_consumers, size=num_consumers)
    demand = (demand / demand.sum()) * (total_supply_demand // 2)
    demand = np.round(demand).astype(int)

    # Ensure total supply equals total demand
    supply[-1] += total_supply_demand // 2 - supply.sum()
    demand[-1] += total_supply_demand // 2 - demand.sum()

    assert supply.sum() == demand.sum(), "Supply and Demand do not match after adjustments!"

    # Generate a sparse cost matrix (sparse random values between 1 and 100)
    rows, cols = num_suppliers, num_consumers
    density = sparsity  # Non-zero fraction of the matrix
    random_costs = sparse_random(rows, cols, density=density, format='csr', random_state=seed,
                                 data_rvs=lambda n: np.random.randint(1, 101, size=n))

    # Serialize the cost matrix for JSON
    cost_matrix = {
        'shape': random_costs.shape,
        'data': list(random_costs.data),
        'indices': list(random_costs.indices),
        'indptr': list(random_costs.indptr)
    }

    # Prepare the dataset object
    dataset = {
        "problem_id": "lp_transportation",
        "description": "Scalable Transportation Problem for GPU and Distributed Optimization",
        "supply": supply.tolist(),
        "demand": demand.tolist(),
        "cost_matrix": cost_matrix,
        "parameters": {
            "num_suppliers": num_suppliers,
            "num_consumers": num_consumers,
            "total_supply_demand": total_supply_demand,
            "sparsity": sparsity,
            "seed": seed
        }
    }

    # Save to file (if output_file is provided)
    if output_file:
        with open(output_file, 'w') as f:
            json.dump(dataset, f, indent=4)
        print(f"Dataset saved to {output_file}")
        return None

    # Otherwise, return the dictionary
    return dataset
