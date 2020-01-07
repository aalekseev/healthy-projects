from bowler import Query


def run(urls, interactive: bool = False) -> Query:
    rename_base_name_to_basename = (
        Query(urls)
        .select_module("router")
        .select_method("register")
        .modify_argument(name="base_name", new_name="basename")
    )
    return rename_base_name_to_basename.diff(interactive=interactive)
