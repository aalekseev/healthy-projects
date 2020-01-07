from bowler import Query
from fissix.pytree import Node
from fissix.fixer_util import KeywordArg, Name, Comma


def on_delete_modifier(node, capture, filename) -> None:
    if not capture:
        return
    args: Node = capture.get("function_arguments")[0]
    has_on_delete = False
    for node in args.children:
        if isinstance(node, Node) and node.type == 261:
            if node.children[0].value == "on_delete":
                has_on_delete = True
    if not has_on_delete:
        if args.children[-1].value != ",":
            args.append_child(Comma())
        args.append_child(
            KeywordArg(Name("on_delete", prefix=" "), Name("models.CASCADE"))
        )


def run(models, interactive: bool = False) -> Query:
    query = (
        Query(models)
        .select_method("ForeignKey")
        .modify(on_delete_modifier)
        .select_method("OneToOneField")
        .modify(on_delete_modifier)
    )
    return query.diff(interactive=interactive)
