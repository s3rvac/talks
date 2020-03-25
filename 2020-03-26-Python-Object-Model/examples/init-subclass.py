# An example of using __init_subclass__. Useful for e.g. pluing systems.
# Available since Python 3.6.

class Plugin:
    registered_plugins = []

    def __init_subclass__(cls):
        Plugin.registered_plugins.append(cls)

class Plugin1(Plugin): ...
class Plugin2(Plugin): ...

print(Plugin.registered_plugins) # [<class '__main__.Plugin1'>, <class '__main__.Plugin2'>]
