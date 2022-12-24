# Issue 4885: fix fallout from sloppy review of 4535

archive/issues_004885.json:
```json
{
    "body": "Assignee: @williamstein\n\nI refereed trac #4535 and I made some serious mistakes in accepting that patch.  This ticket will be about fixing all of those mistakes.\n\n* the function xmin/xmax/ymin/ymax were all removed.  They *must* be all added back exactly as before.  There is a lot of code out there that depends on it.  Also, we do not just delete functions in sage without deprecating them for at least 6 months first.\n\n* some of the new functions get_* have no documentation or docstrings.  Fix this. \n\n* Do \"sage -t\" on the *old* plot.py using the newest version of sage, and make sure nothing breaks (e.g., examples that use .xmin, etc.)  Fix anything that does, or at least *discuss* it.\n\n\nUnless somebody beats me to it, I'll do this, since it is my fault #4535 got a positive review.  I'll post to this ticket, as soon as I work on this, so if I haven't posted a message below that I'm working on it, I haven't started. \n\n  -- William \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4885\n\n",
    "created_at": "2008-12-28T23:25:41Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.3",
    "title": "fix fallout from sloppy review of 4535",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4885",
    "user": "@williamstein"
}
```
Assignee: @williamstein

I refereed trac #4535 and I made some serious mistakes in accepting that patch.  This ticket will be about fixing all of those mistakes.

* the function xmin/xmax/ymin/ymax were all removed.  They *must* be all added back exactly as before.  There is a lot of code out there that depends on it.  Also, we do not just delete functions in sage without deprecating them for at least 6 months first.

* some of the new functions get_* have no documentation or docstrings.  Fix this. 

* Do "sage -t" on the *old* plot.py using the newest version of sage, and make sure nothing breaks (e.g., examples that use .xmin, etc.)  Fix anything that does, or at least *discuss* it.


Unless somebody beats me to it, I'll do this, since it is my fault #4535 got a positive review.  I'll post to this ticket, as soon as I work on this, so if I haven't posted a message below that I'm working on it, I haven't started. 

  -- William 


Issue created by migration from https://trac.sagemath.org/ticket/4885





---

archive/issue_comments_037029.json:
```json
{
    "body": "Is that an official deprecation policy now?  (I think it's a great idea.)  Is that deprecation policy documented somewhere?  If not, it should be.",
    "created_at": "2008-12-29T11:15:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4885#issuecomment-37029",
    "user": "@jasongrout"
}
```

Is that an official deprecation policy now?  (I think it's a great idea.)  Is that deprecation policy documented somewhere?  If not, it should be.



---

archive/issue_comments_037030.json:
```json
{
    "body": "> Is that an official deprecation policy now? (I think it's a great idea.)\n\nYes. \n\n> Is that deprecation policy documented somewhere? If not, it should be. \n\nI think it was only documented in sage-devel.  It would be good add more documentation if I'm wrong.",
    "created_at": "2008-12-30T01:21:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4885#issuecomment-37030",
    "user": "@williamstein"
}
```

> Is that an official deprecation policy now? (I think it's a great idea.)

Yes. 

> Is that deprecation policy documented somewhere? If not, it should be. 

I think it was only documented in sage-devel.  It would be good add more documentation if I'm wrong.



---

archive/issue_comments_037031.json:
```json
{
    "body": "The deprecation policy isn't documented and we could definitely need a good example and something official in the development manual.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-30T01:24:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4885#issuecomment-37031",
    "user": "mabshoff"
}
```

The deprecation policy isn't documented and we could definitely need a good example and something official in the development manual.

Cheers,

Michael



---

archive/issue_comments_037032.json:
```json
{
    "body": "I thought this was high priority to get in? I have been waiting to see something happening here, otherwise this will get bumped.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-30T11:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4885#issuecomment-37032",
    "user": "mabshoff"
}
```

I thought this was high priority to get in? I have been waiting to see something happening here, otherwise this will get bumped.

Cheers,

Michael



---

archive/issue_comments_037033.json:
```json
{
    "body": "> I thought this was high priority to get in? I have been waiting to see something \n> happening here, otherwise this will get bumped. \n\nThanks for the reminder.  This is high priority.",
    "created_at": "2008-12-30T23:27:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4885#issuecomment-37033",
    "user": "@williamstein"
}
```

> I thought this was high priority to get in? I have been waiting to see something 
> happening here, otherwise this will get bumped. 

Thanks for the reminder.  This is high priority.



---

archive/issue_comments_037034.json:
```json
{
    "body": "I'm doctesting the old plot.py and finding what was broke by the refactoring. \n\n1. Lots of xmin/xmax, etc.  That's known.\n\n2. The API of text changed:\n\n```\n    sage: text(\"Sage is really neat!!\",(2,12,1))\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wstein/build/sage-3.2.3.alpha0/local/lib/python2.5/site-packages/sage/plot/text.py\", line 79, in text\n        def text(string, (x,y), **options):\n    ValueError: too many values to unpack\n```\n\n\nInstead of ValueError, it might be better to be\n\n```\nValueError: too many values to unpack (try using text3d)\n```\n\nat least when 3 coordinates are given.  This will help with people transition code that uses the old text command. \n\nThis example used to work fine before the refactoring, but #4535 broke it:\n\n```\nE = EllipticCurve('37a')\nP = E(0,0)\ndef get_points(n): return sum([point(i*P, pointsize=3) for i in range(-n,n) if i != 0 and (i*P)[0] < 3])\nsum([get_points(15*n).plot3d(z=n) for n in range(1,10)])\n```\n\n\nit fails with this error:\n\n\n```\n        self.loc = (float(center[0]), float(center[1]), float(center[2]))\n      File \"rational.pyx\", line 1112, in sage.rings.rational.Rational.__getitem__ (sage/rings/rational.c:8532)\n    IndexError: index n (=1) out of range; it must be 0\n```\n\n\nEverything else is harmless as far as I can tell.",
    "created_at": "2008-12-31T00:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4885#issuecomment-37034",
    "user": "@williamstein"
}
```

I'm doctesting the old plot.py and finding what was broke by the refactoring. 

1. Lots of xmin/xmax, etc.  That's known.

2. The API of text changed:

```
    sage: text("Sage is really neat!!",(2,12,1))
Exception raised:
    Traceback (most recent call last):
      File "/home/wstein/build/sage-3.2.3.alpha0/local/lib/python2.5/site-packages/sage/plot/text.py", line 79, in text
        def text(string, (x,y), **options):
    ValueError: too many values to unpack
```


Instead of ValueError, it might be better to be

```
ValueError: too many values to unpack (try using text3d)
```

at least when 3 coordinates are given.  This will help with people transition code that uses the old text command. 

This example used to work fine before the refactoring, but #4535 broke it:

```
E = EllipticCurve('37a')
P = E(0,0)
def get_points(n): return sum([point(i*P, pointsize=3) for i in range(-n,n) if i != 0 and (i*P)[0] < 3])
sum([get_points(15*n).plot3d(z=n) for n in range(1,10)])
```


it fails with this error:


```
        self.loc = (float(center[0]), float(center[1]), float(center[2]))
      File "rational.pyx", line 1112, in sage.rings.rational.Rational.__getitem__ (sage/rings/rational.c:8532)
    IndexError: index n (=1) out of range; it must be 0
```


Everything else is harmless as far as I can tell.



---

archive/issue_comments_037035.json:
```json
{
    "body": "Attachment [trac_4885.patch](tarball://root/attachments/some-uuid/ticket4885/trac_4885.patch) by @williamstein created at 2008-12-31 01:20:05\n\nthis patch fixes all the problems reported in the tickets and commentary up to this point.",
    "created_at": "2008-12-31T01:20:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4885#issuecomment-37035",
    "user": "@williamstein"
}
```

Attachment [trac_4885.patch](tarball://root/attachments/some-uuid/ticket4885/trac_4885.patch) by @williamstein created at 2008-12-31 01:20:05

this patch fixes all the problems reported in the tickets and commentary up to this point.



---

archive/issue_comments_037036.json:
```json
{
    "body": "I posted a new patch which makes it so that get_minmax_data is *not* cached.  Having it cached will break things if new primitives are added to the graphics object.  The idea is that get_minmax_data comes directly from the primitives, and any custom stuff the user wants is stored in axes_range.",
    "created_at": "2009-01-02T05:31:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4885#issuecomment-37036",
    "user": "@mwhansen"
}
```

I posted a new patch which makes it so that get_minmax_data is *not* cached.  Having it cached will break things if new primitives are added to the graphics object.  The idea is that get_minmax_data comes directly from the primitives, and any custom stuff the user wants is stored in axes_range.



---

archive/issue_comments_037037.json:
```json
{
    "body": "The idea is good.  I don't like that you replaced:\n\n```\n>  WARNING: The returned dictionary is mutable, but changing it does \n>  not change the xmin/xmax/ymin/ymax data.  To change that, call \n>   the methods xmin, xmax, ymin, and ymax.  \n```\n\nby \n\n```\n> Note that this is recomputed every time the function is called. \n```\n\n\nThe first is very clear and explicit, but of course not right anymore.  The second implicitly suggests what the first said.  The WARNING would be a good place to make it clear that it doesn't make sense to change the minmax data, since it's a function of the actual points in the objects.  And there one could point to the other relevant functions for setting the axes ranges.",
    "created_at": "2009-01-02T07:15:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4885#issuecomment-37037",
    "user": "@williamstein"
}
```

The idea is good.  I don't like that you replaced:

```
>  WARNING: The returned dictionary is mutable, but changing it does 
>  not change the xmin/xmax/ymin/ymax data.  To change that, call 
>   the methods xmin, xmax, ymin, and ymax.  
```

by 

```
> Note that this is recomputed every time the function is called. 
```


The first is very clear and explicit, but of course not right anymore.  The second implicitly suggests what the first said.  The WARNING would be a good place to make it clear that it doesn't make sense to change the minmax data, since it's a function of the actual points in the objects.  And there one could point to the other relevant functions for setting the axes ranges.



---

archive/issue_comments_037038.json:
```json
{
    "body": "Attachment [trac_4885-2.patch](tarball://root/attachments/some-uuid/ticket4885/trac_4885-2.patch) by @williamstein created at 2009-01-02 21:26:34\n\nAssuming mhansen gave my patch a positive review modulo me giving his a positive review, this gets a positive review. I nitpick about the docs, but that's not enough to stop this going in.",
    "created_at": "2009-01-02T21:26:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4885#issuecomment-37038",
    "user": "@williamstein"
}
```

Attachment [trac_4885-2.patch](tarball://root/attachments/some-uuid/ticket4885/trac_4885-2.patch) by @williamstein created at 2009-01-02 21:26:34

Assuming mhansen gave my patch a positive review modulo me giving his a positive review, this gets a positive review. I nitpick about the docs, but that's not enough to stop this going in.



---

archive/issue_comments_037039.json:
```json
{
    "body": "Merged both patches in Sage 3.2.3.final",
    "created_at": "2009-01-02T22:15:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4885#issuecomment-37039",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.2.3.final



---

archive/issue_comments_037040.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-02T22:15:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4885#issuecomment-37040",
    "user": "mabshoff"
}
```

Resolution: fixed
