# Issue 5540: search_doc produces incorrect URLs

archive/issues_005540.json:
```json
{
    "body": "Assignee: tba\n\nKeywords: sphinx, documentation, search_doc\n\nFrom [sage-devel](http://groups.google.com/group/sage-devel/t/2da54338e1dda0fe):\n\n```\nIf I do search_doc(\"orbit\") in sage 3.4 (in the notebook), I get\n(amongst others) a link:\n\nhttps://localhost:8000/doc/live/html/en/reference/genindex-F.html\n\nwhich leads to a \"resource cannot be found\". The appropriate link\nseems to be\n\nhttps://localhost:8000/doc/live/reference/genindex-F.html\n\nIt could be that my sage is just screwed up, but if someone else can\nconfirm this error, a ticket should be opened. I bet it's easy to fix.}}}\n\nIssue created by migration from https://trac.sagemath.org/ticket/5540\n\n",
    "created_at": "2009-03-17T02:26:54Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "search_doc produces incorrect URLs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5540",
    "user": "https://github.com/dandrake"
}
```
Assignee: tba

Keywords: sphinx, documentation, search_doc

From [sage-devel](http://groups.google.com/group/sage-devel/t/2da54338e1dda0fe):

```
If I do search_doc("orbit") in sage 3.4 (in the notebook), I get
(amongst others) a link:

https://localhost:8000/doc/live/html/en/reference/genindex-F.html

which leads to a "resource cannot be found". The appropriate link
seems to be

https://localhost:8000/doc/live/reference/genindex-F.html

It could be that my sage is just screwed up, but if someone else can
confirm this error, a ticket should be opened. I bet it's easy to fix.}}}

Issue created by migration from https://trac.sagemath.org/ticket/5540





---

archive/issue_comments_043012.json:
```json
{
    "body": "Changing assignee from tba to @jhpalmieri.",
    "created_at": "2009-03-17T03:22:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5540#issuecomment-43012",
    "user": "https://github.com/jhpalmieri"
}
```

Changing assignee from tba to @jhpalmieri.



---

archive/issue_comments_043013.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-17T03:22:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5540#issuecomment-43013",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to assigned.



---

archive/issue_comments_043014.json:
```json
{
    "body": "Changing component from documentation to misc.",
    "created_at": "2009-03-17T03:22:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5540#issuecomment-43014",
    "user": "https://github.com/jhpalmieri"
}
```

Changing component from documentation to misc.



---

archive/issue_comments_043015.json:
```json
{
    "body": "The attached patch fixes the problem for me.  I fixed the URLs by getting rid of the first two components of the path (replacing 'F', the filename, with `F.split('/', 2)[2]`).  I found another issue: for some reason, probably to get rid of the Sage banner which used to be part of the search output, the raw results 'r' of the search were processed using `r.splitlines()[4:]`.  Since the Sage banner is no longer part of the search output, this now discards the first four results.  (Therefore it's probably my fault: see #4832.) I fixed that, too.",
    "created_at": "2009-03-17T03:22:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5540#issuecomment-43015",
    "user": "https://github.com/jhpalmieri"
}
```

The attached patch fixes the problem for me.  I fixed the URLs by getting rid of the first two components of the path (replacing 'F', the filename, with `F.split('/', 2)[2]`).  I found another issue: for some reason, probably to get rid of the Sage banner which used to be part of the search output, the raw results 'r' of the search were processed using `r.splitlines()[4:]`.  Since the Sage banner is no longer part of the search output, this now discards the first four results.  (Therefore it's probably my fault: see #4832.) I fixed that, too.



---

archive/issue_comments_043016.json:
```json
{
    "body": "Attachment [5540.patch](tarball://root/attachments/some-uuid/ticket5540/5540.patch) by @nbruin created at 2009-03-17 04:06:43\n\nPatch solves the problem for me. The patch is also tiny, so while I'm not familiar with the code, I wouldn't expect it to cause any regressions.",
    "created_at": "2009-03-17T04:06:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5540#issuecomment-43016",
    "user": "https://github.com/nbruin"
}
```

Attachment [5540.patch](tarball://root/attachments/some-uuid/ticket5540/5540.patch) by @nbruin created at 2009-03-17 04:06:43

Patch solves the problem for me. The patch is also tiny, so while I'm not familiar with the code, I wouldn't expect it to cause any regressions.



---

archive/issue_comments_043017.json:
```json
{
    "body": "Positive review here.",
    "created_at": "2009-03-17T04:09:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5540#issuecomment-43017",
    "user": "https://github.com/dandrake"
}
```

Positive review here.



---

archive/issue_comments_043018.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-25T07:34:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5540#issuecomment-43018",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_043019.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T07:34:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5540#issuecomment-43019",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_events_005787.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-03-25T07:34:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5540",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5540#event-5787"
}
```
