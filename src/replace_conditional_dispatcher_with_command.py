# Original code
# Many conditionals in a method that need to be extended if other workshop handlers
# are necessary. The code can became complex overtime
class CatalogApp:
    def handle_workshops(self, action_name):
        if action_name == "new":
            # create workshop
            return "execute new"
        elif action_name == "all":
            # display workshops
            return "execute all"
        # many other elifs
        else:
            # other codes
            return "execute else"


def client():
    catalog = CatalogApp()
    return catalog.handle_workshops("new")


# Refactored code
# The Handler interface has a method "execute" which has to be implemented by its
# child classes. Each subclass implements the correct handler for each situation.
# These handlers are registred in a map (dict) and accessed by the client method using
# the keys which is the action_name. If new handlers are necessary, then new subclasses are
# created and registred in the map
class HandlerRefac:
    def execute(self):
        raise NotImplementedError


class NewWorkshopHandlerRefac(HandlerRefac):
    def execute(self):
        return "execute new"


class AllWorkshopHandlerRefac(HandlerRefac):
    def execute(self):
        return "execute all"


# Other classes for other elifs...
class ElseWorkshopHandler(HandlerRefac):
    def execute(self):
        return "execute else"


class CatalogAppRefac:
    # maps all handlers
    handlers: dict[HandlerRefac] = {
        "new": NewWorkshopHandlerRefac(),
        "all": AllWorkshopHandlerRefac(),
        "else": ElseWorkshopHandler(),
    }

    def lookup_handler_by(self, action_name):
        # executes the correct handler by name
        return self.handlers[action_name].execute()


def client_refac():
    catalog = CatalogAppRefac()
    return catalog.lookup_handler_by(action_name="new")
