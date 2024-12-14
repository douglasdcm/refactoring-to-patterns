# Original code
# This rectoring is usefull when multiple instances of the class are created
# decreasing the performance of the code. It the example of the book the implementation
# used State patten. Each state was instanciated many times causing ter performance
# issue


class Permission:
    def state(self):
        pass


class PermissionRequested(Permission):
    NAME = "REQUESTED"

    def claimed_by(self, permission):
        permission.set_state(PermissionClaimed())


class PermissionClaimed(Permission):
    pass


class SystemPermission:

    def __init__(self):
        state = PermissionRequested()

    def set_state(permission):
        pass


# Rectored code
# The code was refctored to instanciate the Stated just once


class PermissionRefac:
    def state(self):
        pass


class SystemPermissionRefac:

    def __init__(self):
        state = PermissionRequestedRefac().state()

    def set_state(permission):
        pass


class PermissionClaimedRefac(Permission):
    pass


class PermissionRequestedRefac(PermissionRefac):
    NAME = "REQUESTED"
    local_state = None

    @staticmethod
    def state():
        # Singleton instance
        if not PermissionRequestedRefac.local_state:
            PermissionRequestedRefac.local_state = PermissionRequestedRefac()
        return PermissionRequestedRefac.local_state

    def claimed_by(self, permission: SystemPermissionRefac):
        permission.set_state(PermissionClaimedRefac())


def run_refactored():
    assert PermissionRequested() != PermissionRequested()
    # Assert the instance returned are always the same
    assert PermissionRequestedRefac().state() == PermissionRequestedRefac().state()
    return True
