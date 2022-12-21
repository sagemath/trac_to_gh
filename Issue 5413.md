# Issue 5413: [with patch, needs review] deprecate substitution via __call__ w/ unnamed arguments

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2009-03-01 18:00:29

Assignee: burcin

CC:  jason

As discussed on sage-devel here: http://groups.google.com/group/sage-devel/browse_thread/thread/b1a03f8fc8ae8fcd/553773d7ba600ae7#553773d7ba600ae7

I added deprecation warnings to the four affected __call__ functions (two for symbolic values, one for equations, one for matrices), and fixed almost all the warnings in all the doctests other than the doctests specifically for those __call__ methods.

There's one set of warnings that I didn't figure out how to fix (in piecewise.py), so I just added the warning to the expected output for now.


---

Comment by mabshoff created at 2009-03-02 06:51:43

Two trivial doctest failures:

```
sage -t -long devel/sage/doc/en/constructions/calculus.rst # 1 doctests failed
sage -t -long devel/sage/doc/fr/tutorial/tour_algebra.rst # 1 doctests failed
```


Cheers,

Michael


---

Attachment

Oops, forgot to doctest the documentation.  I've replaced my original patch with a new one that also fixes these two doctest failures.


---

Comment by jason created at 2009-03-13 19:17:29

This is an (email) reminder to myself to review this to get it in.


---

Comment by jason created at 2009-03-13 19:29:24

This ticket probably also affects #5093.


---

Comment by burcin created at 2009-03-14 12:08:38

Thanks for working on this Carl.

I only read the patch, didn't test it yet. Explicitly having to use .function() in two places bothers me:

 * for each component of Piecewise
 * in the call to generate_plot_points

Perhaps we should modify these to handle non function arguments more gracefully after this change. 

I understand that this might require a new syntax to construct Piecewise objects. One option is to add a new parameter, which includes an ordered list of variables. E.g.,


```
    sage: Piecewise([[(0,1),x^2],[(1,2),5-x^2]] ,[x])
```

or

```
    sage: f = Piecewise([This is the Trac macro ** that was inherited from the migration called with arguments (-1,1),1/2+x-x^3 + y)](https://trac.sagemath.org/wiki/WikiMacros#-macro),[x,y])
```


Comments?


---

Comment by jason created at 2009-03-14 12:21:19

The above comment for Piecewise would probably also apply to symbolic matrices and vectors, right? (well, at least, as soon as symbolic vectors are callable, anyway).  I think that Burcin's proposal is okay, but doesn't extend very well to matrices and vectors, since I'd hate to mess up the standard matrix/vector constructors.  I'm don't know a better way to extend this to matrices and vectors, though.  Maybe we ought to just deprecate calling a symbolic matrix without keyword arguments, and just implement the callable symbolic vector with the same restrictions.


---

Comment by cwitty created at 2009-03-14 13:22:11

The patch already does deprecate calling a symbolic matrix without keyword arguments.


---

Comment by jason created at 2009-03-14 13:38:15

Yes.  I thought Burcin's comment was about a syntax to avoid the .function() call.  That's what I was commenting on.


---

Comment by cwitty created at 2009-03-16 21:22:25

After discussions on IRC and sage-devel (http://groups.google.com/group/sage-devel/browse_thread/thread/97cdf80edb089481/73e8e6659c09e1d9#73e8e6659c09e1d9) we've decided on a much more extensive deprecation scheme.  So it's not worth reviewing the current patch.  (I should have a new patch within a few days.)


---

Attachment

I've posted a patch that implements the more extensive deprecation described here: http://groups.google.com/group/sage-devel/browse_thread/thread/97cdf80edb089481#

The patch now depends on #5093.

Apply only the second patch.


---

Comment by jason created at 2009-03-25 01:15:38

This is really odd:


```
[19:53] <jason> sage: g(x)=sin
[19:53] <jason> sage: g(3)
[19:53] <jason> sin(3)
[19:53] <jason> sage: g(x)=sin+x
[19:53] <jason> sage: g(3)
[19:53] <jason> sin + 3
[19:54] <jason> but
[19:54] <jason> sage: g(x)=sin+cos; g(3)
[19:54] <jason> sin + cos
```



---

Comment by burcin created at 2009-03-25 10:35:11

Jason, I get the same behavior without Carl's patch on Sage-3.4. I suggest moving that to a separate ticket. We could also argue if that is valid syntax there.

I give a positive review to this. It would be good to get this in an alpha and let more people play with it. Thanks again Carl.

Cheers,
Burcin


---

Comment by burcin created at 2009-03-25 10:58:58

comment:12 is now #5607.


---

Comment by jason created at 2009-03-25 14:37:20

I agree that we should get this into the alpha so it gets wider exposure.  (providing doctests pass) positive review from me too.


---

Comment by mabshoff created at 2009-03-25 23:12:25

There is one tiny doctest issue left - at least in my merge tree :)

```
sage -t -long "devel/sage/doc/en/constructions/calculus.rst"
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage/doc/en/constructions/calculus.rst", line 222:
    sage: f.integral()
Expected:
    Piecewise defined function with 2 parts, [[(0, 1), x^3/3], [(1, 2), (15*x - x^3)/3 - 13/3]]
Got:
    Piecewise defined function with 2 parts, [[(0, 1), x |--> x^3/3], [(1, 2), x |--> (15*x - x^3)/3 - 13/3]]
**********************************************************************
1 items had failures:
   1 of   9 in __main__.example_8
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/sage-3.4.1.alpha0/tmp/.doctest_calculus.py
	 [4.3 s]
exit code: 1024
```


I am fixing this with a reviewer patch.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2009-03-25 23:31:14

Resolution: fixed


---

Comment by mabshoff created at 2009-03-25 23:31:14

Merged trac5413-deprecate-symbolic-unnamed-call.patch and trac_5413-reviewer.patch in Sage 3.4.1.alpha0.

Cheers,

Michael
