# -*- encoding: utf-8 -*-
# Copyright (c) 2016 b<>com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from __future__ import unicode_literals

from oslo_log import log

from watcher.applier.actions.loading import default

LOG = log.getLogger(__name__)


class ActionFactory(object):
    def __init__(self):
        self.action_loader = default.DefaultActionLoader()

    def make_action(self, object_action):
        LOG.debug("Creating instance of %s", object_action.action_type)
        loaded_action = self.action_loader.load(name=object_action.action_type)
        loaded_action.input_parameters = object_action.input_parameters
        loaded_action.applies_to = object_action.applies_to
        return loaded_action