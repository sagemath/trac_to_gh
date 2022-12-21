# Issue 7478: Remove "..." in the output of TestSuite.

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2009-11-17 08:03:23

Assignee: tbd

CC:  sage-combinat

Keywords: TestSuite

When testing something in verbose mode the typical output of sage is:

```
   sage: P = Sets().example("inherits")
   sage: TestSuite(P).run(verbose=True)
   running ._test_an_element() ... done
   running ._test_element_pickling() ... done
   running ._test_not_implemented_methods() ... done
   running ._test_pickling() ... done
   running ._test_some_elements() ... done
```

And there is some risks that the "..." match something they should'nt I change them to ".."

Cheers,

Florent


---

Comment by hivert created at 2009-11-17 08:03:55

Changing assignee from tbd to hivert.


---

Comment by nthiery created at 2009-11-18 15:18:51

Changing status from new to needs_review.


---

Comment by nthiery created at 2009-11-18 15:19:25

Changing component from misc to doctest.


---

Comment by nthiery created at 2009-11-18 15:19:25

Changing type from defect to enhancement.


---

Comment by mhansen created at 2009-11-18 18:06:55

There is a spurious "only" to "o.." change in sets_cat.py.


---

Comment by nthiery created at 2009-11-18 18:35:33

Replying to [comment:4 mhansen]:
> There is a spurious "only" to "o.." change in sets_cat.py.

Good spot :-)

I had already found a couple, and thought I had done a systematic search.

Fixed in the newly uploaded patch.


---

Comment by nthiery created at 2009-11-18 20:15:59

Updated patch fix a doctest I had missed.


---

Comment by hivert created at 2009-11-18 21:28:29

There are still some minor problems (missing ```...``` in the documentation of testsuite. Aside those everything is ok for me. Nicolas can you review 
`trac_7478_testsuite_dots-fh-review.patch`
on the queue. Then either me or you fold, reupload and set positive review. 

...trying to ping you on irc for synchro.


---

Attachment

Replying to [comment:7 hivert]:
> There are still some minor problems (missing ```...``` in the documentation of testsuite. Aside those everything is ok for me. Nicolas can you review 
> `trac_7478_testsuite_dots-fh-review.patch`
> on the queue. Then either me or you fold, reupload and set positive review. 
> 
> ...trying to ping you on irc for synchro.

Review patch is good. Folded and uploaded. positive review.


---

Comment by nthiery created at 2009-11-18 22:09:46

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-19 17:01:35

Resolution: fixed


---

Comment by mpatel created at 2009-11-27 15:03:40

I just "discovered" `sage.misc.sage_unittest`.  In case it's of wider use: At #7390 there's a `unittest` HTML report generator that may make it into SageNB.
