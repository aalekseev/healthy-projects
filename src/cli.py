import argparse
import sys
import glob

import django_patches
import restframework_patches


def main() -> int:
    """Entry point."""

    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="Path to source files")
    parser.add_argument(
        "--interactive",
        dest="interactive",
        action="store_true",
        default=False,
        help="Apply changes interactively",
    )

    source: str = parser.parse_args().source
    interactive: bool = parser.parse_args().interactive

    files = glob.glob(f"{source}/*/*.py")
    models = glob.glob(f"{source}/*/models.py")
    urls = glob.glob(f"{source}/*/urls.py")

    django_patches.url_2_path.patch.run(urls, interactive=interactive)
    django_patches.on_delete.patch.run(models, interactive=interactive)
    django_patches.user_is_authenticated.patch.run(files, interactive=interactive)

    restframework_patches.base_name_depreciation.patch.run(
        urls, interactive=interactive
    )
    restframework_patches.detail_route_2_action.patch.run(
        files, interactive=interactive
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
