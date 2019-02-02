class CreateRoleReq:
    """Empty class to denote a certain request type"""
    pass

class ApproveTokenReq:

    """This is an empty class to denote a request issued by a client machine to approve a token sent by a
    server asking it to approve a token sent by analyst to client machine """

    pass


class ModifyClientRolesReq:

    """This is an empty class denoting a request type issued by a client to modify the roles available for
    server users(analysts and admins alike) to assume"""

    pass

class DeleteClientRole():

    """Empty class to denote the request sent by a client to delete a certain role that is available to be
    assumed by server users"""

    pass


class RefreshTokenReq():

    """Empty class to denote the request send by a server user to refresh a token that is about to expire
    so that they can continue functioning properly"""

    pass

