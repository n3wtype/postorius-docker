#!/usr/bin/env python

import os
import sys

from django.contrib.auth.models import User

def env_unset_or_blank(env, value=''):
    e = os.getenv(env, '')
    if e:
        return e
    else:
        return value


password = env_unset_or_blank('POSTORIUS_ADMIN_PASS', 'postoriusadmin')
site_owner = env_unset_or_blank('MAILMAN_SITE_OWNER', 'admin@{}'.format(env_unset_or_blank('HOSTNAME', 'localhost')))

try:
    a = User.objects.get(username='admin')
    a.set_password(password)
    a.email=site_owner
    a.save()
except User.DoesNotExist:
    a = User.objects.create_superuser('admin', site_owner, password)

sys.exit(0)

