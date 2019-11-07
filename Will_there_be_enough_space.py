def enough(cap, on, wait):
    # Your code here
    if cap - on < wait:
        return wait - (cap - on)
    return 0