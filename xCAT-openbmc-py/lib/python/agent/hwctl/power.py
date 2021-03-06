#!/usr/bin/env python
###############################################################################
# IBM(c) 2018 EPL license http://www.eclipse.org/legal/epl-v10.html
###############################################################################
# -*- coding: utf-8 -*-
#

class PowerInterface(object):
    """Interface for power-related actions."""
    interface_type = 'power'
    version = '1.0'

    def get_power_state(self, task):
        """Return the power state of the task's nodes.

        :param task: a Task instance containing the nodes to act on.
        :raises: MissingParameterValue if a required parameter is missing.
        :returns: a power state.
        """
        return task.run('get_state')

    def set_power_state(self, task, power_state, timeout=None):
        """Set the power state of the task's nodes.

        :param task: a Task instance containing the nodes to act on.
        :param power_state: Any power state from :mod:`ironic.common.states`.
        :param timeout: timeout (in seconds) positive integer (> 0) for any
          power state. ``None`` indicates to use default timeout.
        :raises: MissingParameterValue if a required parameter is missing.
        """
        return task.run('set_state', power_state, timeout=timeout)

    def reboot(self, task, optype='boot', timeout=None):
        """Perform a hard reboot of the task's nodes.

        Drivers are expected to properly handle case when node is powered off
        by powering it on.

        :param task: a Task instance containing the node to act on.
        :param timeout: timeout (in seconds) positive integer (> 0) for any
          power state. ``None`` indicates to use default timeout.
        """
        return task.run('reboot', optype, timeout=timeout)

    def get_bmc_state(self, task):
        """Return the bmc state of the task's nodes.

        :param task: a Task instance containing the nodes to act on.
        :raises: MissingParameterValue if a required parameter is missing.
        :returns: a power state.
        """
        return task.run('get_bmcstate')

    def reboot_bmc(self, task, optype='warm'):
        """Return the bmc state of the task's nodes.

        :param task: a Task instance containing the nodes to act on.
        :raises: MissingParameterValue if a required parameter is missing.
        :returns: a power state.
        """
        return task.run('reboot_bmc', optype)


class DefaultPowerManager(PowerInterface):
    """Interface for power-related actions."""
    pass
