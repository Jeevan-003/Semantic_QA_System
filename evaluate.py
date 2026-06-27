def precision_at_k(relevant_files, retrieved_files):

    relevant_files = set(relevant_files)

    correct = 0

    for file in retrieved_files:

        if file in relevant_files:
            correct += 1

    return correct / len(retrieved_files)