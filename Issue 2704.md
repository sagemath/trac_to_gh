# Issue 2704: bug in lcm(a,b) for a,b polynomials in QQ[] if a is constant

Issue created by migration from https://trac.sagemath.org/ticket/2704

Original creator: cremona

Original creation time: 2008-03-28 18:22:46

Assignee: was

Keywords: lcm, polynomial, singular

In `QQ[]`, `lcm(X,1)` works fine but not `lcm(1,X)`:


```
sage: R.<X>=QQ[]
sage: a=R(1)
sage: b=X
sage: lcm(b,a)
X
sage: lcm(a,b)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/jec/sage-2.11.alpha1/devel/sage-generic/sage/rings/<ipython console> in <module>()

/home/jec/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/rings/arith.py in lcm(a, b, integer)
   1096     if not isinstance(a, RingElement):
   1097         a = integer_ring.ZZ(a)
-> 1098     return a.lcm(b)
   1099
   1100 LCM = lcm

/home/jec/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py in lcm(self, singular, have_ring)
    284         return _singular_init_func(self, singular, have_ring, force)
    285     def lcm(self, singular=singular_default, have_ring=False):
--> 286         return lcm_func(self, singular, have_ring)
    287     def resultant(self, other, variable=None):
    288         return resultant_func(self, other, variable)

/home/jec/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py in lcm_func(self, right, have_ring)
    385         (a^2 + a)*x^6*y + (a^3 + a - 1)*x^4*y + (-a)*x^4
    386     """
--> 387     lcm = self._singular_(have_ring=have_ring).lcm(right._singular_(have_ring=have_ring))
    388     return lcm.sage_poly(self.parent())
    389

/home/jec/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, *args)
    970
    971     def __call__(self, *args):
--> 972         return self._obj.parent().function_call(self._name, [self._obj] + list(args))
    973
    974     def help(self):

/home/jec/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/interfaces/expect.py in function_call(self, function, args)
    899             if not isinstance(args[i], ExpectElement):
    900                 args[i] = self.new(args[i])
--> 901         return self.new("%s(%s)"%(function, ",".join([s.name() for s in args])))
    902
    903     def call(self, function_name, *args):

/home/jec/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/interfaces/expect.py in new(self, code)
    801
    802     def new(self, code):
--> 803         return self(code)
    804
    805     ###################################################################

/home/jec/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/interfaces/singular.py in __call__(self, x, type)
    496             x = str(x)[1:-1]
    497
--> 498         return SingularElement(self, type, x, False)
    499
    500

/home/jec/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/interfaces/singular.py in __init__(self, parent, type, value, is_name)
    817             except (RuntimeError, TypeError, KeyboardInterrupt), x:
    818                 self._session_number = -1
--> 819                 raise TypeError, x
    820         else:
    821             self._name = value

<type 'exceptions.TypeError'>: Singular error:
   ? // ** list element must be an integer
   ? error occurred in poly.lib::lcm line 721: ` ERROR("// ** list element must be an integer");`
   ? leaving poly.lib::lcm
   skipping text from `;` error at token `)`
```


It works fine in ZZ[] so I guess it's a problem with the singular interface.



---

Comment by mabshoff created at 2008-04-15 04:03:47

Changing assignee from was to malb.


---

Comment by mabshoff created at 2008-04-15 04:03:47

Changing priority from major to critical.


---

Comment by mabshoff created at 2008-04-15 04:03:47

Changing component from interfaces to commutative algebra.


---

Comment by mabshoff created at 2008-04-15 04:03:47

Martin,

this sounds like something that is in your domain. Can you check it out?

Cheers,

Michael


---

Attachment


---

Comment by malb created at 2008-04-15 09:03:20

patch attached.


---

Comment by mhansen created at 2008-04-15 09:15:24

Looks good to me.


---

Comment by mabshoff created at 2008-04-15 09:28:28

Merged in Sage 3.0.alpha5


---

Comment by mabshoff created at 2008-04-15 09:28:28

Resolution: fixed
