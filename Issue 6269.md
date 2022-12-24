# Issue 6269: Coloring speed up

archive/issues_006269.json:
```json
{
    "body": "Assignee: @williamstein\n\nIt would be nice to have faster versions of things like hue() and rainbow(), and to have them in their own submodule of plot.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6269\n\n",
    "created_at": "2009-06-12T17:25:52Z",
    "labels": [
        "graphics",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "Coloring speed up",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6269",
    "user": "@kcrisman"
}
```
Assignee: @williamstein

It would be nice to have faster versions of things like hue() and rainbow(), and to have them in their own submodule of plot.

Issue created by migration from https://trac.sagemath.org/ticket/6269





---

archive/issue_comments_050074.json:
```json
{
    "body": "Attachment [colors.patch](tarball://root/attachments/some-uuid/ticket6269/colors.patch) by @kcrisman created at 2009-06-12 17:43:56\n\nThis patch does several closely related things:\n\n1. Takes all coloring functions from plot.plot, plot.misc, and plot.tachyon and puts them in new file plot.colors\n2. Writes most of these in Cython, for anywhere between a 3 and 10 times speedup.  This is not so crucial, given that most are called only once or some number of times less than 100 in a given plot, but is still nice.\n3. Changes complex_plot.pyx in two ways:\n   a. Makes the coloring conform with documentation, in that roygbiv goes from positive real axis counterclockwise (increasing argument) instead of the other way around\n   b. Changes the function mag_to_lightness to use log(sqrt(r)+1) instead of log(r+1)\n\nNone of these need explanation except the last subpoint. Previous behavior was so dark as to obscure tick marks even on the doctest plots, and so light as to make plotting even z squared look pretty vague.  This only adds about .02 ms on average to plots, which means that complex_plot(sqrt) takes a little bit longer but complex_plot(zeta) is indistinguishable from before in timing.  One can quibble about it, but this makes zeros still recognizable for polynomials while not allowing them to drown out for zeta, and makes anything yielding high moduli easier to view, while incurring a very modest performance hit, which seems in line with the pedagogical point of complex_plot.",
    "created_at": "2009-06-12T17:43:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6269#issuecomment-50074",
    "user": "@kcrisman"
}
```

Attachment [colors.patch](tarball://root/attachments/some-uuid/ticket6269/colors.patch) by @kcrisman created at 2009-06-12 17:43:56

This patch does several closely related things:

1. Takes all coloring functions from plot.plot, plot.misc, and plot.tachyon and puts them in new file plot.colors
2. Writes most of these in Cython, for anywhere between a 3 and 10 times speedup.  This is not so crucial, given that most are called only once or some number of times less than 100 in a given plot, but is still nice.
3. Changes complex_plot.pyx in two ways:
   a. Makes the coloring conform with documentation, in that roygbiv goes from positive real axis counterclockwise (increasing argument) instead of the other way around
   b. Changes the function mag_to_lightness to use log(sqrt(r)+1) instead of log(r+1)

None of these need explanation except the last subpoint. Previous behavior was so dark as to obscure tick marks even on the doctest plots, and so light as to make plotting even z squared look pretty vague.  This only adds about .02 ms on average to plots, which means that complex_plot(sqrt) takes a little bit longer but complex_plot(zeta) is indistinguishable from before in timing.  One can quibble about it, but this makes zeros still recognizable for polynomials while not allowing them to drown out for zeta, and makes anything yielding high moduli easier to view, while incurring a very modest performance hit, which seems in line with the pedagogical point of complex_plot.



---

archive/issue_comments_050075.json:
```json
{
    "body": "My main concern with this is that converting to something to Cython that is not time critical adds unnecessary build time to the Sage library.  Doing development on Cython files is a lot more annoying than with Python files.  But, I think the other changes are useful.",
    "created_at": "2009-06-13T04:25:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6269#issuecomment-50075",
    "user": "@mwhansen"
}
```

My main concern with this is that converting to something to Cython that is not time critical adds unnecessary build time to the Sage library.  Doing development on Cython files is a lot more annoying than with Python files.  But, I think the other changes are useful.



---

archive/issue_comments_050076.json:
```json
{
    "body": "Replying to [comment:2 mhansen]:\n> My main concern with this is that converting to something to \n> Cython that is not time critical adds unnecessary build time \n> to the Sage library.  Doing development on Cython files is a \n> lot more annoying than with Python files. \n\n+1 -- I strongly agree with this.  One also can't trace through code\nthat is in Cython nearly so easily as with Python.  One should only\nCythonize code where there is a clear important benefit to doing so.\n\nWilliam",
    "created_at": "2009-06-13T09:55:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6269#issuecomment-50076",
    "user": "@williamstein"
}
```

Replying to [comment:2 mhansen]:
> My main concern with this is that converting to something to 
> Cython that is not time critical adds unnecessary build time 
> to the Sage library.  Doing development on Cython files is a 
> lot more annoying than with Python files. 

+1 -- I strongly agree with this.  One also can't trace through code
that is in Cython nearly so easily as with Python.  One should only
Cythonize code where there is a clear important benefit to doing so.

William



---

archive/issue_comments_050077.json:
```json
{
    "body": "Okay, these comments seem reasonable. It was still a good learning experience, and it was very impressive how much faster the commands became.  Perhaps there could be some suggestions added in developer guide as to when not to use Cython.\n\nAnyway, I will try to put up a patch for 1 and 3ab above sometime in the near future!  Description and summary changed accordingly.",
    "created_at": "2009-06-13T23:51:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6269#issuecomment-50077",
    "user": "@kcrisman"
}
```

Okay, these comments seem reasonable. It was still a good learning experience, and it was very impressive how much faster the commands became.  Perhaps there could be some suggestions added in developer guide as to when not to use Cython.

Anyway, I will try to put up a patch for 1 and 3ab above sometime in the near future!  Description and summary changed accordingly.



---

archive/issue_comments_050078.json:
```json
{
    "body": "I get doctest errors on sage.math and my laptop.  They seem to be to do with graph coloring rather than the valuable refactor of the Color stuff.  Could these be separated?\n\n\n```\n/Users/ncalexan/sage-4.0.1.alpha0/sage -tp 10 -long devel/sage/sage/plot/tachyon.py devel/sage/sage/plot/tri_plot.py devel/sage/sage/plot/circle.py devel/sage/sage/plot/text.py devel/sage/sage/plot/line.py devel/sage/sage/plot/complex_plot.pyx devel/sage/sage/server/notebook/interact.py devel/sage/sage/graphs/graph_coloring.py devel/sage/sage/plot/arrow.py devel/sage/sage/plot/contour_plot.py devel/sage/sage/plot/plot.py devel/sage/sage/plot/matrix_plot.py devel/sage/sage/plot/polygon.py devel/sage/sage/graphs/graph_plot.py devel/sage/sage/plot/bezier_path.py devel/sage/sage/graphs/graph.py devel/sage/sage/plot/plot_field.py devel/sage/sage/plot/plot3d/platonic.py devel/sage/sage/plot/point.py devel/sage/sage/plot/all.py devel/sage/sage/plot/plot3d/plot3d.py devel/sage/sage/plot/disk.py devel/sage/sage/plot/misc.py devel/sage/sage/plot/density_plot.py devel/sage/sage/plot/plot3d/texture.py devel/sage/sage/plot/colors.py devel/sage/sage/plot/primitive.py\n\nGlobal iterations: 1\nFile iterations: 1\nUsing long cached timings to run longest doctests first.\nDoctesting 26 files doing 10 jobs in parallel\nsage -t -long devel/sage/sage/plot/bezier_path.py\n         [34.9 s]\nsage -t -long devel/sage/sage/graphs/graph_coloring.py\n**********************************************************************\nFile \"/Users/ncalexan/sage-4.0.1.alpha0/devel/sage-nca/sage/graphs/graph_coloring.py\", line 152:\n    sage: first_coloring(G,3)\nExpected:\n    {'#00ff00': [1, 3], '#ff0000': [0], '#0000ff': [2]}\nGot:\n    {'#ff0000': [0, 1, 2, 3]}\n**********************************************************************\nFile \"/Users/ncalexan/sage-4.0.1.alpha0/devel/sage-nca/sage/graphs/graph_coloring.py\", line 248:\n    sage: Test().random(1)\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/ncalexan/sage/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/ncalexan/sage/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/ncalexan/sage/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_7[3]>\", line 1, in <module>\n        Test().random(Integer(1))###line 248:\n    sage: Test().random(1)\n      File \"/Users/ncalexan/sage-4.0.1.alpha0/local/lib/python2.5/site-packages/sage/graphs/graph_coloring.py\", line 250, in random\n        self.random_all_graph_colorings(tests)\n      File \"/Users/ncalexan/sage-4.0.1.alpha0/local/lib/python2.5/site-packages/sage/graphs/graph_coloring.py\", line 281, in random_all_graph_colorings\n        raise RuntimeError, \"Coloring Failed.\"\n    RuntimeError: Coloring Failed.\n**********************************************************************\nFile \"/Users/ncalexan/sage-4.0.1.alpha0/devel/sage-nca/sage/graphs/graph_coloring.py\", line 263:\n    sage: Test().random_all_graph_colorings(1)\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/ncalexan/sage/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/ncalexan/sage/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/ncalexan/sage/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_8[3]>\", line 1, in <module>\n        Test().random_all_graph_colorings(Integer(1))###line 263:\n    sage: Test().random_all_graph_colorings(1)\n      File \"/Users/ncalexan/sage-4.0.1.alpha0/local/lib/python2.5/site-packages/sage/graphs/graph_coloring.py\", line 281, in random_all_graph_colorings\n        raise RuntimeError, \"Coloring Failed.\"\n    RuntimeError: Coloring Failed.\n**********************************************************************\n3 items had failures:\n   1 of   5 in __main__.example_2\n   1 of   4 in __main__.example_7\n   1 of   4 in __main__.example_8\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file /Users/ncalexan/sage-4.0.1.alpha0/tmp/.doctest_graph_coloring.py\n         [36.1 s]\nsage -t -long devel/sage/sage/plot/colors.py\n         [36.4 s]\nsage -t -long devel/sage/sage/plot/density_plot.py\n         [42.3 s]\nsage -t -long devel/sage/sage/plot/arrow.py\n         [43.8 s]\nsage -t -long devel/sage/sage/plot/misc.py\n         [11.4 s]\nsage -t -long devel/sage/sage/plot/circle.py\n         [58.4 s]\nsage -t -long devel/sage/sage/plot/matrix_plot.py\n         [23.4 s]\nsage -t -long devel/sage/sage/plot/disk.py\n         [25.7 s]\nsage -t -long devel/sage/sage/plot/complex_plot.pyx\n         [69.4 s]\nsage -t -long devel/sage/sage/plot/plot3d/texture.py\n         [11.6 s]\nsage -t -long devel/sage/sage/plot/plot3d/platonic.py\n         [18.7 s]\nsage -t -long devel/sage/sage/graphs/graph_plot.py\n         [79.5 s]\nsage -t -long devel/sage/sage/plot/primitive.py\n         [15.4 s]\nsage -t -long devel/sage/sage/plot/plot_field.py\n         [28.1 s]\nsage -t -long devel/sage/sage/plot/plot3d/plot3d.py\n         [32.2 s]\nsage -t -long devel/sage/sage/plot/line.py\n         [62.4 s]\nsage -t -long devel/sage/sage/plot/tri_plot.py\n         [10.4 s]\nsage -t -long devel/sage/sage/server/notebook/interact.py\n         [12.5 s]\nsage -t -long devel/sage/sage/plot/contour_plot.py\n         [103.6 s]\nsage -t -long devel/sage/sage/plot/text.py\n         [18.0 s]\nsage -t -long devel/sage/sage/plot/point.py\n         [36.7 s]\nsage -t -long devel/sage/sage/plot/polygon.py\n         [36.7 s]\nsage -t -long devel/sage/sage/plot/tachyon.py\n         [53.6 s]\nsage -t -long devel/sage/sage/plot/plot.py\n         [129.0 s]\nsage -t -long devel/sage/sage/graphs/graph.py\n**********************************************************************\nFile \"/Users/ncalexan/sage-4.0.1.alpha0/devel/sage-nca/sage/graphs/graph.py\", line 6160:\n    sage: G._color_by_label()\nExpected:\n    {'#00ffff': [((1,4)(3,5), (1,5,4), (3,4,5)),\n     ...],\n     '#ff0000': [((1,4)(3,5), (1,5,4,2,3), (1,2,3,4,5)),\n     ...]}\nGot:\n    {'#ff0000': [((1,4)(3,5), (1,5,4), (3,4,5)), ((1,3)(2,5), (1,4,5,2,3), (3,4,5)), ((2,3,5), (2,4,5), (3,4,5)), ((1,3,4,5,2), (1,4,3,5,2), (3,4,5)), ((1,4,3), (1,5,3), (3,4,5)), ((1,3,2,4,5), (1,4,3,2,5), (3,4,5)), ((1,3,5), (1,4,5), (3,4,5)), ((1,3,4,2,5), (1,4,2,3,5), (3,4,5)), ((1,5,3), (1,3)(4,5), (3,4,5)), ((1,4,5,2,3), (1,5,2,4,3), (3,4,5)), ((1,5,2,4,3), (1,3)(2,5), (3,4,5)), ((1,5,4,3,2), (1,3,2), (3,4,5)), ((2,5,4), (2,3,4), (3,4,5)), ((1,4,2,5,3), (1,5,4,2,3), (3,4,5)), ((1,3)(2,4), (1,4,2,5,3), (3,4,5)), ((1,5,3,4,2), (1,3,5,4,2), (3,4,5)), ((1,2,3,5,4), (1,2,4), (3,4,5)), ((1,4,5,3,2), (1,5,4,3,2), (3,4,5)), ((2,4)(3,5), (2,5,4), (3,4,5)), ((1,2,3,4,5), (1,2,4,3,5), (3,4,5)), ((1,4)(2,5), (1,5,2,3,4), (3,4,5)), ((2,4,3), (2,5,3), (3,4,5)), ((1,3,2,5,4), (1,4)(2,3), (3,4,5)), ((1,4,2), (1,5,3,4,2), (3,4,5)), ((3,4,5), (3,5,4), (3,4,5)), ((1,2)(3,5), (1,2)(4,5), (3,4,5)), ((1,3,4), (1,4)(3,5), (3,4,5)), ((3,5,4), (), (3,4,5)), ((1,2)(4,5), (1,2)(3,4), (3,4,5)), ((1,4,3,5,2), (1,5,2), (3,4,5)), ((), (3,4,5), (3,4,5)), ((1,5,3,2,4), (1,3,2,5,4), (3,4,5)), ((1,4,3,2,5), (1,5)(2,3), (3,4,5)), ((2,5,3), (2,3)(4,5), (3,4,5)), ((1,2,4,3,5), (1,2,5), (3,4,5)), ((2,3)(4,5), (2,4,3), (3,4,5)), ((2,3,4), (2,4)(3,5), (3,4,5)), ((1,2,4,5,3), (1,2,5,4,3), (3,4,5)), ((1,5,2), (1,3,4,5,2), (3,4,5)), ((1,3,5,4,2), (1,4,2), (3,4,5)), ((1,5,4), (1,3,4), (3,4,5)), ((1,3)(4,5), (1,4,3), (3,4,5)), ((1,2,3), (1,2,4,5,3), (3,4,5)), ((1,3,2), (1,4,5,3,2), (3,4,5)), ((1,2)(3,4), (1,2)(3,5), (3,4,5)), ((1,2,4), (1,2,5,3,4), (3,4,5)), ((1,4,2,3,5), (1,5)(2,4), (3,4,5)), ((1,2,5,3,4), (1,2,3,5,4), (3,4,5)), ((1,5,2,3,4), (1,3,5,2,4), (3,4,5)), ((1,5,4,2,3), (1,3)(2,4), (3,4,5)), ((1,2,5,4,3), (1,2,3), (3,4,5)), ((2,5)(3,4), (2,3,5), (3,4,5)), ((1,2,5), (1,2,3,4,5), (3,4,5)), ((1,5)(2,4), (1,3,4,2,5), (3,4,5)), ((2,4,5), (2,5)(3,4), (3,4,5)), ((1,4)(2,3), (1,5,3,2,4), (3,4,5)), ((1,5)(2,3), (1,3,2,4,5), (3,4,5)), ((1,3,5,2,4), (1,4)(2,5), (3,4,5)), ((1,4,5), (1,5)(3,4), (3,4,5)), ((1,5)(3,4), (1,3,5), (3,4,5))]}\n**********************************************************************\nFile \"/Users/ncalexan/sage-4.0.1.alpha0/devel/sage-nca/sage/graphs/graph.py\", line 8902:\n    sage: P = G.coloring(); P\nExpected:\n    [[1, 2, 3], [0, 5, 6], [4]]\nGot:\n    [[0, 1, 4, 2, 5, 6, 3]]\n**********************************************************************\nFile \"/Users/ncalexan/sage-4.0.1.alpha0/devel/sage-nca/sage/graphs/graph.py\", line 8907:\n    sage: for c in sorted(H.keys()):\n       print c, H[c]\nExpected:\n    #0000ff [4]\n    #00ff00 [1, 2, 3]\n    #ff0000 [0, 5, 6]\nGot:\n    #ff0000 [0, 1, 4, 2, 5, 6, 3]\n**********************************************************************\n2 items had failures:\n   1 of   5 in __main__.example_132\n   2 of   8 in __main__.example_163\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file /Users/ncalexan/sage-4.0.1.alpha0/tmp/.doctest_graph.py\n         [287.4 s]\n \n----------------------------------------------------------------------\n\nThe following tests failed:\n\n        sage -t -long devel/sage/sage/graphs/graph_coloring.py # 3 doctests failed\n        sage -t -long devel/sage/sage/graphs/graph.py # 3 doctests failed\n----------------------------------------------------------------------\nTotal time for all tests: 287.5 seconds\nTests failed!\n```\n",
    "created_at": "2009-06-15T20:30:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6269#issuecomment-50078",
    "user": "@ncalexan"
}
```

I get doctest errors on sage.math and my laptop.  They seem to be to do with graph coloring rather than the valuable refactor of the Color stuff.  Could these be separated?


```
/Users/ncalexan/sage-4.0.1.alpha0/sage -tp 10 -long devel/sage/sage/plot/tachyon.py devel/sage/sage/plot/tri_plot.py devel/sage/sage/plot/circle.py devel/sage/sage/plot/text.py devel/sage/sage/plot/line.py devel/sage/sage/plot/complex_plot.pyx devel/sage/sage/server/notebook/interact.py devel/sage/sage/graphs/graph_coloring.py devel/sage/sage/plot/arrow.py devel/sage/sage/plot/contour_plot.py devel/sage/sage/plot/plot.py devel/sage/sage/plot/matrix_plot.py devel/sage/sage/plot/polygon.py devel/sage/sage/graphs/graph_plot.py devel/sage/sage/plot/bezier_path.py devel/sage/sage/graphs/graph.py devel/sage/sage/plot/plot_field.py devel/sage/sage/plot/plot3d/platonic.py devel/sage/sage/plot/point.py devel/sage/sage/plot/all.py devel/sage/sage/plot/plot3d/plot3d.py devel/sage/sage/plot/disk.py devel/sage/sage/plot/misc.py devel/sage/sage/plot/density_plot.py devel/sage/sage/plot/plot3d/texture.py devel/sage/sage/plot/colors.py devel/sage/sage/plot/primitive.py

Global iterations: 1
File iterations: 1
Using long cached timings to run longest doctests first.
Doctesting 26 files doing 10 jobs in parallel
sage -t -long devel/sage/sage/plot/bezier_path.py
         [34.9 s]
sage -t -long devel/sage/sage/graphs/graph_coloring.py
**********************************************************************
File "/Users/ncalexan/sage-4.0.1.alpha0/devel/sage-nca/sage/graphs/graph_coloring.py", line 152:
    sage: first_coloring(G,3)
Expected:
    {'#00ff00': [1, 3], '#ff0000': [0], '#0000ff': [2]}
Got:
    {'#ff0000': [0, 1, 2, 3]}
**********************************************************************
File "/Users/ncalexan/sage-4.0.1.alpha0/devel/sage-nca/sage/graphs/graph_coloring.py", line 248:
    sage: Test().random(1)
Exception raised:
    Traceback (most recent call last):
      File "/Users/ncalexan/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/ncalexan/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/ncalexan/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_7[3]>", line 1, in <module>
        Test().random(Integer(1))###line 248:
    sage: Test().random(1)
      File "/Users/ncalexan/sage-4.0.1.alpha0/local/lib/python2.5/site-packages/sage/graphs/graph_coloring.py", line 250, in random
        self.random_all_graph_colorings(tests)
      File "/Users/ncalexan/sage-4.0.1.alpha0/local/lib/python2.5/site-packages/sage/graphs/graph_coloring.py", line 281, in random_all_graph_colorings
        raise RuntimeError, "Coloring Failed."
    RuntimeError: Coloring Failed.
**********************************************************************
File "/Users/ncalexan/sage-4.0.1.alpha0/devel/sage-nca/sage/graphs/graph_coloring.py", line 263:
    sage: Test().random_all_graph_colorings(1)
Exception raised:
    Traceback (most recent call last):
      File "/Users/ncalexan/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/ncalexan/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/ncalexan/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[3]>", line 1, in <module>
        Test().random_all_graph_colorings(Integer(1))###line 263:
    sage: Test().random_all_graph_colorings(1)
      File "/Users/ncalexan/sage-4.0.1.alpha0/local/lib/python2.5/site-packages/sage/graphs/graph_coloring.py", line 281, in random_all_graph_colorings
        raise RuntimeError, "Coloring Failed."
    RuntimeError: Coloring Failed.
**********************************************************************
3 items had failures:
   1 of   5 in __main__.example_2
   1 of   4 in __main__.example_7
   1 of   4 in __main__.example_8
***Test Failed*** 3 failures.
For whitespace errors, see the file /Users/ncalexan/sage-4.0.1.alpha0/tmp/.doctest_graph_coloring.py
         [36.1 s]
sage -t -long devel/sage/sage/plot/colors.py
         [36.4 s]
sage -t -long devel/sage/sage/plot/density_plot.py
         [42.3 s]
sage -t -long devel/sage/sage/plot/arrow.py
         [43.8 s]
sage -t -long devel/sage/sage/plot/misc.py
         [11.4 s]
sage -t -long devel/sage/sage/plot/circle.py
         [58.4 s]
sage -t -long devel/sage/sage/plot/matrix_plot.py
         [23.4 s]
sage -t -long devel/sage/sage/plot/disk.py
         [25.7 s]
sage -t -long devel/sage/sage/plot/complex_plot.pyx
         [69.4 s]
sage -t -long devel/sage/sage/plot/plot3d/texture.py
         [11.6 s]
sage -t -long devel/sage/sage/plot/plot3d/platonic.py
         [18.7 s]
sage -t -long devel/sage/sage/graphs/graph_plot.py
         [79.5 s]
sage -t -long devel/sage/sage/plot/primitive.py
         [15.4 s]
sage -t -long devel/sage/sage/plot/plot_field.py
         [28.1 s]
sage -t -long devel/sage/sage/plot/plot3d/plot3d.py
         [32.2 s]
sage -t -long devel/sage/sage/plot/line.py
         [62.4 s]
sage -t -long devel/sage/sage/plot/tri_plot.py
         [10.4 s]
sage -t -long devel/sage/sage/server/notebook/interact.py
         [12.5 s]
sage -t -long devel/sage/sage/plot/contour_plot.py
         [103.6 s]
sage -t -long devel/sage/sage/plot/text.py
         [18.0 s]
sage -t -long devel/sage/sage/plot/point.py
         [36.7 s]
sage -t -long devel/sage/sage/plot/polygon.py
         [36.7 s]
sage -t -long devel/sage/sage/plot/tachyon.py
         [53.6 s]
sage -t -long devel/sage/sage/plot/plot.py
         [129.0 s]
sage -t -long devel/sage/sage/graphs/graph.py
**********************************************************************
File "/Users/ncalexan/sage-4.0.1.alpha0/devel/sage-nca/sage/graphs/graph.py", line 6160:
    sage: G._color_by_label()
Expected:
    {'#00ffff': [((1,4)(3,5), (1,5,4), (3,4,5)),
     ...],
     '#ff0000': [((1,4)(3,5), (1,5,4,2,3), (1,2,3,4,5)),
     ...]}
Got:
    {'#ff0000': [((1,4)(3,5), (1,5,4), (3,4,5)), ((1,3)(2,5), (1,4,5,2,3), (3,4,5)), ((2,3,5), (2,4,5), (3,4,5)), ((1,3,4,5,2), (1,4,3,5,2), (3,4,5)), ((1,4,3), (1,5,3), (3,4,5)), ((1,3,2,4,5), (1,4,3,2,5), (3,4,5)), ((1,3,5), (1,4,5), (3,4,5)), ((1,3,4,2,5), (1,4,2,3,5), (3,4,5)), ((1,5,3), (1,3)(4,5), (3,4,5)), ((1,4,5,2,3), (1,5,2,4,3), (3,4,5)), ((1,5,2,4,3), (1,3)(2,5), (3,4,5)), ((1,5,4,3,2), (1,3,2), (3,4,5)), ((2,5,4), (2,3,4), (3,4,5)), ((1,4,2,5,3), (1,5,4,2,3), (3,4,5)), ((1,3)(2,4), (1,4,2,5,3), (3,4,5)), ((1,5,3,4,2), (1,3,5,4,2), (3,4,5)), ((1,2,3,5,4), (1,2,4), (3,4,5)), ((1,4,5,3,2), (1,5,4,3,2), (3,4,5)), ((2,4)(3,5), (2,5,4), (3,4,5)), ((1,2,3,4,5), (1,2,4,3,5), (3,4,5)), ((1,4)(2,5), (1,5,2,3,4), (3,4,5)), ((2,4,3), (2,5,3), (3,4,5)), ((1,3,2,5,4), (1,4)(2,3), (3,4,5)), ((1,4,2), (1,5,3,4,2), (3,4,5)), ((3,4,5), (3,5,4), (3,4,5)), ((1,2)(3,5), (1,2)(4,5), (3,4,5)), ((1,3,4), (1,4)(3,5), (3,4,5)), ((3,5,4), (), (3,4,5)), ((1,2)(4,5), (1,2)(3,4), (3,4,5)), ((1,4,3,5,2), (1,5,2), (3,4,5)), ((), (3,4,5), (3,4,5)), ((1,5,3,2,4), (1,3,2,5,4), (3,4,5)), ((1,4,3,2,5), (1,5)(2,3), (3,4,5)), ((2,5,3), (2,3)(4,5), (3,4,5)), ((1,2,4,3,5), (1,2,5), (3,4,5)), ((2,3)(4,5), (2,4,3), (3,4,5)), ((2,3,4), (2,4)(3,5), (3,4,5)), ((1,2,4,5,3), (1,2,5,4,3), (3,4,5)), ((1,5,2), (1,3,4,5,2), (3,4,5)), ((1,3,5,4,2), (1,4,2), (3,4,5)), ((1,5,4), (1,3,4), (3,4,5)), ((1,3)(4,5), (1,4,3), (3,4,5)), ((1,2,3), (1,2,4,5,3), (3,4,5)), ((1,3,2), (1,4,5,3,2), (3,4,5)), ((1,2)(3,4), (1,2)(3,5), (3,4,5)), ((1,2,4), (1,2,5,3,4), (3,4,5)), ((1,4,2,3,5), (1,5)(2,4), (3,4,5)), ((1,2,5,3,4), (1,2,3,5,4), (3,4,5)), ((1,5,2,3,4), (1,3,5,2,4), (3,4,5)), ((1,5,4,2,3), (1,3)(2,4), (3,4,5)), ((1,2,5,4,3), (1,2,3), (3,4,5)), ((2,5)(3,4), (2,3,5), (3,4,5)), ((1,2,5), (1,2,3,4,5), (3,4,5)), ((1,5)(2,4), (1,3,4,2,5), (3,4,5)), ((2,4,5), (2,5)(3,4), (3,4,5)), ((1,4)(2,3), (1,5,3,2,4), (3,4,5)), ((1,5)(2,3), (1,3,2,4,5), (3,4,5)), ((1,3,5,2,4), (1,4)(2,5), (3,4,5)), ((1,4,5), (1,5)(3,4), (3,4,5)), ((1,5)(3,4), (1,3,5), (3,4,5))]}
**********************************************************************
File "/Users/ncalexan/sage-4.0.1.alpha0/devel/sage-nca/sage/graphs/graph.py", line 8902:
    sage: P = G.coloring(); P
Expected:
    [[1, 2, 3], [0, 5, 6], [4]]
Got:
    [[0, 1, 4, 2, 5, 6, 3]]
**********************************************************************
File "/Users/ncalexan/sage-4.0.1.alpha0/devel/sage-nca/sage/graphs/graph.py", line 8907:
    sage: for c in sorted(H.keys()):
       print c, H[c]
Expected:
    #0000ff [4]
    #00ff00 [1, 2, 3]
    #ff0000 [0, 5, 6]
Got:
    #ff0000 [0, 1, 4, 2, 5, 6, 3]
**********************************************************************
2 items had failures:
   1 of   5 in __main__.example_132
   2 of   8 in __main__.example_163
***Test Failed*** 3 failures.
For whitespace errors, see the file /Users/ncalexan/sage-4.0.1.alpha0/tmp/.doctest_graph.py
         [287.4 s]
 
----------------------------------------------------------------------

The following tests failed:

        sage -t -long devel/sage/sage/graphs/graph_coloring.py # 3 doctests failed
        sage -t -long devel/sage/sage/graphs/graph.py # 3 doctests failed
----------------------------------------------------------------------
Total time for all tests: 287.5 seconds
Tests failed!
```




---

archive/issue_comments_050079.json:
```json
{
    "body": "I should have caught this - I only tested files in plot/, forgot about the graphs/ changes...\n\nAt first I thought that somehow rainbow() was giving only one color to all these graphs (which have n=3) but as far as I can tell rainbow works fine.  And (for example) doing\n\n```\nsage: from sage.graphs.graph_coloring import *\nsage: G = Graph({0:[1,2,3],1:[2]})\nsage: list(all_graph_colorings(G,3))\n```\n\ngives the correct answer.  For some reason something in the generator (as opposed to list) definition of all_graph_colorings() is causing a problem, but why this wouldn't have cropped up before is puzzling.  I will try to look at it soon.",
    "created_at": "2009-06-16T02:39:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6269#issuecomment-50079",
    "user": "@kcrisman"
}
```

I should have caught this - I only tested files in plot/, forgot about the graphs/ changes...

At first I thought that somehow rainbow() was giving only one color to all these graphs (which have n=3) but as far as I can tell rainbow works fine.  And (for example) doing

```
sage: from sage.graphs.graph_coloring import *
sage: G = Graph({0:[1,2,3],1:[2]})
sage: list(all_graph_colorings(G,3))
```

gives the correct answer.  For some reason something in the generator (as opposed to list) definition of all_graph_colorings() is causing a problem, but why this wouldn't have cropped up before is puzzling.  I will try to look at it soon.



---

archive/issue_comments_050080.json:
```json
{
    "body": "Changing assignee from @williamstein to @kcrisman.",
    "created_at": "2009-06-16T14:19:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6269#issuecomment-50080",
    "user": "@kcrisman"
}
```

Changing assignee from @williamstein to @kcrisman.



---

archive/issue_comments_050081.json:
```json
{
    "body": "I finally figured out what is going on.  \n\n```\nsage: rainbow(3)\n['#ff0000', '#00ff00', '#0000ff']\nsage: rainbow(int(3))\n['#ff0000', '#ff0000', '#ff0000']\n```\n\nThis is because \n\n```\nsage: int(1)/3\n1/3\nsage: int(1)/int(3)\n0\n```\n\nand in all the above cases I believe the rainbow input is a Python int coming from a range() or len().  Very annoying.\n\nThe patch trac_6269.patch should now pass graph and plot doctests, at least it does for me.",
    "created_at": "2009-06-16T14:19:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6269#issuecomment-50081",
    "user": "@kcrisman"
}
```

I finally figured out what is going on.  

```
sage: rainbow(3)
['#ff0000', '#00ff00', '#0000ff']
sage: rainbow(int(3))
['#ff0000', '#ff0000', '#ff0000']
```

This is because 

```
sage: int(1)/3
1/3
sage: int(1)/int(3)
0
```

and in all the above cases I believe the rainbow input is a Python int coming from a range() or len().  Very annoying.

The patch trac_6269.patch should now pass graph and plot doctests, at least it does for me.



---

archive/issue_comments_050082.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-16T14:19:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6269#issuecomment-50082",
    "user": "@kcrisman"
}
```

Changing status from new to assigned.



---

archive/issue_comments_050083.json:
```json
{
    "body": "Attachment [trac_6269.patch](tarball://root/attachments/some-uuid/ticket6269/trac_6269.patch) by @kcrisman created at 2009-06-16 14:19:28",
    "created_at": "2009-06-16T14:19:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6269#issuecomment-50083",
    "user": "@kcrisman"
}
```

Attachment [trac_6269.patch](tarball://root/attachments/some-uuid/ticket6269/trac_6269.patch) by @kcrisman created at 2009-06-16 14:19:28



---

archive/issue_comments_050084.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-06-16T17:49:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6269#issuecomment-50084",
    "user": "@ncalexan"
}
```

Looks good to me.



---

archive/issue_comments_050085.json:
```json
{
    "body": "Some hunk failures when applied against Sage 4.1.alpha0:\n\n```\nsage: hg_sage.apply(\"http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6269/trac_6269.patch\")\nAttempting to load remote file: http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6269/trac_6269.patch\nLoading: [......]\ncd \"/scratch/mvngu/sage-4.1.alpha0-sage.math-only-x86_64-Linux/devel/sage\" && hg status\ncd \"/scratch/mvngu/sage-4.1.alpha0-sage.math-only-x86_64-Linux/devel/sage\" && hg status\ncd \"/scratch/mvngu/sage-4.1.alpha0-sage.math-only-x86_64-Linux/devel/sage\" && hg import   \"/home/mvngu/.sage/temp/sage.math.washington.edu/11758/tmp_1.patch\"\napplying /home/mvngu/.sage/temp/sage.math.washington.edu/11758/tmp_1.patch\npatching file sage/plot/complex_plot.pyx\nHunk #2 FAILED at 43\nHunk #6 FAILED at 195\n2 out of 6 hunks FAILED -- saving rejects to file sage/plot/complex_plot.pyx.rej\nabort: patch failed to apply\n```\n",
    "created_at": "2009-06-24T22:22:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6269#issuecomment-50085",
    "user": "mvngu"
}
```

Some hunk failures when applied against Sage 4.1.alpha0:

```
sage: hg_sage.apply("http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6269/trac_6269.patch")
Attempting to load remote file: http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6269/trac_6269.patch
Loading: [......]
cd "/scratch/mvngu/sage-4.1.alpha0-sage.math-only-x86_64-Linux/devel/sage" && hg status
cd "/scratch/mvngu/sage-4.1.alpha0-sage.math-only-x86_64-Linux/devel/sage" && hg status
cd "/scratch/mvngu/sage-4.1.alpha0-sage.math-only-x86_64-Linux/devel/sage" && hg import   "/home/mvngu/.sage/temp/sage.math.washington.edu/11758/tmp_1.patch"
applying /home/mvngu/.sage/temp/sage.math.washington.edu/11758/tmp_1.patch
patching file sage/plot/complex_plot.pyx
Hunk #2 FAILED at 43
Hunk #6 FAILED at 195
2 out of 6 hunks FAILED -- saving rejects to file sage/plot/complex_plot.pyx.rej
abort: patch failed to apply
```




---

archive/issue_comments_050086.json:
```json
{
    "body": "After testing the library of Sage 4.1.alpha0, I received the following test failures, as reported at this by [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/c15b5f57e380cc19) thread by Robert Miller. \n\n```\nThe following tests failed:\n\n\tsage -t -long devel/sage-main/sage/databases/database.py # 20 doctests failed\n\tsage -t -long devel/sage-main/sage/geometry/polyhedra.py # 1 doctests failed\n\tsage -t -long devel/sage-main/sage/graphs/graph.py # 25 doctests failed\n```\n\nSo when rebasing the patch `trac_6269.patch`, I think the part that touches `sage/graphs/graph.py` should be left out. As Robert Miller is currently working on a Cython implementation of a graph theory backend, called c_graph (see #6085), perhaps the graph theory modules should not be touched by the rebase so as to prevent any further complication with getting c_graph in.",
    "created_at": "2009-06-24T23:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6269#issuecomment-50086",
    "user": "mvngu"
}
```

After testing the library of Sage 4.1.alpha0, I received the following test failures, as reported at this by [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/c15b5f57e380cc19) thread by Robert Miller. 

```
The following tests failed:

	sage -t -long devel/sage-main/sage/databases/database.py # 20 doctests failed
	sage -t -long devel/sage-main/sage/geometry/polyhedra.py # 1 doctests failed
	sage -t -long devel/sage-main/sage/graphs/graph.py # 25 doctests failed
```

So when rebasing the patch `trac_6269.patch`, I think the part that touches `sage/graphs/graph.py` should be left out. As Robert Miller is currently working on a Cython implementation of a graph theory backend, called c_graph (see #6085), perhaps the graph theory modules should not be touched by the rebase so as to prevent any further complication with getting c_graph in.



---

archive/issue_comments_050087.json:
```json
{
    "body": "The patch `trac_6269-rebased.patch` is rebased against Sage 4.1.alpha0. Unlike the patch `trac_6269.patch`, the `trac_6269-rebased.patch` doesn't touch anything to do with the graph theory modules.",
    "created_at": "2009-06-25T00:11:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6269#issuecomment-50087",
    "user": "mvngu"
}
```

The patch `trac_6269-rebased.patch` is rebased against Sage 4.1.alpha0. Unlike the patch `trac_6269.patch`, the `trac_6269-rebased.patch` doesn't touch anything to do with the graph theory modules.



---

archive/issue_comments_050088.json:
```json
{
    "body": "Reinstating ncalexan's positive review.",
    "created_at": "2009-06-25T00:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6269#issuecomment-50088",
    "user": "mvngu"
}
```

Reinstating ncalexan's positive review.



---

archive/issue_comments_050089.json:
```json
{
    "body": "Replying to [comment:13 mvngu]:\n> After testing the library of Sage 4.1.alpha0, I received the following test failures, as reported at this by [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/c15b5f57e380cc19) thread by Robert Miller. \n> {{{\n> The following tests failed:\n> \n> \tsage -t -long devel/sage-main/sage/databases/database.py # 20 doctests failed\n> \tsage -t -long devel/sage-main/sage/geometry/polyhedra.py # 1 doctests failed\n> \tsage -t -long devel/sage-main/sage/graphs/graph.py # 25 doctests failed\n> }}}\n> So when rebasing the patch `trac_6269.patch`, I think the part that touches `sage/graphs/graph.py` should be left out. As Robert Miller is currently working on a Cython implementation of a graph theory backend, called c_graph (see #6085), perhaps the graph theory modules should not be touched by the rebase so as to prevent any further complication with getting c_graph in.\n\nBut rlm says in the same thread,  \"These are all due to the removal of graph_isom.pyx, and I will be...\".  So that should not be the problem.  In fact, I am not sure how one can NOT include graph stuff, because the graph theory modules need some of the coloring stuff, e.g. in graph_colorings.py and several other such files there is the line \n\n\n```\nfrom sage.plot.plot import rainbow\n```\n\n\nand that is no longer where rainbow lives.  Now, it is true that rainbow lives in the global namespace, so maybe those lines are all redundant, but as it stands they might cause failure at startup because sage.plot.plot doesn't have rainbow anymore.  \n\nSince sage.plot.plot does import rainbow, maybe that's enough for rainbow to be re-imported into those files from there for now.  I don't feel I have enough of an understanding of Python imports to judge all that.  But at the very least the import statements should be correct or deleted; it makes no sense to leave in imports of a non-existent function which cause no problems (now that I fixed the Integer thing noted above).",
    "created_at": "2009-06-25T13:42:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6269#issuecomment-50089",
    "user": "@kcrisman"
}
```

Replying to [comment:13 mvngu]:
> After testing the library of Sage 4.1.alpha0, I received the following test failures, as reported at this by [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/c15b5f57e380cc19) thread by Robert Miller. 
> {{{
> The following tests failed:
> 
> 	sage -t -long devel/sage-main/sage/databases/database.py # 20 doctests failed
> 	sage -t -long devel/sage-main/sage/geometry/polyhedra.py # 1 doctests failed
> 	sage -t -long devel/sage-main/sage/graphs/graph.py # 25 doctests failed
> }}}
> So when rebasing the patch `trac_6269.patch`, I think the part that touches `sage/graphs/graph.py` should be left out. As Robert Miller is currently working on a Cython implementation of a graph theory backend, called c_graph (see #6085), perhaps the graph theory modules should not be touched by the rebase so as to prevent any further complication with getting c_graph in.

But rlm says in the same thread,  "These are all due to the removal of graph_isom.pyx, and I will be...".  So that should not be the problem.  In fact, I am not sure how one can NOT include graph stuff, because the graph theory modules need some of the coloring stuff, e.g. in graph_colorings.py and several other such files there is the line 


```
from sage.plot.plot import rainbow
```


and that is no longer where rainbow lives.  Now, it is true that rainbow lives in the global namespace, so maybe those lines are all redundant, but as it stands they might cause failure at startup because sage.plot.plot doesn't have rainbow anymore.  

Since sage.plot.plot does import rainbow, maybe that's enough for rainbow to be re-imported into those files from there for now.  I don't feel I have enough of an understanding of Python imports to judge all that.  But at the very least the import statements should be correct or deleted; it makes no sense to leave in imports of a non-existent function which cause no problems (now that I fixed the Integer thing noted above).



---

archive/issue_comments_050090.json:
```json
{
    "body": "rebased against Sage 4.1.alpha1",
    "created_at": "2009-06-25T21:15:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6269#issuecomment-50090",
    "user": "mvngu"
}
```

rebased against Sage 4.1.alpha1



---

archive/issue_comments_050091.json:
```json
{
    "body": "Attachment [trac_6269-rebased.patch](tarball://root/attachments/some-uuid/ticket6269/trac_6269-rebased.patch) by mvngu created at 2009-06-25 21:46:54\n\nThe patch `trac_6269-rebased.patch` is rebased against Sage 4.1.alpha1. It also touches those graph theory modules that `trac_6269.patch` touches. For all files that `trac_6269-rebased.patch` touches, testing passed with options `-t -long`. I'm re-instating Nick Alexander's positive review, unless there's a reason not to.",
    "created_at": "2009-06-25T21:46:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6269#issuecomment-50091",
    "user": "mvngu"
}
```

Attachment [trac_6269-rebased.patch](tarball://root/attachments/some-uuid/ticket6269/trac_6269-rebased.patch) by mvngu created at 2009-06-25 21:46:54

The patch `trac_6269-rebased.patch` is rebased against Sage 4.1.alpha1. It also touches those graph theory modules that `trac_6269.patch` touches. For all files that `trac_6269-rebased.patch` touches, testing passed with options `-t -long`. I'm re-instating Nick Alexander's positive review, unless there's a reason not to.



---

archive/issue_comments_050092.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-26T17:44:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6269#issuecomment-50092",
    "user": "boothby"
}
```

Resolution: fixed
