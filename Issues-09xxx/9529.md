# Issue 9529: in graph_plot.py, sometimes get "libpng error: Image width or height is zero in IHDR"

archive/issues_009529.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  @fchapoton @tscrim\n\nTo reproduce this, you can do something like the following in bash:\n\n```\n\nsage-4.5.rc1/devel/sage-main$ for i in `seq 1 20`;\n> do\n>     ../../sage -t sage/graphs/graph_plot.py\n> done\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9529\n\n",
    "closed_at": "2016-08-30T13:32:25Z",
    "created_at": "2010-07-17T12:56:30Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "in graph_plot.py, sometimes get \"libpng error: Image width or height is zero in IHDR\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9529",
    "user": "https://github.com/rlmill"
}
```
Assignee: jason, ncohen, rlm

CC:  @fchapoton @tscrim

To reproduce this, you can do something like the following in bash:

```

sage-4.5.rc1/devel/sage-main$ for i in `seq 1 20`;
> do
>     ../../sage -t sage/graphs/graph_plot.py
> done

```


Issue created by migration from https://trac.sagemath.org/ticket/9529





---

archive/issue_comments_091529.json:
```json
{
    "body": "See also #5906.",
    "created_at": "2010-07-17T12:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9529#issuecomment-91529",
    "user": "https://github.com/rlmill"
}
```

See also #5906.



---

archive/issue_comments_091530.json:
```json
{
    "body": "```\n**********************************************************************\nFile \"/scratch/rlmill/sage-4.5.rc1/devel/sage-main/sage/graphs/graph_plot.py\", line 267:\n    sage: GP.plot()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/rlmill/sage-4.5.rc1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/rlmill/sage-4.5.rc1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/rlmill/sage-4.5.rc1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_4[13]>\", line 1, in <module>\n        GP.plot()###line 267:\n    sage: GP.plot()\n      File \"/scratch/rlmill/sage-4.5.rc1/local/lib/python/site-packages/sage/misc/displayhook.py\", line 174, in displayhook   \n        print_obj(sys.stdout, obj)\n      File \"/scratch/rlmill/sage-4.5.rc1/local/lib/python/site-packages/sage/misc/displayhook.py\", line 142, in print_obj\n        print >>out_stream, `obj`\n      File \"sage_object.pyx\", line 101, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1370) \n      File \"/scratch/rlmill/sage-4.5.rc1/local/lib/python/site-packages/sage/plot/plot.py\", line 915, in _repr_\n        self.show()\n      File \"/scratch/rlmill/sage-4.5.rc1/local/lib/python/site-packages/sage/plot/plot.py\", line 1437, in show\n        self.save(DOCTEST_MODE_FILE, **options)\n      File \"/scratch/rlmill/sage-4.5.rc1/local/lib/python/site-packages/sage/plot/plot.py\", line 1973, in save\n        figure.savefig(filename,dpi=dpi,bbox_inches='tight',**options)\n      File \"/scratch/rlmill/sage-4.5.rc1/local/lib/python/site-packages/matplotlib/figure.py\", line 1032, in savefig\n        self.canvas.print_figure(*args, **kwargs)\n      File \"/scratch/rlmill/sage-4.5.rc1/local/lib/python/site-packages/matplotlib/backend_bases.py\", line 1455, in print_figure\n        **kwargs)\n      File \"/scratch/rlmill/sage-4.5.rc1/local/lib/python/site-packages/matplotlib/backends/backend_agg.py\", line 366, in print_png\n        filename_or_obj, self.figure.dpi)\n    RuntimeError: Error building image\n**********************************************************************\n```",
    "created_at": "2010-07-17T12:57:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9529#issuecomment-91530",
    "user": "https://github.com/rlmill"
}
```

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

archive/issue_comments_091531.json:
```json
{
    "body": "To reproduce this fairly quickly, type:\n\n```\nsage.plot.plot.DOCTEST_MODE = True\nwhile True:\n    d = DiGraph({}, loops=True, multiedges=True, sparse=True)\n    d.add_edges([(0,0,'a'),(0,0,'b'),(0,1,'c'),(0,1,'d'),\n            (0,1,'e'),(0,1,'f'),(0,1,'f'),(2,1,'g'),(2,2,'h')])\n    GP = d.graphplot(vertex_size=100, edge_labels=True, color_by_label=True, edge_style='dashed')\n    GP.set_edges(edge_style='solid')\n    GP.plot()\n```\nat a sage: prompt.\n\nI spent some time looking into this; here are the results I found before I gave up.\n\nWe draw our plots with bbox_inches='tight', which means:\n\n```\n            Bbox in inches. Only the given portion of the figure is\n            saved. If 'tight', try to figure out the tight bbox of\n            the figure.\n```\n\nThere's also a parameter pad_inches:\n\n```\n            Amount of padding around the figure when bbox_inches is\n            'tight'.\n```\n\nmatplotlib gets its \"tight bbox\" with the appropriately-named get_tightbbox() function, in src/lib/matplotlib/figure.py.  Its docstring proclaims,\n\n```\n        It only accounts axes title, axis labels, and axis\n        ticklabels. Needs improvement.\n```\nand it's true, it does need improvement.\n\nOur graph_plot figure has \"empty\" axes (no title, labels, or ticklabel), but it does have an axes object with a size, which gets used for the tight bbox.  I believe that size comes indirectly from get_minmax_data in sage/plot/plot.py, but I'm not sure.\n\nI can think of a few possibilities to fix the problem, ordered from best to worst.\n\n1) Fix matplotlib get_tightbbox() to actually be a bounding box for the drawing, not just for the \"axes\".  This would definitely be best... it would also fix problems like graphs with loops going off the edge of the plot, etc.\n\n2) Adjust our get_minmax_data functions to be closer to a correct bounding box.  For instance, currently get_minmax_data on a Text object only looks at the center of the text, and doesn't take the size into account.  There's a limit to how good a job we could do, though... we don't want to start digging through font metrics, etc.\n\n3) Set pad_inches to make all our plots \"a little bit bigger\".  The downside, of course, is that this simple approach would affect *all* our plots.\n\nLike I said, I'm giving up now.",
    "created_at": "2010-07-17T19:55:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9529#issuecomment-91531",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

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

archive/issue_comments_091532.json:
```json
{
    "body": "See #9211, where similar issues are dealt with.  With the new matplotlib at #9221, we can add some extra artists whose bounding boxes should be included in the tight bbox calculations (so, for example, we should be able to add the text boxes and then the tight bbox calculations would include those bounds as well).",
    "created_at": "2010-07-18T06:13:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9529#issuecomment-91532",
    "user": "https://github.com/jasongrout"
}
```

See #9211, where similar issues are dealt with.  With the new matplotlib at #9221, we can add some extra artists whose bounding boxes should be included in the tight bbox calculations (so, for example, we should be able to add the text boxes and then the tight bbox calculations would include those bounds as well).



---

archive/issue_comments_091533.json:
```json
{
    "body": "Changing component from algebra to graph theory.",
    "created_at": "2010-07-19T08:53:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9529#issuecomment-91533",
    "user": "https://github.com/rlmill"
}
```

Changing component from algebra to graph theory.



---

archive/issue_comments_091534.json:
```json
{
    "body": "Changing assignee from @aghitza to jason, ncohen, rlm.",
    "created_at": "2010-07-19T08:53:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9529#issuecomment-91534",
    "user": "https://github.com/rlmill"
}
```

Changing assignee from @aghitza to jason, ncohen, rlm.



---

archive/issue_comments_091535.json:
```json
{
    "body": "I can not reproduce this, and this is six years old. I suppose this one can be closed as the code has been changed many times. Fr\u00e9d\u00e9ric, do you agree?",
    "created_at": "2016-07-16T04:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9529#issuecomment-91535",
    "user": "https://github.com/jm58660"
}
```

I can not reproduce this, and this is six years old. I suppose this one can be closed as the code has been changed many times. Frédéric, do you agree?



---

archive/issue_events_023676.json:
```json
{
    "actor": "https://github.com/jm58660",
    "created_at": "2016-07-16T04:40:19Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9529",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9529#event-23676"
}
```



---

archive/issue_comments_091536.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-07-16T04:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9529#issuecomment-91536",
    "user": "https://github.com/jm58660"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091537.json:
```json
{
    "body": "Travis, do you agree that we can close this?",
    "created_at": "2016-08-09T05:06:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9529#issuecomment-91537",
    "user": "https://github.com/jm58660"
}
```

Travis, do you agree that we can close this?



---

archive/issue_comments_091538.json:
```json
{
    "body": "Just pinging this wontfix-confirmation.",
    "created_at": "2016-08-17T12:29:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9529#issuecomment-91538",
    "user": "https://github.com/jm58660"
}
```

Just pinging this wontfix-confirmation.



---

archive/issue_comments_091539.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-08-17T12:37:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9529#issuecomment-91539",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091540.json:
```json
{
    "body": "I can't reproduce it either.",
    "created_at": "2016-08-17T12:37:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9529#issuecomment-91540",
    "user": "https://github.com/tscrim"
}
```

I can't reproduce it either.



---

archive/issue_comments_091541.json:
```json
{
    "body": "Determined to be invalid/duplicate/wontfix (closing as \"wontfix\" as a catch-all resolution).",
    "created_at": "2016-08-30T13:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9529#issuecomment-91541",
    "user": "https://github.com/embray"
}
```

Determined to be invalid/duplicate/wontfix (closing as "wontfix" as a catch-all resolution).



---

archive/issue_events_023677.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2016-08-30T13:32:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9529",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9529#event-23677"
}
```



---

archive/issue_comments_091542.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2016-08-30T13:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9529#issuecomment-91542",
    "user": "https://github.com/embray"
}
```

Resolution: wontfix
