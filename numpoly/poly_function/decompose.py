"""Decompose a polynomial to component form."""
import numpy
import numpoly


def decompose(poly):
    """
    Decompose a polynomial to component form.

    In array missing values are padded with 0 to make decomposition compatible
    with ``chaospy.sum(ouput, 0)``.

    Args:
        poly (numpoly.ndpoly):
            Polynomial to decompose

    Returns:
        (numpoly.ndpoly):
            Decomposed polynomial with ``poly.shape==(M,)+output.shape``
            where ``M`` is the number of components in `poly`.

    Examples:
        >>> x = numpoly.symbols()
        >>> poly = numpoly.polynomial([x**2-1, 2])
        >>> poly
        polynomial([-1+q**2, 2])
        >>> numpoly.decompose(poly)
        polynomial([[-1, 2],
                    [q**2, 0]])
        >>> numpoly.sum(numpoly.decompose(poly), 0)
        polynomial([-1+q**2, 2])

    """
    return numpoly.concatenate([
        numpoly.construct.polynomial_from_attributes(
            exponents=[expon],
            coefficients=[poly[key]],
            names=poly.indeterminants,
            clean=False,
        )[numpy.newaxis] for key, expon in zip(poly.keys, poly.exponents)
    ])
