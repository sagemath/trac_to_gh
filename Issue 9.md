# Issue 9: Pari stack overflow

archive/issues_000009.json:
```json
{
    "body": "Assignee: somebody\n\nOnce the Pari stack overflows, subsequent sage commands which use the Pari library do not work.\n\nIfti.\n----\n\n\n```\nburhanud@sage:~$ sage\n--------------------------------------------------------\n--------------------------------------------------------\n| SAGE Version 1.3.7.1, Build Date: 2006-09-10-2157    |\n| Distributed under the GNU General Public License V2. |\n\nsage: E = EllipticCurve([0,0,0,-307*1907,0])\n\nsage: E.Lseries_deriv_at1()\n---------------------------------------------------------------------------\nexceptions.RuntimeError                              Traceback (most\nrecent call last)\n\n/home/burhanud/<ipython console>\n\n/home/was/sage/local/lib/python2.4/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py\nin Lseries_deriv_at1(self, k)\n   1724         # Compute z = e^(-2pi/sqrt(N))\n   1725         pi = 3.14159265358979323846\n-> 1726         v = transcendental.exponential_integral_1(2*pi/sqrtN, k)\n   1727         L = 2*float(sum([ (v[n-1] * an[n])/n for n in\nxrange(1,k+1)]))\n   1728         error = 2*exp(-2*pi*(k+1)/sqrtN)/(1-exp(-2*pi/sqrtN))\n\n/home/was/sage/local/lib/python2.4/site-packages/sage/functions/transcendental.py\nin exponential_integral_1(x, n)\n     83         return float(pari(x).eint1())\n     84     else:\n---> 85         return [float(z) for z in pari(x).eint1(n)]\n     86\n     87 def gamma(s):\n\n/home/burhanud/gen.pyx in gen._pari_trap()\n\nRuntimeError: The PARI stack overflowed.  Use pari.allocatemem() to double\nthe stack.\n\nsage: factor(4)\n---------------------------------------------------------------------------\nexceptions.RuntimeError                              Traceback (most\nrecent call last)\n\n/home/burhanud/<ipython console>\n\n/home/was/sage/local/lib/python2.4/site-packages/sage/rings/arith.py in\nfactor(n, proof, int_, algorithm, verbose)\n   1244     if algorithm == 'pari':\n   1245         return factorization.Factorization(__factor_using_pari(n,\n-> 1246                                    int_=int_,\ndebug_level=verbose), unit)\n   1247     elif algorithm == 'kash':\n   1248         F = kash.eval('Factorization(%s)'%n)\n\n/home/was/sage/local/lib/python2.4/site-packages/sage/rings/arith.py in\n__factor_using_pari(n, int_, debug_level)\n   1168         import sage.rings.integer_ring\n   1169         Z = sage.rings.integer_ring.IntegerRing()\n-> 1170     prev = pari.get_debug_level()\n   1171     pari.set_debug_level(debug_level)\n   1172     F = pari(n).factor()\n\n/home/burhanud/gen.pyx in gen.PariInstance.get_debug_level()\n\n/home/burhanud/gen.pyx in gen.PariInstance.default()\n\n/home/burhanud/gen.pyx in gen._pari_trap()\n\nRuntimeError: The PARI stack overflowed.  Use pari.allocatemem() to double\nthe stack.\n\nsage: factor(4, algorithm='kash')\n 2^2\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9\n\n",
    "created_at": "2006-09-12T09:02:28Z",
    "labels": [
        "component: basic arithmetic",
        "minor",
        "bug"
    ],
    "title": "Pari stack overflow",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9",
    "user": "Iftikhar Burhanuddin"
}
```
Assignee: somebody

Once the Pari stack overflows, subsequent sage commands which use the Pari library do not work.

Ifti.
----


```
burhanud@sage:~$ sage
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


Issue created by migration from https://trac.sagemath.org/ticket/9





---

archive/issue_comments_000028.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2006-10-15T17:32:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9#issuecomment-28",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000009.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2006-10-15T17:32:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9#event-9"
}
```



---

archive/issue_comments_000029.json:
```json
{
    "body": "Fixed by modifying _pari_trap in devel/sage/sage/libs/pari/gen.pyx:\n\n```\ncdef void _pari_trap \"_pari_trap\" (long errno, long retries) except *:\n    if retries > 100:\n        raise RuntimeError, \"_pari_trap recursion too deep\"\n    if errno == errpile:\n        P.allocatemem()\n        raise RuntimeError, \"The PARI stack overflowed.  It has automaticallyed been doubled using pari.allocatemem().  Please retry your computation, possibly after you manually call pari.allocatemem() a few times.\"\n    \n```\n",
    "created_at": "2006-10-15T17:32:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9#issuecomment-29",
    "user": "https://github.com/williamstein"
}
```

Fixed by modifying _pari_trap in devel/sage/sage/libs/pari/gen.pyx:

```
cdef void _pari_trap "_pari_trap" (long errno, long retries) except *:
    if retries > 100:
        raise RuntimeError, "_pari_trap recursion too deep"
    if errno == errpile:
        P.allocatemem()
        raise RuntimeError, "The PARI stack overflowed.  It has automaticallyed been doubled using pari.allocatemem().  Please retry your computation, possibly after you manually call pari.allocatemem() a few times."
    
```

