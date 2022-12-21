# Issue 6357: make sage -t worksheet.sws work

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-06-18 17:05:01

Assignee: tbd

CC:  kini novoselt

Keywords: sage test worksheet doctest

This came up on the mailing list: it would be nice if sage -t worksheet.sws worked.

Separate, but also nice, would be "worksheet-ify" command that took a series of doctests and made a nice worksheet out of it.


---

Comment by ncalexan created at 2009-06-18 17:05:08

Changing type from defect to enhancement.


---

Comment by was created at 2009-06-18 19:04:14

(NOTE -- I rethought this in the last paragraph below, but didn't delete the stuff above, in case it is useful still.)

How I would implement this:

```
 sage -t foo.sws
```

would

1. extract foo.sws into a temporary directory.  Try to use builtin library calls instead of calling tar on the command line, if possible.  Note that foo.sws is a .tar.bz2

2. Ignore everything not in {{}}'s.  I'm using {{ instead of triple {'s to avoid trac's wiki preformat mode.

3. Create a file foo.py.  For each chunk of code 

```
{{
input lines
///
output lines
```

insert into the file foo.py lines:

```
sage: sage.server.notebook.cell.eval_for_testing(r"""input lines
input lines...""")
output lines
```

since I think how the notebook works is best simulated by using the sage0 pexpect interface (that's what the notebook really uses).  

4. Doctest foo.py using `sage -t foo.py` and let normal doctest report the results.  Possibly postprocess the `print sage0.eval(r"""` wrapper crap out of the result.


The above plan has the advantage that it reduces things to the existing python doctest framework instead of trying to write another doctest system.   One disadvantage is that using sage0 means that two Python processes are spawned instead of 1.

The function `sage.server.notebook.cell.eval_for_testing` has not been written.  It would make a blank directory, call sage0.eval -- just like the notebook does -- then apply all transformations the notebook does on output.  

Actually, writing the above makes me think that this problem is harder than I thought when I started writing this comment!  The problem is the output is potentially very complicated, since it can be a bunch of sagexxx.png files, html, etc.   Maybe a better approach is to completely use the notebook codebase -- as is done in all the notebook doctesting -- to run a *copy* of the whole worksheet (a sort of evaluate all) -- then simply compare the original's output to the copy's.


---

Comment by kini created at 2011-11-03 00:06:57

Changing keywords from "sage test worksheet doctest" to "doctest sws notebook worksheet test".


---

Comment by roed created at 2013-03-14 21:51:30

After #12415, this just needs to add a parser for .sws files in `sage.doctest.sources` analogous to `PythonSource`, `RestSource` and `TexSource`.


---

Comment by roed created at 2013-03-28 22:41:49

Changing component from doctest to doctest framework.


---

Comment by novoselt created at 2017-01-02 22:48:07

Changing status from new to needs_review.


---

Comment by novoselt created at 2017-01-02 22:48:07

With no progress on it and with sws planned for retirement together with SageNB, I think we should close it.


---

Comment by chapoton created at 2017-01-05 16:50:42

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2017-01-05 16:50:42

yes, let us close that


---

Comment by vbraun created at 2017-01-21 18:03:11

Resolution: invalid
