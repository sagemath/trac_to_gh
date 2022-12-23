# Issue 291: strange printing of -1 in multivariate polynomial rings

Issue created by migration from https://trac.sagemath.org/ticket/291

Original creator: ncalexan

Original creation time: 2007-02-24 05:13:52

Assignee: somebody

Keywords: multivariate polynomial ring printing


```
sage: R.<r1, r0, s1, s2, z> = QQ['r1', 'r0', 's1', 's2', 'z']
sage: R(-r1)
-1*r1
```


This is tricky.  This is an issue with stacking rings... how does QQ['x']['y'] tell (QQ['x'](-1))*y to print as '-y'?  I don't know.


---

Comment by ncalexan created at 2007-02-25 09:37:18

Changing assignee from somebody to ncalexan.


---

Comment by ncalexan created at 2007-02-25 09:37:18

The following demonstrates this nicely:


```
sage: K.<a> = NumberField(ZZ['x'].0^2 - 3)

sage: L.<b> = K.extension(K['x'].0^2 - 5)

sage: L
 Extension by x^2 + -5 of the Number Field in a with defining polynomial x^2 - 3
```



---

Comment by was created at 2007-08-18 21:06:29

Changing type from defect to enhancement.


---

Comment by was created at 2007-08-18 21:06:29

nick's xeample is annoying, but it illustrates a completely different problem.

In any case the original multivariate example no longer fails since singular does the printing.
However this example fails:


```
sage: K.<a> = NumberField(ZZ['x'].0^2 - 3) 
sage: R.<r1, r0, s1, s2, z> = K['r1', 'r0', 's1', 's2', 'z']
sage: -r1
(-1)*r1
```


However, since the output is correct, this is not a bug, but an enhancement issue.


---

Comment by mabshoff created at 2007-08-21 13:03:37

The original printing issue has been solved by 2.8.1pre:

```
sage: R.<r1, r0, s1, s2, z> = QQ['r1', 'r0', 's1', 's2', 'z']
sage: R(-r1)
-r1
```

The points made by was in the replies still apply.

Cheers,

Michael


---

Attachment


---

Comment by jbmohler created at 2008-03-20 12:11:28

The attached patch fixes this bug and the associated doc-tests.  As an added bonus, it speeds up the str conversion just a little bit too.

Before patch:

```
sage: R.<x,y,z> = ZZ[]
sage: f=prod([2*g^2-4*g+8 for g in R.gens()])
sage: len(f.monomials())
27
sage: %timeit str(f)
100 loops, best of 3: 2.85 ms per loop
```


After patch:

```
sage: R.<x,y,z> = ZZ[]
sage: f=prod([2*g^2-4*g+8 for g in R.gens()])
sage: len(f.monomials())
27
sage: %timeit str(f)
100 loops, best of 3: 2.43 ms per loop
```



---

Comment by AlexGhitza created at 2008-03-21 22:49:30

Looks good.


---

Comment by mabshoff created at 2008-03-21 23:29:58

Resolution: fixed


---

Comment by mabshoff created at 2008-03-21 23:29:58

Merged in Sage 2.11.alpha1


---

Comment by mabshoff created at 2008-03-22 00:04:03

fixes two trivial doctest failures in const.tex


---

Attachment

Merged trac_291-doctest-failures.patch in Sage 2.11.alpha1 - if anybody does want to review this patch feel free to do so.

Cheers,

Michael
