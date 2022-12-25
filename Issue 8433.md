# Issue 8433: plot3d for tachyon hangs

archive/issues_008433.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jasongrout @robertwb drkirkby mhampton @jdemeyer mvngu\n\nKeywords: tachyon\n\nThe following plot command fails (tachyon gets all CPU usage and no picture is shown)\n\n```\ny=var('y')\nB=plot3d(sqrt(sin(x)*sin(y)),(x,-2*pi,2*pi),(y,-2*pi,2*pi),viewer='tachyon')\nB.show()\n```\nThis works fine\n\n```\ny=var('y')\nB=plot3d(sqrt(sin(x)*sin(y)),(x,0,2),(y,0,2), viewer='tachyon')\nB.show()\n```\nand this does not work\n\n```\ny=var('y')\nB=plot3d(sqrt(sin(x)*sin(y)),(x,-2,2),(y,-2,2), viewer='tachyon')\nB.show()\n```\nRelated trac is #8424, but the problem seems to be independent.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8433\n\n",
    "closed_at": "2021-08-26T02:08:43Z",
    "created_at": "2010-03-04T08:08:52Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "plot3d for tachyon hangs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8433",
    "user": "https://github.com/robert-marik"
}
```
Assignee: @williamstein

CC:  @jasongrout @robertwb drkirkby mhampton @jdemeyer mvngu

Keywords: tachyon

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

archive/issue_comments_075543.json:
```json
{
    "body": "Changing assignee from @aghitza to @williamstein.",
    "created_at": "2010-03-04T08:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75543",
    "user": "https://github.com/robert-marik"
}
```

Changing assignee from @aghitza to @williamstein.



---

archive/issue_comments_075544.json:
```json
{
    "body": "Changing component from algebra to graphics.",
    "created_at": "2010-03-04T08:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75544",
    "user": "https://github.com/robert-marik"
}
```

Changing component from algebra to graphics.



---

archive/issue_comments_075545.json:
```json
{
    "body": "This sounds like the NaNs are giving tachyon (or the triangle constructing routine) problems.  That's where I would look first for the problem, anyway.",
    "created_at": "2010-03-04T10:52:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75545",
    "user": "https://github.com/jasongrout"
}
```

This sounds like the NaNs are giving tachyon (or the triangle constructing routine) problems.  That's where I would look first for the problem, anyway.



---

archive/issue_comments_075546.json:
```json
{
    "body": "All three commands produce output on my sage-4.5.3 installation.",
    "created_at": "2010-11-03T00:41:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75546",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

All three commands produce output on my sage-4.5.3 installation.



---

archive/issue_comments_075547.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-11-03T00:41:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75547",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_075548.json:
```json
{
    "body": "Yep, seems to work for me too (sage 4.6).  I think this has been fixed.\n\nCcing the release manager.  I don't know if he wants to close it as invalid or fixed.  Also CCing Minh, who knows the policy for closing these sorts of things.",
    "created_at": "2010-11-03T00:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75548",
    "user": "https://github.com/jasongrout"
}
```

Yep, seems to work for me too (sage 4.6).  I think this has been fixed.

Ccing the release manager.  I don't know if he wants to close it as invalid or fixed.  Also CCing Minh, who knows the policy for closing these sorts of things.



---

archive/issue_events_020214.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-11-03T07:01:39Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "milestone": "sage-4.6.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8433#event-20214"
}
```



---

archive/issue_comments_075549.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-11-03T07:01:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75549",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_075550.json:
```json
{
    "body": "Replying to [comment:5 jason]:\n> Also CCing Minh, who knows the policy for closing these sorts of things.\n\n\nIt's better to add the above doctests to the documentation for `plot3d.py` just to be safe. See the attachment.",
    "created_at": "2010-11-03T07:01:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75550",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:5 jason]:
> Also CCing Minh, who knows the policy for closing these sorts of things.


It's better to add the above doctests to the documentation for `plot3d.py` just to be safe. See the attachment.



---

archive/issue_comments_075551.json:
```json
{
    "body": "Changing priority from major to trivial.",
    "created_at": "2010-11-03T07:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75551",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing priority from major to trivial.



---

archive/issue_comments_075552.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-03T09:31:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75552",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075553.json:
```json
{
    "body": "I agree that these doctests pass, but the actual problem is not solved.  When doing\n\n```\ny=var('y')\nB=plot3d(sqrt(sin(x)*sin(y)),(x,-2,2),(y,-2,2), viewer='tachyon')\nB.show()\n```\nin the notebook, Tachyon runs forever.\n\nMinor comment: the tests should be marked \"long time\".  On my Linux x86_64 machine, testing `plot3d.py` goes from 18s to 30s.",
    "created_at": "2010-11-03T09:31:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75553",
    "user": "https://github.com/jdemeyer"
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

archive/issue_comments_075554.json:
```json
{
    "body": "Replying to [comment:10 jdemeyer]:\n> I agree that these doctests pass, but the actual problem is not solved.  When doing\n> \n> ```\n> y=var('y')\n> B=plot3d(sqrt(sin(x)*sin(y)),(x,-2,2),(y,-2,2), viewer='tachyon')\n> B.show()\n> ```\n> in the notebook, Tachyon runs forever.\n\n\n\nI didn't run doctests.  I ran the three commands in notebook().  All three produced output (attached is the output I receive for the command above).  What version of sage are you using?",
    "created_at": "2010-11-03T12:16:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75554",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Replying to [comment:10 jdemeyer]:
> I agree that these doctests pass, but the actual problem is not solved.  When doing
> 
> ```
> y=var('y')
> B=plot3d(sqrt(sin(x)*sin(y)),(x,-2,2),(y,-2,2), viewer='tachyon')
> B.show()
> ```
> in the notebook, Tachyon runs forever.



I didn't run doctests.  I ran the three commands in notebook().  All three produced output (attached is the output I receive for the command above).  What version of sage are you using?



---

archive/issue_comments_075555.json:
```json
{
    "body": "Attachment [sage0.png](tarball://root/attachments/some-uuid/ticket8433/sage0.png) by ryan created at 2010-11-03 12:17:50\n\nnotebook output to second commmand in bug report",
    "created_at": "2010-11-03T12:17:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75555",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Attachment [sage0.png](tarball://root/attachments/some-uuid/ticket8433/sage0.png) by ryan created at 2010-11-03 12:17:50

notebook output to second commmand in bug report



---

archive/issue_comments_075556.json:
```json
{
    "body": "sorry, make the the third command\n\ny=var('y')\nB=plot3d(sqrt(sin(x)*sin(y)),(x,-2,2),(y,-2,2), viewer='tachyon')\nB.show()",
    "created_at": "2010-11-03T12:18:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75556",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

sorry, make the the third command

y=var('y')
B=plot3d(sqrt(sin(x)*sin(y)),(x,-2,2),(y,-2,2), viewer='tachyon')
B.show()



---

archive/issue_comments_075557.json:
```json
{
    "body": "Attachment [trac-8433_plot3d.patch](tarball://root/attachments/some-uuid/ticket8433/trac-8433_plot3d.patch) by mvngu created at 2010-11-04 04:48:31",
    "created_at": "2010-11-04T04:48:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75557",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac-8433_plot3d.patch](tarball://root/attachments/some-uuid/ticket8433/trac-8433_plot3d.patch) by mvngu created at 2010-11-04 04:48:31



---

archive/issue_comments_075558.json:
```json
{
    "body": "Replying to [comment:10 jdemeyer]:\n> Minor comment: the tests should be marked \"long time\".\n\n\nDone. See the updated patch.",
    "created_at": "2010-11-04T04:54:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75558",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:10 jdemeyer]:
> Minor comment: the tests should be marked "long time".


Done. See the updated patch.



---

archive/issue_comments_075559.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-04T04:54:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75559",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075560.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-04T08:32:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75560",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075561.json:
```json
{
    "body": "Replying to [comment:11 ryan]:\n> I didn't run doctests.  I ran the three commands in notebook().  All three produced output (attached is the output I receive for the command above).  What version of sage are you using?\n\n\nThis is with sage-4.6.1.alpha0 on a Gentoo Linux x86_64 system.\n\nFor me, only the second plot in the bug report works.",
    "created_at": "2010-11-04T08:32:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75561",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:11 ryan]:
> I didn't run doctests.  I ran the three commands in notebook().  All three produced output (attached is the output I receive for the command above).  What version of sage are you using?


This is with sage-4.6.1.alpha0 on a Gentoo Linux x86_64 system.

For me, only the second plot in the bug report works.



---

archive/issue_comments_075562.json:
```json
{
    "body": "Everything does work on alpha.sagenb.org (sage-4.6.rc0, Ubuntu Linux x86_64).",
    "created_at": "2010-11-04T08:33:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75562",
    "user": "https://github.com/jdemeyer"
}
```

Everything does work on alpha.sagenb.org (sage-4.6.rc0, Ubuntu Linux x86_64).



---

archive/issue_comments_075563.json:
```json
{
    "body": "All three work for me (4.6 on ubuntu 64-bit + firefox)",
    "created_at": "2010-11-04T09:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75563",
    "user": "https://github.com/JohnCremona"
}
```

All three work for me (4.6 on ubuntu 64-bit + firefox)



---

archive/issue_comments_075564.json:
```json
{
    "body": "Possibly for another ticket, but notice this:\n\n```\nsage: var('y')\nsage: B=plot3d(sqrt(sin(x)*sin(y)),(x,-2*pi,2*pi),(y,-2*pi,2*pi),viewer='tachyon',adaptive=True)\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/Users/grout/<ipython console> in <module>()\n\n/Users/grout/sage/local/lib/python2.6/site-packages/sage/plot/plot3d/plot3d.pyc in plot3d(f, urange, vrange, adaptive, transformation, **kwds)\n    684             raise ValueError, 'unknown transformation type'\n    685     elif adaptive:\n--> 686         P = plot3d_adaptive(f, urange, vrange, **kwds)\n    687     else:\n    688         u=fast_float_arg(0)\n\n/Users/grout/sage/local/lib/python2.6/site-packages/sage/plot/plot3d/plot3d.pyc in plot3d_adaptive(f, x_range, y_range, color, grad_f, max_bend, max_depth, initial_depth, num_colors, **kwds)\n    775             else:\n    776                 span = (len(texture)-1) / (max_z - min_z)    # max to avoid dividing by 0\n--> 777             parts = P.partition(lambda x,y,z: int((z-min_z)*span))\n    778         all = []\n    779         for k, G in parts.iteritems():\n\n/Users/grout/sage/local/lib/python2.6/site-packages/sage/plot/plot3d/index_face_set.so in sage.plot.plot3d.index_face_set.IndexFaceSet.partition (sage/plot/plot3d/index_face_set.c:6081)()\n\n/Users/grout/sage/local/lib/python2.6/site-packages/sage/plot/plot3d/plot3d.pyc in <lambda>(x, y, z)\n    775             else:\n    776                 span = (len(texture)-1) / (max_z - min_z)    # max to avoid dividing by 0\n--> 777             parts = P.partition(lambda x,y,z: int((z-min_z)*span))\n    778         all = []\n    779         for k, G in parts.iteritems():\n\nValueError: cannot convert float NaN to integer\n```",
    "created_at": "2010-11-04T12:59:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75564",
    "user": "https://github.com/jasongrout"
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

archive/issue_comments_075565.json:
```json
{
    "body": "#7423 would be at least related to the NaN issue.",
    "created_at": "2010-11-04T14:08:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75565",
    "user": "https://github.com/kcrisman"
}
```

#7423 would be at least related to the NaN issue.



---

archive/issue_comments_075566.json:
```json
{
    "body": "Replying to [comment:18 kcrisman]:\n> #7423 would be at least related to the NaN issue.\n\n\nThat ticket now works for me, so maybe people should test it to see if it should be closed too?",
    "created_at": "2010-11-04T14:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75566",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:18 kcrisman]:
> #7423 would be at least related to the NaN issue.


That ticket now works for me, so maybe people should test it to see if it should be closed too?



---

archive/issue_comments_075567.json:
```json
{
    "body": "Why are the tests marked \"long time\"? They take about 1.5 seconds on my machine. \n\nDave",
    "created_at": "2010-11-06T00:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75567",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Why are the tests marked "long time"? They take about 1.5 seconds on my machine. 

Dave



---

archive/issue_comments_075568.json:
```json
{
    "body": "Replying to [comment:20 drkirkby]:\n> Why are the tests marked \"long time\"? They take about 1.5 seconds on my machine. \n\n\nI seem to remember a policy that 1 second is the bound for \"long time\".",
    "created_at": "2010-11-06T00:15:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75568",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:20 drkirkby]:
> Why are the tests marked "long time"? They take about 1.5 seconds on my machine. 


I seem to remember a policy that 1 second is the bound for "long time".



---

archive/issue_events_020215.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "milestone": "sage-4.6.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8433#event-20215"
}
```



---

archive/issue_events_020216.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8433#event-20216"
}
```



---

archive/issue_events_020217.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8433#event-20217"
}
```



---

archive/issue_events_020218.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8433#event-20218"
}
```



---

archive/issue_events_020219.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8433#event-20219"
}
```



---

archive/issue_events_020220.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8433#event-20220"
}
```



---

archive/issue_comments_075569.json:
```json
{
    "body": "Changing keywords from \"\" to \"tachyon\".",
    "created_at": "2014-07-25T14:29:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75569",
    "user": "https://github.com/fchapoton"
}
```

Changing keywords from "" to "tachyon".



---

archive/issue_events_020221.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8433#event-20221"
}
```



---

archive/issue_events_020222.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8433#event-20222"
}
```



---

archive/issue_comments_075570.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2021-07-22T01:07:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75570",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_events_020223.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-07-22T01:07:59Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8433#event-20223"
}
```



---

archive/issue_events_020224.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-07-22T01:07:59Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8433#event-20224"
}
```



---

archive/issue_comments_075571.json:
```json
{
    "body": "outdated, works for me",
    "created_at": "2021-07-22T01:07:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75571",
    "user": "https://github.com/mkoeppe"
}
```

outdated, works for me



---

archive/issue_comments_075572.json:
```json
{
    "body": "> outdated, works for me\n\n\nAlready outdated years ago.  Should we still add a doctest?\n\nBy the way, Jason's comment in comment:17 is still true, so it is now #32261.",
    "created_at": "2021-07-22T01:57:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75572",
    "user": "https://github.com/kcrisman"
}
```

> outdated, works for me


Already outdated years ago.  Should we still add a doctest?

By the way, Jason's comment in comment:17 is still true, so it is now #32261.



---

archive/issue_comments_075573.json:
```json
{
    "body": "Replying to [comment:28 kcrisman]:\n> Should we still add a doctest?\n\nI don't think this would be useful\n\n> By the way, Jason's comment in comment:17 is still true, so it is now #32261.\n\nThanks! This bug appears to be unrelated to the `fast_float` cleanup that we are doing, but someone who knows about the plotting code may want to take a look",
    "created_at": "2021-07-22T05:48:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75573",
    "user": "https://github.com/mkoeppe"
}
```

Replying to [comment:28 kcrisman]:
> Should we still add a doctest?

I don't think this would be useful

> By the way, Jason's comment in comment:17 is still true, so it is now #32261.

Thanks! This bug appears to be unrelated to the `fast_float` cleanup that we are doing, but someone who knows about the plotting code may want to take a look



---

archive/issue_comments_075574.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-07-22T12:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75574",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_020225.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-08-26T02:08:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8433#event-20225"
}
```



---

archive/issue_comments_075575.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-08-26T02:08:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8433#issuecomment-75575",
    "user": "https://github.com/mkoeppe"
}
```

Resolution: invalid
