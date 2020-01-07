import re
from bowler import Query

from fissix.pytree import Node, Leaf
from fissix.fixer_util import FromImport, Name, Comma, is_import
from bowler.types import Capture, Filename


def update_regex_to_path(regex: str) -> str:
    match = re.findall(r"\(\?P<(\w+)>([^\)]+)\)", regex)
    if match:
        for name, exp in match:
            converted = ""
            if exp == r"\d+" or exp == "[0-9]+":
                converted = f"<int:{name}>"
            if converted:
                regex = regex.replace(f"(?P<{name}>{exp})", converted)
                regex = re.sub(r"[\^\$]", "", regex)
        return regex
    return re.sub(r"[\^\$]", "", regex)


def convert_regex_to_path_modifier(
    node: Node, capture: Capture, filename: Filename
) -> None:
    # Replace the import
    if is_import(node):
        name_leafs = [
            Name("path", prefix=" "),
            Comma(),
            Name("re_path", prefix=" "),
        ]
        node.replace([FromImport("django.url", name_leafs=name_leafs)])
    # And function calls from url to path, re_path
    if capture and "function_arguments" in capture:
        function_node: Node = next(node.leaves())
        args = capture.get("function_arguments")
        regex_leaf: Leaf = next(args[0].leaves())
        converted = update_regex_to_path(regex_leaf.value)

        if converted == regex_leaf.value:
            function_node.replace(Name("re_path", prefix=function_node.prefix))
        else:
            function_node.replace(Name("path", prefix=function_node.prefix))
            regex_leaf.value = update_regex_to_path(regex_leaf.value)


def run(urls, interactive: bool = False) -> Query:
    convert_to_path = (
        Query(urls).select_function("url").modify(convert_regex_to_path_modifier)
    )
    return convert_to_path.diff(interactive=interactive)
