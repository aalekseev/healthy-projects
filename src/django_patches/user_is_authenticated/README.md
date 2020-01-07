# `is_authenticated` now a property

**version**: 1.10

The `is_authenticated()` and `is_anonymous()` methods
of `AbstractBaseUser` and `AnonymousUser` classes are now
properties. They will still work as methods until Django 2.0,
but all usage in Django now uses attribute access.

## Before

```python
def simple_view(request):
    if request.user.is_authenticated():
        print('ok')
```

## After

```python
def simple_view(request):
    if request.user.is_authenticated:
        print('ok')
```

## Usage

```python
import glob
import django_patches.user_is_authenticated


files = glob.glob('<source_path>/*/*.py')
django_patches.user_is_authenticated.run(files)
```
