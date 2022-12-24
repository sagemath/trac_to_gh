# Issue 2134: arrows for digraphs

archive/issues_002134.json:
```json
{
    "body": "Assignee: was\n\nnote - author of patch doesn't give a hoot. do what you will with it, i won't touch it again. several things may break, for example, the only guaranteed color format is a float tuple. also, no new documentation.\n\neverybody wants it, so here it is... :-D\n\nIssue created by migration from https://trac.sagemath.org/ticket/2134\n\n",
    "created_at": "2008-02-10T00:25:14Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "arrows for digraphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2134",
    "user": "rlm"
}
```
Assignee: was

note - author of patch doesn't give a hoot. do what you will with it, i won't touch it again. several things may break, for example, the only guaranteed color format is a float tuple. also, no new documentation.

everybody wants it, so here it is... :-D

Issue created by migration from https://trac.sagemath.org/ticket/2134





---

archive/issue_comments_013992.json:
```json
{
    "body": "Attachment [arrows.patch](tarball://root/attachments/some-uuid/ticket2134/arrows.patch) by rlm created at 2008-02-10 00:26:13",
    "created_at": "2008-02-10T00:26:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2134#issuecomment-13992",
    "user": "rlm"
}
```

Attachment [arrows.patch](tarball://root/attachments/some-uuid/ticket2134/arrows.patch) by rlm created at 2008-02-10 00:26:13



---

archive/issue_comments_013993.json:
```json
{
    "body": "Note -- the author rlm of the patch was days without sleep at time of writing... :-)",
    "created_at": "2008-02-10T06:47:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2134#issuecomment-13993",
    "user": "was"
}
```

Note -- the author rlm of the patch was days without sleep at time of writing... :-)



---

archive/issue_comments_013994.json:
```json
{
    "body": "Attachment [arrows-2.patch](tarball://root/attachments/some-uuid/ticket2134/arrows-2.patch) by rlm created at 2008-02-11 21:02:55",
    "created_at": "2008-02-11T21:02:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2134#issuecomment-13994",
    "user": "rlm"
}
```

Attachment [arrows-2.patch](tarball://root/attachments/some-uuid/ticket2134/arrows-2.patch) by rlm created at 2008-02-11 21:02:55



---

archive/issue_comments_013995.json:
```json
{
    "body": "Oops, I touched it again... But this is after 14 straight hours of sleep.",
    "created_at": "2008-02-11T21:03:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2134#issuecomment-13995",
    "user": "rlm"
}
```

Oops, I touched it again... But this is after 14 straight hours of sleep.



---

archive/issue_comments_013996.json:
```json
{
    "body": "Looking a bit at this patch, does NetworkX do much for graph drawing that we couldn't be doing ourselves with matplotlib. Right now, for instance, it doesn't play well with the 2d->3d command because you can't (easily) get at the primitives that make up a graph. \n\nThat being said, I think arrows are much nicer than sleeves.",
    "created_at": "2008-02-12T01:40:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2134#issuecomment-13996",
    "user": "robertwb"
}
```

Looking a bit at this patch, does NetworkX do much for graph drawing that we couldn't be doing ourselves with matplotlib. Right now, for instance, it doesn't play well with the 2d->3d command because you can't (easily) get at the primitives that make up a graph. 

That being said, I think arrows are much nicer than sleeves.



---

archive/issue_comments_013997.json:
```json
{
    "body": "I might have the exact details wrong, but NetworkX uses pylab, which uses matplotlib. In fact, after trying to implement the arrows in NX, I think it would be easier to ultimately phase NX out of graph plotting completely. (After reimplementing the base structure, I'm starting to wonder how much NX we ultimately need...)",
    "created_at": "2008-02-12T20:25:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2134#issuecomment-13997",
    "user": "rlm"
}
```

I might have the exact details wrong, but NetworkX uses pylab, which uses matplotlib. In fact, after trying to implement the arrows in NX, I think it would be easier to ultimately phase NX out of graph plotting completely. (After reimplementing the base structure, I'm starting to wonder how much NX we ultimately need...)



---

archive/issue_comments_013998.json:
```json
{
    "body": "Looks good to me. I've created a ticket for phasing NetworkX out of the graph plotting code: #2157, though I bet it implements lots of other useful stuff.",
    "created_at": "2008-02-14T05:48:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2134#issuecomment-13998",
    "user": "robertwb"
}
```

Looks good to me. I've created a ticket for phasing NetworkX out of the graph plotting code: #2157, though I bet it implements lots of other useful stuff.



---

archive/issue_comments_013999.json:
```json
{
    "body": "Robert, the patch currently doesn't apply cleanly any more due to\n\n```\nchangeset:   8329:657c0727bbd2\nuser:        Robert L. Miller <rlm@rlmiller.org>\ndate:        Thu Feb 07 00:18:51 2008 -0800\nsummary:     plot loops.\n```\n\nThe issue is with the second hunk in `sage/graphs/graph.py`, so could you rebase the patch with your plot loop patch applied?\n\nCheers,\n\nMichael",
    "created_at": "2008-02-14T09:56:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2134#issuecomment-13999",
    "user": "mabshoff"
}
```

Robert, the patch currently doesn't apply cleanly any more due to

```
changeset:   8329:657c0727bbd2
user:        Robert L. Miller <rlm@rlmiller.org>
date:        Thu Feb 07 00:18:51 2008 -0800
summary:     plot loops.
```

The issue is with the second hunk in `sage/graphs/graph.py`, so could you rebase the patch with your plot loop patch applied?

Cheers,

Michael



---

archive/issue_comments_014000.json:
```json
{
    "body": "Apply this instead of the others.",
    "created_at": "2008-02-15T00:42:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2134#issuecomment-14000",
    "user": "rlm"
}
```

Apply this instead of the others.



---

archive/issue_comments_014001.json:
```json
{
    "body": "Attachment [arrows-new.patch](tarball://root/attachments/some-uuid/ticket2134/arrows-new.patch) by rlm created at 2008-02-15 00:45:06\n\nRebased- in doing so, I uncovered two bugs:\n1 Graphics import depended magically on it happening on another level\n2 Arrow plotting would have crashed on plotting loops\n\nShould now be ready to include.",
    "created_at": "2008-02-15T00:45:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2134#issuecomment-14001",
    "user": "rlm"
}
```

Attachment [arrows-new.patch](tarball://root/attachments/some-uuid/ticket2134/arrows-new.patch) by rlm created at 2008-02-15 00:45:06

Rebased- in doing so, I uncovered two bugs:
1 Graphics import depended magically on it happening on another level
2 Arrow plotting would have crashed on plotting loops

Should now be ready to include.



---

archive/issue_comments_014002.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-15T02:18:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2134#issuecomment-14002",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014003.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha0",
    "created_at": "2008-02-15T02:18:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2134#issuecomment-14003",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha0
