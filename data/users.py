test_users = [
    {"user": "standard_user", "password": "secret_sauce", "result": "success"},
    {"user": "standard_user", "password": "wrong_password", "result": "Username and password do not match any user in this service"},
    {"user": "locked_out_user", "password": "secret_sauce", "result": "Sorry, this user has been locked out."},
    {"user": "problem_user", "password": "secret_sauce", "result": "success"},
    {"user": "performance_glitch_user", "password": "secret_sauce", "result": "success"},
    {"user": "error_user", "password": "secret_sauce", "result": "success"},
    {"user": "visual_user", "password": "secret_sauce", "result": "success"}
]