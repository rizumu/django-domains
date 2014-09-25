# coding: utf-8

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from django.conf import settings
from domains.utils import get_hooks, set_hook, apply_hook


for hook in get_hooks():
    set_hook(hook)
