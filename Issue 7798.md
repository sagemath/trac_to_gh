# Issue 7798: Text in Plots at any given Function

Issue created by migration from Trac.

Original creator: slosoi

Original creation time: 2009-12-31 00:56:07

Assignee: was

Keywords: plot, label

The purpose of the ticket is to locate where the function text should be applied to the function plot to be able to have lables for plots like: var('x'); f = x**2; p = plot(f,x); p.text("hello") for one function.

------ not sure about this -------------
Two functions: g = x; p2 = plot(g,x); (g + f).text("eggs fro g", g) where the string prints the label for g, while "g" prints label only for f.


---

Attachment

Not working attempt: trying to get some text initially to the plot


---

Comment by slosoi created at 2009-12-31 01:13:10

Changing status from new to needs_work.


---

Comment by slosoi created at 2009-12-31 23:34:38

To recompute line first to get coordinates right


---

Attachment

I get the error in running the patch. There is somewhere a bug which prevents the loading of the module.


---

Attachment


---

Comment by slosoi created at 2010-01-02 04:25:52

Changing keywords from "plot, label" to "axes, range".


---

Comment by jason created at 2010-03-17 05:29:19

Changing type from defect to enhancement.
