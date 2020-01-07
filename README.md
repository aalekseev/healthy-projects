# Healthy Projects

> A proof of concept, to programmatically
> update depreciation warnings of package upgrades

## Supported Upgrades
- [Django](src/django_patches/README.md)
- [Django Rest Framework](src/restframework_patches/README.md)

## Usage

```bash
(venv) $ python src/cli.py example --interactive
```

## Tools

- [bowler](https://pybowler.io/) - A modern approach to
    refactorings, but API is unstable, to be changed in the future

### Alternatives

While researching this topic I found out some interesting
packages:

- [rope](https://github.com/python-rope/rope) - This is
    probably the oldest and most stable refactoring tool
    out there for Python. But the API seems funky
- [undebt](https://github.com/Yelp/undebt) - A tool from
    Yelp, seems abandoned from 2017, but I liked the API,
    a simple one yet powerful

### Honorable members

- [pyupgrade](https://github.com/asottile/pyupgrade) - A
    modern tool to help transition Python from 2 to 3
    automatically
- [slicker](https://github.com/Khan/slicker) - A tool
    developed by Khan Academy, will help with splitting
    huge files into smaller ones and moving stuff around

## Dev Tools

- [Black](https://github.com/psf/black) - Opinionated
    autoformatter
- [Pytest](https://github.com/pytest-dev/pytest) - Best tool
    to write and run tests for Python
