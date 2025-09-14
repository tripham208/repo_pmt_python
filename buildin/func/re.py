"""
Python's `re` (regular expressions) standard library provides powerful pattern matching
and text processing capabilities. This module demonstrates the most useful functions
and concepts with small, runnable examples so you can see what each one does.

Core concepts covered below:
- Raw strings for regex patterns (r"...")
- Literals and character classes
- Quantifiers and anchors
- Groups (positional and named), alternation
- Common functions: match, search, findall, finditer, split, sub, fullmatch, compile
- Flags (re.IGNORECASE, re.MULTILINE, re.DOTALL, etc.)

Run this file directly to see example outputs.
"""
from __future__ import annotations

import re
from typing import List, Tuple


def demo_match_vs_search() -> Tuple[str, str]:
    # match: only checks from the beginning of the string
    m1 = re.match(r"cat", "caterpillar")
    # search: finds first occurrence anywhere in the string
    s1 = re.search(r"pill", "caterpillar")
    return m1.group(0) if m1 else "<no match>", s1.group(0) if s1 else "<no match>"


def demo_findall_and_groups() -> Tuple[List[str], List[Tuple[str, str]]]:
    text = "Name: Alice, Age: 30; Name: Bob, Age: 25"
    # findall with a single group returns the group content list
    names = re.findall(r"Name:\s*(\w+)", text)
    # multiple groups -> list of tuples
    pairs = re.findall(r"Name:\s*(\w+).*?Age:\s*(\d+)", text)
    return names, pairs


def demo_named_groups() -> List[dict]:
    pattern = re.compile(r"(?P<user>[A-Za-z_][\w_]*)@(?P<domain>[A-Za-z0-9.-]+)")
    emails = [
        "alice@example.com",
        "bob.smith@sub.domain.org",
        "invalid@",  # will not match
    ]
    result = []
    for e in emails:
        m = pattern.search(e)
        if m:
            result.append(m.groupdict())
    return result


def demo_split_and_sub() -> Tuple[List[str], str, str]:
    text = "one,two;three|four  five"
    parts = re.split(r"[\s,;|]+", text)
    # Replace all digits with '#'
    replaced = re.sub(r"\d", "#", "Call me at 123-456-7890")

    # Use a function in sub
    def repl(m: re.Match) -> str:
        return m.group(0).upper()

    highlighted = re.sub(r"\b[a-z]{3}\b", repl, "one two three four five six")
    return parts, replaced, highlighted


def demo_flags_multiline_dotall_ignorecase() -> Tuple[List[str], List[str], str]:
    text = """First line\nsecond LINE\nTHIRD line"""
    # IGNORECASE makes case-insensitive
    matches_icase = re.findall(r"line", text, flags=re.IGNORECASE)
    # MULTILINE: ^ and $ match start/end of each line
    starts = re.findall(r"^\w+", text, flags=re.MULTILINE)
    # DOTALL: . matches newlines too
    s = re.search(r"First(.*)line", text, flags=re.DOTALL)
    return matches_icase, starts, (s.group(1).strip() if s else "<no match>")


def demo_fullmatch_compile() -> Tuple[bool, bool]:
    # fullmatch: entire string must match
    is_hex = re.compile(r"^[0-9a-fA-F]+$")  # you can also use pattern.fullmatch(s)
    ok = bool(is_hex.fullmatch("CafeBabe"))
    bad = bool(is_hex.fullmatch("Cafe-Babe"))
    return ok, bad


def demo_greedy_vs_nongreedy() -> Tuple[str, str]:
    text = "<tag>content</tag><tag>more</tag>"
    greedy = re.findall(r"<tag>.*</tag>", text)  # greedy: matches the longest
    nongreedy = re.findall(r"<tag>.*?</tag>", text)  # non-greedy: shortest
    return ",".join(greedy), ",".join(nongreedy)


def quick_reference() -> str:
    return (
        "Common tokens: \n"
        "  . any char (except newline unless DOTALL)\n"
        "  ^ start, $ end, \n"
        "  \b word boundary, \B non-boundary\n"
        "  [] character class, () group, | alternation\n"
        "  * 0+, + 1+, ? 0/1, {m,n} quantifier\n"
        "  \d digit, \w word, \s whitespace (capitals negate)\n"
        "Use raw strings for patterns: r'\\d+\\.\\w+'.\n"
    )


if __name__ == "__main__":
    print("re library quick reference:\n" + quick_reference())

    print("\nmatch vs search:")
    print(demo_match_vs_search())  # ('cat', 'pill')

    print("\nfindall and groups:")
    print(demo_findall_and_groups())  # (['Alice', 'Bob'], [('Alice', '30'), ('Bob', '25')])

    print("\nnamed groups:")
    print(demo_named_groups())  # [{'user': 'alice', 'domain': 'example.com'}, ...]

    print("\nsplit and sub:")
    print(demo_split_and_sub())

    print("\nflags (IGNORECASE, MULTILINE, DOTALL):")
    print(demo_flags_multiline_dotall_ignorecase())

    print("\nfullmatch and compile:")
    print(demo_fullmatch_compile())  # (True, False)

    print("\ngreedy vs non-greedy:")
    print(demo_greedy_vs_nongreedy())
