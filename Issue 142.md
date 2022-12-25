# Issue 142: sage build shouldn't modify $HOME

archive/issues_000142.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\n>\n> Yep...  My $HOME/.sage belonged to \"root\".  I have no idea why that\n> happened either...  Maybe I used a \"sudo\" when I shouldn't...  (But I\n> really think I just used to \"make\".)  In any case, a \"sudo chown -R\"\n> fixed it.\n\nYes, this is a known bug in the install process. SAGE get's run \nduring the install, which can cause some problems like you just\nhad if the user doing the build is root but the $HOME for root\nis not /root.\n\nWilliam\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/142\n\n",
    "created_at": "2006-10-21T03:37:21Z",
    "labels": [
        "component: packages: standard",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sage build shouldn't modify $HOME",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/142",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
>
> Yep...  My $HOME/.sage belonged to "root".  I have no idea why that
> happened either...  Maybe I used a "sudo" when I shouldn't...  (But I
> really think I just used to "make".)  In any case, a "sudo chown -R"
> fixed it.

Yes, this is a known bug in the install process. SAGE get's run 
during the install, which can cause some problems like you just
had if the user doing the build is root but the $HOME for root
is not /root.

William
```


Issue created by migration from https://trac.sagemath.org/ticket/142





---

archive/issue_events_000148.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-10-21T01:48:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/142",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/142#event-148"
}
```



---

archive/issue_comments_000653.json:
```json
{
    "body": "Sage should *definitely* be allowed to run during the build.  That's just the\nway it is.",
    "created_at": "2007-10-21T01:48:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/142#issuecomment-653",
    "user": "https://github.com/williamstein"
}
```

Sage should *definitely* be allowed to run during the build.  That's just the
way it is.



---

archive/issue_comments_000654.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2007-10-21T01:48:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/142#issuecomment-654",
    "user": "https://github.com/williamstein"
}
```

Resolution: invalid
