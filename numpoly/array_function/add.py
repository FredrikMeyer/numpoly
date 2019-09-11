"""Add arguments element-wise."""
import numpy
import numpoly

from .implements import implements


@implements(numpy.add)
def add(x1, x2, out=None, where=True, **kwargs):
    """
    Add arguments element-wise.

    Args:
        x1, x2 (numpoly.ndpoly):
            The arrays to be added. If ``x1.shape != x2.shape``, they must be
            broadcastable to a common shape (which becomes the shape of the
            output).
        out (Optional[numpy.ndarray]):
            A location into which the result is stored. If provided, it must
            have a shape that the inputs broadcast to. If not provided or
            `None`, a freshly-allocated array is returned. A tuple (possible
            only as a keyword argument) must have length equal to the number of
            outputs.
        where (Union[bool, numpy.ndarray]):
            This condition is broadcast over the input. At locations where the
            condition is True, the `out` array will be set to the ufunc result.
            Elsewhere, the `out` array will retain its original value. Note
            that if an uninitialized `out` array is created via the default
            ``out=None``, locations within it where the condition is False will
            remain uninitialized.
        **kwargs
            Keyword args passed to numpy.ufunc.

    Returns:
        (numpoly.ndpoly):
            The sum of `x1` and `x2`, element-wise. This is a scalar if both
            `x1` and `x2` are scalars.

    Examples:
        >>> x, y = numpoly.symbols("x y")
        >>> numpoly.add(x, 4)
        polynomial(4+x)
        >>> poly1 = x**numpy.arange(9).reshape((3, 3))
        >>> poly2 = y**numpy.arange(3)
        >>> numpoly.add(poly1, poly2)
        polynomial([[2, y+x, y**2+x**2],
                    [1+x**3, y+x**4, y**2+x**5],
                    [1+x**6, y+x**7, y**2+x**8]])
    """
    x1, x2 = numpoly.align_polynomials(x1, x2)
    no_output = out is None
    if no_output:
        out = numpoly.ndpoly(
            exponents=x1.exponents,
            shape=x1.shape,
            indeterminants=x1.indeterminants,
            dtype=x1.dtype,
        )
    for key in x1.keys:
        numpy.add(x1[key], x2[key], out=out[key], where=where, **kwargs)
    if no_output:
        out = numpoly.clean_attributes(out)
    return out