from __future__ import unicode_literals

import warnings


warnings.warn(
    ('django.contrib.contenttypes.generic is deprecated and will be removed in '
     'Django 1.9. Its contents have been moved to the fields, forms, and admin '
     'submodules of django.contrib.contenttypes.'), PendingDeprecationWarning, stacklevel=2
)

from django.contrib.contenttypes.admin import (  # NOQA
    GenericInlineModelAdmin, GenericStackedInline, GenericTabularInline
)
from django.contrib.contenttypes.fields import (  # NOQA
    GenericForeignKey, GenericRelation
)
from django.contrib.contenttypes.forms import (  # NOQA
    BaseGenericInlineFormSet, generic_inlineformset_factory
)
