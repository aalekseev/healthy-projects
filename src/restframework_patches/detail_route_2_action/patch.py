from bowler import Query

from typing import List

from fissix.fixer_util import is_import, FromImport, Name, KeywordArg, Comma
from fissix.pytree import Node, Leaf
from bowler.types import Capture, Filename


def import_modifier(node: Node, capture: Capture, filename: Filename) -> None:
    imports: List[Leaf] = capture["module_imports"]
    name_leafs = []
    for module_import in imports:
        if (
            module_import.value in ("detail_route", "list_route")
            or module_import.value == ","
        ):
            continue
        else:
            name_leafs.extend([module_import, Comma()])
    name_leafs.append(Name("action", prefix=" "))
    node.replace([FromImport("rest_framework.decorators", name_leafs=name_leafs)])


DECORATOR_PATTERN = "decorator< '@' name=NAME '(' decorator_arguments=any* ')' any* >"


def is_detail_or_list_filter(node: Node, capture: Capture, filename: Filename) -> bool:
    if node.children[1].value in ("detail_route", "list_route"):
        return True
    return False


def route_modifier(node: Node, capture: Capture, filename: Filename) -> None:
    name_leaf: Leaf = node.children[1]
    if name_leaf.value == "detail_route":
        args: Node = capture["decorator_arguments"][0]
        args.children += [Comma(), KeywordArg(Name("detail", prefix=" "), Name("True"))]

    name_leaf.value = "action"


def run(files, interactive: bool = False) -> Query:
    query = (
        Query(files)
        .select_module("rest_framework.decorators")
        .modify(import_modifier)
        .select(pattern=DECORATOR_PATTERN)
        .filter(is_detail_or_list_filter)
        .modify(route_modifier)
    )
    return query.diff(interactive=interactive)
