import argparse
from optibench.datasets import generate_transportation_dataset


def main():
    parser = argparse.ArgumentParser(description="OptiBench CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    # Subcommand: generate-dataset
    parser_generate = subparsers.add_parser("generate-dataset", help="Generate a transportation problem dataset")
    parser_generate.add_argument("--num-suppliers", type=int, required=True, help="Number of suppliers.")
    parser_generate.add_argument("--num-consumers", type=int, required=True, help="Number of consumers.")
    parser_generate.add_argument("--total-supply-demand", type=int, default=1000000,
                                 help="Total supply and demand (balanced).")
    parser_generate.add_argument("--sparsity", type=float, default=0.1, help="Sparsity of the cost matrix (0 to 1).")
    parser_generate.add_argument("--seed", type=int, default=42, help="Random seed.")
    parser_generate.add_argument("--output-file", type=str, required=True, help="Output file for the dataset.")

    args = parser.parse_args()

    if args.command == "generate-dataset":
        generate_transportation_dataset(
            num_suppliers=args.num_suppliers,
            num_consumers=args.num_consumers,
            total_supply_demand=args.total_supply_demand,
            sparsity=args.sparsity,
            seed=args.seed,
            output_file=args.output_file
        )
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
