# Issue 7650: Fix sagenb doctesting

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2009-12-10 03:12:15

Assignee: was

CC:  was timdumol mhansen jason

`sage -t sagenb/` yields several

```
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
```



---

Comment by mpatel created at 2009-12-10 03:13:58

Part of the problem is that notebook directories now need to end in `.sagenb`.

I'm working on a patch for this and whatever other problems I can fix.


---

Comment by mpatel created at 2009-12-10 03:27:21


```python
sage -t -verbose "notebook.py"                              
Traceback (most recent call last):
  File "/home/.sage//tmp/.doctest_notebook.py", line 18, in <module>
    from notebook import *
  File "/home/.sage/tmp/notebook.py", line 38, in <module>
    import css          # style
ImportError: No module named css
         [2.5 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -verbose "notebook.py"
Total time for all tests: 2.5 seconds
```


Adding

```python
import sys
sys.path.append('/home/sage/notebook/sagenb/sagenb')
sys.path.append('/home/sage/notebook/sagenb/sagenb/notebook')
```

to the top of `notebook.py` allows testing to proceed.  I'm not sure about a real solution.


---

Attachment

Add `--force_lib` option to `sage-doctest`.  Use `os.path.join`.  *scripts* repo.


---

Comment by mpatel created at 2009-12-10 11:40:51

Fix sagenb doctests.  *sagenb* repo.


---

Comment by mpatel created at 2009-12-10 11:57:53

Changing priority from major to blocker.


---

Attachment

*Please note: The attachments (or their descriptions) are switched.*  I apologize for this.

Anyway, with the scripts repository patch, we can do, e.g.,

```sh
$ sage -t --force_lib sagenb/
```

With the sagenb repository patch applied to #7625 + #7483 + #7482 + #7514 + #7648, all tests but 3 pass.  The failures are in `sagenb/misc/sageinspect.py` (cf. #7514).  The Selenium tests still pass.

Remarks:

 * I hope I did not create false-negatives.
 * [This sage-notebook thread](http://groups.google.com/group/sage-notebook/browse_thread/thread/9dd524690bb1588b/38855ecc2819205a?#38855ecc2819205a) _might_ be relevant to some tests that evaluate cells.
 * I "untabified" `cell.py`, `worksheet.py`, `notebook.py`, and `twist.py`.
 * I added `'nodoctest'` to `simple/twist.py`, since at least one test appears to hang indefinitely.  I don't know why.
 * Feel free to lower the priority.


---

Comment by mpatel created at 2009-12-10 11:57:53

Changing status from new to needs_review.


---

Comment by mpatel created at 2009-12-10 12:23:50

Should we add, e.g., 

```sh
sage -t --force_lib $SAGE_ROOT/local/lib/python/site-packages/sagenb
```

to `$SAGE_ROOT/makefile`?  Or `sage-test`?


---

Comment by was created at 2009-12-10 18:18:48

Changing status from needs_review to needs_work.


---

Comment by was created at 2009-12-10 18:18:48

I like this patch a lot.  However, a nitpick: get rid of the / before tmp here:

```
SAGE_TESTDIR = os.path.join(DOT_SAGE, "/tmp") 
```

Likewise, elsewhere in the patch there are a bunch of os.path.joins combined with explicit* slashes.  

Regarding adding sage -t sagenb, etc., to sage-test or whatever: "yes!"


---

Comment by mpatel created at 2009-12-11 14:29:05

Updated scripts repo patch.  Replaces previous.


---

Attachment

Quit spawned worksheet processes.  Replaces previous sagenb repo patch.


---

Comment by mpatel created at 2009-12-14 03:17:19

Auto-detect `site-packages`.  scripts repo.  Replaces previous.


---

Attachment

Adds `-sagenb` option.  scripts repo.  Replaces previous.


---

Attachment

Updated `SAGE_ROOT/makefile`.


---

Comment by mpatel created at 2009-12-14 06:18:29

Changing status from needs_work to needs_review.


---

Attachment

With [attachment:trac_7650-scripts_doctest_force_lib_v4.patch] and an updated top-level [attachment: makefile], we can do

 * `make test`
 * `make ptest`
 * `sage -t -sagenb`
 * `sage -tp -sagenb`

etc.  Maybe we should unify the test scripts and use [optparse](http://docs.python.org/library/optparse.html)?


---

Comment by timdumol created at 2009-12-21 03:48:53

Changing status from needs_review to needs_work.


---

Comment by timdumol created at 2009-12-21 03:48:53

The new options to `sage -t` (-force_lib and -sagenb) are not documented in the help message. Please do so.


---

Comment by was created at 2009-12-24 07:06:27

I'm declaring a total feature freeze on sage-4.3.


---

Comment by mpatel created at 2009-12-24 18:19:27

Also: Be more agressive with `os.path.join`-ery.


---

Attachment

Document new options.  More `os.path.join`-ery.  Replaces previous.


---

Comment by mpatel created at 2009-12-28 23:20:59

Changing status from needs_work to needs_review.


---

Comment by mpatel created at 2010-01-01 10:56:04

Rebased vs. #7482's v4.  Replaces previous *sagenb* patch.


---

Attachment


---

Comment by mpatel created at 2010-01-05 00:48:34

Rebased vs. 4.3.1.alpha0 + #7269.  Replaces previous sagenb patch.


---

Attachment


---

Comment by mpatel created at 2010-01-05 00:57:02

I've attached a rebased sagenb patch.  I added `"""nodoctests"""` to the top of `sagenb.misc.ipaddr`.  It's also easy to make its doctest pass, but I haven't done this.  Please let me know, if I should.


---

Attachment

Fix tags / user_view asymmetry.  Replaces previous sagenb patch.


---

Comment by mpatel created at 2010-01-14 22:04:54

V5 makes it so a worksheet `reconstruct`ed from the `basic` representation of another has the same `tags` and `user_view` as the original.


---

Comment by mpatel created at 2010-01-15 21:32:58

Fix interact doctests for 4.3.1.alpha2 (colors.py).  Replaces previous sagenb patch.


---

Attachment

Replying to [comment:17 mpatel]:
> V5 makes it so a worksheet `reconstruct`ed from the `basic` representation of another has the same `tags` and `user_view` as the original.

Shouldn't this be put in a new ticket?


---

Comment by mpatel created at 2010-01-17 14:31:13

Yes, but it's already here.  :)  In the course of fixing many failed doctests, I noticed it and a few other small problems:

 * In `run_notebook.notebook_twisted`: Replaced `nb.directory()` (not defined) with `nb._dir`.
 * In `worksheet`: Replaced `self.__collaborators` (`AttributeError`) with `self.collaborators()` in a few places.
 * In `worksheet.set_filename`:

```diff
-        self.__dir = os.path.join(self.notebook().worksheet_directory(), filename)
+        self.__dir = os.path.join(self.notebook()._dir, filename)
```

 * In `worksheet.tags`:

```diff
             d = dict(self.__user_view)
         except AttributeError:
             self.user_view(self.owner())
-            d = self.__user_view
+            d = copy.copy(self.__user_view)
         for user, val in d.iteritems():
-            d[user] = [val]
+            if not isinstance(val, list):
+                d[user] = [val]
         return d
```

 This ensures the tests in `Worksheet.reconstruct_from_basic` pass and that calling `tags` does not alter the current user view, e.g., turning `1` into `[1]`.

Also:

 * Removed argument `verbose` (obsolete) from `Cell.set_introspect_html`.


---

Comment by timdumol created at 2010-01-17 18:19:35

This bags a positive review from me, except for the few changes I've made in the reviewer patch. Can someone sign them off?


---

Comment by timdumol created at 2010-01-17 19:24:18

A few documentation fixes (precision errors and style), and a couple of changes to try-except blocks to make it easier to transition to Python 3


---

Attachment

Fix two doctest failures.  Replaces reviewer patch.  sagenb repo.


---

Comment by mpatel created at 2010-01-18 04:17:30

Changing status from needs_review to positive_review.


---

Attachment

V2 of the reviewer patch:

 * Adds a missing dot (`.`) in `interact.py`.
 * Moves `# output depends on timezone` to the input statement in `worksheet.py`.
 * [Pre-existing] `most be defined` --> `must be defined`.


---

Comment by rlm created at 2010-01-19 01:44:36

I applied the scripts patch and replaced makefile in SAGE_ROOT. Please post a `sagenb-0.5.1.spkg`.


---

Comment by rlm created at 2010-01-19 02:55:28

Resolution: fixed


---

Comment by rlm created at 2010-01-19 02:55:28

Merged http://boxen.math.washington.edu/home/timdumol/sagenb-0.6.spkg into spkg/standard.
