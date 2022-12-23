# Issue 9430: Update SageNB to version 0.8.1

Issue created by migration from https://trac.sagemath.org/ticket/9430

Original creator: timdumol

Original creation time: 2010-07-05 11:30:03

Assignee: jason, was

CC:  acleone was mpatel leif

Download at: http://sage.math.washington.edu/home/timdumol/sagenb-0.8.1.spkg

Version 0.8.1 solves the following tickets:

#9294, #8760, #8758, #8686, #7633, #7418, #7379

Please merge the Sage main library patch at #7379 when including this.


---

Comment by timdumol created at 2010-07-05 11:30:39

Changing status from new to needs_review.


---

Comment by leif created at 2010-07-07 13:11:09

I can yet say I get doctest errors related to this spkg (with Sage 4.5.alpha4), but the complete test will take some hours... (i.e. more to come later).


---

Comment by leif created at 2010-07-07 14:09:33

Changing status from needs_review to needs_work.


---

Comment by leif created at 2010-07-07 14:09:33

Doctest error preview (`ptestlong` still running):

```
sage -t  -long local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/notebook/interact.py
**********************************************************************
File "/home/leif/sage-4.5.alpha4/local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/notebook/interact.py", line 2205:
    sage: @interact
    def _(n=(Integer(10),Integer(100),Integer(1)), auto_update=False):
        show(factor(x**n - Integer(1)))
Exception raised:
    Traceback (most recent call last):
      File "/home/leif/sage-4.5.alpha4/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/leif/sage-4.5.alpha4/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/leif/sage-4.5.alpha4/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_99[9]>", line 2, in <module>
        def _(n=(Integer(10),Integer(100),Integer(1)), auto_update=False):
      File "/home/leif/sage-4.5.alpha4/local/lib/python/site-packages/sage/misc/misc.py", line 2666, in my_wrap
        return func(*args)
      File "/home/leif/sage-4.5.alpha4/local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/notebook/interact.py", line 2519, in interact
        html(C.render())
      File "/home/leif/sage-4.5.alpha4/local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/notebook/interact.py", line 2058, in render
        s = "%s%s"%(self.render_controls(), self.render_output())
      File "/home/leif/sage-4.5.alpha4/local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/notebook/interact.py", line 1994, in render_controls
        layout = [[c.var()] for c in self.__controls]
    AttributeError: 'UpdateButton' object has no attribute 'var'
**********************************************************************
1 items had failures:
   1 of  34 in __main__.example_99
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/leif/.sage//tmp/.doctest_interact.py
	 [6.3 s]
```

(Ubuntu 9.04 x86, P4 Prescott, gcc 4.3.3, sequential build)

With vanilla Sage 4.5.*alpha3*, all doctests passed on that system (same with alpha4 on Ubuntu 9.04 x86_64, gcc 4.5.0; `ptestlong`).

I've copied `sagenb-0.8.1.spkg` and `zodb3-3.7.0.p4.spkg` (#9436) to `spkg/standard`, built Sage, applied #7379 (Sage library patch for sagenb 0.8.1), run `./sage -b`, rebuilt the documentation and then started the test.

I blindly guess there won't come up further errors originating from the new sagenb package.


---

Comment by timdumol created at 2010-07-07 15:14:20

I forgot to put in the patch for that. New version now at the same url.

To test sagenb packages, all you need to do is install it via `sage -f sagenb-0.8.1.spkg` and run `sage -t -sagenb`.


---

Comment by timdumol created at 2010-07-07 15:14:20

Changing status from needs_work to needs_review.


---

Comment by leif created at 2010-07-07 17:14:51

Replying to [comment:4 leif]:
> With vanilla Sage 4.5.*alpha3*, all doctests passed on that system (same with alpha4 on Ubuntu 9.04 x86_64, gcc 4.5.0; `ptestlong`).

Not _really_ vanilla, actually alpha3 with #9432 (fixing a single doctest error, unrelated to this ticket, merged in alpha4) passed all tests.


---

Comment by leif created at 2010-07-07 17:27:24

I don't know if this is sufficient, but after forcing reinstallation of Tim's corrected SageNB package, `./sage -t -sagenb` and `./sage -t -long -sagenb` (there seem to be no `long` tests) passed all tests, especially the (only) one that previously failed.

So I can give it a *positive review*, unless somebody tells me what further tests should be performed.

I'll test it on Ubuntu 9.04 x86_64 tomorrow.


---

Comment by leif created at 2010-07-07 18:28:31

Rebuilding the HTML documentation also succeeded (except for the missing `conf.py` in `thematic_tutorials`, which is unrelated).


---

Comment by leif created at 2010-07-08 16:09:41

Replying to [comment:7 leif]:
> I'll test it on Ubuntu 9.04 x86_64 tomorrow.

I've successfully built Sage 4.5.alpha4 with SageNB 0.8.1 and zodb3 3.7.0.p4 (#9436), both sequentially and in parallel (`SAGE_PARALLEL_SPKG_BUILD="yes", MAKE="make -j4"`).

No downloads during install, HTML documentation builds (except missing `conf.py` in `thematic_tutorials`), and all long tests passed (`make ptestlong`).

All builds/tests performed independently, i.e. from scratch.

Leaving as "needs review" since IMHO tests by others on other platforms should follow.


---

Comment by rlm created at 2010-07-08 19:52:12

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-07-08 19:52:12

Moving to positive review. I'm about to release rc0, so this will get plenty of testing on all platforms.


---

Comment by rlm created at 2010-07-08 19:53:21

Resolution: fixed
