from typing import Callable, Dict, Any

from bowler import Query
from bowler.types import Capture, Filename
from fissix.pytree import Node


def method_to_property_modifier(
    node: Node, capture: Capture, filename: Filename
) -> None:
    node.children = node.children[:-1]


def run(files, interactive: bool = False) -> Query:
    query = (
        Query(files)
        .select_method("is_authenticated")
        .modify(method_to_property_modifier)
        .select_method("is_anonymous")
        .modify(method_to_property_modifier)
    )
    return query.diff(interactive=interactive)
