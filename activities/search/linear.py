def search(haystack, needle) -> int:
    """Search for needle in the haystack, if found return the index else -1."""
    n = len(haystack)
    for i in range(n):
        if haystack[i] == needle:
            return i
    return -1
