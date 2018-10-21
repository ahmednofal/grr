
@ /home/naufal/Documents/auc/semesters/fall2018/seniorprj1/grr/grr/server/grr_response_server/flows/cron/data_retention.py

There are statically defined values as args.

@ /home/naufal/Documents/auc/semesters/fall2018/seniorprj1/grr/grr/server/grr_response_server/access_control.py

The access control utility is not implemented, flagged as NotImplementedError

@ /home/naufal/Documents/auc/semesters/fall2018/seniorprj1/grr/grr/server/grr_response_server/access_control.py
```
  def CheckClientAccess(self, token, client_urn):
    """Checks access to the given client.

    Args:
      token: User credentials token.
      client_urn: URN of a client to check.

    Returns:
      True if access is allowed, raises otherwise.
    """
    logging.debug("Checking %s for client %s access.", token, client_urn)
    raise NotImplementedError()
```
