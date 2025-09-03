def split(string: str, split_char: str):
    ret = []

    if not string:
        return ret
    
    cur = []
    for c in string:
        if c == split_char:
            ret.append("".join(cur))
            cur = []
            continue
        cur.append(c)
    ret.append("".join(cur))

    return ret


def run_tests():
    tests = [
        # Example 1 from the book
        ("split by space", ' ', ["split", "by", "space"]),
        # Example 2 from the book
        ("beekeeper needed", 'e', ["b", "", "k", "", "p", "r n", "", "d", "d"]),
        # Example 3 from the book
        ("/home/./..//Documents/", '/',
            ["", "home", ".", "..", "", "Documents", ""]),
        # Example 4 from the book
        ("", '?', []),
        # Edge case - empty string with various delimiters
        ("", ' ', []),
        ("", '\n', []),
        ("", '', []),
        # Edge case - single character string
        ("a", 'a', ["", ""]),
        ("a", 'b', ["a"]),
        # Edge case - no splits
        ("hello", 'x', ["hello"]),
        ("hello", '?', ["hello"]),
        # Edge case - all splits
        ("aaa", 'a', ["", "", "", ""]),
        # Edge case - special characters
        ("\n\n\n", '\n', ["", "", "", ""]),
        ("tab\tseparated\ttext", '\t', ["tab", "separated", "text"]),
        # Edge case - consecutive delimiters
        ("one,,two,,,three", ',', ["one", "", "two", "", "", "three"]),
        # Edge case - delimiter at start/end
        (",start,middle,end,", ',', ["", "start", "middle", "end", ""]),
        # Edge case - mixed length strings
        ("short,medium string,very very long string", ',', [
            "short", "medium string", "very very long string"]),
        # Edge case - whitespace handling
        ("  leading space", ' ', ["", "", "leading", "space"]),
        ("trailing space  ", ' ', ["trailing", "space", "", ""]),
        # Edge case - numbers and special chars
        ("123,456,789", ',', ["123", "456", "789"]),
        ("!@#$%", '@', ["!", "#$%"]),
    ]
    for s, c, want in tests:
        got = split(s, c) 
        assert got == want, f"\nsplit({s}, {c}): got: {got}, want: {want}\n"

if __name__ == "__main__":
    run_tests()