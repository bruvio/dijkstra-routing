import os
import pathlib
import sys

import pytest

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils import Graph


@pytest.fixture(scope="module")
def graph():
    graph = Graph(
        [
            ("a", "b", 7),
            ("a", "c", 9),
            ("a", "f", 14),
            ("b", "c", 10),
            ("b", "d", 15),
            ("c", "d", 11),
            ("c", "f", 2),
            ("d", "e", 6),
            ("e", "f", 9),
        ]
    )
    yield graph
