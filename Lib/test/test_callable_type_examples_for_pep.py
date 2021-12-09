import ast
import sys
import unittest
import textwrap

"""
This module isn't intended to merge, we just want it here for a more
readable verification of examples that are specifically called out in
our draft PEP.

Run tests with:
./python Lib/test/test_callable_examples_for_pep.py

Print out a snippet to paste into the PEP's rst with:
./python Lib/test/test_callable_examples_for_pep.py --print-examples
"""


edge_case_examples = [
    "Trailing commas are permitted except in empty args lists",
    (
        "(int,) -> bool",
        "(int) -> bool",
    ),
    (
        "(int, **P,) -> bool",
        "(int, **P) -> bool",
    ),
    (
        "(...,) -> bool",
        "(...) -> bool",
    ),
    "``->`` binds less tightly than other operators, both inside types and"
    "in function signatures",
    (
        "(int) -> str | bool",
        "(int) -> (str | bool)",
    ),
    "``->`` associates to the right, both inside types and"
    "in function signatures",
    (
        "(int) -> (str) -> bool",
        "(int) -> ((str) -> bool)",
    ),
    (
        "def f() -> (int, str) -> bool: pass",
        "def f() -> ((int, str) -> bool): pass",
    ),
    (
        "def f() -> (int) -> (str) -> bool: pass",
        "def f() -> ((int) -> ((str) -> bool)): pass",
    ),
    "All of the binding rules still work for async callable types",
    (
        "(int) -> async (float) -> str | bool",
        "(int) -> (async (float) -> (str | bool))",
    ),
    (
        "def f() -> async (int, str) -> bool: pass",
        "def f() -> (async (int, str) -> bool): pass",
    ),
    (
        "def f() -> async (int) -> async (str) -> bool: pass",
        "def f() -> (async (int) -> (async (str) -> bool)): pass",
    ),
    "Splitting lines should work fine",
    (
        textwrap.dedent("""
        (
            (int, bool) -> str,
            list[dict[str, int]],
        ) -> async (int, bool) -> str
        """),
        "((int, bool) -> str, list[dict[str, int]]) -> async (int, bool) -> str",
    )
]


class CallableTypeOperatorBindingTests(unittest.TestCase):

    def test_binding_examples(self):
        for entry in edge_case_examples:
            is_comment = isinstance(entry, str)
            if not is_comment:
                implicit_code, explicit_code = entry
                self.assertEqual(
                    ast.dump(ast.parse(implicit_code)),
                    ast.dump(ast.parse(explicit_code)),
                )

if __name__ == "__main__":
    if sys.argv[1:] == ['--print-examples']:
        print()
        indent = 4 * " "
        for entry in edge_case_examples:
            is_comment = isinstance(entry, str)
            if is_comment:
                print(entry + "::\n")
            else:
                try:
                    implicit_code, explicit_code = entry
                except:
                    import pdb; pdb.set_trace()
                print(indent + implicit_code)
                print(indent + explicit_code)
                print()
    else:
        unittest.main()
