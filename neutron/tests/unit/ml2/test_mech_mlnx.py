# Copyright (c) 2013 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from neutron.common import constants
from neutron.extensions import portbindings
from neutron.plugins.ml2.drivers.mlnx import mech_mlnx
from neutron.tests.unit.ml2 import _test_mech_agent as base


class MlnxMechanismBaseTestCase(base.AgentMechanismBaseTestCase):
    VIF_TYPE = portbindings.VIF_TYPE_DIRECT
    CAP_PORT_FILTER = True
    AGENT_TYPE = constants.AGENT_TYPE_MLNX

    GOOD_MAPPINGS = {'fake_physical_network': 'fake_bridge'}
    GOOD_CONFIGS = {'interface_mappings': GOOD_MAPPINGS}

    BAD_MAPPINGS = {'wrong_physical_network': 'wrong_bridge'}
    BAD_CONFIGS = {'interface_mappings': BAD_MAPPINGS}

    AGENTS = [{'alive': True,
               'configurations': GOOD_CONFIGS}]
    AGENTS_DEAD = [{'alive': False,
                    'configurations': GOOD_CONFIGS}]
    AGENTS_BAD = [{'alive': False,
                   'configurations': GOOD_CONFIGS},
                  {'alive': True,
                   'configurations': BAD_CONFIGS}]

    def setUp(self):
        super(MlnxMechanismBaseTestCase, self).setUp()
        self.driver = mech_mlnx.MlnxMechanismDriver()
        self.driver.initialize()


class MlnxMechanismGenericTestCase(MlnxMechanismBaseTestCase,
                                   base.AgentMechanismGenericTestCase):
    pass


class MlnxMechanismLocalTestCase(MlnxMechanismBaseTestCase,
                                 base.AgentMechanismLocalTestCase):
    pass


class MlnxMechanismFlatTestCase(MlnxMechanismBaseTestCase,
                                base.AgentMechanismFlatTestCase):
    pass


class MlnxMechanismVlanTestCase(MlnxMechanismBaseTestCase,
                                base.AgentMechanismVlanTestCase):
    pass
