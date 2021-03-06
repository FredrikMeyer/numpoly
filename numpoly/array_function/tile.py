"""Construct an array by repeating A the number of times given by reps."""
import numpy
import numpoly

from .common import implements


@implements(numpy.tile)
def tile(A, reps):
    """
    Construct an array by repeating A the number of times given by reps.

    If `reps` has length ``d``, the result will have dimension of
    ``max(d, A.ndim)``.

    If ``A.ndim < d``, `A` is promoted to be d-dimensional by prepending new
    axes. So a shape (3,) array is promoted to (1, 3) for 2-D replication,
    or shape (1, 1, 3) for 3-D replication. If this is not the desired
    behavior, promote `A` to d-dimensions manually before calling this
    function.

    If ``A.ndim > d``, `reps` is promoted to `A`.ndim by pre-pending 1's to it.
    Thus for an `A` of shape (2, 3, 4, 5), a `reps` of (2, 2) is treated as
    (1, 1, 2, 2).

    Args:
        A (numpoly.ndpoly):
            The input array.
        reps (numpy.ndarray):
            The number of repetitions of `A` along each axis.

    Returns:
        (numpoly.ndpoly):
            The tiled output array.

    Examples:
        >>> x = numpoly.symbols("x")
        >>> numpoly.tile(x, 4)
        polynomial([x, x, x, x])
        >>> poly = numpoly.polynomial([[1, x-1], [x**2, x]])
        >>> numpoly.tile(poly, 2)
        polynomial([[1, -1+x, 1, -1+x],
                    [x**2, x, x**2, x]])
        >>> numpoly.tile(poly, [2, 1])
        polynomial([[1, -1+x],
                    [x**2, x],
                    [1, -1+x],
                    [x**2, x]])

    """
    A = numpoly.aspolynomial(A)
    result = numpy.tile(A.values, reps=reps)
    return numpoly.aspolynomial(result, names=A.indeterminants)
