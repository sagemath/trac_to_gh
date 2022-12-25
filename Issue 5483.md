# Issue 5483: [with preliminary patch; not ready for review; request comments] Add explain_pickle module; allow overriding class lookup for unpickling

archive/issues_005483.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  @williamstein\n\nexplain_pickle is an unpickler (intended to be totally compatible with the cPickle unpickler) that produces Sage source code, which can then be evaluated by sage_eval.  This is useful to see exactly how the unpickle process works.  For example:\n\n\n```\nsage: explain_pickle(dumps(3))\n\npg_make_integer = unpickle_global('sage.rings.integer', 'make_integer')\npg_make_integer('3')\nsage: explain_pickle(dumps(3), in_current_sage=True)\n\nfrom sage.rings.integer import make_integer\nmake_integer('3')\n```\n\n\nI think the code works, but I'm not done writing documentation and doctests.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5483\n\n",
    "created_at": "2009-03-11T07:12:13Z",
    "labels": [
        "component: misc"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "[with preliminary patch; not ready for review; request comments] Add explain_pickle module; allow overriding class lookup for unpickling",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5483",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: cwitty

CC:  @williamstein

explain_pickle is an unpickler (intended to be totally compatible with the cPickle unpickler) that produces Sage source code, which can then be evaluated by sage_eval.  This is useful to see exactly how the unpickle process works.  For example:


```
sage: explain_pickle(dumps(3))

pg_make_integer = unpickle_global('sage.rings.integer', 'make_integer')
pg_make_integer('3')
sage: explain_pickle(dumps(3), in_current_sage=True)

from sage.rings.integer import make_integer
make_integer('3')
```


I think the code works, but I'm not done writing documentation and doctests.

Issue created by migration from https://trac.sagemath.org/ticket/5483





---

archive/issue_comments_042462.json:
```json
{
    "body": "I am not technically qualified to review this, patch it has been in the sage-combinat queue for a couple weeks, and has proven really useful! So +1 from Florent and myself.",
    "created_at": "2009-04-16T16:59:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5483#issuecomment-42462",
    "user": "https://github.com/nthiery"
}
```

I am not technically qualified to review this, patch it has been in the sage-combinat queue for a couple weeks, and has proven really useful! So +1 from Florent and myself.



---

archive/issue_comments_042463.json:
```json
{
    "body": "Carl: Can you change the summary in case this patch is ready for review?\n\nI changed it so that this ticket is picked up by the right report.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T21:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5483#issuecomment-42463",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Carl: Can you change the summary in case this patch is ready for review?

I changed it so that this ticket is picked up by the right report.

Cheers,

Michael



---

archive/issue_comments_042464.json:
```json
{
    "body": "Attachment [trac5483-explain-pickle-v2.patch](tarball://root/attachments/some-uuid/ticket5483/trac5483-explain-pickle-v2.patch) by cwitty created at 2009-05-17 00:29:40\n\nI finally managed to finish writing the doctests (and fixed a few bugs in the process).",
    "created_at": "2009-05-17T00:29:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5483#issuecomment-42464",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac5483-explain-pickle-v2.patch](tarball://root/attachments/some-uuid/ticket5483/trac5483-explain-pickle-v2.patch) by cwitty created at 2009-05-17 00:29:40

I finally managed to finish writing the doctests (and fixed a few bugs in the process).



---

archive/issue_comments_042465.json:
```json
{
    "body": "The new file(s) should get added to the reference manual so that people actually can read about them ;).\n\nCheers,\n\nMichael",
    "created_at": "2009-05-19T20:28:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5483#issuecomment-42465",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The new file(s) should get added to the reference manual so that people actually can read about them ;).

Cheers,

Michael



---

archive/issue_comments_042466.json:
```json
{
    "body": "Changing keywords from \"\" to \"pickling\".",
    "created_at": "2009-05-22T00:34:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5483#issuecomment-42466",
    "user": "https://github.com/nthiery"
}
```

Changing keywords from "" to "pickling".



---

archive/issue_comments_042467.json:
```json
{
    "body": "I have been using this patch on a regular basis without any issue. It is extremely useful, and very well and thoroughly documented.\n\nThe code itself is for the most part straightforward, yet pretty technical.\nBy its nature of the code, the included systematic unit tests should catch most potential bugs.\nChecking the tests themselves would require a thorough knowledge of the cpickle protocol which I do not have. But which I trust Carl to have.\nThe included integration test (comparing the result with cPickle on all the sage pickle jar) is a positive sign.\nAlso this code is mainly intended for interactive users, so remaining bugs in them should not cause a threat to the rest of the Sage library.\nBesides, this patch is a blocker for the category integration.\n\nI am about to attach a short patch fixing some ReST stuff, and adding explain_pickle to the reference manual as recommended by Michael.\n\nFor all those reason, I would give my two thumbs up for a positive review. And for advertising this cool tool beyond the Sage world.\n\nWilliam: what do you think?",
    "created_at": "2009-05-22T00:34:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5483#issuecomment-42467",
    "user": "https://github.com/nthiery"
}
```

I have been using this patch on a regular basis without any issue. It is extremely useful, and very well and thoroughly documented.

The code itself is for the most part straightforward, yet pretty technical.
By its nature of the code, the included systematic unit tests should catch most potential bugs.
Checking the tests themselves would require a thorough knowledge of the cpickle protocol which I do not have. But which I trust Carl to have.
The included integration test (comparing the result with cPickle on all the sage pickle jar) is a positive sign.
Also this code is mainly intended for interactive users, so remaining bugs in them should not cause a threat to the rest of the Sage library.
Besides, this patch is a blocker for the category integration.

I am about to attach a short patch fixing some ReST stuff, and adding explain_pickle to the reference manual as recommended by Michael.

For all those reason, I would give my two thumbs up for a positive review. And for advertising this cool tool beyond the Sage world.

William: what do you think?



---

archive/issue_comments_042468.json:
```json
{
    "body": "Attachment [trac5483-explain-pickle-v2-review.patch](tarball://root/attachments/some-uuid/ticket5483/trac5483-explain-pickle-v2-review.patch) by @nthiery created at 2009-05-22 22:53:36\n\nOral comment by William: no reason not to integrate this. Positive Review.",
    "created_at": "2009-05-22T22:53:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5483#issuecomment-42468",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac5483-explain-pickle-v2-review.patch](tarball://root/attachments/some-uuid/ticket5483/trac5483-explain-pickle-v2-review.patch) by @nthiery created at 2009-05-22 22:53:36

Oral comment by William: no reason not to integrate this. Positive Review.



---

archive/issue_comments_042469.json:
```json
{
    "body": "I get the failure at http://sage.pastebin.com/m4bec1638\n\nCarl, is it trivial?",
    "created_at": "2009-06-01T05:24:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5483#issuecomment-42469",
    "user": "https://github.com/mwhansen"
}
```

I get the failure at http://sage.pastebin.com/m4bec1638

Carl, is it trivial?



---

archive/issue_comments_042470.json:
```json
{
    "body": "This appears to be a difference in Python's repr(), possibly between Python 2.5.2 (from Sage 3.4.2 on my laptop, where I developed the patch) and Python 2.5.4 (from Sage 4.0 on sage.math).\n\nPython 2.5.2:\n\n```\n>>> v = ([],)\n>>> v[0].append(v)\n>>> repr(v)\n'([([...],)],)'\n```\n\n\nPython 2.5.4:\n\n```\n>>> v = ([],)\n>>> v[0].append(v)\n>>> repr(v)\n'([(...)],)'\n```\n\n\nI don't have time to experiment further right now, but I would suggest changing the expected output to the new version, and if it's consistent across all the test platforms then chalk it up to a change in Python and call it good.",
    "created_at": "2009-06-02T20:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5483#issuecomment-42470",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

This appears to be a difference in Python's repr(), possibly between Python 2.5.2 (from Sage 3.4.2 on my laptop, where I developed the patch) and Python 2.5.4 (from Sage 4.0 on sage.math).

Python 2.5.2:

```
>>> v = ([],)
>>> v[0].append(v)
>>> repr(v)
'([([...],)],)'
```


Python 2.5.4:

```
>>> v = ([],)
>>> v[0].append(v)
>>> repr(v)
'([(...)],)'
```


I don't have time to experiment further right now, but I would suggest changing the expected output to the new version, and if it's consistent across all the test platforms then chalk it up to a change in Python and call it good.



---

archive/issue_comments_042471.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-03T20:52:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5483#issuecomment-42471",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_012813.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-06-03T20:52:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5483",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5483#event-12813"
}
```



---

archive/issue_comments_042472.json:
```json
{
    "body": "I fixed the doctest.\n\nMerged in 4.0.1.rc0.",
    "created_at": "2009-06-03T20:52:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5483#issuecomment-42472",
    "user": "https://github.com/mwhansen"
}
```

I fixed the doctest.

Merged in 4.0.1.rc0.
