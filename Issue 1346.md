# Issue 1346: fpLLL doctests don't test fpLLL

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-12-01 02:51:13

Assignee: was

If the next version of fpLLL started returning bogus answers, the doctests in sage/libs/fplll/fplll.pyx would still pass, because they use random input and output.

There should be at least some doctests where fplll is run on constant input with a known result.


---

Comment by mabshoff created at 2007-12-06 13:50:42

Bill Hart wrote in http://groups.google.com/group/sage-devel/t/e54f8dd59f799354

```
Someone noted in ticket 1346 that the fpLLL doctests use random data,
and said that we should do tests with fixed data which return a known
result.

I don't agree with this. There is no reason why LLL should return the
same result from implementation to implementation. fpLLL may well
change the lattices returned and this would break any fixed doctests,
but would not necessarily constitute a bug in fpLLL.

Instead, the tests should generate random matrices of various kinds
using the programs provided with fpLLL for this purpose, then is
should reduce the lattices using the SAGE wrapping of fpLLL. Then it
should test that the lattices really have been reduced, using whatever
test you like. The one distributed with fpLLL for this purpose should
be sufficient, though one written in SAGE to directly test the Lovasz
condition or some such thing would be better.

I don't know how the doctests work at the moment, but I don't think
the defect as reported really is a defect.
```


Cheers,

Michael


---

Comment by was created at 2008-04-05 20:49:32


```
13:48 < wstein-2813> re: #1346 -- do we have an is_LLL_reduced function anywhere yet?
13:49 < wstein-2813> If so, we could just use that on the output of LLL functions.
13:49 < wstein-2813> That would be the way to solve the problem (but keep the random output).
```



---

Comment by cwitty created at 2008-08-23 19:22:51

William's suggestion above is not sufficient to actually test fpLLL; at least we should also test that the input and output matrices generate the same lattice.


---

Attachment


---

Comment by malb created at 2008-10-06 13:09:58

Damien Stehlé suggested three ways to check for LLL reduction off-list:


```
In order to checking the LLL-reducedness of a basis, I have three ideas.

1) One could think that  LLL on a LLL-reduced basis should not do anything. So one idea would be 
to run another (reliable) LLL routine on the output, and see if it actually does nothing. That 
should be easy in SAGE, since you have an easy access to several LLLs. You have to pay attention 
to the LLL parameters (delta and eta), which could be annoying since eta is not specified in NTL
(though it is >1/2).
You also have to pay attention to the precision if you use fp-arithmetic (it should be high 
enough). In any case,  it is going to be dirty and provide bugs or inconsistences between the 
different codes. And on top of it, a LLL may actually do something on an already-reduced basis,
as long as it provides another reduced basis. Due to fp-errors, this may actually occur.
Furthermore, there are portability issues. fplll is not portable between 32 bit and 64 bit 
machine (for efficiency reasons). I know inputs for which it answers something
different on 32 and 64 bit machines.

2) Compute the Gram-Schmidt Orthogonalisation with rational arithmetic and check if the LLL 
conditions are satisfied. Easy, but slow on large examples.

3) Use Gilles Villard's paper that tries to do the same as 2), but with fp-arithmetic.
Certification of the QR factor R and of lattice basis reducedness. ISSAC 2007: 361-368
```


I do 2) in the above patch.


---

Comment by wjp created at 2008-10-10 20:17:51

Second patch attached. It marks the output of LLL in the doctests from malb's patch as random, and checks the LLL condition of those that weren't yet. Also fixes a typo in the LLL docstring, and fixes the LLL reducedness tests in is_LLL_reduced(), I think.


---

Comment by malb created at 2008-10-10 20:25:32

I see one issue with the second patch: It recomputes the norms twice as much as needed, this is why I introduced the norms list.


---

Comment by wjp created at 2008-10-10 21:07:05

Oh, yes, you're right. I forgot for a moment that b_i^* and b_{i+1}^* are orthogonal so you can indeed rewrite the condition like you did. Sorry.


---

Attachment

I attached a new patch without that change to the norm check.


---

Comment by mabshoff created at 2008-10-11 06:40:44

Resolution: fixed


---

Comment by mabshoff created at 2008-10-11 06:40:44

Merged in Sage 3.1.3.rc0
