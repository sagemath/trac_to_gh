# Issue 4656: power series with zero p-adic coefficients

Issue created by migration from https://trac.sagemath.org/ticket/4656

Original creator: wuthrich

Original creation time: 2008-11-29 21:53:42

Assignee: was

Keywords: padic powerseries

The following _repr_ does not look good to me


```
sage: R.<T> = Qp(5,5)[[]]
sage: O(5^3)*T
0
sage: 1+O(5^3)*T
1 + O(5^5) + O(5^3)*T
```


But that is due to 

```
sage: s= O(5^3)*T
sage: s.is_zero()
True
sage: s == R(0)
False
```


This I consider to be a bug according to the docstring of s.is_zero? saying

```
Return True if self equals self.parent()(0).
```



---

Attachment


---

Comment by wuthrich created at 2009-03-12 19:28:18

Looks good to me and passes all tests. I changed the patch as the orinigally posted patch does not apply against sage 3.4. Thanks!


---

Comment by wuthrich created at 2009-03-12 19:29:14

this patch replaces the previous patch. It is the same, but some changes in page lines in order to make it applicable to sage 3.4


---

Attachment

4656.second.patch causes the following doctest failure:

```
sage -t -long "devel/sage/sage/schemes/elliptic_curves/sha_tate.py"
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage/sage/schemes/elliptic_curves/sha_tate.py", line 299:
    sage: EllipticCurve('1483a1').sha().an_padic(5) # rank 2   (long time)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.4/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[11]>", line 1, in <module>
        EllipticCurve('1483a1').sha().an_padic(Integer(5)) # rank 2   (long time)###line 299:
    sage: EllipticCurve('1483a1').sha().an_padic(5) # rank 2   (long time)
      File "/scratch/mabshoff/sage-3.4.1.alpha0/local/lib/python/site-packages/sage/schemes/elliptic_curves/sha_tate.py", line 418, in an_padic
        raise RuntimeError, "There must be a bug in the supersingular routines for the p-adic BSD."
    RuntimeError: There must be a bug in the supersingular routines for the p-adic BSD.
**********************************************************************
```


Cheers,

Michael


---

Comment by wuthrich created at 2009-03-30 10:18:33

That doctest failure is serious and I have to look into that once #4667 is in.


---

Comment by wuthrich created at 2009-04-21 17:43:51

I looked into the problem. It is not due to a bug in supersingular, but due to the following strange behaviour. This happens to me with the above second patch.

I don't think that is ok :

```
sage: R = Qp(5,10)
sage: RT.<T> = R[[]]
sage: f = O(5^3) + O(5)*T +O(T^2)
sage: f
O(5^3) + O(5)*T + O(T^2)
sage: f[1]
0
```


f is now printed correctly, but the coefficient is not. In fact the precision of the coefficient is lost (and that happens without the patch, too):

```
sage: a= f[1]
sage: a
0
sage: a.precision_absolute()
+Infinity
```



Now, this looks really bad: 

```
sage: v = matrix([[1,0],[0,1]])*vector([1,f])
sage: v
(1 + O(5^10), )
sage: v[1]

sage: type(v[1])
<type 'sage.rings.power_series_poly.PowerSeries_poly'>
```


I must admit that I do not understand what is going on and if this ticket is in fact related to other known issues with p-adic series.


---

Comment by roed created at 2009-04-26 19:44:37

I'm working on p-adic polynomials, and thus on p-adic power series.  If you want a status report on this ticket, let me know.


---

Comment by kedlaya created at 2009-05-20 21:47:16

Replying to [comment:7 roed]:
> I'm working on p-adic polynomials, and thus on p-adic power series.  If you want a status report on this ticket, let me know.

More specifically, this appears to be related to #5075. That ticket will (we hope) be resolved by the omnibus patch on #6084.


---

Comment by wuthrich created at 2010-02-05 23:13:33

Finally, I came back to this. I will attach a rebased patch. This patch solves the problem of this ticket, but the doctest failure in sha_tate.py is still present. But this is caused by another problem. I opened a new ticket #8198 for this. Once this new ticket is solved this ticket here should hopefully be resolved with this patch.


---

Attachment

exported against 4.3.2.alpha1


---

Comment by wuthrich created at 2014-01-29 21:42:37

The proposed solutions at #9457 are solving this here partially and the problems there are the same as here.


---

Comment by kedlaya created at 2017-09-06 03:33:37

Ping. Does anyone know what is going on here?


---

Comment by saraedum created at 2018-07-26 22:28:18

Changing keywords from "padic powerseries" to "padic powerseries padicIMA".


---

Comment by saraedum created at 2018-07-26 22:28:18

Changing component from number theory to padics.
