# Problem 1: Scalable Transportation Problem (GPU and Distributed)

## Problem Description
The **Transportation Problem** involves determining the most cost-effective way to transport goods from suppliers to consumers, subject to supply and demand constraints. This problem has many applications in logistics, supply chain management, and network design. 

For benchmarking **GPU** and **distributed optimization algorithms**, we scale the problem to large sizes (thousands of suppliers and consumers) and introduce randomization in the cost matrix to mimic real-world complexity.

### Objective:
Minimize the total transportation cost while satisfying all supply and demand constraints.

## Problem Definition
Given:
- A set of **suppliers**, each with a certain supply of goods.
- A set of **consumers**, each with a certain demand for goods.
- A **cost matrix** representing the cost of transporting goods from each supplier to each consumer.

The task is to determine the optimal transportation plan that minimizes the total cost while satisfying all supply and demand constraints.

### Mathematical Formulation:

Let:
- \( x_{ij} \) be the amount of goods transported from supplier \( i \) to consumer \( j \),
- \( c_{ij} \) be the cost per unit of transporting goods from supplier \( i \) to consumer \( j \),
- \( s_i \) be the supply at supplier \( i \),
- \( d_j \) be the demand at consumer \( j \).

The objective function is:
\[
\min \sum_{i} \sum_{j} c_{ij} x_{ij}
\]

Subject to the constraints:
- Supply constraints: \( \sum_{j} x_{ij} = s_i \), for all \( i \),
- Demand constraints: \( \sum_{i} x_{ij} = d_j \), for all \( j \),
- Non-negativity: \( x_{ij} \geq 0 \), for all \( i, j \).

## Large-Scale Data Generation:

For benchmarking **GPU** or **distributed optimizers**, we generate large datasets by increasing the number of suppliers and consumers. Here's how you can scale the problem:

1. **Problem Size**:
   - Number of suppliers \( n \) (e.g., 1000, 5000, 10000).
   - Number of consumers \( m \) (e.g., 1000, 5000, 10000).
   - The total supply equals the total demand: \( \sum s_i = \sum d_j \).

2. **Cost Matrix**:
   - Randomly generate a sparse **cost matrix** \( C \) of size \( n \times m \), where most entries are zero, but a small percentage have random values between 1 and 100. This mimics the situation where some routes have prohibitively high costs (which is common in real-world logistics networks).
   - Alternatively, the matrix can have a block structure where suppliers are clustered geographically, leading to certain consumers being cheaper to supply than others.

3. **Supply and Demand**:
   - **Supply vector \( s \)**: Random values for each supplier, but the total sum must match the total demand.
   - **Demand vector \( d \)**: Similarly, generate random demand for each consumer.

### Example:
For a **10,000 suppliers** and **10,000 consumers** problem:
- Randomly assign values to the cost matrix.
- Ensure that the supply and demand vectors sum to the same value (e.g., \( \sum s = \sum d = 1,000,000 \)).

#### Example of a Scaled Cost Matrix (Subsection of a larger matrix):

| Supplier / Consumer | Consumer 1 | Consumer 2 | Consumer 3 | ... |
|---------------------|------------|------------|------------|-----|
| **Supplier 1**       | 0          | 6          | 0          | ... |
| **Supplier 2**       | 5          | 0          | 3          | ... |
| **Supplier 3**       | 0          | 2          | 4          | ... |
| ...                 | ...        | ...        | ...        | ... |

### Input:

- **Supply vector** \( s = [s_1, s_2, \dots, s_n] \), where \( n \) is large (e.g., 10,000).
- **Demand vector** \( d = [d_1, d_2, \dots, d_m] \), where \( m \) is large (e.g., 10,000).
- **Cost matrix** \( C \), a sparse \( n \times m \) matrix, generated randomly with non-zero values at a small fraction of positions.

### Output:
- **Optimal transportation plan**: A matrix \( x \), where \( x_{ij} \) represents the amount of goods transported from supplier \( i \) to consumer \( j \).
- **Total transportation cost**: The sum of the transportation costs as defined by the objective function.

### Baseline Algorithms:
- **Simplex Method**: Use the GPU-accelerated Simplex method or its distributed variant.
- **Interior-Point Methods**: Adapt these methods for large-scale optimization on GPUs.
- **Heuristic Algorithms**: Use approximation methods like **Greedy**, **Column Generation**, or **Simulated Annealing** for very large instances.

## Evaluation Metrics:
- **Solution quality**: The total cost of the transportation plan, compared to a known optimal or baseline solution.
- **Runtime performance**: Time taken to solve the problem on a single GPU or distributed system.
- **Scalability**: How well the algorithm performs as the number of suppliers and consumers increases.

### Notes:
- For large-scale instances, ensure that the problem is sparse enough to allow for efficient parallel computation on GPUs.
- The problem should be balanced: \( \sum s_i = \sum d_j \). If not, add a dummy supplier or consumer with zero cost connections.

## Example Scaling:

For GPU and distributed testing, scale the problem size as follows:
- **Problem Size 1**: 1,000 suppliers, 1,000 consumers.
- **Problem Size 2**: 5,000 suppliers, 5,000 consumers.
- **Problem Size 3**: 10,000 suppliers, 10,000 consumers.

You can easily scale this problem using scripts to generate synthetic instances.

## References:
- [Transportation Problem on Wikipedia](https://en.wikipedia.org/wiki/Transportation_problem)
- Dantzig, G. B. (1951). "Application of the Simplex Method to the Transportation Problem." *Operations Research*.
