def can_traverse(matrix):
    # Count steps in each column of the matrix
    steps = [sum(col) for col in zip(*matrix)]
    # Can only start on a 0 or 1 in the first column
    if steps[0] > 1:
        return False
    # Check the difference between subsequent steps is 0 or 1
    for a, b in zip(steps, steps[1::]):
        if abs(a - b) > 1:
            return False
    # All conditions met!
    return True