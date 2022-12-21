# Issue 7993: whitespace error in doctest causes A Mysterious Error.

Issue created by migration from Trac.

Original creator: wjp

Original creation time: 2010-01-19 06:06:55

Assignee: tbd

When doctesting a file `a.sage` containing


```
def foo():
    """
    sage: 1+1
   2
    """
    pass
```


(note the missing space before the 2), you get:


```
[wjp`@`issa sage-4.3.1.rc0]$ ./sage -t a.sage
sage -t  "a.sage"                                           
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
         [2.4 s]
exit code: 768
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "a.sage"
Total time for all tests: 2.4 seconds
```



---

Comment by wjp created at 2010-01-20 05:21:20

Changing status from new to needs_review.


---

Comment by wjp created at 2010-01-20 05:21:20

I changed the `sage-doctest` script to make the actual doctesting process catch exceptions and communicate this to `sage-doctest` via the process exit code.

It now differentiates between a crash and an exception raised by the doctesting code.


This patch depends on the patch at #7995.


---

Comment by nthiery created at 2010-01-20 09:04:42

As for #7995: thanks much for handling this. I'd love to see this in Sage very shortly.

Please include the new output in the ticket description!

I can try to review this, but I'd rather have a testing framework expert to it.


---

Attachment

I noticed an existing, unrelated problem.  Let `foo.py` contain


```python
def g():
    """
    sage: 1 + 1
    11
    """
    return
```

Then `sage -tp 1 foo.py` ends with


```python
1 items had failures:
   1 of   3 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/.sage//tmp/.doctest_foo.py
         [2.0 s]
 
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/apps/sage/local/bin/sage-ptest", line 361, in <module>
    failed_files[F.split('#')[0].split()[2]] = None
IndexError: list index out of range
```



---

Comment by mpatel created at 2010-01-31 07:18:51

Anyway, we can make a separate ticket to unify, simplify, and _doctest_ the doctesting framework.

I'm not an expert, but the changes look OK.  Can we report at least partial results for interrupted tests?


---

Comment by mpatel created at 2010-02-19 09:38:31

Minor update:  The patch works for me in daily (i.e., not heavy) use.  Any other experiences?


---

Comment by zimmerma created at 2010-03-01 17:18:30

Changing status from needs_review to needs_work.


---

Comment by zimmerma created at 2010-03-01 17:18:30

I wanted to try this patch to see if it would by chance solve #7773, but apparently it needs a rebase
for 4.3.3:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: 7993
sage: hg_sage.import_patch("/tmp/scripts_7993_doctest_error_handling.patch")
cd "/usr/local/sage-4.3.3/sage/devel/sage" && hg status
cd "/usr/local/sage-4.3.3/sage/devel/sage" && hg status
cd "/usr/local/sage-4.3.3/sage/devel/sage" && hg import   "/tmp/scripts_7993_doctest_error_handling.patch"
applying /tmp/scripts_7993_doctest_error_handling.patch
unable to find 'sage-doctest' for patching
4 out of 4 hunks FAILED -- saving rejects to file sage-doctest.rej
unable to find 'sage-ptest' for patching
1 out of 1 hunks FAILED -- saving rejects to file sage-ptest.rej
unable to find 'sage-test' for patching
2 out of 2 hunks FAILED -- saving rejects to file sage-test.rej
abort: patch failed to apply
```

| Sage Version 4.3.3, Release Date: 2010-02-21                       |
| Type notebook() for the GUI, and license() for information.        |
Paul


---

Comment by mpatel created at 2010-03-01 17:32:25

The patch is for the scripts repository, whose root is `SAGE_ROOT/local/bin`.  Try using `hg_scripts`, instead.  I think the patch will still apply cleanly to 4.3.3.


---

Comment by zimmerma created at 2010-03-05 20:34:10

Changing status from needs_work to needs_info.


---

Comment by zimmerma created at 2010-03-05 20:34:10

sorry, I still cannot apply this patch on 4.3.3, even with `hg_scripts`:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: 7993
sage: hg_scripts.import_patch("/tmp/scripts_7993_doctest_error_handling.patch")
cd "/usr/local/sage-4.3.3/sage/local/bin" && hg status
cd "/usr/local/sage-4.3.3/sage/local/bin" && hg status
cd "/usr/local/sage-4.3.3/sage/local/bin" && hg import   "/tmp/scripts_7993_doctest_error_handling.patch"
applying /tmp/scripts_7993_doctest_error_handling.patch
patching file sage-doctest
Hunk #1 FAILED at 4
Hunk #2 FAILED at 151
Hunk #3 FAILED at 170
Hunk #4 FAILED at 655
4 out of 4 hunks FAILED -- saving rejects to file sage-doctest.rej
patching file sage-ptest
Hunk #1 FAILED at 163
1 out of 1 hunks FAILED -- saving rejects to file sage-ptest.rej
patching file sage-test
Hunk #1 FAILED at 84
Hunk #2 FAILED at 109
2 out of 2 hunks FAILED -- saving rejects to file sage-test.rej
abort: patch failed to apply
```

Did I something wrong?


---

Comment by wjp created at 2010-03-05 20:59:07

That's strange; the same command works for me in a clean 4.3.3.
Do you have any other patches applied to the scripts repo? (I don't think branching will affect that repo.) You can check with hg_scripts.status() and hg_scripts.log().

Also, since all hunks are failing, could it be a line ending problem? (mac vs. unix vs. dos?)


---

Comment by zimmerma created at 2010-03-05 21:35:23

I get:

```
sage: hg_scripts.status()
Getting status of modified or unknown files:
cd "/usr/local/sage-4.3.3/sage/local/bin" && hg status
? cbc
? clp

---

```

and:

```
sage: hg_scripts.log()
cd "/usr/local/sage-4.3.3/sage/local/bin" && hg log  | less
changeset:   1449:0893591acc56
tag:         tip
user:        Willem Jan Palenstijn <wjp`@`usecode.org>
date:        Wed Jan 20 10:52:15 2010 -0800
summary:     #7993: clean up error handling in sage-doctest

changeset:   1448:77ae8a697bba
user:        Minh Van Nguyen <nguyenminh2`@`gmail.com>
date:        Sun Feb 21 17:22:49 2010 -0800
summary:     4.3.3
...
```

I thought that `sage -clone 7993` would create a fresh clone of 4.3.3, where I could apply
and test your patch. Do you mean that I've already applied your patch?


---

Comment by wjp created at 2010-03-05 22:19:52

Yes, it does look like it. I don't think `sage -clone` touches the scripts repository, but only the main sage library.


---

Comment by zimmerma created at 2010-03-08 15:17:06

with the patch, we now get with the initial example:

```
tarte% sage -t a.sage
sage -t  "a.sage"                                           
Exception raised by doctesting framework. Use -verbose for details.
         [1.4 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "a.sage" # Exception from doctest framework
Total time for all tests: 1.4 seconds
```

and the whole doctest still produces 22 Segfaults (see #7773). However, instead of say:

```
sage -t  tests/benchmark.py
A mysterious error (perhaps a memory error?) occurred, which may have crashed d\
octest.
         [62.3 s]
```

we now get:

```
sage -t  tests/benchmark.py
The doctested process was killed by signal 14
         [62.5 s]
```

which is more informative. I thus give a positive review.


---

Comment by zimmerma created at 2010-03-08 15:17:06

Changing status from needs_info to needs_review.


---

Comment by zimmerma created at 2010-03-08 15:17:42

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-03-08 20:54:04

Resolution: fixed
