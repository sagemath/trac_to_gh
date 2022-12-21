# Issue 9: Pari stack overflow

Issue created by migration from Trac.

Original creator: Iftikhar Burhanuddin

Original creation time: 2006-09-12 09:02:28

Assignee: somebody

Once the Pari stack overflows, subsequent sage commands which use the Pari library do not work.

Ifti.
----


```
burhanud`@`sage:~$ sage
--------------------------------------------------------
--------------------------------------------------------
| SAGE Version 1.3.7.1, Build Date: 2006-09-10-2157    |
| Distributed under the GNU General Public License V2. |

sage: E = EllipticCurve([0,0,0,-307*1907,0])

sage: E.Lseries_deriv_at1()
---------------------------------------------------------------------------
exceptions.RuntimeError                              Traceback (most
recent call last)

/home/burhanud/<ipython console>

/home/was/sage/local/lib/python2.4/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py
in Lseries_deriv_at1(self, k)
   1724         # Compute z = e^(-2pi/sqrt(N))
   1725         pi = 3.14159265358979323846
-> 1726         v = transcendental.exponential_integral_1(2*pi/sqrtN, k)
   1727         L = 2*float(sum([ (v[n-1] * an[n])/n for n in
xrange(1,k+1)]))
   1728         error = 2*exp(-2*pi*(k+1)/sqrtN)/(1-exp(-2*pi/sqrtN))

/home/was/sage/local/lib/python2.4/site-packages/sage/functions/transcendental.py
in exponential_integral_1(x, n)
     83         return float(pari(x).eint1())
     84     else:
---> 85         return [float(z) for z in pari(x).eint1(n)]
     86
     87 def gamma(s):

/home/burhanud/gen.pyx in gen._pari_trap()

RuntimeError: The PARI stack overflowed.  Use pari.allocatemem() to double
the stack.

sage: factor(4)
---------------------------------------------------------------------------
exceptions.RuntimeError                              Traceback (most
recent call last)

/home/burhanud/<ipython console>

/home/was/sage/local/lib/python2.4/site-packages/sage/rings/arith.py in
factor(n, proof, int_, algorithm, verbose)
   1244     if algorithm == 'pari':
   1245         return factorization.Factorization(__factor_using_pari(n,
-> 1246                                    int_=int_,
debug_level=verbose), unit)
   1247     elif algorithm == 'kash':
   1248         F = kash.eval('Factorization(%s)'%n)

/home/was/sage/local/lib/python2.4/site-packages/sage/rings/arith.py in
__factor_using_pari(n, int_, debug_level)
   1168         import sage.rings.integer_ring
   1169         Z = sage.rings.integer_ring.IntegerRing()
-> 1170     prev = pari.get_debug_level()
   1171     pari.set_debug_level(debug_level)
   1172     F = pari(n).factor()

/home/burhanud/gen.pyx in gen.PariInstance.get_debug_level()

/home/burhanud/gen.pyx in gen.PariInstance.default()

/home/burhanud/gen.pyx in gen._pari_trap()

RuntimeError: The PARI stack overflowed.  Use pari.allocatemem() to double
the stack.

sage: factor(4, algorithm='kash')
 2^2

```



---

Comment by was created at 2006-10-15 17:32:36

Resolution: fixed


---

Comment by was created at 2006-10-15 17:32:36

Fixed by modifying _pari_trap in devel/sage/sage/libs/pari/gen.pyx:

```
cdef void _pari_trap "_pari_trap" (long errno, long retries) except *:
    if retries > 100:
        raise RuntimeError, "_pari_trap recursion too deep"
    if errno == errpile:
        P.allocatemem()
        raise RuntimeError, "The PARI stack overflowed.  It has automaticallyed been doubled using pari.allocatemem().  Please retry your computation, possibly after you manually call pari.allocatemem() a few times."
    
```

