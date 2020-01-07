# New path module in Django 2.0

**version**: 2.0

The `django.conf.urls.url()` function from previous versions
is now available as `django.urls.re_path()`. The old location
remains for backwards compatibility, without an imminent
deprecation. The old `django.conf.urls.include()` function
is now importable from `django.urls` so you can use
`from django.urls import include, path, re_path` in your URLconfs.
