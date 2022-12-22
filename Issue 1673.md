# Issue 1673: Failure of coercion between rationals and F_p

Issue created by migration from Trac.

Original creator: ljpk

Original creation time: 2008-01-03 19:18:16

Assignee: malb

If one has a power series over QQ one can coerce it to have coefficients in FF_p using %:

`delta=CuspForms(1,12).0.q_expansion(30)`

`f=CuspForms(11,2).0.q_expansion(30)`

`f % 11`

However, one cannot subtract a series with coefficients in FF_p from a series with coefficients in QQ; the coercion doesn't work:


```
Exception (click to the left for traceback):
...
TypeError: unsupported operand parent(s) for '-': 'Power Series Ring in q over Rational Field' and 'Power Series Ring in q over Ring of integers modulo 11'Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/server2/sage_notebook/worksheets/ljpk/4/code/7.py", line 4, in <module>
    f - delta % Integer(11)
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sympy/plotting/", line 1, in <module>
    
  File "element.pyx", line 785, in sage.structure.element.ModuleElement.__sub__
  File "coerce.pyx", line 272, in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c
TypeError: unsupported operand parent(s) for '-': 'Power Series Ring in q over Rational Field' and 'Power Series Ring in q over Ring of integers modulo 11' }}}


---

Comment by dmharvey created at 2008-01-03 20:23:35

There is no automatic coercion from QQ to Fp because there is no natural map (in the mathematical sense). If you want to subtract an element of QQ from an element of Fp, you have to explicitly coerce from QQ to Fp first. Similarly there is no canonical map from QQ[x] to Fp[x], so the coercion error above is correct.

If anything I think the behaviour where you can do f % 11 and get an element of Fp[x] is incorrect. For example if you take an integer A and compute A % 11, you get an integer, not an element of F11.


---

Comment by was created at 2008-01-04 08:21:54

Resolution: invalid


---

Comment by was created at 2008-01-04 08:24:38

> If anything I think the behaviour where you can do f % 11 and get an element of Fp[x] > is incorrect. For example if you take an integer A and compute A % 11, you get an 
> integer, not an element of F11.

I strongly agree with this.  However, it might be reasonable to have `Mod(f,11)`
do what f%11 currently does.  

Right now, use f.change_ring


```
sage: R.<q> = QQ[[]]
sage: f = 1 + 19*q^2 + q^4
sage: f.change_ring(GF(13))
1 + 6*q^2 + q^4
```

