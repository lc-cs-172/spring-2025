def _search(haystack, needle, lo : int, hi : int) -> int:
    """Search for needle in sorted haystack[lo:hi), if found return the index
    else -1."""
    if hi <= lo: return -1
    mid = (lo + hi)//2
    if haystack[mid] < needle: return _search(haystack, needle, mid + 1, hi)
    if haystack[mid] > needle: return _search(haystack, needle, lo, mid)
    return mid

def search(haystack, needle) -> int:
    """Search for needle in sorted haystack, if found return the index else
    -1."""
    n = len(haystack)
    return _search(haystack, needle, 0, n)
