The  QuantumDividedPowerAlgebra is a graded algebra over a ring R[q]. The component in degree n is the free R[q]-module with basis x^n^. The multiplication is defined on basis elements by x^r^.x^s^ = [r+s,r]_q x^r+s^ where [r+s,r]_q is the quantum binomial coefficient.

The [DividedPowerAlgebra](http://trac.sagemath.org/sage_trac/search/opensearch?q=wiki%3AQuantumDividedPowerAlgebra) is a graded algebra over a ring R. The component in degree n is the free R-module with basis x^n^. The multiplication is defined on basis elements by x^r^.x^s^ = [r+s,r]_q x^r+s^ where [r+s,r] is the binomial coefficient.

The divided power algebra is a Hopf algebra and is the dual Hopf algebra to R[x]. The coproduct on the divided power Hopf algebra is x^k^ |--> x^k^ x 1 + x^k-1^ x x + ... 1 x x^k^ (where I have used x as an indeterminate and as a tensor product symbol).

See ticket [#11979](https://trac.sagemath.org/ticket/11979)
---

Attachments:
 * [dividedpower.py](QuantumDividedPowerAlgebra/dividedpower.py)
