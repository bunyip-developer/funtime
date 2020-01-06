"""
Make use of built-in exception classes when it makes sense. For example, raise a ValueError to indicate a
programming mistake like a violated precondition (such as if you were passed a negative number but required a
positive one). Do not use assert statements for validating argument values of a public API. assert is used to ensure
internal correctness, not to enforce correct usage nor to indicate that some unexpected event occurred. If an
exception is desired in the latter cases, use a raise statement.
"""


def connect_to_next_port(self, minimum):
    """
    Connects to the next available port.

    :param minimum: A port value greater or equal to 1024
    :return: The new minimum port
    """
    if minimum < 1024:
        # Note that this raising of a ValueError is not mentioned in the doc string's "Raises:" section because it is
        # not appropriate to guarantee this specific behavioural reaction to API misuse.
        raise ValueError('Minimum port must be at least 1024, not %d.' % (minimum,))
    port = self._find_next_open_port(minimum)
    if not port:
        raise ConnectionError('Could not connect to service on %d or higher.' % (minimum,))

    # Correct usage of assert.
    assert port >= minimum, 'Unexpected port %d when minimum was %d.' % (port, minimum)
    return port
