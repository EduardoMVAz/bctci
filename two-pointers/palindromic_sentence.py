def palindromic_sentence(s: str):
    p1 = 0
    p2 = len(s) - 1
    while p1 < p2:

        if not s[p1].isalnum():
            p1 += 1
            continue

        if not s[p2].isalnum():
            p2 -= 1
            continue

        if s[p1].lower() != s[p2].lower():
            return False
        
        p1 += 1
        p2 -= 1

    return True

def run_tests():
    tests = [
        # Example from the book
        ("Bob wondered, 'Now, Bob?'", True),
        # Additional test cases
        ("", True),
        ("a", True),
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("Was it a car or a cat I saw?", True),
        ("hello", False),
        (".,?!'", True),
    ]
    for s, want in tests:
        got = palindromic_sentence(s)
        assert got == want, f"\npalindromic_sentence({s}): got: {got}, want: {want}\n"

if __name__ == "__main__":
    run_tests()