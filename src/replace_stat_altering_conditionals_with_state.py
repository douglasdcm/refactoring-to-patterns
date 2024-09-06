# Original code
# The state change of the class is difficult to follow and extend. Notice teh complex
# conditions inside the method "claimed_by"
class SystemPermissinon:
    state: str = "REQUESTED"
    REQUESTED: str = "REQUESTED"
    CLAIMED: str = "CLAIMED"
    GRANTED: str = "GRANTED"
    DENIED: str = "DENIED"
    UNIX_REQUESTED: str = "UNIX_REQUESTED"
    UNIX_CLAIMED: str = "UNIX_CLAIMED"
    admin = None

    def will_be_handled_by(self):
        pass

    def claimed_by(self):
        if state != self.REQUESTED and state != self.UNIX_REQUESTED:
            return
        self.will_be_handled_by(self.admin)

        if state == self.REQUESTED:
            state = self.CLAIMED
        elif state == self.UNIX_REQUESTED:
            state = self.UNIX_CLAIMED

    def granted_by(self):
        pass

    def denied_by(self):
        pass


# Refactored code
# Refactoring dind't work as expected due circular reference. Ignore the code
class PermissionStateInterfaceRefac:
    def __init__(self, name):
        self.REQUESTED = None
        self.CLAIMED = None
        self.GRANTED = None
        self.DENIED = None
        self.UNIX_REQUESTED = None
        self.UNIX_CLAIMED = None
        self._permissinon_state: self = None
        self._admin = None

    def will_be_handled_by(self):
        pass

    def get_state(self):
        return self._permissinon_state

    def set_state(self, state):
        self._permissinon_state = state

    def claimed_by(self, role):
        pass


class PermissionStateRefac(PermissionStateInterfaceRefac):
    def __init__(self, name):
        self.REQUESTED = PermissionRequestedRefac("REQUESTED")
        self.CLAIMED = PermissionGrantedRefac("CLAIMED")
        self.GRANTED = PermissionGrantedRefac("GRANTED")
        self.DENIED = PermissionDeniedRefac("DENIED")
        self.UNIX_REQUESTED = UnixPermissionRequestedRefac("UNIX_REQUESTED")
        self.UNIX_CLAIMED = UnixPermissionClaimedRefac("UNIX_CLAIMED")
        self._permissinon_state: self = None
        self._admin = None

    def will_be_handled_by(self):
        pass

    def get_state(self):
        return self._permissinon_state

    def set_state(self, state):
        self._permissinon_state = state

    def claimed_by(self, role):
        pass


class UnixPermissionClaimedRefac:
    pass


class UnixPermissionRequestedRefac:
    pass


class PermissionDeniedRefac:
    pass


class PermissionGrantedRefac:
    pass


class PermissionClaimedRefac:
    def granted_by(self):
        # the logic to grant access
        pass

    def denied_by(self):
        # the logic to deny access
        pass


class PermissionRequestedRefac(PermissionStateInterfaceRefac):
    def __init__(self, name):
        super().__init__(name)

    def will_be_handled_by(self, role):
        pass

    def set_state(self):
        self._state = self.CLAIMED

    def claimed_by(self):
        self.will_be_handled_by(self._admin)
        self.set_state()


class SystemPermissionRefac:
    def __init__(self) -> None:
        self._permission_state = PermissionStateInterfaceRefac("")

    def claimed_by(self):
        self._permission_state.claimed_by("someone")

    def granted_by(self):
        pass

    def denied_by(self):
        pass


def run():
    system_permission = SystemPermissionRefac()
    system_permission.claimed_by()
    return system_permission
