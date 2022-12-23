# Issue 5112: generic Pollard lambda algorithm

Issue created by migration from https://trac.sagemath.org/ticket/5112

Original creator: ylchapuy

Original creation time: 2009-01-27 20:50:07

Assignee: tbd

CC:  mraum

Following #5098, here is a generic implementation of Pollard lambda algorithm.
There is probably still lots of room for optimization, but it works.


---

Comment by ylchapuy created at 2009-01-27 20:53:54

patch needs #5098 to be applied first.


---

Comment by ylchapuy created at 2009-01-29 12:29:52

patch updated. should be applied after #5098 trac-5098-alpha2based.patch


---

Comment by cremona created at 2009-02-01 15:33:12

Patch applies fine to 3.3.alpha2 + (from #5098) trac-5098-alpha2based.patch and tests pass.  Code looks good and docstring & doctests are fine.

I think it is excellent to have more of these generic algorithms available.  Pass!


---

Comment by mabshoff created at 2009-02-01 15:36:09

John,

please make sure not to sneak extra spaces in between positive and review since the reports do not pick up such tickets. The reports should be fixed to ignore extra white space, but until then ....

Cheers,

Michael


---

Attachment

patch updated after trac-5098-doctest.patch


---

Comment by mabshoff created at 2009-02-11 10:49:30

Hi Yann,

how large are the changes? If it is "just" a rebase with no or minimal functional changes (i.e. some exception changed) the positive review can stand.

Cheers,

Michael


---

Comment by ylchapuy created at 2009-02-11 11:39:21

yes, it's indeed strictly a rebase. I just wanted to be sure the patch applies cleanly.


---

Comment by mabshoff created at 2009-02-14 03:00:24

This is 3.3 material.

Cheers,

Michael


---

Comment by was created at 2009-02-15 08:07:26

SECOND REVIEW:

 * Line 1 of docstring: "Pollard Lambda algorithm for computing discrete logarithm."
It should be "Pollard Lambda algorithm for computing discrete logarithms." or "Pollard Lambda algorithm for computing the discrete logarithm."

 * The docstring has a typo in line 2: "usefull" 

 * The sections in the docstring should have space between them (e.g., a blank line before EXAMPLES:).  This can be ignored because of the ReST/Sphinx transition, which will probably change that. 

 * I noticed this line

```
N = width.isqrt()+1 
```

If width is a Python int then that will fail.  This is easy to trigger and will accidentally happen in library code easily:

```
sage: F.<a> = GF(2^63) 
sage: g = F.gen()
sage: pollard_lambda(g, g^1234567, (1200000,1250000)) 
1234567
sage: pollard_lambda(g, g^1234567, (int(1200000), int(1250000))) 
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/space/wstein/sage-3.3.rc0/<ipython console> in <module>()

/space/wstein/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/groups/generic.pyc in pollard_lambda(base, a, bounds, ord, operation, hash_function, memory)
    649 
    650     width = ub-lb
--> 651     N = width.isqrt()+1
    652 
    653     M = dict()

AttributeError: 'int' object has no attribute 'isqrt'
```


  * the doctests are insufficient.  The function signature is

```
def pollard_lambda(base, a, bounds, ord=None, operation='*', hash_function=hash, memory=None): 
```

At a bare minimum, there must be doctests that test use of all the inputs to the function.


---

Comment by mabshoff created at 2009-02-16 05:00:45

I am cleaning up the 3.3 milestone. If a patch with positive review is put up to this ticket on time it might make it into 3.3.

Cheers,

Michael


---

Comment by ylchapuy created at 2009-12-14 18:43:15

It should be quite similar to #5098.


---

Comment by ylchapuy created at 2009-12-14 18:43:15

Changing status from needs_work to needs_review.


---

Attachment

based on 4.3.alpha1 + #5098


---

Comment by mraum created at 2009-12-15 09:26:17

Good point, it is similar.

According to Micheal's comment, I added one doctest, testing the hash_function, too. Now, I think it's good.


---

Comment by mraum created at 2009-12-15 09:26:17

Changing status from needs_review to positive_review.


---

Attachment


---

Comment by mhansen created at 2009-12-15 16:12:54

Resolution: fixed
