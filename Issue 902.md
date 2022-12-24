# Issue 902: implement computation of minpoly of symbolics

archive/issues_000902.json:
```json
{
    "body": "Assignee: @robertwb\n\nDo this by numerical approximation, algdep, checking equality.\n\nNOTE: Robert Bradshaw has already done this!! I haven't seen any code, etc.\n\nIssue created by migration from https://trac.sagemath.org/ticket/902\n\n",
    "created_at": "2007-10-15T16:54:15Z",
    "labels": [
        "calculus",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "implement computation of minpoly of symbolics",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/902",
    "user": "@williamstein"
}
```
Assignee: @robertwb

Do this by numerical approximation, algdep, checking equality.

NOTE: Robert Bradshaw has already done this!! I haven't seen any code, etc.

Issue created by migration from https://trac.sagemath.org/ticket/902





---

archive/issue_comments_005541.json:
```json
{
    "body": "Attachment [symbolic-minpoly.hg](tarball://root/attachments/some-uuid/ticket902/symbolic-minpoly.hg) by @robertwb created at 2007-10-15 19:49:01\n\nThe above patch implements this. \n\nI also added a bit of code to the ring __getitem__ method so constructions like ZZ[sqrt(2)] and QQ[I] work. I have not yet run \"sage -testall\"to make sure that it doesn't ruin any doctests elsewhere, but it should be good. It is also unclear how to handle names in this case, so the code there just names generators a, b, c, ... except for a couple of special cases.",
    "created_at": "2007-10-15T19:49:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/902#issuecomment-5541",
    "user": "@robertwb"
}
```

Attachment [symbolic-minpoly.hg](tarball://root/attachments/some-uuid/ticket902/symbolic-minpoly.hg) by @robertwb created at 2007-10-15 19:49:01

The above patch implements this. 

I also added a bit of code to the ring __getitem__ method so constructions like ZZ[sqrt(2)] and QQ[I] work. I have not yet run "sage -testall"to make sure that it doesn't ruin any doctests elsewhere, but it should be good. It is also unclear how to handle names in this case, so the code there just names generators a, b, c, ... except for a couple of special cases.



---

archive/issue_comments_005542.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-19T02:29:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/902#issuecomment-5542",
    "user": "@williamstein"
}
```

Resolution: fixed
