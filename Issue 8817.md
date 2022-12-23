# Issue 8817: Rplot001.png left around when doctesting

Issue created by migration from https://trac.sagemath.org/ticket/8817

Original creator: was

Original creation time: 2010-04-29 06:06:26

Assignee: tbd

I doctested after I think #7665 and this file Rplot001.png appeared in SAGE_ROOT.  That's obnoxious. 


---

Comment by kcrisman created at 2010-04-29 16:33:22

eah, this is my fault:

```
+        This example saves a plot to the standard R output, usually 
+        a filename like ``Rplot001.png`` - from the command line, in 
+        the current directory, and in the cell directory in the notebook::
+
+            sage: r.plot("1:10")
+            null device 
+                      1 
+
```

I actually put this one in to show users how to actually get a file in a directory that they have access to, as opposed to a temp directory, but forgot we can't do that.  Is it legitimate to put #not tested with this doctest as a fix, since it is important to have the example there?


---

Comment by kcrisman created at 2010-04-30 00:20:50

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-04-30 14:19:03

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2010-04-30 14:19:03

> but forgot we can't do that.  Is it legitimate to put #not tested with
> this doctest as a fix, since it is important to have the example
> there?
From was:

```
Another option:

1. make sufpre the png file you are about to write doesn't exist in the current directory, then write it.
2. then delete it!


# not tested should be avoided at all costs.
```



---

Comment by kcrisman created at 2010-04-30 15:04:44

Based on Sage 4.4 + R plot patch


---

Comment by kcrisman created at 2010-04-30 15:05:48

Changing status from needs_work to needs_review.


---

Attachment

Okay, try this - it is VERY explicit.  I also replaced occurrences of os.unlink with os.remove, which is identical but makes far more sense to those who are not familiar with the unlink command (like me).


---

Comment by was created at 2010-05-01 05:16:38

I really don't like this very brittle and dangerous patch.  I've posted a new patch.  Please review. I've included this in alpha3 anyways.

William


---

Attachment


---

Comment by mvngu created at 2010-05-02 23:57:20

The directory named by the environment variable `SAGE_TMP` is where junk files can go. Such junk files include temporary files generated during doctesting.


---

Comment by mvngu created at 2010-05-02 23:57:20

Resolution: fixed
