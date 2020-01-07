from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from .api import SimpleAPI
from .views import simple_view


router = SimpleRouter()
router.register(r"dealteam-member", SimpleAPI, base_name="dealteam-member")

urlpatterns = [
    url(r"^$", simple_view, name="home"),
    url(r"^dealroom/$", simple_view, name="dealroom"),
    url(r"^holding-company/?$", simple_view, name="holding_company_list"),
    url(r"^d/(?P<shortlink>[\w-]{11})/?$", simple_view, name="spe_shortlink_redirect"),
    url(r"^(?P<pk>\d+)/update/$", simple_view, name="action_update"),
    url(r"^cars/(?P<car_pk>\d+)/refuel/create/$", simple_view, name="refuel_create"),
] + router.urls
