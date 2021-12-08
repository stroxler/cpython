import unittest
import ast

"""
This module isn't intended to merge, we just want it here for a more
readable verification of operator binding that we can use in a PEP draft.
"""


binding_examples = [
    # Each of these tests provides a more human-readable version of a test
    # from test_ast.py that specifically verifies banding and associativity of
    # callable type syntax by comparing a minimal code snippet to the same
    # code snippet with all possible ambiguities eliminated.
    (
        "(int) -> (str) -> bool",
        "(int) -> ((str) -> bool)",
    ),
    (
        "(int) -> str | bool",
        "(int) -> (str | bool)",
    ),
    (
        "(int) -> async (float) -> str | bool",
        "(int) -> (async (float) -> (str | bool))",
    ),
    (
        "def f() -> (int, str) -> bool: pass",
        "def f() -> ((int, str) -> bool): pass",
    ),
    (
        "def f() -> (int) -> (str) -> bool: pass",
        "def f() -> ((int) -> ((str) -> bool)): pass",
    ),
    (
        "def f() -> async (int, str) -> bool: pass",
        "def f() -> (async (int, str) -> bool): pass",
    ),
    (
        "def f() -> async (int) -> async (str) -> bool: pass",
        "def f() -> (async (int) -> (async (str) -> bool)): pass",
    ),
]


class CallableTypeOperatorBindingTests(unittest.TestCase):

    def test_binding_examples(self):
        for implicit_binding, explicit_binding in binding_examples:
            self.assertEqual(
                ast.dump(ast.parse(implicit_binding)),
                ast.dump(ast.parse(explicit_binding)),
            )


if __name__ == "__main__":
    unittest.main()



