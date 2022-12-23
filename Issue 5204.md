# Issue 5204: simon_two_descent -- bug in the interface when number field has variable name 'x'

Issue created by migration from https://trac.sagemath.org/ticket/5204

Original creator: was

Original creation time: 2009-02-08 05:37:04

Assignee: was

1. A basic bug in the wrapper, which is probably easy to fix:


```
sage: E = EllipticCurve('8320e1').change_ring(QuadraticField(-191,'x'))
sage: E.simon_two_descent()
Traceback (most recent call last):
...
---> 98     ans = sage_eval(v, {'Mod': _gp_mod, 'y': K.gen(0)})
NameError: name 'ans' is not defined
```


The problem is my choice of 'x' as generator name for the number field.  The fix is to always change the variable of the base number field to 'a' before feeding anything to pari.



---

Attachment


---

Comment by cremona created at 2009-02-15 17:37:50

Apply after previous


---

Attachment

Review:  I can only deduce that rlm did not actually test this!

```
sage -t  "devel/sage-5204/sage/schemes/elliptic_curves/gp_simon.py"
**********************************************************************
File "/home/john/sage-3.3.rc0/devel/sage-5204/sage/schemes/elliptic_curves/gp_simon.py", line 54:
    sage: sage.schemes.elliptic_curves.gp_simon.simon_two_descent(E)
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-3.3.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-3.3.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-3.3.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[4]>", line 1, in <module>
        sage.schemes.elliptic_curves.gp_simon.simon_two_descent(E)###line 54:
    sage: sage.schemes.elliptic_curves.gp_simon.simon_two_descent(E)
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/gp_simon.py", line 69, in simon_two_descent
        K = E.base_ring().change_names('a')
    AttributeError: 'RationalField' object has no attribute 'change_names'
**********************************************************************
File "/home/john/sage-3.3.rc0/devel/sage-5204/sage/schemes/elliptic_curves/gp_simon.py", line 56:
    sage: E.simon_two_descent()
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-3.3.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-3.3.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-3.3.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[5]>", line 1, in <module>
        E.simon_two_descent()###line 56:
    sage: E.simon_two_descent()
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 1202, in simon_two_descent
        maxprob=maxprob, limbigprime=limbigprime)
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/gp_simon.py", line 69, in simon_two_descent
        K = E.base_ring().change_names('a')
    AttributeError: 'RationalField' object has no attribute 'change_names'
**********************************************************************
1 items had failures:
   2 of   8 in __main__.example_2
```


I have added a second patch (apply after the first one) which checks that K is not QQ before changing names!

If either rlm or was could review my patch then this can go forward.


---

Comment by rlm created at 2009-02-16 17:49:31

+1


---

Comment by mabshoff created at 2009-02-20 07:19:59

These two patches cause the following doctest failure:

```
sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_number_field.py
**********************************************************************
File "/scratch/mabshoff/sage-3.3.rc3/devel/sage-main/sage/schemes/elliptic_curves/ell_number_field.py", line 9:
    sage: E.simon_two_descent()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.3.rc3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.rc3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.rc3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[5]>", line 1, in <module>
        E.simon_two_descent()###line 9:
    sage: E.simon_two_descent()
      File "/scratch/mabshoff/sage-3.3.rc3/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_number_field.py", line 176, in simon_two_descent
        maxprob=maxprob, limbigprime=limbigprime)
      File "/scratch/mabshoff/sage-3.3.rc3/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/gp_simon.py", line 74, in simon_two_descent
        E = E.change_ring(K)
      File "/scratch/mabshoff/sage-3.3.rc3/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py", line 826, in change_ring
        return constructor.EllipticCurve(R, [R(a) for a in self.ainvs()])
      File "parent.pyx", line 276, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:3653)
      File "coerce_maps.pyx", line 76, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:2793)
      File "coerce_maps.pyx", line 71, in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2700)
      File "/scratch/mabshoff/sage-3.3.rc3/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 831, in _element_constructor_
        return self._coerce_from_other_number_field(x)
      File "/scratch/mabshoff/sage-3.3.rc3/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 3735, in _coerce_from_other_number_field
        raise TypeError, "Cannot coerce element into this number field"
    TypeError: Cannot coerce element into this number field
**********************************************************************
```



---

Comment by cremona created at 2009-02-20 08:46:47

Rats.  I was certain I had tested that file.  I'll look into it when I can (unlikely before this evening GMT).  John


---

Comment by cremona created at 2009-02-20 09:54:05

Apply after previous two


---

Attachment

The trouble is that after changing the name of the field's generator (in that example from 'i' to 'a') there is no coercion from the old field to the new one, even though they only differ i nthe name of the gen.

This could obviously be hacked, and I have done so, but it is not very elegant:   since E's field has changed you have to hack again to get the points found back on the original curve which has the original base field.

I'm sure that there is a better coercion-based way of doing this.  But the tests now pass.  Apply new patch after the other two.


---

Comment by rlm created at 2009-03-16 13:58:44

+1


---

Comment by cremona created at 2009-03-19 16:54:11

The following example actually came up today:

```
sage: K.<b>=QuadraticField(43)
sage: E=EllipticCurve([0,0,0,0,(-3697884*b - 24248647)])
sage: E.simon_two_descent()
NameError                                 Traceback (most recent call last)
...
NameError: name 'ans' is not defined
```


This is after the patches are applied, so bad news.  I called the field generator 'b' since earlier I had called it 'a' and thought that might be the problem.

It turns out that it is a bug in simon's ell.gp:

```
             GP/PARI CALCULATOR Version 2.3.3 (released)
      i686 running linux (ix86/GMP-4.2.1 kernel) 32-bit version
       compiled: Mar 12 2009, gcc-4.1.2 20070115 (SUSE Linux)
          (readline v5.2 enabled, extended help available)

               Copyright (C) 2000-2006 The PARI Group

PARI/GP is free software, covered by the GNU General Public
License, and comes WITHOUT ANY WARRANTY WHATSOEVER.

Type ? for help, \q to quit.
Type ?12 for how to get moral (and possibly technical) support.

parisize = 4000000, primelimit = 500000
? \r ell.gp
? K = bnfinit(y^2 - 43);
? a = Mod(y,K.pol);
? bnfellrank(K, [0,0,0,0,-3697884*a - 24248647]);
courbe elliptique : Y^2 = x^3 + Mod(-3697884*y - 24248647, y^2 - 43)
points triviaux sur la courbe = [[1, 1, 0]]
  ***   array index (1) out of allowed range [none]:
  ***   ...iv,r=nfsqrt(nf,norm(zc))[1];if(DEBUGLEVEL_ell
                                    ^--------------------
```

I will check that it still happens with the latest pari/gp, and if so file a bug report with Denis Simon.


---

Comment by cremona created at 2009-03-23 19:58:37

Denis Simon says:

```
Dear John,

OK, this is really a bug of ell.gp

The problem is that due to a low real precision, the sign
of an algebraic number at some real embedding is misevaluated.

For a quick fix, you have to get into the function 'nfsqrt'
and remove the small loop
for( i = 1, nf.r1,...

This is not a satisfactory solution, and I am looking for a better one.
In particular, I probably have to change the way I handle the real
embeddings. For the moment, it is just something like
subst(algebraic_number,y,nf.roots[1])

Maybe I have to do interval arithmetic...

Thank you for the report.
Denis SIMON.
```

so that will have to wait until he fixes hos gp script.  This should probably be on a different ticket...


---

Comment by mabshoff created at 2009-03-24 23:16:07

Merged all three patches in Sage 3.4.1.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-24 23:16:07

Resolution: fixed
