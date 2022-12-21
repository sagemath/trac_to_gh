# Issue 2224: sage-2.10.2.alpha1 -- strange show doctest bug in group.pyx

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-20 06:56:36

Assignee: was


```
sage -t  devel/sage-main/sage/groups/group.pyx              **********************************************************************
File "group.pyx", line 140:
    sage: show(G, color_by_label=True, edge_labels=True)   # todo -- we must test this, but must not have "sage -t" popping up windows.
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_17[2]>", line 1, in <module>
        show(G, color_by_label=True, edge_labels=True)   # todo -- we must test this, but must not have "sage -t" popping up windows.###line 140:
    sage: show(G, color_by_label=True, edge_labels=True)   # todo -- we must test this, but must not have "sage -t" popping up windows.
      File "/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/site-packages/sage/misc/functional.py", line 926, in show
        return x.show(*args, **kwds)
      File "/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/site-packages/sage/graphs/graph.py", line 3045, in show
        heights=heights).show(**kwds)
      File "/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/site-packages/sage/plot/plot.py", line 1237, in show
        aspect_ratio=aspect_ratio)
      File "/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/site-packages/sage/plot/plot.py", line 1388, in save
        g._render_on_subplot(subplot)
      File "/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/site-packages/sage/plot/plot.py", line 1667, in _render_on_subplot
        c = to_mpl_color(options['rgbcolor'])
      File "/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/site-packages/sage/plot/plot.py", line 3678, in to_mpl_color
        s = float(c[i])
    ValueError: invalid literal for float(): #
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_17
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_group.pyx
	 [21.8 s]

```


Above I have some comments:
 (1) -- clearly that is a weird bug in what is being doctested.

 (2) aside from that, take a look at how show works in plot.py to see
that doctesting sets a certain flag, and show in that contexts writes
files to a temp directory.  That's what the above should do.


---

Attachment

this fixes the doctest by implemeting new code in plot.py so that rgbcolor='#fffff00' works; i.e., improve the plotting code.


---

Comment by mabshoff created at 2008-02-22 01:19:52

Patch looks good, is much nicer than the previous version and is well doctested. The last hunk needs to be removed when merging. Ergo: positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-22 01:22:50

Resolution: fixed


---

Comment by mabshoff created at 2008-02-22 01:22:50

Merged in Sage 2.10.2.rc0
