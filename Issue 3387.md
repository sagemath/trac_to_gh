# Issue 3387: unacceptably slow conversion of rationals from pari to Rational

Issue created by migration from https://trac.sagemath.org/ticket/3387

Original creator: dmharvey

Original creation time: 2008-06-09 22:19:45

Assignee: tbd


```
sage: x = (2^1000000 - 1) / (2^1000000)
sage: time y = pari(x)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
sage: time z = Rational(y)
CPU times: user 11.30 s, sys: 0.02 s, total: 11.32 s
Wall time: 11.33
```




---

Comment by was created at 2008-06-09 22:31:49

Changing assignee from tbd to was.


---

Attachment


---

Comment by was created at 2008-06-09 22:49:56

with this patch the situation is better:


```
sage: x = pari('(2^1000000 - 1) / (2^1000000)')
sage: time y = Rational(x)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
sage: timeit('Rational(x)')
625 loops, best of 3: 858 µs per loop
sage: Rational(pari('x^2+1'))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/was/Desktop/movies/<ipython console> in <module>()

/Users/was/Desktop/movies/rational.pyx in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:3321)()

/Users/was/Desktop/movies/rational.pyx in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:4386)()

/Users/was/Desktop/movies/integer.pyx in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:5183)()

/Users/was/Desktop/movies/gen.pyx in sage.libs.pari.gen.gen.__hex__ (sage/libs/pari/gen.c:5096)()

TypeError: gen must be of PARI type t_INT
```



---

Comment by gfurnish created at 2008-06-10 01:07:35

Doctests pass, code looks fine.


---

Comment by mabshoff created at 2008-06-10 01:21:40

Merged in Sage 3.0.3.alpha2


---

Comment by mabshoff created at 2008-06-10 01:21:40

Resolution: fixed
