# Issue 9089: Graphics3dGroup __add__ modifies its arguments

archive/issues_009089.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @robertwb mhampton @kcrisman @seblabbe @ppurka\n\nIn an attempt to optimize, in some cases the __add__ method of Graphics3dGroup modifies its arguments instead of returning a new Graphics3dGroup object.  This breaks the user expectation, as illustrated below:\n\n\n```\na=point3d([1,0,0])+point3d([0,1,0])\nb=point3d([0,0,1])\na # shows 2 points\na+b # shows all 3 points\na # Now this shows 3 points!!!\n```\n\n\nThe attached patch deletes the offending optimization.  If fast summing is needed, then the user can either create a Graphics3dGroup object themselves, or use something like `sage.misc.misc.balanced_sum`\n\nIssue created by migration from https://trac.sagemath.org/ticket/9089\n\n",
    "created_at": "2010-05-29T20:21:42Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Graphics3dGroup __add__ modifies its arguments",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9089",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @aghitza

CC:  @robertwb mhampton @kcrisman @seblabbe @ppurka

In an attempt to optimize, in some cases the __add__ method of Graphics3dGroup modifies its arguments instead of returning a new Graphics3dGroup object.  This breaks the user expectation, as illustrated below:


```
a=point3d([1,0,0])+point3d([0,1,0])
b=point3d([0,0,1])
a # shows 2 points
a+b # shows all 3 points
a # Now this shows 3 points!!!
```


The attached patch deletes the offending optimization.  If fast summing is needed, then the user can either create a Graphics3dGroup object themselves, or use something like `sage.misc.misc.balanced_sum`

Issue created by migration from https://trac.sagemath.org/ticket/9089





---

archive/issue_comments_084269.json:
```json
{
    "body": "Changing component from algebra to graphics.",
    "created_at": "2010-05-29T20:21:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84269",
    "user": "https://github.com/jasongrout"
}
```

Changing component from algebra to graphics.



---

archive/issue_comments_084270.json:
```json
{
    "body": "Changing assignee from @aghitza to jason, was.",
    "created_at": "2010-05-29T20:21:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84270",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from @aghitza to jason, was.



---

archive/issue_events_022289.json:
```json
{
    "actor": "https://github.com/jasongrout",
    "created_at": "2010-05-29T20:21:55Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "milestone": "sage-4.4.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9089#event-22289"
}
```



---

archive/issue_comments_084271.json:
```json
{
    "body": "Attachment [trac-9089-graphics3d.patch](tarball://root/attachments/some-uuid/ticket9089/trac-9089-graphics3d.patch) by @jasongrout created at 2010-05-29 20:42:55\n\nCredit goes to Ben Woodruff for reporting this issue.",
    "created_at": "2010-05-29T20:42:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84271",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-9089-graphics3d.patch](tarball://root/attachments/some-uuid/ticket9089/trac-9089-graphics3d.patch) by @jasongrout created at 2010-05-29 20:42:55

Credit goes to Ben Woodruff for reporting this issue.



---

archive/issue_comments_084272.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-29T20:42:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84272",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084273.json:
```json
{
    "body": "Do you have any stats on how much this affects performance?",
    "created_at": "2010-06-01T09:50:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84273",
    "user": "https://github.com/robertwb"
}
```

Do you have any stats on how much this affects performance?



---

archive/issue_comments_084274.json:
```json
{
    "body": "Before patch:\n\n\n```\nsage: from sage.misc.misc import balanced_sum\nsage: from sage.plot.plot3d.base import Graphics3dGroup\nsage: lines=[line3d([[0,0,0],[cos(t),sin(t),1]]) for t in [0,0.05,..,6]]; len(lines)\n121\nsage: %timeit p=sum(lines)\n625 loops, best of 3: 82.1 \u00b5s per loop\nsage: lines=[line3d([[0,0,0],[cos(t),sin(t),1]]) for t in [0,0.05,..,6]]; len(lines)\n121\nsage: %timeit p=balanced_sum(lines)\n625 loops, best of 3: 455 \u00b5s per loop\nsage: lines=[line3d([[0,0,0],[cos(t),sin(t),1]]) for t in [0,0.05,..,6]]; len(lines)\n121\nsage: %timeit p=Graphics3dGroup(lines)\n625 loops, best of 3: 179 \u00b5s per loop\n```\n\n\n\nAfter patch:\n\n\n```\n\nsage: from sage.misc.misc import balanced_sum\nsage: from sage.plot.plot3d.base import Graphics3dGroup\nsage: lines=[line3d([[0,0,0],[cos(t),sin(t),1]]) for t in [0,0.05,..,6]]; len(lines)\n121\nsage: %timeit p=sum(lines)\n625 loops, best of 3: 1.48 ms per loop\nsage: lines=[line3d([[0,0,0],[cos(t),sin(t),1]]) for t in [0,0.05,..,6]]; len(lines)\n121\nsage: %timeit p=balanced_sum(lines)\n625 loops, best of 3: 1.45 ms per loop\nsage: lines=[line3d([[0,0,0],[cos(t),sin(t),1]]) for t in [0,0.05,..,6]]; len(lines)\n121\nsage: %timeit p=Graphics3dGroup(lines)\n625 loops, best of 3: 180 \u00b5s per loop\n\n```\n\n\nSo, as could be expected, performance of sum is impacted quite a bit.  However, I would still say that the current behavior is wrong, and correctness trumps speed, especially if the overall total speed is still quite fast.",
    "created_at": "2010-06-02T20:26:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84274",
    "user": "https://github.com/jasongrout"
}
```

Before patch:


```
sage: from sage.misc.misc import balanced_sum
sage: from sage.plot.plot3d.base import Graphics3dGroup
sage: lines=[line3d([[0,0,0],[cos(t),sin(t),1]]) for t in [0,0.05,..,6]]; len(lines)
121
sage: %timeit p=sum(lines)
625 loops, best of 3: 82.1 µs per loop
sage: lines=[line3d([[0,0,0],[cos(t),sin(t),1]]) for t in [0,0.05,..,6]]; len(lines)
121
sage: %timeit p=balanced_sum(lines)
625 loops, best of 3: 455 µs per loop
sage: lines=[line3d([[0,0,0],[cos(t),sin(t),1]]) for t in [0,0.05,..,6]]; len(lines)
121
sage: %timeit p=Graphics3dGroup(lines)
625 loops, best of 3: 179 µs per loop
```



After patch:


```

sage: from sage.misc.misc import balanced_sum
sage: from sage.plot.plot3d.base import Graphics3dGroup
sage: lines=[line3d([[0,0,0],[cos(t),sin(t),1]]) for t in [0,0.05,..,6]]; len(lines)
121
sage: %timeit p=sum(lines)
625 loops, best of 3: 1.48 ms per loop
sage: lines=[line3d([[0,0,0],[cos(t),sin(t),1]]) for t in [0,0.05,..,6]]; len(lines)
121
sage: %timeit p=balanced_sum(lines)
625 loops, best of 3: 1.45 ms per loop
sage: lines=[line3d([[0,0,0],[cos(t),sin(t),1]]) for t in [0,0.05,..,6]]; len(lines)
121
sage: %timeit p=Graphics3dGroup(lines)
625 loops, best of 3: 180 µs per loop

```


So, as could be expected, performance of sum is impacted quite a bit.  However, I would still say that the current behavior is wrong, and correctness trumps speed, especially if the overall total speed is still quite fast.



---

archive/issue_comments_084275.json:
```json
{
    "body": "Since we now have a Sage-written sum function, maybe we could just have the sum function call first_object._sum(list of things to sum) if it exists, and make a _sum method that does a Graphics3dGroup(sum_list) behind the scenes?  This would also help with a recent ticket that ncohen opened about sum being really slow for linear programming stuff.",
    "created_at": "2010-06-02T20:30:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84275",
    "user": "https://github.com/jasongrout"
}
```

Since we now have a Sage-written sum function, maybe we could just have the sum function call first_object._sum(list of things to sum) if it exists, and make a _sum method that does a Graphics3dGroup(sum_list) behind the scenes?  This would also help with a recent ticket that ncohen opened about sum being really slow for linear programming stuff.



---

archive/issue_comments_084276.json:
```json
{
    "body": "Replying to [comment:5 jason]:\n> Since we now have a Sage-written sum function, maybe we could just have the sum function call first_object._sum(list of things to sum) if it exists, and make a _sum method that does a Graphics3dGroup(sum_list) behind the scenes?  This would also help with a recent ticket that ncohen opened about sum being really slow for linear programming stuff.\n\nThat's a great idea! (Certainly a new ticket.)",
    "created_at": "2010-06-02T20:50:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84276",
    "user": "https://github.com/robertwb"
}
```

Replying to [comment:5 jason]:
> Since we now have a Sage-written sum function, maybe we could just have the sum function call first_object._sum(list of things to sum) if it exists, and make a _sum method that does a Graphics3dGroup(sum_list) behind the scenes?  This would also help with a recent ticket that ncohen opened about sum being really slow for linear programming stuff.

That's a great idea! (Certainly a new ticket.)



---

archive/issue_comments_084277.json:
```json
{
    "body": "Replying to [comment:6 robertwb]:\n> Replying to [comment:5 jason]:\n> > Since we now have a Sage-written sum function, maybe we could just have the sum function call first_object._sum(list of things to sum) if it exists, and make a _sum method that does a Graphics3dGroup(sum_list) behind the scenes?  This would also help with a recent ticket that ncohen opened about sum being really slow for linear programming stuff.\n> \n> That's a great idea! (Certainly a new ticket.)\n\nActually, I just checked, and something like it is already being done.  If you do sum(something,...), then if something has a sum method, it is called: something.sum(...).  Of course, this won't work with lists or generators.\n\nAnyways, feel free to review this ticket!",
    "created_at": "2010-06-02T20:53:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84277",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:6 robertwb]:
> Replying to [comment:5 jason]:
> > Since we now have a Sage-written sum function, maybe we could just have the sum function call first_object._sum(list of things to sum) if it exists, and make a _sum method that does a Graphics3dGroup(sum_list) behind the scenes?  This would also help with a recent ticket that ncohen opened about sum being really slow for linear programming stuff.
> 
> That's a great idea! (Certainly a new ticket.)

Actually, I just checked, and something like it is already being done.  If you do sum(something,...), then if something has a sum method, it is called: something.sum(...).  Of course, this won't work with lists or generators.

Anyways, feel free to review this ticket!



---

archive/issue_comments_084278.json:
```json
{
    "body": "Okay, the sum stuff is at #9115",
    "created_at": "2010-06-02T22:26:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84278",
    "user": "https://github.com/jasongrout"
}
```

Okay, the sum stuff is at #9115



---

archive/issue_comments_084279.json:
```json
{
    "body": "ping about reviewing this bug fix.  There has been several times in the past few weeks that this bug has caught me.",
    "created_at": "2010-06-15T14:14:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84279",
    "user": "https://github.com/jasongrout"
}
```

ping about reviewing this bug fix.  There has been several times in the past few weeks that this bug has caught me.



---

archive/issue_comments_084280.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-15T17:08:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84280",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084281.json:
```json
{
    "body": "Looks ok.  \n\n```\nsage: len(G)\n2\n```\n\nin the old example as desired, inheritance is correct.  Currently building doc to make sure looks right... okay. Should `:meth:__add__` point to the method in `sage.plot.plot3d.base.Graphics3d`via hyperlink?  Otherwise positive review, though of course the speed thing would be great to take care of if #9115 becomes available.",
    "created_at": "2010-06-15T17:08:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84281",
    "user": "https://github.com/kcrisman"
}
```

Looks ok.  

```
sage: len(G)
2
```

in the old example as desired, inheritance is correct.  Currently building doc to make sure looks right... okay. Should `:meth:__add__` point to the method in `sage.plot.plot3d.base.Graphics3d`via hyperlink?  Otherwise positive review, though of course the speed thing would be great to take care of if #9115 becomes available.



---

archive/issue_comments_084282.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-06-30T21:33:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84282",
    "user": "https://github.com/loefflerd"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_084283.json:
```json
{
    "body": "I'm getting a doctest failure with this patch on 4.5.alpha1:\n\n```\n**********************************************************************\nFile \"/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/plot/plot.py\", line 428:\n    sage: g.show()\nException raised:\n    Traceback (most recent call last):\n      File \"/storage/masiao/sage-4.5.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/storage/masiao/sage-4.5.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/storage/masiao/sage-4.5.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[11]>\", line 1, in <module>\n        g.show()###line 428:\n    sage: g.show()\n      File \"base.pyx\", line 1081, in sage.plot.plot3d.base.Graphics3d.show (sage/plot/plot3d/base.c:10184)\n      File \"base.pyx\", line 524, in sage.plot.plot3d.base.Graphics3d.tachyon (sage/plot/plot3d/base.c:4785)\n      File \"base.pyx\", line 1408, in sage.plot.plot3d.base.Graphics3dGroup.texture_set (sage/plot/plot3d/base.c:13371)\n      File \"base.pyx\", line 1408, in sage.plot.plot3d.base.Graphics3dGroup.texture_set (sage/plot/plot3d/base.c:13371)\n      File \"base.pyx\", line 1408, in sage.plot.plot3d.base.Graphics3dGroup.texture_set (sage/plot/plot3d/base.c:13371)\n      File \"base.pyx\", line 1408, in sage.plot.plot3d.base.Graphics3dGroup.texture_set (sage/plot/plot3d/base.c:13387)\n    TypeError: reduce() of empty sequence with no initial value\n**********************************************************************\n```\n\n\nAlso, if I install this together with the patches at #9066 I get a bunch more failures coming in:\n\n```\nsage -t  -long devel/sage/sage/plot/plot3d/shapes2.py # 5 doctests failed\n```\n",
    "created_at": "2010-06-30T21:33:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84283",
    "user": "https://github.com/loefflerd"
}
```

I'm getting a doctest failure with this patch on 4.5.alpha1:

```
**********************************************************************
File "/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/plot/plot.py", line 428:
    sage: g.show()
Exception raised:
    Traceback (most recent call last):
      File "/storage/masiao/sage-4.5.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/storage/masiao/sage-4.5.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/storage/masiao/sage-4.5.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[11]>", line 1, in <module>
        g.show()###line 428:
    sage: g.show()
      File "base.pyx", line 1081, in sage.plot.plot3d.base.Graphics3d.show (sage/plot/plot3d/base.c:10184)
      File "base.pyx", line 524, in sage.plot.plot3d.base.Graphics3d.tachyon (sage/plot/plot3d/base.c:4785)
      File "base.pyx", line 1408, in sage.plot.plot3d.base.Graphics3dGroup.texture_set (sage/plot/plot3d/base.c:13371)
      File "base.pyx", line 1408, in sage.plot.plot3d.base.Graphics3dGroup.texture_set (sage/plot/plot3d/base.c:13371)
      File "base.pyx", line 1408, in sage.plot.plot3d.base.Graphics3dGroup.texture_set (sage/plot/plot3d/base.c:13371)
      File "base.pyx", line 1408, in sage.plot.plot3d.base.Graphics3dGroup.texture_set (sage/plot/plot3d/base.c:13387)
    TypeError: reduce() of empty sequence with no initial value
**********************************************************************
```


Also, if I install this together with the patches at #9066 I get a bunch more failures coming in:

```
sage -t  -long devel/sage/sage/plot/plot3d/shapes2.py # 5 doctests failed
```




---

archive/issue_comments_084284.json:
```json
{
    "body": "Attachment [trac-9089-graphics3d-2.patch](tarball://root/attachments/some-uuid/ticket9089/trac-9089-graphics3d-2.patch) by @jasongrout created at 2010-09-07 17:53:12\n\napply on top of previous patches",
    "created_at": "2010-09-07T17:53:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84284",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-9089-graphics3d-2.patch](tarball://root/attachments/some-uuid/ticket9089/trac-9089-graphics3d-2.patch) by @jasongrout created at 2010-09-07 17:53:12

apply on top of previous patches



---

archive/issue_comments_084285.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-07T17:54:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84285",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084286.json:
```json
{
    "body": "The errors should be taken care of now: on 4.5.2, plot/*.py* and plot/plot3d/*.py* all pass doctests.  Apply the two patches on top of each other.",
    "created_at": "2010-09-07T17:54:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84286",
    "user": "https://github.com/jasongrout"
}
```

The errors should be taken care of now: on 4.5.2, plot/*.py* and plot/plot3d/*.py* all pass doctests.  Apply the two patches on top of each other.



---

archive/issue_comments_084287.json:
```json
{
    "body": "Ping to someone to look at this.  I believe I corrected all of the failing doctests.",
    "created_at": "2010-09-22T06:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84287",
    "user": "https://github.com/jasongrout"
}
```

Ping to someone to look at this.  I believe I corrected all of the failing doctests.



---

archive/issue_comments_084288.json:
```json
{
    "body": "Looks OK to me. I don't use the graphics code myself; but it had a positive review before I grumbled about failing doctests, and I can confirm that the doctests are now fixed, so I feel that merits giving it a positive review again.",
    "created_at": "2010-09-22T09:29:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84288",
    "user": "https://github.com/loefflerd"
}
```

Looks OK to me. I don't use the graphics code myself; but it had a positive review before I grumbled about failing doctests, and I can confirm that the doctests are now fixed, so I feel that merits giving it a positive review again.



---

archive/issue_comments_084289.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-22T09:29:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84289",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084290.json:
```json
{
    "body": "Thanks.  This bug hit me again yesterday.",
    "created_at": "2010-09-22T15:33:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84290",
    "user": "https://github.com/jasongrout"
}
```

Thanks.  This bug hit me again yesterday.



---

archive/issue_comments_084291.json:
```json
{
    "body": "Hang on a minute. I was lazy and ran long doctests on graphics and only short doctests on everything else, so I missed a weird side-effect of this patch: if you install the two patches above on vanilla 4.6.alpha1 and do\n\n```\nsage -t -long sage/combinat/root_system/weyl_group.py\n```\n\nthen you get an infinite loop:\n\n```\nFile \"/storage/masiao/sage-4.6.alpha1/devel/sage-hacking/sage/combinat/root_system/weyl_group.py\", line 27:\n    sage: d.show3d(color_by_label=True, edge_size=0.01, vertex_size=0.03) #long time (less than one minute)\nException raised:\n    Traceback (most recent call last):\n      File \"/storage/masiao/sage-4.6.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/storage/masiao/sage-4.6.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/storage/masiao/sage-4.6.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[7]>\", line 1, in <module>\n        d.show3d(color_by_label=True, edge_size=RealNumber('0.01'), vertex_size=RealNumber('0.03')) #long time (less than one minute)###line 27:\n    sage: d.show3d(color_by_label=True, edge_size=0.01, vertex_size=0.03) #long time (less than one minute)\n      File \"/storage/masiao/sage-4.6.alpha1/local/lib/python/site-packages/sage/graphs/generic_graph.py\", line 12407, in show3d\n        color_by_label=color_by_label, **kwds).show()\n      File \"base.pyx\", line 1048, in sage.plot.plot3d.base.Graphics3d.show (sage/plot/plot3d/base.c:9726)\n      File \"base.pyx\", line 953, in sage.plot.plot3d.base.Graphics3d._process_viewing_options (sage/plot/plot3d/base.c:9519)\n      File \"base.pyx\", line 198, in sage.plot.plot3d.base.Graphics3d._determine_frame_aspect_ratio (sage/plot/plot3d/base.c:3307)\n      File \"base.pyx\", line 214, in sage.plot.plot3d.base.Graphics3d._safe_bounding_box (sage/plot/plot3d/base.c:3460)\n      File \"base.pyx\", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)\n      File \"base.pyx\", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)\n      File \"base.pyx\", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)\n      File \"base.pyx\", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)\n      File \"base.pyx\", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)\n      File \"base.pyx\", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)\n      File \"base.pyx\", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)\n[ ... ]\n      File \"base.pyx\", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)\n      File \"base.pyx\", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)\n      File \"base.pyx\", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)\n      File \"base.pyx\", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)\n      File \"base.pyx\", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12234)\n    RuntimeError: maximum recursion depth exceeded in __subclasscheck__\n**********************************************************************\n1 items had failures:\n   1 of   8 in __main__.example_0\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/masiao/.sage//tmp/.doctest_weyl_group.py\n         [41.9 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t -long \"devel/sage-hacking/sage/combinat/root_system/weyl_group.py\"\nTotal time for all tests: 41.9 seconds\n```\n\n\nApologies for my sloppiness in not having caught this bug earlier.",
    "created_at": "2010-09-23T12:31:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84291",
    "user": "https://github.com/loefflerd"
}
```

Hang on a minute. I was lazy and ran long doctests on graphics and only short doctests on everything else, so I missed a weird side-effect of this patch: if you install the two patches above on vanilla 4.6.alpha1 and do

```
sage -t -long sage/combinat/root_system/weyl_group.py
```

then you get an infinite loop:

```
File "/storage/masiao/sage-4.6.alpha1/devel/sage-hacking/sage/combinat/root_system/weyl_group.py", line 27:
    sage: d.show3d(color_by_label=True, edge_size=0.01, vertex_size=0.03) #long time (less than one minute)
Exception raised:
    Traceback (most recent call last):
      File "/storage/masiao/sage-4.6.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/storage/masiao/sage-4.6.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/storage/masiao/sage-4.6.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[7]>", line 1, in <module>
        d.show3d(color_by_label=True, edge_size=RealNumber('0.01'), vertex_size=RealNumber('0.03')) #long time (less than one minute)###line 27:
    sage: d.show3d(color_by_label=True, edge_size=0.01, vertex_size=0.03) #long time (less than one minute)
      File "/storage/masiao/sage-4.6.alpha1/local/lib/python/site-packages/sage/graphs/generic_graph.py", line 12407, in show3d
        color_by_label=color_by_label, **kwds).show()
      File "base.pyx", line 1048, in sage.plot.plot3d.base.Graphics3d.show (sage/plot/plot3d/base.c:9726)
      File "base.pyx", line 953, in sage.plot.plot3d.base.Graphics3d._process_viewing_options (sage/plot/plot3d/base.c:9519)
      File "base.pyx", line 198, in sage.plot.plot3d.base.Graphics3d._determine_frame_aspect_ratio (sage/plot/plot3d/base.c:3307)
      File "base.pyx", line 214, in sage.plot.plot3d.base.Graphics3d._safe_bounding_box (sage/plot/plot3d/base.c:3460)
      File "base.pyx", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)
      File "base.pyx", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)
      File "base.pyx", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)
      File "base.pyx", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)
      File "base.pyx", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)
      File "base.pyx", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)
      File "base.pyx", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)
[ ... ]
      File "base.pyx", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)
      File "base.pyx", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)
      File "base.pyx", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)
      File "base.pyx", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)
      File "base.pyx", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12234)
    RuntimeError: maximum recursion depth exceeded in __subclasscheck__
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/masiao/.sage//tmp/.doctest_weyl_group.py
         [41.9 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage-hacking/sage/combinat/root_system/weyl_group.py"
Total time for all tests: 41.9 seconds
```


Apologies for my sloppiness in not having caught this bug earlier.



---

archive/issue_comments_084292.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-09-23T12:31:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84292",
    "user": "https://github.com/loefflerd"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_084293.json:
```json
{
    "body": "Replying to [comment:16 davidloeffler]:\n\n\n> Apologies for my sloppiness in not having caught this bug earlier.\n\nWell, please accept my apologies for not thinking we had to check ptestlong.  I'll fix it and run ptestlong before posting a new patch!\n\nThanks for your patience.",
    "created_at": "2010-09-23T12:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84293",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:16 davidloeffler]:


> Apologies for my sloppiness in not having caught this bug earlier.

Well, please accept my apologies for not thinking we had to check ptestlong.  I'll fix it and run ptestlong before posting a new patch!

Thanks for your patience.



---

archive/issue_events_022290.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "milestone": "sage-4.4.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9089#event-22290"
}
```



---

archive/issue_events_022291.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9089#event-22291"
}
```



---

archive/issue_events_022292.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9089#event-22292"
}
```



---

archive/issue_events_022293.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9089#event-22293"
}
```



---

archive/issue_events_022294.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9089#event-22294"
}
```



---

archive/issue_events_022295.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9089#event-22295"
}
```



---

archive/issue_events_022296.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9089#event-22296"
}
```



---

archive/issue_events_022297.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9089#event-22297"
}
```



---

archive/issue_comments_084294.json:
```json
{
    "body": "solved in #17258",
    "created_at": "2015-03-18T20:54:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84294",
    "user": "https://github.com/fchapoton"
}
```

solved in #17258



---

archive/issue_events_022298.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2015-03-18T20:54:46Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9089#event-22298"
}
```



---

archive/issue_events_022299.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2015-03-18T20:54:46Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9089#event-22299"
}
```



---

archive/issue_comments_084295.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-03-18T20:54:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84295",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084296.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-03-18T21:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84296",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084297.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-03-21T09:30:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84297",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_022300.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-03-21T09:30:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9089#event-22300"
}
```
