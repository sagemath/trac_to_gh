# Issue 351: issue running cremona's abelian_group command and memory usage in gp

Issue created by migration from https://trac.sagemath.org/ticket/351

Original creator: was

Original creation time: 2007-04-11 15:15:33

Assignee: was


```
Hello William:

I was trying to compute with elliptic curves on SAGE (and
www.sagenb.com) and I have found a problem since in MAGMA works very fast.

Here are the output of both programs:


///////////////////////
IN SAGE
//////////////////////


E=EllipticCurve(GF(2^192-2^64-1),[-3,100001010101])
E
sage: E=EllipticCurve(GF(2^192-2^64-1),[-3,100001010101])
sage: E
Elliptic Curve defined by y^2  = x^3 +
6277101735386680763835789423207666416083908700390324961276*x +
100001010101 over Finite Field of size
6277101735386680763835789423207666416083908700390324961279
sage: n=E.cardinality()
nsage: n.factor()
2 * 3 * 5^2 * 7 * 29 * 83 * 642529 * 71354419 *
54172661118016618880771252420611881049
sage: E.abelian_group()
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/enrique/<ipython console> in <module>()

/usr/local/sage-2.1.4/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_finite_field.py
in abelian_group(self)
   334             pass
   335         if self.base_ring().degree() == 1:
--> 336             I, G = self._cremona_abgrp_data()
   337             A = AbelianGroup(I)
   338             G = tuple(reversed([self(P) for P in G]))

/usr/local/sage-2.1.4/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_finite_field.py
in _cremona_abgrp_data(self)
   297
   298     def _cremona_abgrp_data(self):
--> 299         E = self._gp()
   300         gp = E.parent()
   301         return eval(gp.eval('[%s.isotype,
lift(%s.generators)]'%(E.name(), E.name())))

/usr/local/sage-2.1.4/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_finite_field.py
in _gp(self)
    77         if not F.is_prime():
    78             raise NotImplementedError
---> 79         self.__gp = gp_cremona.ellinit(self.a_invariants(),
F.characteristic())
    80         return self.__gp
    81

/usr/local/sage-2.1.4/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/gp_cremona.py
in ellinit(e, p)
    74     """
    75     init()
---> 76     return gp("e=ellzpinit(%s,%s);"%(e,p))
    77
    78

/usr/local/sage-2.1.4/local/lib/python2.5/site-packages/sage/interfaces/expect.py
in __call__(self, x)
   490             return x
   491         if isinstance(x, str):
--> 492             return cls(self, x)
   493         try:
   494             return self._coerce_impl(x)

/usr/local/sage-2.1.4/local/lib/python2.5/site-packages/sage/interfaces/expect.py
in __init__(self, parent, value, is_name)
   719             except (TypeError, KeyboardInterrupt, RuntimeError,
ValueError), x:
   720                 self._session_number = -1
--> 721                 raise TypeError, x
   722         self._session_number = parent._session_number
   723

<type 'exceptions.TypeError'>: Error executing code in GP/PARI:
CODE:
       sage[1]=e=ellzpinit([0, 0, 0,
6277101735386680763835789423207666416083908700390324961276,
100001010101],6277101735386680763835789423207666416083908700390324961279);;
GP/PARI ERROR:
 *** ellap: not enough memory


///////////////////////
IN MAGMA
//////////////////////
> K:=GF(2^192-2^64-1);
> K;
Finite field of size
6277101735386680763835789423207666416083908700390324961279
> E:=EllipticCurve([-3,K!100001010101])
> ;
> E;
Elliptic Curve defined by y^2 = x^3 +
6277101735386680763835789423207666416083908700390324961276*x +
100001010101 over
GF(6277101735386680763835789423207666416083908700390324961279)
> A:=AbelianGroup(E);
> A;
Abelian Group isomorphic to
Z/6277101735386680763835789423079145837183917076777215537650
Defined on 1 generator
Relations:
   6277101735386680763835789423079145837183917076777215537650*A.1 = 0
> #A;
6277101735386680763835789423079145837183917076777215537650

Total time: 6.629 seconds, Total memory usage: 5.53MB
```



---

Comment by cremona created at 2007-08-18 09:49:17

Changing assignee from was to cremona.


---

Comment by cremona created at 2007-08-18 09:49:17

The problem is this:  The function uses pari's ellap() function to find the group order, and this does not work for huge primes.  I found that withh gp using a stack of 110M (my default) I could go to p=nextprim(2^78) but no further;  after increaasing the stack, p=nextprime(95) is ok but p=nextprime(100) produces an error message.

I suggest that (1) the underlyi,ng call to gp initializes gp with a largish stack if the prime is medium-large;  (2) if the prime is greater than that (say >2^95) then raise a not-implemented error.

I should also say that the implementation of abelian_group() in my gp script was not intended to handle such large primes -- it only uses baby-step-giant-step techniques and not fancier methods such as SEA.  Magma, by contrast, as better methods for large primes, so an alternative to (3) would be to use Magma's function instead if Magma is available.


---

Comment by cremona created at 2007-08-18 09:49:17

Changing status from new to assigned.


---

Comment by was created at 2007-08-18 10:02:56


```
Good!  If you send me a login to the trac system I might be able to
comment on a few items there, for example in
http://www.sagemath.org:9002/sage_trac/ticket/351
my gp program was never intended to manage "huge" prime fields & hence
huge group orders.  Perhaps we should guesstimate what the largest
prime is for which it makes sense to use my code and otherwise use
Magma if available, or give a "not implemented" error or something.
```



---

Comment by was created at 2007-08-19 01:50:54

John -- SAGE includes a very good SEA implementation written in PARI.  You could load that and call it.


---

Comment by was created at 2007-08-19 01:54:38

Changing type from defect to enhancement.


---

Comment by was created at 2007-08-19 01:54:38

For example, in the above, SEA can compute the order in seconds (this only works on a 64-bit computer -- on a 32-bit one you can't even define the curve in pari using your script):

```
sage: E=EllipticCurve(GF(2^192-2^64-1),[-3,100001010101])                                                    
sage: time c = E.cardinality()
CPU times: user 0.01 s, sys: 0.01 s, total: 0.02 s
Wall time: 3.40
sage: c
6277101735386680763835789423079145837183917076777215537650
sage: factor(c)
2 * 3 * 5^2 * 7 * 29 * 83 * 642529 * 71354419 * 54172661118016618880771252420611881049
sage:
KeyboardInterrupt
sage:            
```



I'm changing this from a bug to an "enhancement", since after all any command with infinitely many inputs has it's limits in any program, and hence everything would be buggy.

That said, a better error message would be good.


---

Comment by cremona created at 2008-04-05 14:01:41

Can we close this now?


```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0.alpha1, Release Date: 2008-04-04                  |
| Type notebook() for the GUI, and license() for information.        |
sage: E=EllipticCurve(GF(2^192-2^64-1),[-3,100001010101])
sage: E
Elliptic Curve defined by y^2  = x^3 + 6277101735386680763835789423207666416083908700390324961276*x + 100001010101 over Finite Field of size 6277101735386680763835789423207666416083908700390324961279
sage: n=E.cardinality()
sage: n.factor()
2 * 3 * 5^2 * 7 * 29 * 83 * 642529 * 71354419 * 54172661118016618880771252420611881049
sage: E.abelian_group()

(Multiplicative Abelian Group isomorphic to C6277101735386680763835789423079145837183917076777215537650,
 ((4153000426260909917154178788800583218670192457236809343835 : 2657174507413387032212810112685256696116491447557332765409 : 1),))
```



---

Comment by mabshoff created at 2008-04-05 14:23:24

I can confirm that this is fixed, so I am closing it. Can you tell me which ticket fixed the issue for the record and to assign proper credit?

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-05 14:23:24

Resolution: fixed
