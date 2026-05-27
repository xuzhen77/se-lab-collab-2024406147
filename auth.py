def authenticate_user(username: str, password: str) -> bool:
    """模拟用户登录功能"""
    if username == "admin" and password == "123456":
        return True
    return False
