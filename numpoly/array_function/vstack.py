"""Stack arrays in sequence vertically (row wise)."""
import numpy
import numpoly

from .common import implements


@implements(numpy.vstack)
def vstack(tup):
    """
    Stack arrays in sequence vertically (row wise).

    This is equivalent to concatenation along the first axis after 1-D arrays
    of shape `(N,)` have been reshaped to `(1,N)`. Rebuilds arrays divided by
    `vsplit`.

    This function makes most sense for arrays with up to 3 dimensions. For
    instance, for pixel-data with a height (first axis), width (second axis),
    and r/g/b channels (third axis). The functions `concatenate`, `stack` and
    `block` provide more general stacking and concatenation operations.

    Args:
        tup (Sequence[numpoly.ndpoly]):
            The arrays must have the same shape along all but the first axis.
            1-D arrays must have the same length.

    Returns:
        (numpoly.ndpoly):
            The array formed by stacking the given arrays, will be at least
            2-D.

    Examples:
        >>> a = numpoly.symbols("x y z")
        >>> b = numpoly.polynomial([1, 2, 3])
        >>> numpoly.vstack([a, b])
        polynomial([[x, y, z],
                    [1, 2, 3]])
        >>> c = numpoly.polynomial([[1], [2], [3]])
        >>> d = a.reshape(3, 1)
        >>> numpoly.vstack([c, d])
        polynomial([[1],
                    [2],
                    [3],
                    [x],
                    [y],
                    [z]])

    """
    arrays = numpoly.align_exponents(*tup)
    arrays = numpoly.align_dtype(*arrays)
    result = numpy.vstack([array.values for array in arrays])
    return numpoly.aspolynomial(result, names=arrays[0].indeterminants)
