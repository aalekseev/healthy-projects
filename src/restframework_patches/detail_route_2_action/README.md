# `detail_route` and `list_route` merged into `action` 

version**: 3.8.0

Deprecated `list_route` & `detail_route`
in favor of `action` decorator with `detail` boolean.

## Before

```python
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import detail_route


class ActsViewSet(GenericViewSet):

    @detail_route(methods=['POST'])
    def add_paper_waybill(self, request, pk=None):
        act = self.get_object()
```

## After

```python
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action


class ActsViewSet(GenericViewSet):

    @action(detail=True, methods=['POST'])
    def add_paper_waybill(self, request, pk=None):
        act = self.get_object()
```

## Usage

```python
import glob
import restframework_patches

files = glob.glob('<source_path>/*/urls.py')
restframework_patches.base_name_depreciation.run(files)
```
