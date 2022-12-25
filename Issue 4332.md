# Issue 4332: notebook() docstring needs improvement

archive/issues_004332.json:
```json
{
    "body": "Assignee: @dandrake\n\nCC:  @jasongrout\n\nThe docstring for notebook() could use a bit of improvement. In particular, the `directory` option should be clearer. I also think we should *not* say \"do a web search for more details\"; if the information is too much for the docstring, we should make a page on the wiki and point users to that.\n\nAlso, given the recent forkbomb on sage.math, the `-u` flag for ulimit should be documented.\n\nI plan to work on this during this week's Bug Day.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4332\n\n",
    "created_at": "2008-10-21T00:28:35Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "notebook() docstring needs improvement",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4332",
    "user": "https://github.com/dandrake"
}
```
Assignee: @dandrake

CC:  @jasongrout

The docstring for notebook() could use a bit of improvement. In particular, the `directory` option should be clearer. I also think we should *not* say "do a web search for more details"; if the information is too much for the docstring, we should make a page on the wiki and point users to that.

Also, given the recent forkbomb on sage.math, the `-u` flag for ulimit should be documented.

I plan to work on this during this week's Bug Day.

Issue created by migration from https://trac.sagemath.org/ticket/4332





---

archive/issue_comments_031705.json:
```json
{
    "body": "Attachment [trac4332.patch](tarball://root/attachments/some-uuid/ticket4332/trac4332.patch) by @dandrake created at 2008-10-24 02:50:21\n\nPatch attached. A lot of it is reformatting and typos, but I also added a reference to a new page on the wiki: http://wiki.sagemath.org/StartingTheNotebook. The installation guide only has a page on running a publically-accessible notebook server (http://sagemath.org/doc/inst/node10.html) and nothing on other single-user cases.\n\nAlso, that page on the installation guide is outdated; someone should go through and fix it up, and perhaps add something on using virtual machines, which these days seems to be the way to go; I have a start at that at http://wiki.sagemath.org/DanDrake/JustEnoughSageServer.",
    "created_at": "2008-10-24T02:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4332#issuecomment-31705",
    "user": "https://github.com/dandrake"
}
```

Attachment [trac4332.patch](tarball://root/attachments/some-uuid/ticket4332/trac4332.patch) by @dandrake created at 2008-10-24 02:50:21

Patch attached. A lot of it is reformatting and typos, but I also added a reference to a new page on the wiki: http://wiki.sagemath.org/StartingTheNotebook. The installation guide only has a page on running a publically-accessible notebook server (http://sagemath.org/doc/inst/node10.html) and nothing on other single-user cases.

Also, that page on the installation guide is outdated; someone should go through and fix it up, and perhaps add something on using virtual machines, which these days seems to be the way to go; I have a start at that at http://wiki.sagemath.org/DanDrake/JustEnoughSageServer.



---

archive/issue_comments_031706.json:
```json
{
    "body": "Nice work.",
    "created_at": "2008-10-24T02:55:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4332#issuecomment-31706",
    "user": "https://github.com/mwhansen"
}
```

Nice work.



---

archive/issue_comments_031707.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-26T03:25:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4332#issuecomment-31707",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_031708.json:
```json
{
    "body": "Merged in Sage 3.2.alpha1.\n\nDan: Please post patches and not diffs in the future.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-26T03:25:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4332#issuecomment-31708",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha1.

Dan: Please post patches and not diffs in the future.

Cheers,

Michael



---

archive/issue_comments_031709.json:
```json
{
    "body": "Replying to [comment:4 mabshoff]:\n> Dan: Please post patches and not diffs in the future.\n\nOops. Sorry. I keep doing `qdiff` when I mean `export qtip`.",
    "created_at": "2008-10-26T23:52:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4332#issuecomment-31709",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:4 mabshoff]:
> Dan: Please post patches and not diffs in the future.

Oops. Sorry. I keep doing `qdiff` when I mean `export qtip`.
