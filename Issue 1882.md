# Issue 1882: new phcpack spkg

Issue created by migration from https://trac.sagemath.org/ticket/1882

Original creator: mhampton

Original creation time: 2008-01-21 23:06:32

Assignee: mabshoff

Keywords: phcpack

Phcpack has had many releases since the last spkg.  This brings it up to date as of January 21, 2008, with release 2.3.38.  I have changed the install script to python instead of a shell script, because that's what I know how to do.  I have also tried to add AIX support but I don't have a machine to test it on.


---

Comment by mhampton created at 2008-01-21 23:20:50

file is at:

http://www.d.umn.edu/~mhampton/phc-2.3.38.spkg

[with experimental spkg]


---

Comment by mabshoff created at 2008-01-21 23:25:52

Oops, 2.3.21 is the version that is currently in the repo.


---

Comment by mhampton created at 2008-01-22 01:53:28

Unfortunately it looks like the Mac Intel version is broken, so this should not be included.  I am corresponding with Jan Verschelde (the creator of phcpack) to figure out what is going on.


---

Comment by mhampton created at 2008-01-22 13:20:24

I have changed the install file so that, as before, intel macs will run the ppc version (through rosetta).  This makes the update much less exciting but it actually works.


---

Comment by mhampton created at 2008-02-24 17:50:58

I have edited the installer slightly, please re-download this for putting in 10.2.3.

I have also added to the phc interface (in sage/interfaces) and fixed a typo of mine that incorrectly described the type of an output.  The new file is:
[www.d.umn.edu/~mhampton/phc.py]

This adds a command phc.mixed_volume that quickly computes the mixed volume of a polynomial system.


---

Comment by mhampton created at 2008-02-24 17:53:39

Sorry I should have previewed.  Interface file is at:

[http://www.d.umn.edu/~mhampton/phc.py](http://www.d.umn.edu/~mhampton/phc.py)

and the spkg is at

[http://www.d.umn.edu/~mhampton/phc-2.3.38.spkg](http://www.d.umn.edu/~mhampton/phc-2.3.38.spkg)


---

Comment by mhampton created at 2008-02-26 00:24:43

I changed the patch so that the Integer type is imported; the previous one had a bug. I am actively using this for a research project so it should get some more stress testing this week.


---

Comment by mhampton created at 2008-02-27 00:38:38

Fixed a bug that affected larger problems, added optional tag to doctests - I assume that causes them to be skipped usually.


---

Comment by mhampton created at 2008-02-28 18:52:30

Changing assignee from mabshoff to was.


---

Comment by mhampton created at 2008-02-28 18:52:30

Changing component from packages to interfaces.


---

Comment by cwitty created at 2008-03-14 01:56:10

The spkg installs and appears to work on my 32-bit x86 Debian testing system.  However, the spkg does include some junk OSX files (._spkg-install, .DS_Store, etc.)

The patch includes a syntax error, which I fixed like this:

```
--- a/sage/interfaces/phc.py    Tue Feb 26 18:36:37 2008 -0600
+++ b/sage/interfaces/phc.py    Thu Mar 13 18:34:51 2008 -0700
@@ -274,7 +274,7 @@ class PHC:
         child_phc.expect('results')
         dots = child_phc.read()
         if verbose:
-            print "should be ... :" dots
+            print "should be ... :", dots
         child_phc.close()
         if not os.path.exists(output_filename):
             raise RuntimeError, "The output file does not exist; something went wrong running phc."
```


After applying the patch and installing the spkg, testing phc.py (with -optional) failed with:

```
sage -t -optional devel/sage-mq/sage/interfaces/phc.py      **********************************************************************
File "phc.py", line 181:
    e: v.solutions()                    # optional
Expected:
    [[-1.00000000000000*I, 1.00000000000000*I], [1.00000000000000*I, -1.00000000000000*I]]
Got:
    [[1.00000000000000*I, -1.00000000000000*I], [-1.00000000000000*I, 1.00000000000000*I]]
**********************************************************************
File "phc.py", line 183:
    e: v.solution_dicts()               # optional
Expected:
    [{x: -1.00000000000000*I, y: 1.00000000000000*I}, {x: 1.00000000000000*I, y: -1.00000000000000*I}]
Got:
    [{y: 1.00000000000000*I, x: -1.00000000000000*I}, {y: -1.00000000000000*I, x: 1.00000000000000*I}]
**********************************************************************
1 items had failures:
   2 of   9 in __main__.example_5
***Test Failed*** 2 failures.
```


It looks like you may need to sort the results.  Also, printing dictionaries often gives different results on 32-bit vs. 64-bit systems (due to the different hash functions used); you may need to have "# 32-bit" and "# 64-bit" versions of the output.


---

Comment by mhampton created at 2008-03-18 18:14:34

Changing assignee from was to mabshoff.


---

Comment by mhampton created at 2008-03-18 18:14:34

The file phc.py at http://www.d.umn.edu/~mhampton/phc.py has been changed to address the review comments.  I have updated the spkg to try to remove the superfluous OS X files.


---

Attachment


---

Comment by mhampton created at 2008-03-20 19:24:29

I just noticed that Jan released another version, so I have updated to that and fixed a bug in my spkg-install script.  The new spkg is at:

http://www.d.umn.edu/~mhampton/phc-2.3.39.spkg

[with experimental spkg]


---

Attachment


---

Comment by cwitty created at 2008-03-29 15:06:18

I've attached a patch to fix some minor doctest issues.

1) add a missing "# optional"

2) improve (IMHO) the solution_dicts() doctest to make it clearer (IMHO) what the method returns, while still letting the doctest be portable

3) copy some doctests from a class docstring to a method docstring, to make "sage -coverage" happier

With this patch and phc-2.3.39, doctests pass in interfaces/phc.py, both with and without -optional.  Positive review.


---

Comment by mabshoff created at 2008-03-29 15:38:16

I fixed some issues in the spkg. It is now at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/optional/phc-2.3.39.p0.spkg

In addition I put up the new SPKG.txt at 

http://wiki.sagemath.org/spkg/phcpack

The SPKG has been uploaded to the optional repo and mirrored out.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-29 15:40:24

Resolution: fixed


---

Comment by mabshoff created at 2008-03-29 15:40:24

Merged in Sage 2.11.rc0
