import sys
import os

# Ensure we can import from the same directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from validator import is_valid_path

def check_permission(user_data, resource):
    """
    Checks if a user has permission to access a resource.
    Resource is expected to be a path.
    """
    if not is_valid_path(resource):
        return False
    
    # Simuliere Berechtigungsprüfung
    if user_data.get("role") == "admin":
        return True
    elif user_data.get("role") == "user" and not resource.startswith("/etc"):
        return True
    
    return False
