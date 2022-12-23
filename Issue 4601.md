# Issue 4601: [with patch; needs review] optional magma interface -- fix all broken optional doctests by introducing _magma_init_(self, magma) signature

Issue created by migration from https://trac.sagemath.org/ticket/4601

Original creator: was

Original creation time: 2008-11-24 03:37:26

Assignee: was




---

Attachment

this patch should be applied to sage-3.2.1.alpha0.  it should fix *all* optional doctest failures related to the magma interface!  Note that there is a problem with -only_optional=magma (#4600) so doctesting with that will still show a few false errors.


---

Comment by mabshoff created at 2008-11-24 21:52:20

There is one slight problem here with the doctests:

```
sage -t -long devel/sage/sage/interfaces/magma.py           
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage/sage/interfaces/magma.py", line 1559:
    sage: magma(S.gen_names()[1])
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_52[3]>", line 1, in <module>
        magma(S.gen_names()[Integer(1)])###line 1559:
    sage: magma(S.gen_names()[1])
    NameError: name 'S' is not defined
**********************************************************************
```

But that is obviously easy to fix :)

I have read the patch and while it wouldn't hurt that mhansen for example would take another look everything looks peachy :)

Cheers,

Michael


---

Comment by was created at 2008-11-24 22:11:27

Sorry, I forgot a # optional - magma.  I assume you're going to fix that... or are you requesting I do it?


---

Comment by mabshoff created at 2008-11-24 22:17:38

I am fixing it and I will also put a dummy Magma executable in $PATH before the real one to make sure no missing "#optional" slips by :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-24 23:38:46

Merged in Sage 3.2.1.alpha1 - I will put a reviewers patch for the doctest issue in a second for completeness sake.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-24 23:38:46

Resolution: fixed
