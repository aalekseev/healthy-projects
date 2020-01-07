# Depreciation `base_name`

version**: 3.9.0

Deprecate the `Router.register` `base_name` argument
in favor of `basename`

## Before

```python
from rest_framework.routers import SimpleRouter
from .api import SimpleAPI


router = SimpleRouter()
router.register(r"dealteam-member", SimpleAPI, base_name="dealteam-member")
```

## After

```python
from rest_framework.routers import SimpleRouter
from .api import SimpleAPI


router = SimpleRouter()
router.register(r"dealteam-member", SimpleAPI, basename="dealteam-member")
```

## Usage

```python
import glob
import restframework_patches

files = glob.glob('<source_path>/*/urls.py')
restframework_patches.base_name_depreciation.run(files)
```
