# Issue 1046: speed regression in mq.SR.polynomial_system()  due to new coercion code?

Issue created by migration from https://trac.sagemath.org/ticket/1046

Original creator: malb

Original creation time: 2007-10-31 23:57:30

Assignee: robertwb

Try to run this code:


```
sage: sr = mq.SR(4,4,4,8, aes_mode=True, star=True, allow_zero_inversions=True)
sage: F,s = sr.polynomial_system()
```


and wait for it to terminate (~17s on my 2.33Ghz system) in a fresh SAGE session. The second run takes only 2s.


I profiled this with hotshot like this:


```
sage: import hotshot
sage: filename = "pythongrind.prof"
sage: prof = hotshot.Profile(filename, lineevents=1)
sage: prof.run("sr.polynomial_system()")
<hotshot.Profile instance at 0x414c11ec>
sage: prof.close()
```


and converted the result to cachegrind/calltree format


```
hotshot2calltree -o cachegrind.out.42 pythongrind.prof
```


to inspect the result with kcachegrind. Apparently, both `sr.round_polynomials` and `sr.key_schedule_polynomials` call `MatrixSpace.get_action_impl` which in turn calls `pushout` which calls `construction_tower`. `construction_tower` creates *7164* polynomial rings and this ring construction takes up 85% of the entire runtime. 

So apparently the most time is spent in coercion (which also explains the better runtime for the second run) and I believe this is due to a bug.



---

Comment by malb created at 2007-11-01 11:39:19

I tracked this down a bit more:


```
sage: n = 296
sage: P = PolynomialRing(GF(2),n,'x')
sage: v = vector(P,100)
sage: A = matrix(P,100,100)

# this time depends on $n$ above

sage: %time _ = A*v
CPU times: user 0.53 s, sys: 0.00 s, total: 0.53 s
Wall time: 0.53

sage: %time _ = A*v
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
```



---

Comment by malb created at 2007-11-01 11:50:25

Some more hints:

First try:


```
sage: n = 296
sage: P = PolynomialRing(GF(2),n,'x')
sage: v = matrix(P,100,1)
sage: A = matrix(P,100,100)
sage: time _ = A*v
CPU times: user 0.69 s, sys: 0.03 s, total: 0.72 s
Wall time: 0.75
```


then restart Sage and try:


```
sage: n = 296
sage: P = PolynomialRing(GF(2),n,'x')
sage: v = matrix(P,100,1)
sage: A = matrix(P,100,100)
sage: time _ = A._multiply_classical(v)
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01
```



---

Comment by robertwb created at 2007-11-09 22:08:47

I am pretty sure this is because the coercion model tries to compute the construction tower and "pushout" one-variable at a time. This is to support stuff like


```
sage: ZZ['x,y,z'].gen(1) + QQ['y'].gen(0)
2*y
```


Of course it is bad when you have multi-variate polynomials in 100's of variables...


---

Comment by robertwb created at 2007-11-26 20:48:28

Changing status from new to assigned.


---

Comment by robertwb created at 2007-11-26 20:48:28

This has been fixed--but it may be difficult to pull out of the massive coercion changes that David Roe and I are in the middle of doing. 

See #1283


---

Comment by malb created at 2008-08-18 16:13:40

This bug is still present in Sage 3.1.1.:


```
sage: sr = mq.SR(4,4,4,8, aes_mode=True, star=True, allow_zero_inversions=True)
sage: time F,s = sr.polynomial_system()
CPU times: user 53.67 s, sys: 1.30 s, total: 54.97 s
Wall time: 54.94 s
sage: sr = mq.SR(4,4,4,8, aes_mode=True, star=True, allow_zero_inversions=True)
sage: time F,s = sr.polynomial_system()
CPU times: user 8.53 s, sys: 0.29 s, total: 8.82 s
Wall time: 8.81 s
```


The times were obtained on sage.math.


---

Comment by robertwb created at 2008-08-18 16:59:22

This is because the whole of the coercion branch was not merged over, just the core. I'll put merging this in up on the priority queue now that 3.1 has the underlying model.


---

Attachment

The attached patch should resolve this issue.


---

Comment by mabshoff created at 2008-10-17 20:30:48

It improves the doctest run from 1100 seconds to

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha0$ ./sage -t -long devel/sage/sage/crypto/mq/sr.py
sage -t -long devel/sage/sage/crypto/mq/sr.py                
	 [684.8 s]
```

I am doctesting with this patch applied. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-17 21:03:16

Robert,

I guess the patch still needs some work :(

```
	sage -t -long devel/sage/sage/structure/parent.pyx # 1 doctests failed
	sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_modular_symbols.py # 8 doctests failed
	sage -t -long devel/sage/sage/schemes/elliptic_curves/padic_lseries.py # 37 doctests failed
	sage -t -long devel/sage/sage/schemes/elliptic_curves/padics.py # 10 doctests failed
	sage -t -long devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 9 doctests failed
	sage -t -long devel/sage/sage/modules/free_quadratic_module.py # 3 doctests failed
	sage -t -long devel/sage/sage/modules/free_module.py # 6 doctests failed
	sage -t -long devel/sage/sage/modular/modsym/space.py # 4 doctests failed
	sage -t -long devel/sage/sage/modular/modsym/ambient.py # 2 doctests failed
	sage -t -long devel/sage/sage/modular/abvar/torsion_subgroup.py # 5 doctests failed
	sage -t -long devel/sage/sage/modular/abvar/cuspidal_subgroup.py # 4 doctests failed
	sage -t -long devel/sage/sage/modular/abvar/finite_subgroup.py # 21 doctests failed
	sage -t -long devel/sage/sage/modular/abvar/morphism.py # 2 doctests failed
	sage -t -long devel/sage/sage/modular/abvar/abvar.py # 10 doctests failed
	sage -t -long devel/sage/sage/matrix/matrix_real_double_dense.pyx # 3 doctests failed
```

I hope you had a good flight home from SD 10.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-17 21:05:25

One more data point to the above remark malb did. With the patch applied:

```
sage: n = 296
sage: P = PolynomialRing(GF(2),n,'x')
sage: v = vector(P,100)
sage: A = matrix(P,100,100)
sage: %time _ = A*v
CPU times: user 0.04 s, sys: 0.00 s, total: 0.04 s
Wall time: 0.04 s
sage: %time _ = A*v
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
```

So there is more than an order of magnitude improvement here :)

Cheers,

Michael


---

Comment by robertwb created at 2008-10-18 17:11:40

Oh, I didn't test -t -long. I'll look into that.


---

Attachment


---

Comment by robertwb created at 2008-10-21 17:35:49

I figured out what it was, due to some re-factoring a line got lost and that was raising a type error in the coercion discovery. Fixed.


---

Comment by mabshoff created at 2008-10-25 22:03:26

Doctests pass, mhansen has also looked over the patch and has given it a positive review pending doctests in IRC :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-25 22:04:06

Resolution: fixed


---

Comment by mabshoff created at 2008-10-25 22:04:06

Merged in Sage 3.2.alpha1


---

Comment by mhansen created at 2008-10-25 22:05:31

+1 from me.
