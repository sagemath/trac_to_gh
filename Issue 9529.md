# Issue 9529: in graph_plot.py, sometimes get "libpng error: Image width or height is zero in IHDR"

Issue created by migration from https://trac.sagemath.org/ticket/9529

Original creator: rlm

Original creation time: 2010-07-17 12:56:30

Assignee: AlexGhitza

CC:  chapoton tscrim

To reproduce this, you can do something like the following in bash:

```

sage-4.5.rc1/devel/sage-main$ for i in `seq 1 20`;
> do
>     ../../sage -t sage/graphs/graph_plot.py
> done

```




---

Comment by rlm created at 2010-07-17 12:56:59

See also #5906.


---

Comment by rlm created at 2010-07-17 12:57:23


```
**********************************************************************
File "/scratch/rlmill/sage-4.5.rc1/devel/sage-main/sage/graphs/graph_plot.py", line 267:
    sage: GP.plot()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/rlmill/sage-4.5.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/rlmill/sage-4.5.rc1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/rlmill/sage-4.5.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[13]>", line 1, in <module>
        GP.plot()###line 267:
    sage: GP.plot()
      File "/scratch/rlmill/sage-4.5.rc1/local/lib/python/site-packages/sage/misc/displayhook.py", line 174, in displayhook   
        print_obj(sys.stdout, obj)
      File "/scratch/rlmill/sage-4.5.rc1/local/lib/python/site-packages/sage/misc/displayhook.py", line 142, in print_obj
        print >>out_stream, `obj`
      File "sage_object.pyx", line 101, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1370) 
      File "/scratch/rlmill/sage-4.5.rc1/local/lib/python/site-packages/sage/plot/plot.py", line 915, in _repr_
        self.show()
      File "/scratch/rlmill/sage-4.5.rc1/local/lib/python/site-packages/sage/plot/plot.py", line 1437, in show
        self.save(DOCTEST_MODE_FILE, **options)
      File "/scratch/rlmill/sage-4.5.rc1/local/lib/python/site-packages/sage/plot/plot.py", line 1973, in save
        figure.savefig(filename,dpi=dpi,bbox_inches='tight',**options)
      File "/scratch/rlmill/sage-4.5.rc1/local/lib/python/site-packages/matplotlib/figure.py", line 1032, in savefig
        self.canvas.print_figure(*args, **kwargs)
      File "/scratch/rlmill/sage-4.5.rc1/local/lib/python/site-packages/matplotlib/backend_bases.py", line 1455, in print_figure
        **kwargs)
      File "/scratch/rlmill/sage-4.5.rc1/local/lib/python/site-packages/matplotlib/backends/backend_agg.py", line 366, in print_png
        filename_or_obj, self.figure.dpi)
    RuntimeError: Error building image
**********************************************************************
```



---

Comment by cwitty created at 2010-07-17 19:55:39

To reproduce this fairly quickly, type:

```
sage.plot.plot.DOCTEST_MODE = True
while True:
    d = DiGraph({}, loops=True, multiedges=True, sparse=True)
    d.add_edges([(0,0,'a'),(0,0,'b'),(0,1,'c'),(0,1,'d'),
            (0,1,'e'),(0,1,'f'),(0,1,'f'),(2,1,'g'),(2,2,'h')])
    GP = d.graphplot(vertex_size=100, edge_labels=True, color_by_label=True, edge_style='dashed')
    GP.set_edges(edge_style='solid')
    GP.plot()
```

at a sage: prompt.

I spent some time looking into this; here are the results I found before I gave up.

We draw our plots with bbox_inches='tight', which means:

```
            Bbox in inches. Only the given portion of the figure is
            saved. If 'tight', try to figure out the tight bbox of
            the figure.
```


There's also a parameter pad_inches:

```
            Amount of padding around the figure when bbox_inches is
            'tight'.
```


matplotlib gets its "tight bbox" with the appropriately-named get_tightbbox() function, in src/lib/matplotlib/figure.py.  Its docstring proclaims,

```
        It only accounts axes title, axis labels, and axis
        ticklabels. Needs improvement.
```

and it's true, it does need improvement.

Our graph_plot figure has "empty" axes (no title, labels, or ticklabel), but it does have an axes object with a size, which gets used for the tight bbox.  I believe that size comes indirectly from get_minmax_data in sage/plot/plot.py, but I'm not sure.

I can think of a few possibilities to fix the problem, ordered from best to worst.

1) Fix matplotlib get_tightbbox() to actually be a bounding box for the drawing, not just for the "axes".  This would definitely be best... it would also fix problems like graphs with loops going off the edge of the plot, etc.

2) Adjust our get_minmax_data functions to be closer to a correct bounding box.  For instance, currently get_minmax_data on a Text object only looks at the center of the text, and doesn't take the size into account.  There's a limit to how good a job we could do, though... we don't want to start digging through font metrics, etc.

3) Set pad_inches to make all our plots "a little bit bigger".  The downside, of course, is that this simple approach would affect *all* our plots.

Like I said, I'm giving up now.


---

Comment by jason created at 2010-07-18 06:13:02

See #9211, where similar issues are dealt with.  With the new matplotlib at #9221, we can add some extra artists whose bounding boxes should be included in the tight bbox calculations (so, for example, we should be able to add the text boxes and then the tight bbox calculations would include those bounds as well).


---

Comment by rlm created at 2010-07-19 08:53:59

Changing component from algebra to graph theory.


---

Comment by rlm created at 2010-07-19 08:53:59

Changing assignee from AlexGhitza to jason, ncohen, rlm.


---

Comment by jmantysalo created at 2016-07-16 04:40:19

I can not reproduce this, and this is six years old. I suppose this one can be closed as the code has been changed many times. Frédéric, do you agree?


---

Comment by jmantysalo created at 2016-07-16 04:40:19

Changing status from new to needs_review.


---

Comment by jmantysalo created at 2016-08-09 05:06:05

Travis, do you agree that we can close this?


---

Comment by jmantysalo created at 2016-08-17 12:29:03

Just pinging this wontfix-confirmation.


---

Comment by tscrim created at 2016-08-17 12:37:34

Changing status from needs_review to positive_review.


---

Comment by tscrim created at 2016-08-17 12:37:34

I can't reproduce it either.


---

Comment by embray created at 2016-08-30 13:32:25

Determined to be invalid/duplicate/wontfix (closing as "wontfix" as a catch-all resolution).


---

Comment by embray created at 2016-08-30 13:32:25

Resolution: wontfix
