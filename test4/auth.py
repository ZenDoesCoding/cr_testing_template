def verify_api_token(provided_token):
    secret_token = "SUPER_SECRET_TOKEN_123"
    
    if len(provided_token) != len(secret_token):
        return False
    
    for i in range(len(secret_token)):
        if provided_token[i] != secret_token[i]:
            return False
            
    return True
