# Issue 5898: Plot Field doc

Issue created by migration from https://trac.sagemath.org/ticket/5898

Original creator: kcrisman

Original creation time: 2009-04-26 02:22:12

Assignee: was

There are a few minor bugs in plot_field.py which should be fixed, e.g. importing math.sqrt when in fact the symbolic square root is imported shortly thereafter (and correctly).


---

Comment by kcrisman created at 2009-04-26 02:22:46

Based on 3.4.2.alpha0


---

Attachment

This patch brings coverage of plot_field.py to 100% and fixes a few minor bugs.  

If I did not ReSTify correctly, reviewer please give extremely explicit directions for how to correct this.  Also I hope that the init method test will not cause numerical noise problems but please give explicit instructions on how to correct for that.  I find both of those issues confusing to do properly.


---

Comment by mvngu created at 2009-04-26 04:37:54

reviewer patch based on sage-3.4.2.alpha0


---

Attachment

REFEREE REPORT



That patch `plot_field-patch.patch` applies OK against Sage 3.4.2.alpha0. All doctests passed with options `-t -long`, and the coverage for `sage/plot/plot_field.py` is indeed 100% as claimed. However, when I ran the coverage on that file, I received this

```
[mvngu@sage sage-3.4.2.alpha0]$ ./sage -coverage devel/sage-exp/sage/plot/plot_field.py 
----------------------------------------------------------------------
devel/sage-exp/sage/plot/plot_field.py
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE devel/sage-exp/sage/plot/plot_field.py: 100% (7 of 7)

Possibly wrong (function name doesn't occur in doctests):
         * _repr_(self):
         * _render_on_subplot(self, subplot):
```

Notice the line

```
ERROR: Please define a s == loads(dumps(s)) doctest.
```

Apart from that, there are some minor typos. These are trivial to fix. The reviewer patch `trac_5898-referee.patch` should take care of them. Basically, it adds a test to dump and load a plot so that the above error line should be gone when running coverage on `sage/plot/plot_field.py `. So `plot_field-patch.patch` gets a positive review; only `trac_5898-referee.patch` needs to be reviewed.


---

Comment by wdj created at 2009-04-26 11:54:02

Patches apply to 3.4.2.a0 and pass sage -testall. 
The referee patch fixes some simply typos. The original patch adds details to the documentation, as claimed.


---

Comment by mabshoff created at 2009-04-30 05:37:06

Resolution: fixed


---

Comment by mabshoff created at 2009-04-30 05:37:06

Merged both patches in Sage 3.4.2.rc0.

Cheers,

Michael
