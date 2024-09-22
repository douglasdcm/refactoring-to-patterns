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

    # introduced by me to change the state changes. It is not part of the original code
    def change_state(self, _state):
        self.state = _state

    def will_be_handled_by(self, role):
        pass

    def claimed_by(self):
        if self.state != self.REQUESTED and self.state != self.UNIX_REQUESTED:
            return
        self.will_be_handled_by(self.admin)

        if self.state == self.REQUESTED:
            self.state = self.CLAIMED
        elif self.state == self.UNIX_REQUESTED:
            self.state = self.UNIX_CLAIMED

    def granted_by(self):
        pass

    def denied_by(self):
        pass


def run_original():
    permission = SystemPermissinon()
    permission.claimed_by()
    state1 = permission.state

    permission.change_state("UNIX_REQUESTED")
    permission.claimed_by()
    state2 = permission.state

    return state1, state2


# Refactored code
# The conditionals where simplified in the method "claimed_by". New ConcretStates now implement the methods "request"
# and "unix_request" and change to the next status. This new implementation is based on the one from the book
# "Design Patterns"
class StateRefac:
    state = None
    value = None

    def claimed_by(self, context):
        pass

    def request(self, context):
        pass

    def unix_request(self, contexxt):
        pass

    def change_state(self, context, permission):
        return context.change_state(permission)


class SystemPermissionRequestedRefac(StateRefac):
    value = "REQUESTED"

    def request(self, context):
        self.change_state(context, SystemPermissionClaimedRefac())


class SystemPermissionClaimedRefac(StateRefac):
    value = "CLAIMED"

    def claimed_by(self):
        if not isinstance(
            self.state, SystemPermissionRequestedRefac
        ) and not isinstance(self.state, SystemPermissionUnixRequestedRefac()):
            return
        self.will_be_handled_by(self.admin)

    def will_be_handled_by(self, role):
        pass


class SystemPermissionGrantedRefac(StateRefac):
    pass


class SystemPermissionDeniedRefac(StateRefac):
    pass


class SystemPermissionUnixRequestedRefac(StateRefac):
    value = "UNIX_REQUESTED"

    def claimed_by(self):
        self.state = SystemPermissionUnixClaimedRefac()

    def unix_request(self, context):
        self.change_state(context, SystemPermissionUnixClaimedRefac())


class SystemPermissionUnixClaimedRefac(StateRefac):
    value = "UNIX_CLAIMED"


class SystemPermissinonRefac:
    state = SystemPermissionRequestedRefac()
    admin = None

    # introduced by me to change the state changes. It is not part of the original code
    def change_state(self, _state):
        self.state = _state

    def will_be_handled_by(self, role):
        pass

    def claimed_by(self):
        if not isinstance(
            self.state, SystemPermissionRequestedRefac
        ) and not isinstance(self.state, SystemPermissionUnixRequestedRefac):
            return
        self.will_be_handled_by(self.admin)

    def request(self):
        self.state.request(self)

    def unix_request(self):
        self.state.unix_request(self)

    def granted_by(self):
        pass

    def denied_by(self):
        pass


def run_refac():
    permission = SystemPermissinonRefac()
    permission.request()
    state1 = permission.state.value

    permission.change_state(SystemPermissionUnixRequestedRefac())
    permission.unix_request()
    state2 = permission.state.value

    return state1, state2
