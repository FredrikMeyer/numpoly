"""Split an array into multiple sub-arrays."""
import numpy
import numpoly

from .common import implements


@implements(numpy.split)
def split(ary, indices_or_sections, axis=0):
    """
    Split an array into multiple sub-arrays.

    Args:
        ary (numpoly.ndpoly):
            Array to be divided into sub-arrays.
        indices_or_sections (int, Sequence[int]):
            If `indices_or_sections` is an integer, N, the array will be
            divided into N equal arrays along `axis`.  If such a split is not
            possible, an error is raised.

            If `indices_or_sections` is a 1-D array of sorted integers, the
            entries indicate where along `axis` the array is split.  For
            example, ``[2, 3]`` would, for ``axis=0``, result in

            - ary[:2]
            - ary[2:3]
            - ary[3:]

            If an index exceeds the dimension of the array along `axis`, an
            empty sub-array is returned correspondingly.
        axis (int):
            The axis along which to split, default is 0.

    Returns:
        (List[numpoly.ndpoly])
            A list of sub-arrays.

    Raises:
        ValueError:
            If `indices_or_sections` is given as an integer, but a split does
            not result in equal division.

    See Also:
        array_split:
            Split an array into multiple sub-arrays of equal or near-equal
            size. Does not raise an exception if an equal division cannot be
            made.
        hsplit:
            Split array into multiple sub-arrays horizontally (column-wise).
        vsplit:
            Split array into multiple sub-arrays vertically (row wise).
        dsplit:
            Split array into multiple sub-arrays along the 3rd axis (depth).

    Examples:
        >>> poly = numpoly.monomial(16).reshape(4, 4)
        >>> poly
        polynomial([[1, q, q**2, q**3],
                    [q**4, q**5, q**6, q**7],
                    [q**8, q**9, q**10, q**11],
                    [q**12, q**13, q**14, q**15]])
        >>> part1, _ = numpoly.split(poly, 2, axis=0)
        >>> part1
        polynomial([[1, q, q**2, q**3],
                    [q**4, q**5, q**6, q**7]])
        >>> part1, _ = numpoly.split(poly, 2, axis=1)
        >>> part1
        polynomial([[1, q],
                    [q**4, q**5],
                    [q**8, q**9],
                    [q**12, q**13]])

    """
    ary = numpoly.aspolynomial(ary)
    results = numpy.split(
        ary.values, indices_or_sections=indices_or_sections, axis=axis)
    return [numpoly.aspolynomial(result, names=ary.indeterminants)
            for result in results]
