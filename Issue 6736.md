# Issue 6736: spell-check all modules under sage/symbolic

archive/issues_006736.json:
```json
{
    "body": "Assignee: tba\n\nAs the subject says.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6736\n\n",
    "created_at": "2009-08-11T10:54:05Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "title": "spell-check all modules under sage/symbolic",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6736",
    "user": "mvngu"
}
```
Assignee: tba

As the subject says.

Issue created by migration from https://trac.sagemath.org/ticket/6736





---

archive/issue_comments_055209.json:
```json
{
    "body": "Attachment\n\nbased on Sage 4.1.1.rc2",
    "created_at": "2009-08-11T17:38:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6736",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6736#issuecomment-55209",
    "user": "mvngu"
}
```

Attachment

based on Sage 4.1.1.rc2



---

archive/issue_comments_055210.json:
```json
{
    "body": "Only touches documentation, and all changes seem correct.",
    "created_at": "2009-08-11T19:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6736",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6736#issuecomment-55210",
    "user": "mhampton"
}
```

Only touches documentation, and all changes seem correct.



---

archive/issue_comments_055211.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-12T06:40:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6736",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6736#issuecomment-55211",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_055212.json:
```json
{
    "body": "I had the following one-time doctest failure. It's not repeatable.\n\n```\nsage -t -long devel/sage-main/sage/graphs/graph_bundle.py\nlibpng error: Image width or height is zero in IHDR\n**********************************************************************\nFile \"/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/devel/sage-main/sage/graphs/graph_bundle.py\", line 163:\n    sage: B.plot()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_5[5]>\", line 1, in <module>\n        B.plot()###line 163:\n    sage: B.plot()\n      File \"sage_object.pyx\", line 101, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1387)\n      File \"/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python/site-packages/sage/plot/plot.py\", line 873, in _repr_\n        self.show()\n      File \"/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python/site-packages/sage/plot/plot.py\", line 1360, in show\n        self.save(DOCTEST_MODE_FILE, **options)\n      File \"/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python/site-packages/sage/plot/plot.py\", line 1683, in save\n        canvas.print_figure(filename, dpi=dpi)\n      File \"/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python/site-packages/matplotlib/backend_bases.py\", line 1453, in print_figure\n        **kwargs)\n      File \"/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python/site-packages/matplotlib/backends/backend_agg.py\", line 334, in print_png\n        filename_or_obj, self.figure.dpi)\n    RuntimeError: Error building image\n**********************************************************************\n1 items had failures:\n   1 of   6 in __main__.example_5\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/tmp/.doctest_graph_bundle.py\n\t [2.8 s]\n```\n",
    "created_at": "2009-08-12T06:40:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6736",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6736#issuecomment-55212",
    "user": "mvngu"
}
```

I had the following one-time doctest failure. It's not repeatable.

```
sage -t -long devel/sage-main/sage/graphs/graph_bundle.py
libpng error: Image width or height is zero in IHDR
**********************************************************************
File "/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/devel/sage-main/sage/graphs/graph_bundle.py", line 163:
    sage: B.plot()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[5]>", line 1, in <module>
        B.plot()###line 163:
    sage: B.plot()
      File "sage_object.pyx", line 101, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1387)
      File "/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python/site-packages/sage/plot/plot.py", line 873, in _repr_
        self.show()
      File "/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python/site-packages/sage/plot/plot.py", line 1360, in show
        self.save(DOCTEST_MODE_FILE, **options)
      File "/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python/site-packages/sage/plot/plot.py", line 1683, in save
        canvas.print_figure(filename, dpi=dpi)
      File "/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python/site-packages/matplotlib/backend_bases.py", line 1453, in print_figure
        **kwargs)
      File "/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python/site-packages/matplotlib/backends/backend_agg.py", line 334, in print_png
        filename_or_obj, self.figure.dpi)
    RuntimeError: Error building image
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_5
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/tmp/.doctest_graph_bundle.py
	 [2.8 s]
```

