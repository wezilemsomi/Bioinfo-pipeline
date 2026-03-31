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