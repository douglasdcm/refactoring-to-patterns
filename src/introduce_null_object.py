# Original code
# When there are many "null" or "None" checks in a code it seems to be reasonable
# to introduc NullObjects to reomve the code duplication
# Often the NullObject inherits from superclasses or implements interfaces
class MouseEventHandler:
    def mouse_move(self):
        pass

    def mouse_down(self):
        pass

    def mouse_up(self):
        pass

    def mouse_exit(self):
        pass


class Applet:
    pass


class NavigationApplet(Applet):
    mouse_event_handler: MouseEventHandler = None

    def move_mouse(self):
        # One of the logics to check Null objects
        if NavigationApplet.mouse_event_handler != None:
            return NavigationApplet.mouse_event_handler.mouse_move()
        return True

    def move_down(self):
        if NavigationApplet.mouse_event_handler != None:
            return NavigationApplet.mouse_event_handler.mouse_down()
        return True

    def move_up(self):
        if NavigationApplet.mouse_event_handler != None:
            return NavigationApplet.mouse_event_handler.mouse_up()
        return True

    def move_exit(self):
        if NavigationApplet.mouse_event_handler != None:
            return NavigationApplet.mouse_event_handler.mouse_exit()
        return True


# Refactored code
# Replace the checks with NullObjects


class MouseEventHandlerRefac:

    def mouse_move(self):
        raise NotImplementedError

    def mouse_down(self):
        raise NotImplementedError

    def mouse_up(self):
        raise NotImplementedError

    def mouse_exit(self):
        raise NotImplementedError


class NullMouseEventHandlerRefac(MouseEventHandlerRefac):
    def __init__(self):
        super().__init__()

    def mouse_move(self):
        return True

    def mouse_down(self):
        return True

    def mouse_up(self):
        return True

    def mouse_exit(self):
        return True


class AppletRefac:
    pass


class NavigationAppletRefac(AppletRefac):
    # Initialize the variable with a NullObject
    def __init__(self):
        super().__init__()
        self._mouse_event_handler: MouseEventHandlerRefac = NullMouseEventHandlerRefac()

    def move_mouse(self):
        # Removed the null checks
        return self._mouse_event_handler.mouse_move()

    def move_down(self):
        return self._mouse_event_handler.mouse_down()

    def move_up(self):
        return self._mouse_event_handler.mouse_up()

    def move_exit(self):
        return self._mouse_event_handler.mouse_exit()


def run_refac():
    n1 = NavigationApplet()
    n2 = NavigationAppletRefac()
    n3 = NavigationAppletRefac()
    n3._mouse_event_handler = MouseEventHandlerRefac()
    return n1, n2, n3
