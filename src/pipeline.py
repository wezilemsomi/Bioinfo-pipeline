# Quality Control Step
def qc_check(reads):
    print("Running quality control...")

    if len(reads) == 0:
        print("No reads found")
        return False

    avg_length = sum(len(r) for r in reads) / len(reads)
    print(f"Average read length: {avg_length}")

    if avg_length < 50:
        print("Warning: Low quality reads")
    else:
        print("QC passed")

    return True

# Variant Calling Step (separated properly)
def run_variant_analysis(reads):
    print("Running variant analysis...")

    if len(reads) == 0:
        print("No variants detected")
        return False

    print("Variant module processing reads")
    return True

def main():
    # Example reads 
    reads = ["ATCG", "ATCGGA", "ATC"]

    # Step 1
    qc_passed = qc_check(reads)

    # Step 2:
    if qc_passed:
        run_variant_analysis(reads)

if __name__ == "__main__":
    main()