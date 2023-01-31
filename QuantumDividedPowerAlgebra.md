The  [QuantumDividedPowerAlgebra](QuantumDividedPowerAlgebra) is a graded algebra over a ring R[q]. The component in degree n is the free R[q]-module with basis x<sup>n</sup>. The multiplication is defined on basis elements by x<sup>r</sup>.x<sup>s</sup> = [r+s,r]_q x<sup>r+s</sup> where [r+s,r]_q is the quantum binomial coefficient.

The [DividedPowerAlgebra](http://trac.sagemath.org/sage_trac/search/opensearch?q=wiki%3AQuantumDividedPowerAlgebra) is a graded algebra over a ring R. The component in degree n is the free R-module with basis x<sup>n</sup>. The multiplication is defined on basis elements by x<sup>r</sup>.x<sup>s</sup> = [r+s,r]_q x<sup>r+s</sup> where [r+s,r] is the binomial coefficient.

The divided power algebra is a Hopf algebra and is the dual Hopf algebra to R[x]. The coproduct on the divided power Hopf algebra is x<sup>k</sup> |--> x<sup>k</sup> x 1 + x<sup>k-1</sup> x x + ... 1 x x<sup>k</sup> (where I have used x as an indeterminate and as a tensor product symbol).

See ticket #11979
---

Attachments:
 * [dividedpower.py](QuantumDividedPowerAlgebra/dividedpower.py)
