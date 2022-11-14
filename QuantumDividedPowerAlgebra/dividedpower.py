
r"""
A minimal implementation of the divided power algebra as an algebra with basis

AUTHOR: Bruce Westbury
"""
#*****************************************************************************
#  Copyright (C) 2011 Bruce W. Westbury <brucewestbury@gmail.com>
#
#  Distributed under the terms of the GNU General Public License (GPL)
#                  http://www.gnu.org/licenses/
#******************************************************************************

from sage.misc.cachefunc import cached_method
from sage.sets.family import Family
from sage.categories.all import AlgebrasWithBasis
from sage.combinat.free_module import CombinatorialFreeModule

class DividedPowerAlgebra(CombinatorialFreeModule):
    r"""
    An example of an algebra with basis: the divided power algebra.

    This class illustrates a minimal implementation of the divided power algebra.
    """

    def __init__(self, R):
        assert(R in Rings())
        CombinatorialFreeModule.__init__(self, R, NonNegativeIntegers(), category = AlgebrasWithBasis(R))

    def _repr_(self):
        return "The divided power algebra over %s"%(self.base_ring())

    @cached_method
    def one(self):
        """
        Returns the unit of the algebra
        as per :meth:`AlgebrasWithBasis.ParentMethods.one_basis`.
        """
        u = NonNegativeIntegers.from_integer(0)
        return self.monomial(u)

    def product_on_basis(self, left, right):
        r"""
        Product, on basis elements, as per :meth:`AlgebrasWithBasis.ParentMethods.product_on_basis`.
        """
        return binomial(left+right,left) * self.basis()[left+right] 
       
    @cached_method
    def algebra_generators(self):
        r"""
        The generators of this algebra, as per :meth:`Algebras.ParentMethods.algebra_generators`.

        """

        return Family(NonNegativeIntegers())


