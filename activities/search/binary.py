def _search(haystack, needle, lo : int, hi : int) -> int:
    """Search for needle in sorted haystack[lo:hi), if found return the index
    else -1."""
    pass

def search(haystack, needle) -> int:
    """Search for needle in sorted haystack, if found return the index else
    -1."""
    n = len(haystack)
    return _search(haystack, needle, 0, n)
