def collatz_step(x):
    """Return the result of a single Collatz step."""
    if x > 0 and x % 1 == 0:
        if x % 2 == 0:
            return x // 2
        else:
            return 3 * x + 1
    else:
        # Raise en exception instead of printing an error
        # More details at https://docs.python.org/3/tutorial/errors.html#exceptions
        raise ValueError(f'{x} is not a positive integer')

def collatz_nb_steps(x):
    """Return the number of Collatz steps required to reach 1 from x."""
    steps = 0
    while x != 1:
        x = collatz_step(x)
        steps += 1
    return steps

# Testing code
print([collatz_nb_steps(v) for v in range(126, 131)])
