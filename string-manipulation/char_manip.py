def is_lowercase(char: str):
    return ord(char) >= ord('a') and ord(char) <= ord('z')

def is_uppercase(char: str):
    return ord(char) >= ord('A') and ord(char) <= ord('Z')

def is_letter(char: str):
    return (
        (ord(char) >= ord('a') and ord(char) <= ord('z'))
        or (ord(char) >= ord('A') and ord(char) <= ord('Z'))
    )

def is_number(char: str):
    return ord(char) >= ord('0') and ord(char) <= ord('9')


def is_alphanumeric(char: str):
    if not char:
        return False
    return is_number(char) or is_letter(char)

def to_uppercase(char: str):
    if not is_lowercase(char):
        return
    return chr(ord(char) - 32)

def run_tests():
    assert is_alphanumeric('a') is True
    assert is_alphanumeric(' ') is False
    assert is_alphanumeric('!') is False
    assert is_alphanumeric('Z') is True
    assert is_alphanumeric('') is False

    abc_lower = 'abcdefghijklmnopqrstuvwxyz'
    abc_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(abc_lower)):
        assert to_uppercase(abc_lower[i]) == abc_upper[i]
        

if __name__ == "__main__":
    run_tests()