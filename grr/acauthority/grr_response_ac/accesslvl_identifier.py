class AccessLvlIdentifier:

    """This class will handle checking whether a certain access lvl
    can execute certain flows in the client side"""

    def __init__(self):
        """TODO: to be defined1. """
        pass

    def default_flows(self):
        """This function retrieves the default flows defined in grr-server
        :returns: list of default flows string names

        """
        return []

    def access_lvl_appropriate(self, role):
        """The function checks whether the role available will be sufficient to execute certain
        actions

        :role: keycloak role defined by the client machine
        :returns: a boolean

        """
        return false

