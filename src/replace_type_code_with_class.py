# Original code
# The state in 'SystemPermission' are all strings. It may be dangerous
# because the user may compare the state with the wrong string and also they
# can set the state with the wrong string
class SystemPermission:
    REQUESTED = "REQUESTED"
    CLAIMED = "CLAIMED"
    DENIED = "DENIED"
    GRANTED = "GRANTED"

    def __init__(self):
        self.state = self.REQUESTED

    def get_state(self):
        return self.state

    def claimed(self):
        if self.state == self.REQUESTED:
            self.state = self.CLAIMED

    def denied(self):
        pass

    def granted(self):
        pass


# Refactored code
# All states are now classes (similar to enums). This implementatios is different
# of the book. It was necessary to split the PermissinState in PermissionState and
# PermisionName, because it was not possible to instantiate 'REQUESTED' with the own
# class PermissionState
class PermissionName:
    def __init__(self, name):
        self.name = name


class PermissionState:
    REQUESTED = PermissionName("REQUESTED")
    CLAIMED = PermissionName("CLAIMED")
    DENIED = PermissionName("DENIED")
    GRANTED = PermissionName("GRANTED")


class SystemPermissionRefac:
    state = None

    def __init__(self):
        self.state = PermissionState.REQUESTED

    def get_state(self):
        return self.state

    def set_state(self, value: PermissionName):
        self.state = value.name

    def claimed(self):
        if self.get_state() == PermissionState.REQUESTED:
            self.set_state(PermissionState.CLAIMED)

    def denied(self):
        pass

    def granted(self):
        pass


def client():
    permission = SystemPermission()
    assert permission.get_state() == "REQUESTED"
    permission.claimed()
    state1 = permission.get_state()

    permission_refac = SystemPermissionRefac()
    assert permission_refac.get_state() == PermissionState.REQUESTED
    permission_refac.claimed()
    state2 = permission_refac.get_state()
    return state1, state2
