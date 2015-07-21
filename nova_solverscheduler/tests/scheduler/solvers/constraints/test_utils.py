# Copyright (c) 2015 Cisco Systems Inc.
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

from nova import test
from nova_solverscheduler.scheduler.solvers.constraints import utils


class ConstraintUtilsTestCase(test.NoDBTestCase):

    def test_validate_constraint_configured(self):
        self.flags(
                scheduler_solver_constraints='FakeConstraint1,FakeConstraint2',
                group='solver_scheduler')
        self.assertTrue(utils.validate_constraint('FakeConstraint1'))
        self.assertTrue(utils.validate_constraint('FakeConstraint2'))
        self.assertFalse(utils.validate_constraint('FakeConstraint3'))