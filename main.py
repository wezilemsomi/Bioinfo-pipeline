def qc_filter(reads, min_length=50):
    # Filter reads based on minimum length threshold
    return [r for r in reads if len(r) >= min_length]