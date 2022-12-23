# Issue 817: O(3^(-2)) is broken

Issue created by migration from https://trac.sagemath.org/ticket/817

Original creator: was

Original creation time: 2007-10-04 01:17:50

Assignee: somebody


```
sage: O(3^-2)
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/home/was/<ipython console> in <module>()

/home/was/s/local/lib/python2.5/site-packages/sage/rings/big_oh.py in O(x)
     27             raise ArithmeticError, "x must be prime power"
     28         p, r = F[0]
---> 29         return padics.factory.Zp(p, prec = r, type = 'capped-rel')(0, absprec = r)
     30
     31     elif isinstance(x, padics.padic_generic.pAdicGeneric):

/home/was/s/local/lib/python2.5/site-packages/sage/rings/padics/factory.py in Zp(p, prec, type, print_mode, halt, names, check)
    327             return K
    328     if (type == 'capped-rel'):
--> 329         K = pAdicRingCappedRelative(p, prec, print_mode, name)
    330     elif (type == 'fixed-mod'):
    331         K = pAdicRingFixedMod(p, prec, print_mode, name)

/home/was/s/local/lib/python2.5/site-packages/sage/rings/padics/padic_ring_capped_relative.py in __init__(self, p, prec, print_mode, names)
    134 class pAdicRingCappedRelative(pAdicRingBaseGeneric, pAdicCappedRelativeRingGeneric):
    135     def __init__(self, p, prec, print_mode, names):
--> 136         pAdicRingBaseGeneric.__init__(self, p, prec, print_mode, names, pAdicCappedRelativeElement)
    137
    138     r"""

/home/was/s/local/lib/python2.5/site-packages/sage/rings/padics/padic_generic.py in __init__(self, p, prec, print_mode, names, element_class)
     72         #else:
     73         #    self.prime_pow = PowComputer(p, 3, prec, self.is_field())
---> 74         self.prime_pow = PowComputer(p, prec, self.is_field())
     75         self.__set_print_mode(print_mode)
     76         self._element_class = element_class

/home/was/pow_computer.pyx in pow_computer.PowComputer()

<type 'exceptions.ValueError'>: L must be positive
sage:                                                  

```



---

Attachment


---

Comment by was created at 2007-10-04 02:47:49

Resolution: fixed
