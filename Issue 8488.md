# Issue 8488: Add support for @interact to the Sage library and module for a library of interacts

Issue created by migration from https://trac.sagemath.org/ticket/8488

Original creator: was

Original creation time: 2010-03-10 13:16:54

Assignee: itolkov

CC:  mhampton




---

Comment by was created at 2010-03-10 13:22:48

Changing status from new to needs_review.


---

Attachment


---

Comment by jason created at 2010-03-10 18:43:47

Changing status from needs_review to needs_work.


---

Comment by jason created at 2010-03-10 18:43:47

I think it would be better to use the `@`wraps decorator in python, which automatically copies the documentation, etc.  Also, the source inspection probably won't work here (I haven't checked, though).  We should spruce up this decorator to follow the pattern in sage/plot/misc.py (see the `@`options or `@`suboptions decorator classes).


---

Comment by jason created at 2010-03-10 18:45:04

or even better, we should make a `@`wrap_sage decorator which does the same thing as `@`wraps and additionally does:


```
        from sage.misc.sageinspect import sage_getsource
        wrapper._sage_src_ = lambda: sage_getsource(func)
```


like in the sage/plot/misc.py files.


---

Comment by jason created at 2010-03-10 20:16:22

I just attached a patch which implements a "sage_wraps" decorator which mirrors the functools wraps decorator, but also adds the sage-specific _sage_src_ attribute, so that `interacts.demo??` works.

This is still "needs work", since the sage_wraps function needs some doctests.

We can now simplify the code in sage/plot/misc.py and a few other places that call the `@`wraps decorator using `@`sage_wraps.


---

Comment by jason created at 2010-03-10 20:26:17

Note that there is a bug in the ReST formatting.  After applying both patches above, `interacts.demo??` gives output that is all messed up since apparently the formatting engine doesn't deal well with the single newlines that _sage_src_() returns.  I've run out of time to try to track this down and see if it is a bug in the introspection or in the file or what.


---

Comment by jason created at 2010-03-10 20:29:14

Also, I don't think we should import library_interact into the interacts namespace.  I think interacts.<tab> should just give a list of interacts (in fact, I think it should be broken down a bit further, so that interacts.calculus.<tab> gives calculus interacts, etc.)  Note that because of wonderful namespaces, the same interact could be imported into interacts.calculus and interacts.linear_algebra, for example.


---

Comment by jason created at 2010-03-11 01:50:05

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-03-11 01:51:50

Changing assignee from itolkov to jason.


---

Comment by jason created at 2010-03-11 01:51:50

Oops, I deleted the title, instead of adding a comment, apparently.

Okay, William or Marshall, the ball's back in your court to review my patch.


---

Comment by was created at 2010-03-11 04:54:19

REVIEW:

  * very nice using the python wrapping stuff, and making source code introspection work, in theory!

  * In practice, source code introspection does not work, though this is due to a lazy assumption *I* made I think when implementing interact in the notebook, namely I think when the notebook server sees "`@`interact" in the output, it does something funny with formatting.  Anyway, if you try:

```
interacts.calculus.taylor_polynomial??
```

in a cell then shift-enter, you'll see the source is all on one long line, which isn't good.  That said, fixing this shouldn't be part of this patch, since it's a very different issue in the sage notebook itself, and maybe quite tricky to deal with.

   * Important. Try this in an input cell:

```
interacts.calculus.[tab]
```

Instead of getting *one* thing, you get 15.  This *has* to be fixed. 

   * Otherwise, I'm happy with this patch.


---

Comment by was created at 2010-03-11 04:54:19

Changing status from needs_review to needs_work.


---

Comment by jason created at 2010-03-11 05:31:19

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-03-11 05:31:19

Replying to [comment:11 was]:

> REVIEW: * very nice using the python wrapping stuff, and making source code introspection work, in theory! * In practice, source code introspection does not work, though this is due to a lazy assumption *I* made I think when implementing interact in the notebook, namely I think when the notebook server sees "`@`interact" in the output, it does something funny with formatting.  Anyway, if you try: ` interacts.calculus.taylor_polynomial?? ` in a cell then shift-enter, you'll see the source is all on one long line, which isn't good.  That said, fixing this shouldn't be part of this patch, since it's a very different issue in the sage notebook itself, and maybe quite tricky to deal with.

Ah, that makes sense.  I saw this, and even started writing a ticket for it, but I couldn't reproduce it with anything besides the interact stuff (see my comment above about ReST formatting), and then I ran out of time.

I'm attaching a new patch which takes care of the namespace issue you mentioned.  Basically, I lump everything into a library file, and then just import into calculus.py the actual interact. I'm sure there's a fancy object we could make that would nicely categorize everything, but this quick solution takes advantage of the nice namespace framework we already have.


---

Attachment

apply on top of previous patch


---

Comment by jason created at 2010-03-11 15:55:52

Replying to [comment:11 was]:

>    * Otherwise, I'm happy with this patch. 

FYI, I'm leaving it to you to set "positive review" after my last patch, if you're still happy.


---

Comment by was created at 2010-03-27 17:45:02

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-16 19:59:52

I applied both patches to 4.3.5 and I'm getting doctest failures:

```
sage -t  devel/sage/sage/interacts/library.py
**********************************************************************
File "/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/devel/sage-new/sage/interacts/library.py", line 18:
    sage: @interacts.decorator.library_interact
    def f(n=Integer(5)): print n
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[2]>", line 1, in <module>
        @interacts.decorator.library_interact###line 18:
    sage: @interacts.decorator.library_interact
    AttributeError: 'module' object has no attribute 'decorator'
**********************************************************************
File "/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/devel/sage-new/sage/interacts/library.py", line 21:
    sage: f()  # an interact appears
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[3]>", line 1, in <module>
        f()  # an interact appears###line 21:
    sage: f()  # an interact appears
    NameError: name 'f' is not defined
**********************************************************************
File "/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/devel/sage-new/sage/interacts/library.py", line 45:
    sage: interacts.decorator.demo()
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/palmieri/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[2]>", line 1, in <module>
        interacts.decorator.demo()###line 45:
    sage: interacts.decorator.demo()
    AttributeError: 'module' object has no attribute 'decorator'
**********************************************************************
2 items had failures:
   2 of   4 in __main__.example_1
   1 of   3 in __main__.example_2
***Test Failed*** 3 failures.
```



---

Comment by jhpalmieri created at 2010-04-16 19:59:52

Changing status from positive_review to needs_work.


---

Comment by was created at 2010-04-18 00:31:59

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by was created at 2010-04-18 00:33:27

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-18 18:59:53

Changing status from positive_review to needs_work.


---

Comment by jhpalmieri created at 2010-04-18 18:59:53

When I apply this, I get a new doctest failure:

```
**********************************************************************
File "/Applications/sage_builds/sage-4.4.alpha0/devel/sage-new/sage/symbolic/ring.pyx", line 443:
    sage: SR.symbol() # temporary variable
Expected:
    symbol160
Got:
    symbol162
**********************************************************************
```

I don't know why these patches cause this file to file.  Can we just change "160" to "162"?


---

Comment by was created at 2010-04-18 22:04:48

Replying to [comment:18 jhpalmieri]:
> When I apply this, I get a new doctest failure:
> {{{
> **********************************************************************
> File "/Applications/sage_builds/sage-4.4.alpha0/devel/sage-new/sage/symbolic/ring.pyx", line 443:
>     sage: SR.symbol() # temporary variable
> Expected:
>     symbol160
> Got:
>     symbol162
> **********************************************************************
> }}}
> I don't know why these patches cause this file to file.  Can we just change "160" to "162"?

Yes.  It's just some internal counter.   That's a stupid doctest though, since an unrelated change anywhere else in Sage could break it.  Can you change the output to

   symbol...

?

William


---

Comment by jhpalmieri created at 2010-04-19 00:07:00

Okay, here's a patch.


---

Comment by jhpalmieri created at 2010-04-19 00:07:00

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by jhpalmieri created at 2010-04-19 05:09:40

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-19 05:10:09

(I just got around now to applying the patch and running doctests.)


---

Comment by jhpalmieri created at 2010-04-19 05:22:30

Merged into 4.4.alpha1:
 - trac_8488.patch
 - trac-8488-sage_wrap_decorator.patch
 - trac_8488-part3.patch
 - trac_8488-part4.patch


---

Comment by jhpalmieri created at 2010-04-19 05:22:30

Resolution: fixed
