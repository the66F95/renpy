# Copyright 2004-2025 Tom Rothamel <pytom@bishoujo.us>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from typing import Any

def hash32(s : Any) -> int:
    """
    Returns a stable 32-bit hash of the string `s`.

    `s`
        A unicode string. Other types will be coerced to unicode before hashing.
    """


def hash64(s : Any) -> int:
    """
    Returns a stable 64-bit hash of the string `s`.

    `s`
        A unicode string. Other types will be coerced to unicode before hashing.
    """

class PyExpr(str):
    """
    Represents a string containing python expression.
    """

    filename: str
    linenumber: int
    py: int
    hashcode: int

    @staticmethod
    def checkpoint() -> Any:
        """
        Checkpoints the pyexpr list. Returns an opaque object that can be used
        with PyExpr.revert to revert the list.
        """

    @staticmethod
    def revert(opaque: Any):
        """
        Reverts the pyexpr list to the state it was in when checkpoint was called.
        """
