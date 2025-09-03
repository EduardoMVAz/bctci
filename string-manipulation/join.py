def join(strings, join_char):
    ret = []
    for i in range(len(strings)):
        for c in strings[i]:
            ret.append(c)
        
        if i < len(strings) - 1:
            ret.append(join_char)

    return "".join(ret)


def run_tests():
    tests = [
        # Example 1 from the book
        (["join", "by", "space"], " ", "join by space"),
        # Example 2 from the book
        (["b", "", "k", "", "p", "r n", "", "d", "d!!"],
            "ee", "beeeekeeeepeer neeeedeed!!"),
        # Edge case - empty arrays
        ([], "x", ""),
        ([], "", ""),
        ([], "long separator", ""),
        # Edge case - single element arrays
        (["a"], "x", "a"),
        ([""], "x", ""),
        (["multiple words"], "x", "multiple words"),
        # two element arrays
        (["a", "b"], "", "ab"),
        (["a", "b"], " ", "a b"),
        (["", ""], ",", ","),
        # Edge case - empty strings in array
        (["", "", ""], ",", ",,"),
        (["hello", "", "world"], " ", "hello  world"),
        # special characters
        (["\n", "\t"], ",", "\n,\t"),
        (["tab", "separated"], "\t", "tab\tseparated"),
        # long separators
        (["short", "strings"], "very long separator",
        "shortvery long separatorstrings"),
        # mixed content
        (["123", "abc", "!@#", "   "], "|", "123|abc|!@#|   "),
        # whitespace handling
        (["  leading", "trailing  ", "  both  "],
            "|", "  leading|trailing  |  both  "),
        # numbers and special chars
        (["123", "456"], "-", "123-456"),
        (["!@#", "$%^"], "&", "!@#&$%^"),
    ]
    for arr, s, want in tests:
        got = join(arr, s)
        assert got == want, f"\njoin({arr}, {s}): got: {got}, want: {want}\n"

if __name__ == "__main__":
    run_tests()