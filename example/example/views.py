from django.http import Http404, HttpResponseForbidden, JsonResponse


def simple_view(request):
    if request.user.is_authenticated():
        return JsonResponse({"errors": []})
    elif request.user.is_anonymous():
        return HttpResponseForbidden
    return Http404
