# Issue 9089: Graphics3dGroup __add__ modifies its arguments

archive/issues_009089.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  robertwb mhampton kcrisman slabbe ppurka\n\nIn an attempt to optimize, in some cases the __add__ method of Graphics3dGroup modifies its arguments instead of returning a new Graphics3dGroup object.  This breaks the user expectation, as illustrated below:\n\n\n```\na=point3d([1,0,0])+point3d([0,1,0])\nb=point3d([0,0,1])\na # shows 2 points\na+b # shows all 3 points\na # Now this shows 3 points!!!\n```\n\n\nThe attached patch deletes the offending optimization.  If fast summing is needed, then the user can either create a Graphics3dGroup object themselves, or use something like `sage.misc.misc.balanced_sum`\n\nIssue created by migration from https://trac.sagemath.org/ticket/9089\n\n",
    "created_at": "2010-05-29T20:21:42Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "Graphics3dGroup __add__ modifies its arguments",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9089",
    "user": "jason"
}
```
Assignee: AlexGhitza

CC:  robertwb mhampton kcrisman slabbe ppurka

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

archive/issue_comments_084405.json:
```json
{
    "body": "Changing component from algebra to graphics.",
    "created_at": "2010-05-29T20:21:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84405",
    "user": "jason"
}
```

Changing component from algebra to graphics.



---

archive/issue_comments_084406.json:
```json
{
    "body": "Changing assignee from AlexGhitza to jason, was.",
    "created_at": "2010-05-29T20:21:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84406",
    "user": "jason"
}
```

Changing assignee from AlexGhitza to jason, was.



---

archive/issue_comments_084407.json:
```json
{
    "body": "Attachment\n\nCredit goes to Ben Woodruff for reporting this issue.",
    "created_at": "2010-05-29T20:42:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84407",
    "user": "jason"
}
```

Attachment

Credit goes to Ben Woodruff for reporting this issue.



---

archive/issue_comments_084408.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-29T20:42:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84408",
    "user": "jason"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084409.json:
```json
{
    "body": "Do you have any stats on how much this affects performance?",
    "created_at": "2010-06-01T09:50:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84409",
    "user": "robertwb"
}
```

Do you have any stats on how much this affects performance?



---

archive/issue_comments_084410.json:
```json
{
    "body": "Before patch:\n\n\n```\nsage: from sage.misc.misc import balanced_sum\nsage: from sage.plot.plot3d.base import Graphics3dGroup\nsage: lines=[line3d([[0,0,0],[cos(t),sin(t),1]]) for t in [0,0.05,..,6]]; len(lines)\n121\nsage: %timeit p=sum(lines)\n625 loops, best of 3: 82.1 \u00b5s per loop\nsage: lines=[line3d([[0,0,0],[cos(t),sin(t),1]]) for t in [0,0.05,..,6]]; len(lines)\n121\nsage: %timeit p=balanced_sum(lines)\n625 loops, best of 3: 455 \u00b5s per loop\nsage: lines=[line3d([[0,0,0],[cos(t),sin(t),1]]) for t in [0,0.05,..,6]]; len(lines)\n121\nsage: %timeit p=Graphics3dGroup(lines)\n625 loops, best of 3: 179 \u00b5s per loop\n```\n\n\n\nAfter patch:\n\n\n```\n\nsage: from sage.misc.misc import balanced_sum\nsage: from sage.plot.plot3d.base import Graphics3dGroup\nsage: lines=[line3d([[0,0,0],[cos(t),sin(t),1]]) for t in [0,0.05,..,6]]; len(lines)\n121\nsage: %timeit p=sum(lines)\n625 loops, best of 3: 1.48 ms per loop\nsage: lines=[line3d([[0,0,0],[cos(t),sin(t),1]]) for t in [0,0.05,..,6]]; len(lines)\n121\nsage: %timeit p=balanced_sum(lines)\n625 loops, best of 3: 1.45 ms per loop\nsage: lines=[line3d([[0,0,0],[cos(t),sin(t),1]]) for t in [0,0.05,..,6]]; len(lines)\n121\nsage: %timeit p=Graphics3dGroup(lines)\n625 loops, best of 3: 180 \u00b5s per loop\n\n```\n\n\nSo, as could be expected, performance of sum is impacted quite a bit.  However, I would still say that the current behavior is wrong, and correctness trumps speed, especially if the overall total speed is still quite fast.",
    "created_at": "2010-06-02T20:26:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84410",
    "user": "jason"
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

archive/issue_comments_084411.json:
```json
{
    "body": "Since we now have a Sage-written sum function, maybe we could just have the sum function call first_object._sum(list of things to sum) if it exists, and make a _sum method that does a Graphics3dGroup(sum_list) behind the scenes?  This would also help with a recent ticket that ncohen opened about sum being really slow for linear programming stuff.",
    "created_at": "2010-06-02T20:30:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84411",
    "user": "jason"
}
```

Since we now have a Sage-written sum function, maybe we could just have the sum function call first_object._sum(list of things to sum) if it exists, and make a _sum method that does a Graphics3dGroup(sum_list) behind the scenes?  This would also help with a recent ticket that ncohen opened about sum being really slow for linear programming stuff.



---

archive/issue_comments_084412.json:
```json
{
    "body": "Replying to [comment:5 jason]:\n> Since we now have a Sage-written sum function, maybe we could just have the sum function call first_object._sum(list of things to sum) if it exists, and make a _sum method that does a Graphics3dGroup(sum_list) behind the scenes?  This would also help with a recent ticket that ncohen opened about sum being really slow for linear programming stuff.\n\nThat's a great idea! (Certainly a new ticket.)",
    "created_at": "2010-06-02T20:50:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84412",
    "user": "robertwb"
}
```

Replying to [comment:5 jason]:
> Since we now have a Sage-written sum function, maybe we could just have the sum function call first_object._sum(list of things to sum) if it exists, and make a _sum method that does a Graphics3dGroup(sum_list) behind the scenes?  This would also help with a recent ticket that ncohen opened about sum being really slow for linear programming stuff.

That's a great idea! (Certainly a new ticket.)



---

archive/issue_comments_084413.json:
```json
{
    "body": "Replying to [comment:6 robertwb]:\n> Replying to [comment:5 jason]:\n> > Since we now have a Sage-written sum function, maybe we could just have the sum function call first_object._sum(list of things to sum) if it exists, and make a _sum method that does a Graphics3dGroup(sum_list) behind the scenes?  This would also help with a recent ticket that ncohen opened about sum being really slow for linear programming stuff.\n> \n> That's a great idea! (Certainly a new ticket.)\n\nActually, I just checked, and something like it is already being done.  If you do sum(something,...), then if something has a sum method, it is called: something.sum(...).  Of course, this won't work with lists or generators.\n\nAnyways, feel free to review this ticket!",
    "created_at": "2010-06-02T20:53:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84413",
    "user": "jason"
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

archive/issue_comments_084414.json:
```json
{
    "body": "Okay, the sum stuff is at #9115",
    "created_at": "2010-06-02T22:26:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84414",
    "user": "jason"
}
```

Okay, the sum stuff is at #9115



---

archive/issue_comments_084415.json:
```json
{
    "body": "ping about reviewing this bug fix.  There has been several times in the past few weeks that this bug has caught me.",
    "created_at": "2010-06-15T14:14:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84415",
    "user": "jason"
}
```

ping about reviewing this bug fix.  There has been several times in the past few weeks that this bug has caught me.



---

archive/issue_comments_084416.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-15T17:08:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84416",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084417.json:
```json
{
    "body": "Looks ok.  \n\n```\nsage: len(G)\n2\n```\n\nin the old example as desired, inheritance is correct.  Currently building doc to make sure looks right... okay. Should `:meth:__add__` point to the method in `sage.plot.plot3d.base.Graphics3d`via hyperlink?  Otherwise positive review, though of course the speed thing would be great to take care of if #9115 becomes available.",
    "created_at": "2010-06-15T17:08:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84417",
    "user": "kcrisman"
}
```

Looks ok.  

```
sage: len(G)
2
```

in the old example as desired, inheritance is correct.  Currently building doc to make sure looks right... okay. Should `:meth:__add__` point to the method in `sage.plot.plot3d.base.Graphics3d`via hyperlink?  Otherwise positive review, though of course the speed thing would be great to take care of if #9115 becomes available.



---

archive/issue_comments_084418.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-06-30T21:33:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84418",
    "user": "davidloeffler"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_084419.json:
```json
{
    "body": "I'm getting a doctest failure with this patch on 4.5.alpha1:\n\n```\n**********************************************************************\nFile \"/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/plot/plot.py\", line 428:\n    sage: g.show()\nException raised:\n    Traceback (most recent call last):\n      File \"/storage/masiao/sage-4.5.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/storage/masiao/sage-4.5.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/storage/masiao/sage-4.5.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[11]>\", line 1, in <module>\n        g.show()###line 428:\n    sage: g.show()\n      File \"base.pyx\", line 1081, in sage.plot.plot3d.base.Graphics3d.show (sage/plot/plot3d/base.c:10184)\n      File \"base.pyx\", line 524, in sage.plot.plot3d.base.Graphics3d.tachyon (sage/plot/plot3d/base.c:4785)\n      File \"base.pyx\", line 1408, in sage.plot.plot3d.base.Graphics3dGroup.texture_set (sage/plot/plot3d/base.c:13371)\n      File \"base.pyx\", line 1408, in sage.plot.plot3d.base.Graphics3dGroup.texture_set (sage/plot/plot3d/base.c:13371)\n      File \"base.pyx\", line 1408, in sage.plot.plot3d.base.Graphics3dGroup.texture_set (sage/plot/plot3d/base.c:13371)\n      File \"base.pyx\", line 1408, in sage.plot.plot3d.base.Graphics3dGroup.texture_set (sage/plot/plot3d/base.c:13387)\n    TypeError: reduce() of empty sequence with no initial value\n**********************************************************************\n```\n\n\nAlso, if I install this together with the patches at #9066 I get a bunch more failures coming in:\n\n```\nsage -t  -long devel/sage/sage/plot/plot3d/shapes2.py # 5 doctests failed\n```\n",
    "created_at": "2010-06-30T21:33:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84419",
    "user": "davidloeffler"
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

archive/issue_comments_084420.json:
```json
{
    "body": "Attachment\n\napply on top of previous patches",
    "created_at": "2010-09-07T17:53:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84420",
    "user": "jason"
}
```

Attachment

apply on top of previous patches



---

archive/issue_comments_084421.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-07T17:54:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84421",
    "user": "jason"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084422.json:
```json
{
    "body": "The errors should be taken care of now: on 4.5.2, plot/*.py* and plot/plot3d/*.py* all pass doctests.  Apply the two patches on top of each other.",
    "created_at": "2010-09-07T17:54:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84422",
    "user": "jason"
}
```

The errors should be taken care of now: on 4.5.2, plot/*.py* and plot/plot3d/*.py* all pass doctests.  Apply the two patches on top of each other.



---

archive/issue_comments_084423.json:
```json
{
    "body": "Ping to someone to look at this.  I believe I corrected all of the failing doctests.",
    "created_at": "2010-09-22T06:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84423",
    "user": "jason"
}
```

Ping to someone to look at this.  I believe I corrected all of the failing doctests.



---

archive/issue_comments_084424.json:
```json
{
    "body": "Looks OK to me. I don't use the graphics code myself; but it had a positive review before I grumbled about failing doctests, and I can confirm that the doctests are now fixed, so I feel that merits giving it a positive review again.",
    "created_at": "2010-09-22T09:29:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84424",
    "user": "davidloeffler"
}
```

Looks OK to me. I don't use the graphics code myself; but it had a positive review before I grumbled about failing doctests, and I can confirm that the doctests are now fixed, so I feel that merits giving it a positive review again.



---

archive/issue_comments_084425.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-22T09:29:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84425",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084426.json:
```json
{
    "body": "Thanks.  This bug hit me again yesterday.",
    "created_at": "2010-09-22T15:33:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84426",
    "user": "jason"
}
```

Thanks.  This bug hit me again yesterday.



---

archive/issue_comments_084427.json:
```json
{
    "body": "Hang on a minute. I was lazy and ran long doctests on graphics and only short doctests on everything else, so I missed a weird side-effect of this patch: if you install the two patches above on vanilla 4.6.alpha1 and do\n\n```\nsage -t -long sage/combinat/root_system/weyl_group.py\n```\n\nthen you get an infinite loop:\n\n```\nFile \"/storage/masiao/sage-4.6.alpha1/devel/sage-hacking/sage/combinat/root_system/weyl_group.py\", line 27:\n    sage: d.show3d(color_by_label=True, edge_size=0.01, vertex_size=0.03) #long time (less than one minute)\nException raised:\n    Traceback (most recent call last):\n      File \"/storage/masiao/sage-4.6.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/storage/masiao/sage-4.6.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/storage/masiao/sage-4.6.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[7]>\", line 1, in <module>\n        d.show3d(color_by_label=True, edge_size=RealNumber('0.01'), vertex_size=RealNumber('0.03')) #long time (less than one minute)###line 27:\n    sage: d.show3d(color_by_label=True, edge_size=0.01, vertex_size=0.03) #long time (less than one minute)\n      File \"/storage/masiao/sage-4.6.alpha1/local/lib/python/site-packages/sage/graphs/generic_graph.py\", line 12407, in show3d\n        color_by_label=color_by_label, **kwds).show()\n      File \"base.pyx\", line 1048, in sage.plot.plot3d.base.Graphics3d.show (sage/plot/plot3d/base.c:9726)\n      File \"base.pyx\", line 953, in sage.plot.plot3d.base.Graphics3d._process_viewing_options (sage/plot/plot3d/base.c:9519)\n      File \"base.pyx\", line 198, in sage.plot.plot3d.base.Graphics3d._determine_frame_aspect_ratio (sage/plot/plot3d/base.c:3307)\n      File \"base.pyx\", line 214, in sage.plot.plot3d.base.Graphics3d._safe_bounding_box (sage/plot/plot3d/base.c:3460)\n      File \"base.pyx\", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)\n      File \"base.pyx\", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)\n      File \"base.pyx\", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)\n      File \"base.pyx\", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)\n      File \"base.pyx\", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)\n      File \"base.pyx\", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)\n      File \"base.pyx\", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)\n[ ... ]\n      File \"base.pyx\", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)\n      File \"base.pyx\", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)\n      File \"base.pyx\", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)\n      File \"base.pyx\", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12236)\n      File \"base.pyx\", line 1271, in sage.plot.plot3d.base.Graphics3dGroup.bounding_box (sage/plot/plot3d/base.c:12234)\n    RuntimeError: maximum recursion depth exceeded in __subclasscheck__\n**********************************************************************\n1 items had failures:\n   1 of   8 in __main__.example_0\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/masiao/.sage//tmp/.doctest_weyl_group.py\n         [41.9 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t -long \"devel/sage-hacking/sage/combinat/root_system/weyl_group.py\"\nTotal time for all tests: 41.9 seconds\n```\n\n\nApologies for my sloppiness in not having caught this bug earlier.",
    "created_at": "2010-09-23T12:31:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84427",
    "user": "davidloeffler"
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

archive/issue_comments_084428.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-09-23T12:31:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84428",
    "user": "davidloeffler"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_084429.json:
```json
{
    "body": "Replying to [comment:16 davidloeffler]:\n\n\n> Apologies for my sloppiness in not having caught this bug earlier.\n\nWell, please accept my apologies for not thinking we had to check ptestlong.  I'll fix it and run ptestlong before posting a new patch!\n\nThanks for your patience.",
    "created_at": "2010-09-23T12:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84429",
    "user": "jason"
}
```

Replying to [comment:16 davidloeffler]:


> Apologies for my sloppiness in not having caught this bug earlier.

Well, please accept my apologies for not thinking we had to check ptestlong.  I'll fix it and run ptestlong before posting a new patch!

Thanks for your patience.



---

archive/issue_comments_084430.json:
```json
{
    "body": "solved in #17258",
    "created_at": "2015-03-18T20:54:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84430",
    "user": "chapoton"
}
```

solved in #17258



---

archive/issue_comments_084431.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-03-18T20:54:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84431",
    "user": "chapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084432.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-03-18T21:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84432",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084433.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-03-21T09:30:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9089#issuecomment-84433",
    "user": "vbraun"
}
```

Resolution: fixed
