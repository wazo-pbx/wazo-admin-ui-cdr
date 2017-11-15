# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import logging

from wazo_admin_ui.helpers.call_logd import call_logd

logger = logging.getLogger(__name__)


class CdrService(object):

    def list(self, limit=None, order=None, direction=None, offset=None, search=None, **kwargs):
        return call_logd.cdr.list(search=search,
                                  order=order,
                                  limit=limit,
                                  direction=direction,
                                  offset=offset,
                                  **kwargs)
