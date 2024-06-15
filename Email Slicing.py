def email_slicer(email):
    try:
        username, domain = email.split('@')
        return username, domain
    except ValueError:
        return "Invalid email format"

#Example usage
if __name__ == "__main__":
    email = input("Enter your email address:")
    result = email_slicer(email)
    if isinstance(result, tuple):
        username, domain = result
        print(f"Username: {username}")
        print(f"Domain: {domain}")
    else:
        print(result)
