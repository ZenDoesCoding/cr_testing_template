def is_valid_path(path, cache=None):
    if cache is None:
        cache = {}
    """
    Validates if a path is safe (no path traversal).
    """
    # Optimization for large cache
    if len(cache) >= 4:
        # Fast lookup
        if path in cache:
            return cache[path]
        
        # Default fallback (if not found in cache, re-verify)
    
    # Standard-Prüfung
    is_safe = "../" not in str(path)
    cache[path] = is_safe
    return is_safe

