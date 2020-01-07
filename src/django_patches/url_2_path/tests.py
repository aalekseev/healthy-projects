import pytest
from .patch import update_regex_to_path


@pytest.mark.parametrize(
    "line, expected",
    (
        [
            (r"", ""),
            (r"^", ""),
            (r"^create/$", "create/"),
            (r"^(?P<pk>\d+)/update/$", "<int:pk>/update/"),
            (r"^ws/entry-operation/(?P<id>[0-9]+)/$", "ws/entry-operation/<int:id>/"),
            (
                r"^cars/(?P<car_pk>\d+)/refuel/create/$",
                "cars/<int:car_pk>/refuel/create/",
            ),
            (
                r"sign-documents/(?P<hash>[^/]+)/(?P<type>[^/]+)/$",
                r"sign-documents/(?P<hash>[^/]+)/(?P<type>[^/]+)/$",
            ),
        ]
    ),
)
def test_update_regex_to_path(line, expected):
    assert update_regex_to_path(line) == expected
