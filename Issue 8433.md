# Issue 8433: plot3d for tachyon hangs

archive/issues_008433.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  jason robertwb drkirkby mhampton jdemeyer mvngu\n\nThe following plot command fails (tachyon gets all CPU usage and no picture is shown)\n\n```\ny=var('y')\nB=plot3d(sqrt(sin(x)*sin(y)),(x,-2*pi,2*pi),(y,-2*pi,2*pi),viewer='tachyon')\nB.show()\n```\n\nThis works fine\n\n```\ny=var('y')\nB=plot3d(sqrt(sin(x)*sin(y)),(x,0,2),(y,0,2), viewer='tachyon')\nB.show()\n```\n\nand this does not work\n\n```\ny=var('y')\nB=plot3d(sqrt(sin(x)*sin(y)),(x,-2,2),(y,-2,2), viewer='tachyon')\nB.show()\n```\n\nRelated trac is #8424, but the problem seems to be independent.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8433\n\n",
    "created_at": "2010-03-04T08:08:52Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "plot3d for tachyon hangs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8433",
    "user": "robert.marik"
}
```
Assignee: AlexGhitza

CC:  jason robertwb drkirkby mhampton jdemeyer mvngu

The following plot command fails (tachyon gets all CPU usage and no picture is shown)

```
y=var('y')
B=plot3d(sqrt(sin(x)*sin(y)),(x,-2*pi,2*pi),(y,-2*pi,2*pi),viewer='tachyon')
B.show()
```

This works fine

```
y=var('y')
B=plot3d(sqrt(sin(x)*sin(y)),(x,0,2),(y,0,2), viewer='tachyon')
B.show()
```

and this does not work

```
y=var('y')
B=plot3d(sqrt(sin(x)*sin(y)),(x,-2,2),(y,-2,2), viewer='tachyon')
B.show()
```

Related trac is #8424, but the problem seems to be independent.

Issue created by migration from https://trac.sagemath.org/ticket/8433





---

archive/issue_comments_075668.json:
```json
{
    "body": "Changing assignee from AlexGhitza to was.",
    "created_at": "2010-03-04T08:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75668",
    "user": "robert.marik"
}
```

Changing assignee from AlexGhitza to was.



---

archive/issue_comments_075669.json:
```json
{
    "body": "Changing component from algebra to graphics.",
    "created_at": "2010-03-04T08:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75669",
    "user": "robert.marik"
}
```

Changing component from algebra to graphics.



---

archive/issue_comments_075670.json:
```json
{
    "body": "This sounds like the NaNs are giving tachyon (or the triangle constructing routine) problems.  That's where I would look first for the problem, anyway.",
    "created_at": "2010-03-04T10:52:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75670",
    "user": "jason"
}
```

This sounds like the NaNs are giving tachyon (or the triangle constructing routine) problems.  That's where I would look first for the problem, anyway.



---

archive/issue_comments_075671.json:
```json
{
    "body": "All three commands produce output on my sage-4.5.3 installation.",
    "created_at": "2010-11-03T00:41:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75671",
    "user": "ryan"
}
```

All three commands produce output on my sage-4.5.3 installation.



---

archive/issue_comments_075672.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-11-03T00:41:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75672",
    "user": "ryan"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_075673.json:
```json
{
    "body": "Yep, seems to work for me too (sage 4.6).  I think this has been fixed.\n\nCcing the release manager.  I don't know if he wants to close it as invalid or fixed.  Also CCing Minh, who knows the policy for closing these sorts of things.",
    "created_at": "2010-11-03T00:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75673",
    "user": "jason"
}
```

Yep, seems to work for me too (sage 4.6).  I think this has been fixed.

Ccing the release manager.  I don't know if he wants to close it as invalid or fixed.  Also CCing Minh, who knows the policy for closing these sorts of things.



---

archive/issue_comments_075674.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-11-03T07:01:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75674",
    "user": "mvngu"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_075675.json:
```json
{
    "body": "Replying to [comment:5 jason]:\n> Also CCing Minh, who knows the policy for closing these sorts of things.\n\nIt's better to add the above doctests to the documentation for `plot3d.py` just to be safe. See the attachment.",
    "created_at": "2010-11-03T07:01:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75675",
    "user": "mvngu"
}
```

Replying to [comment:5 jason]:
> Also CCing Minh, who knows the policy for closing these sorts of things.

It's better to add the above doctests to the documentation for `plot3d.py` just to be safe. See the attachment.



---

archive/issue_comments_075676.json:
```json
{
    "body": "Changing priority from major to trivial.",
    "created_at": "2010-11-03T07:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75676",
    "user": "mvngu"
}
```

Changing priority from major to trivial.



---

archive/issue_comments_075677.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-03T09:31:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75677",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075678.json:
```json
{
    "body": "I agree that these doctests pass, but the actual problem is not solved.  When doing\n\n```\ny=var('y')\nB=plot3d(sqrt(sin(x)*sin(y)),(x,-2,2),(y,-2,2), viewer='tachyon')\nB.show()\n```\n\nin the notebook, Tachyon runs forever.\n\nMinor comment: the tests should be marked \"long time\".  On my Linux x86_64 machine, testing `plot3d.py` goes from 18s to 30s.",
    "created_at": "2010-11-03T09:31:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75678",
    "user": "jdemeyer"
}
```

I agree that these doctests pass, but the actual problem is not solved.  When doing

```
y=var('y')
B=plot3d(sqrt(sin(x)*sin(y)),(x,-2,2),(y,-2,2), viewer='tachyon')
B.show()
```

in the notebook, Tachyon runs forever.

Minor comment: the tests should be marked "long time".  On my Linux x86_64 machine, testing `plot3d.py` goes from 18s to 30s.



---

archive/issue_comments_075679.json:
```json
{
    "body": "Replying to [comment:10 jdemeyer]:\n> I agree that these doctests pass, but the actual problem is not solved.  When doing\n> {{{\n> y=var('y')\n> B=plot3d(sqrt(sin(x)*sin(y)),(x,-2,2),(y,-2,2), viewer='tachyon')\n> B.show()\n> }}}\n> in the notebook, Tachyon runs forever.\n\n\nI didn't run doctests.  I ran the three commands in notebook().  All three produced output (attached is the output I receive for the command above).  What version of sage are you using?",
    "created_at": "2010-11-03T12:16:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75679",
    "user": "ryan"
}
```

Replying to [comment:10 jdemeyer]:
> I agree that these doctests pass, but the actual problem is not solved.  When doing
> {{{
> y=var('y')
> B=plot3d(sqrt(sin(x)*sin(y)),(x,-2,2),(y,-2,2), viewer='tachyon')
> B.show()
> }}}
> in the notebook, Tachyon runs forever.


I didn't run doctests.  I ran the three commands in notebook().  All three produced output (attached is the output I receive for the command above).  What version of sage are you using?



---

archive/issue_comments_075680.json:
```json
{
    "body": "Attachment\n\nnotebook output to second commmand in bug report",
    "created_at": "2010-11-03T12:17:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75680",
    "user": "ryan"
}
```

Attachment

notebook output to second commmand in bug report



---

archive/issue_comments_075681.json:
```json
{
    "body": "sorry, make the the third command\n\ny=var('y')\nB=plot3d(sqrt(sin(x)*sin(y)),(x,-2,2),(y,-2,2), viewer='tachyon')\nB.show()",
    "created_at": "2010-11-03T12:18:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75681",
    "user": "ryan"
}
```

sorry, make the the third command

y=var('y')
B=plot3d(sqrt(sin(x)*sin(y)),(x,-2,2),(y,-2,2), viewer='tachyon')
B.show()



---

archive/issue_comments_075682.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-11-04T04:48:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75682",
    "user": "mvngu"
}
```

Attachment



---

archive/issue_comments_075683.json:
```json
{
    "body": "Replying to [comment:10 jdemeyer]:\n> Minor comment: the tests should be marked \"long time\".\n\nDone. See the updated patch.",
    "created_at": "2010-11-04T04:54:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75683",
    "user": "mvngu"
}
```

Replying to [comment:10 jdemeyer]:
> Minor comment: the tests should be marked "long time".

Done. See the updated patch.



---

archive/issue_comments_075684.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-04T04:54:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75684",
    "user": "mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075685.json:
```json
{
    "body": "Changing priority from trivial to major.",
    "created_at": "2010-11-04T08:32:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75685",
    "user": "jdemeyer"
}
```

Changing priority from trivial to major.



---

archive/issue_comments_075686.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-04T08:32:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75686",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075687.json:
```json
{
    "body": "Replying to [comment:11 ryan]:\n> I didn't run doctests.  I ran the three commands in notebook().  All three produced output (attached is the output I receive for the command above).  What version of sage are you using?\n\nThis is with sage-4.6.1.alpha0 on a Gentoo Linux x86_64 system.\n\nFor me, only the second plot in the bug report works.",
    "created_at": "2010-11-04T08:32:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75687",
    "user": "jdemeyer"
}
```

Replying to [comment:11 ryan]:
> I didn't run doctests.  I ran the three commands in notebook().  All three produced output (attached is the output I receive for the command above).  What version of sage are you using?

This is with sage-4.6.1.alpha0 on a Gentoo Linux x86_64 system.

For me, only the second plot in the bug report works.



---

archive/issue_comments_075688.json:
```json
{
    "body": "Everything does work on alpha.sagenb.org (sage-4.6.rc0, Ubuntu Linux x86_64).",
    "created_at": "2010-11-04T08:33:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75688",
    "user": "jdemeyer"
}
```

Everything does work on alpha.sagenb.org (sage-4.6.rc0, Ubuntu Linux x86_64).



---

archive/issue_comments_075689.json:
```json
{
    "body": "All three work for me (4.6 on ubuntu 64-bit + firefox)",
    "created_at": "2010-11-04T09:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75689",
    "user": "cremona"
}
```

All three work for me (4.6 on ubuntu 64-bit + firefox)



---

archive/issue_comments_075690.json:
```json
{
    "body": "Possibly for another ticket, but notice this:\n\n\n```\nsage: var('y')\nsage: B=plot3d(sqrt(sin(x)*sin(y)),(x,-2*pi,2*pi),(y,-2*pi,2*pi),viewer='tachyon',adaptive=True)\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/Users/grout/<ipython console> in <module>()\n\n/Users/grout/sage/local/lib/python2.6/site-packages/sage/plot/plot3d/plot3d.pyc in plot3d(f, urange, vrange, adaptive, transformation, **kwds)\n    684             raise ValueError, 'unknown transformation type'\n    685     elif adaptive:\n--> 686         P = plot3d_adaptive(f, urange, vrange, **kwds)\n    687     else:\n    688         u=fast_float_arg(0)\n\n/Users/grout/sage/local/lib/python2.6/site-packages/sage/plot/plot3d/plot3d.pyc in plot3d_adaptive(f, x_range, y_range, color, grad_f, max_bend, max_depth, initial_depth, num_colors, **kwds)\n    775             else:\n    776                 span = (len(texture)-1) / (max_z - min_z)    # max to avoid dividing by 0\n--> 777             parts = P.partition(lambda x,y,z: int((z-min_z)*span))\n    778         all = []\n    779         for k, G in parts.iteritems():\n\n/Users/grout/sage/local/lib/python2.6/site-packages/sage/plot/plot3d/index_face_set.so in sage.plot.plot3d.index_face_set.IndexFaceSet.partition (sage/plot/plot3d/index_face_set.c:6081)()\n\n/Users/grout/sage/local/lib/python2.6/site-packages/sage/plot/plot3d/plot3d.pyc in <lambda>(x, y, z)\n    775             else:\n    776                 span = (len(texture)-1) / (max_z - min_z)    # max to avoid dividing by 0\n--> 777             parts = P.partition(lambda x,y,z: int((z-min_z)*span))\n    778         all = []\n    779         for k, G in parts.iteritems():\n\nValueError: cannot convert float NaN to integer\n```\n",
    "created_at": "2010-11-04T12:59:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75690",
    "user": "jason"
}
```

Possibly for another ticket, but notice this:


```
sage: var('y')
sage: B=plot3d(sqrt(sin(x)*sin(y)),(x,-2*pi,2*pi),(y,-2*pi,2*pi),viewer='tachyon',adaptive=True)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/Users/grout/<ipython console> in <module>()

/Users/grout/sage/local/lib/python2.6/site-packages/sage/plot/plot3d/plot3d.pyc in plot3d(f, urange, vrange, adaptive, transformation, **kwds)
    684             raise ValueError, 'unknown transformation type'
    685     elif adaptive:
--> 686         P = plot3d_adaptive(f, urange, vrange, **kwds)
    687     else:
    688         u=fast_float_arg(0)

/Users/grout/sage/local/lib/python2.6/site-packages/sage/plot/plot3d/plot3d.pyc in plot3d_adaptive(f, x_range, y_range, color, grad_f, max_bend, max_depth, initial_depth, num_colors, **kwds)
    775             else:
    776                 span = (len(texture)-1) / (max_z - min_z)    # max to avoid dividing by 0
--> 777             parts = P.partition(lambda x,y,z: int((z-min_z)*span))
    778         all = []
    779         for k, G in parts.iteritems():

/Users/grout/sage/local/lib/python2.6/site-packages/sage/plot/plot3d/index_face_set.so in sage.plot.plot3d.index_face_set.IndexFaceSet.partition (sage/plot/plot3d/index_face_set.c:6081)()

/Users/grout/sage/local/lib/python2.6/site-packages/sage/plot/plot3d/plot3d.pyc in <lambda>(x, y, z)
    775             else:
    776                 span = (len(texture)-1) / (max_z - min_z)    # max to avoid dividing by 0
--> 777             parts = P.partition(lambda x,y,z: int((z-min_z)*span))
    778         all = []
    779         for k, G in parts.iteritems():

ValueError: cannot convert float NaN to integer
```




---

archive/issue_comments_075691.json:
```json
{
    "body": "#7423 would be at least related to the NaN issue.",
    "created_at": "2010-11-04T14:08:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75691",
    "user": "kcrisman"
}
```

#7423 would be at least related to the NaN issue.



---

archive/issue_comments_075692.json:
```json
{
    "body": "Replying to [comment:18 kcrisman]:\n> #7423 would be at least related to the NaN issue.\n\nThat ticket now works for me, so maybe people should test it to see if it should be closed too?",
    "created_at": "2010-11-04T14:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75692",
    "user": "jason"
}
```

Replying to [comment:18 kcrisman]:
> #7423 would be at least related to the NaN issue.

That ticket now works for me, so maybe people should test it to see if it should be closed too?



---

archive/issue_comments_075693.json:
```json
{
    "body": "Why are the tests marked \"long time\"? They take about 1.5 seconds on my machine. \n\nDave",
    "created_at": "2010-11-06T00:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75693",
    "user": "drkirkby"
}
```

Why are the tests marked "long time"? They take about 1.5 seconds on my machine. 

Dave



---

archive/issue_comments_075694.json:
```json
{
    "body": "Replying to [comment:20 drkirkby]:\n> Why are the tests marked \"long time\"? They take about 1.5 seconds on my machine. \n\nI seem to remember a policy that 1 second is the bound for \"long time\".",
    "created_at": "2010-11-06T00:15:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75694",
    "user": "jdemeyer"
}
```

Replying to [comment:20 drkirkby]:
> Why are the tests marked "long time"? They take about 1.5 seconds on my machine. 

I seem to remember a policy that 1 second is the bound for "long time".



---

archive/issue_comments_075695.json:
```json
{
    "body": "Changing keywords from \"\" to \"tachyon\".",
    "created_at": "2014-07-25T14:29:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75695",
    "user": "chapoton"
}
```

Changing keywords from "" to "tachyon".



---

archive/issue_comments_075696.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2021-07-22T01:07:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75696",
    "user": "mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075697.json:
```json
{
    "body": "outdated, works for me",
    "created_at": "2021-07-22T01:07:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75697",
    "user": "mkoeppe"
}
```

outdated, works for me



---

archive/issue_comments_075698.json:
```json
{
    "body": "> outdated, works for me\n\nAlready outdated years ago.  Should we still add a doctest?\n\nBy the way, Jason's comment in comment:17 is still true, so it is now #32261.",
    "created_at": "2021-07-22T01:57:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75698",
    "user": "kcrisman"
}
```

> outdated, works for me

Already outdated years ago.  Should we still add a doctest?

By the way, Jason's comment in comment:17 is still true, so it is now #32261.



---

archive/issue_comments_075699.json:
```json
{
    "body": "Replying to [comment:28 kcrisman]:\n> Should we still add a doctest?\nI don't think this would be useful\n\n> By the way, Jason's comment in comment:17 is still true, so it is now #32261.\nThanks! This bug appears to be unrelated to the `fast_float` cleanup that we are doing, but someone who knows about the plotting code may want to take a look",
    "created_at": "2021-07-22T05:48:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75699",
    "user": "mkoeppe"
}
```

Replying to [comment:28 kcrisman]:
> Should we still add a doctest?
I don't think this would be useful

> By the way, Jason's comment in comment:17 is still true, so it is now #32261.
Thanks! This bug appears to be unrelated to the `fast_float` cleanup that we are doing, but someone who knows about the plotting code may want to take a look



---

archive/issue_comments_075700.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-07-22T12:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75700",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075701.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-08-26T02:08:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75701",
    "user": "mkoeppe"
}
```

Resolution: invalid
