def qc_filter(reads):
    # Remove reads shorter than 50 bases
    return [r for r in reads if len(r) > 50]