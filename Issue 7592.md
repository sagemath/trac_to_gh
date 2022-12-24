# Issue 7592: Flow method using LP

archive/issues_007592.json:
```json
{
    "body": "Assignee: rlm\n\nAs the title says, this patch implements the flow function for Graphs ( weighted or not, directed or not )\n\nIssue created by migration from https://trac.sagemath.org/ticket/7592\n\n",
    "created_at": "2009-12-03T14:34:56Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Flow method using LP",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7592",
    "user": "ncohen"
}
```
Assignee: rlm

As the title says, this patch implements the flow function for Graphs ( weighted or not, directed or not )

Issue created by migration from https://trac.sagemath.org/ticket/7592





---

archive/issue_comments_064726.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-03T15:18:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7592#issuecomment-64726",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064727.json:
```json
{
    "body": "This does not apply to 4.3.a1 on an imac running 10.6.1:\n\n\n```\njeeves:sage-4.3.alpha1 wdj$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nWARNING: There is one major unsolved bug in some versions of\nSage on OS X 10.6 that causes an 'Abort trap' crash when\ndoing certain symbolic computations.\nSee http://trac.sagemath.org/sage_trac/ticket/7095/.\nLoading Sage library. Current Mercurial branch is: 7592-flow\nsage: hg_sage.apply(\"/Users/wdj/sagefiles/trac_7592.patch\")\ncd \"/Users/wdj/sagefiles/sage-4.3.alpha1/devel/sage\" && hg status\n/Users/wdj/sagefiles/sage-4.3.alpha1/local/lib/python2.6/site-packages/sage/misc/hg.py:240: DeprecationWarning: os.popen3 is deprecated.  Use the subprocess module.\n  x = os.popen3(s)\ncd \"/Users/wdj/sagefiles/sage-4.3.alpha1/devel/sage\" && hg status\ncd \"/Users/wdj/sagefiles/sage-4.3.alpha1/devel/sage\" && hg import   \"/Users/wdj/sagefiles/trac_7592.patch\"\napplying /Users/wdj/sagefiles/trac_7592.patch\npatching file sage/graphs/graph.py\nHunk #2 FAILED at 3019\n1 out of 2 hunks FAILED -- saving rejects to file sage/graphs/graph.py.rej\nabort: patch failed to apply\nsage: \n```\n",
    "created_at": "2009-12-08T19:52:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7592#issuecomment-64727",
    "user": "wdj"
}
```

This does not apply to 4.3.a1 on an imac running 10.6.1:


```
jeeves:sage-4.3.alpha1 wdj$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
WARNING: There is one major unsolved bug in some versions of
Sage on OS X 10.6 that causes an 'Abort trap' crash when
doing certain symbolic computations.
See http://trac.sagemath.org/sage_trac/ticket/7095/.
Loading Sage library. Current Mercurial branch is: 7592-flow
sage: hg_sage.apply("/Users/wdj/sagefiles/trac_7592.patch")
cd "/Users/wdj/sagefiles/sage-4.3.alpha1/devel/sage" && hg status
/Users/wdj/sagefiles/sage-4.3.alpha1/local/lib/python2.6/site-packages/sage/misc/hg.py:240: DeprecationWarning: os.popen3 is deprecated.  Use the subprocess module.
  x = os.popen3(s)
cd "/Users/wdj/sagefiles/sage-4.3.alpha1/devel/sage" && hg status
cd "/Users/wdj/sagefiles/sage-4.3.alpha1/devel/sage" && hg import   "/Users/wdj/sagefiles/trac_7592.patch"
applying /Users/wdj/sagefiles/trac_7592.patch
patching file sage/graphs/graph.py
Hunk #2 FAILED at 3019
1 out of 2 hunks FAILED -- saving rejects to file sage/graphs/graph.py.rej
abort: patch failed to apply
sage: 
```




---

archive/issue_comments_064728.json:
```json
{
    "body": "Replying to [comment:3 wdj]:\n> This does not apply to 4.3.a1 on an imac running 10.6.1:\n> \n\n...\n\n\nI should add though that this version of sage has the latest networkx package installed.\nWould that screw things up?",
    "created_at": "2009-12-08T19:54:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7592#issuecomment-64728",
    "user": "wdj"
}
```

Replying to [comment:3 wdj]:
> This does not apply to 4.3.a1 on an imac running 10.6.1:
> 

...


I should add though that this version of sage has the latest networkx package installed.
Would that screw things up?



---

archive/issue_comments_064729.json:
```json
{
    "body": "It could have, but in this case it was mainly my fault. I have no idea why, but the patch did not even apply on my version, perhaps they were not based on alpha... Here is a new version based on alpha, with my excuses :-)",
    "created_at": "2009-12-08T20:52:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7592#issuecomment-64729",
    "user": "ncohen"
}
```

It could have, but in this case it was mainly my fault. I have no idea why, but the patch did not even apply on my version, perhaps they were not based on alpha... Here is a new version based on alpha, with my excuses :-)



---

archive/issue_comments_064730.json:
```json
{
    "body": "There was a small mistake in the \n\n```\nif vertex_bound:            \n        CORRECTED LINE\n```\n\nSome variable had no assigned value.... And the patch I just updated takes this into account :-)",
    "created_at": "2009-12-08T21:11:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7592#issuecomment-64730",
    "user": "ncohen"
}
```

There was a small mistake in the 

```
if vertex_bound:            
        CORRECTED LINE
```

Some variable had no assigned value.... And the patch I just updated takes this into account :-)



---

archive/issue_comments_064731.json:
```json
{
    "body": "You need more examples in the doctest section. Some of the options return something different than what the docs say, such as:\n\n```\nsage: g.flow(1,2, value_only=False)\n[3.0, Pappus Graph: Graph on 18 vertices]\n```\n",
    "created_at": "2009-12-15T17:04:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7592#issuecomment-64731",
    "user": "rlm"
}
```

You need more examples in the doctest section. Some of the options return something different than what the docs say, such as:

```
sage: g.flow(1,2, value_only=False)
[3.0, Pappus Graph: Graph on 18 vertices]
```




---

archive/issue_comments_064732.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-15T17:04:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7592#issuecomment-64732",
    "user": "rlm"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_064733.json:
```json
{
    "body": "Attachment [trac_7592.patch](tarball://root/attachments/some-uuid/ticket7592/trac_7592.patch) by ncohen created at 2009-12-16 00:44:53\n\nI corrected the documentation as I finally thought returning a graph would be much more useful :-)\n\nI also added a more interesting example of what one can do with flows :-)\n\nNathann",
    "created_at": "2009-12-16T00:44:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7592#issuecomment-64733",
    "user": "ncohen"
}
```

Attachment [trac_7592.patch](tarball://root/attachments/some-uuid/ticket7592/trac_7592.patch) by ncohen created at 2009-12-16 00:44:53

I corrected the documentation as I finally thought returning a graph would be much more useful :-)

I also added a more interesting example of what one can do with flows :-)

Nathann



---

archive/issue_comments_064734.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-16T00:44:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7592#issuecomment-64734",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064735.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-16T02:52:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7592#issuecomment-64735",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064736.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-19T21:09:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7592#issuecomment-64736",
    "user": "mhansen"
}
```

Resolution: fixed
