def is_lowercase(s: str):
    return ord(s) >= ord('a') and ord(s) <= ord('z')

def is_uppercase(s: str):
    return ord(s) >= ord('A') and ord(s) <= ord('Z')

def reverse_case_match(s: str):
    p1 = 0
    p2 = len(s)-1
    lowercase = []
    uppercase = []

    for i in range(len(s)):
        if is_lowercase(s[p1]):
            lowercase.append(s[p1])
        
        if is_uppercase(s[p2]):
            uppercase.append(s[p2])
        
        p1 += 1
        p2 -= 1
    
    uppercase = "".join(uppercase)
    lowercase = "".join(lowercase)

    return lowercase == uppercase.lower()

def run_tests():
    tests = [
        # Example 1 from the book
        ("haDrRAHd", True),
        # Example 2 from the book
        ("haHrARDd", False),
        # Additional test cases
        ("", True),
        ("aA", True),
        ("Aa", True),
        ("BbbB", True),
        ("abAB", False),
        ("abBA", True),
        ("helloworldHELLOWORLD", False),
    ]
    for s, want in tests:
        got = reverse_case_match(s)
        assert got == want, f"\nreverse_case_match({s}): got: {got}, want: {want}\n"

if __name__ == "__main__":
    run_tests()