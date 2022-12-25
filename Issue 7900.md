# Issue 7900: Replace variables like $RM with  'rm' in Mercurial

archive/issues_007900.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @jaapspies @jhpalmieri\n\nIt was agreed recently that variables would not be used for very common commands like MV, MKDIR etc.\n\n     http://groups.google.com/group/sage-devel/browse_thread/thread/bd7ae07a1157bead/970aa0dc8fa56ab7?lnk=raot\n\n#7818 usets these, so this package will break. The fix is to simply replace things like\n\n$LN with 'ln'\n\nAn updated .spkg can be found at \n\nhttp://boxen.math.washington.edu/home/kirkby/portability/mercurial-1.3.1.p1/mercurial-1.3.1.p1.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/7900\n\n",
    "created_at": "2010-01-12T04:09:55Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Replace variables like $RM with  'rm' in Mercurial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7900",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: GeorgSWeber

CC:  @jaapspies @jhpalmieri

It was agreed recently that variables would not be used for very common commands like MV, MKDIR etc.

     http://groups.google.com/group/sage-devel/browse_thread/thread/bd7ae07a1157bead/970aa0dc8fa56ab7?lnk=raot

#7818 usets these, so this package will break. The fix is to simply replace things like

$LN with 'ln'

An updated .spkg can be found at 

http://boxen.math.washington.edu/home/kirkby/portability/mercurial-1.3.1.p1/mercurial-1.3.1.p1.spkg

Issue created by migration from https://trac.sagemath.org/ticket/7900





---

archive/issue_comments_068590.json:
```json
{
    "body": "Attachment [mercurial-variables-to-commands.patch](tarball://root/attachments/some-uuid/ticket7900/mercurial-variables-to-commands.patch) by drkirkby created at 2010-01-12 04:11:49",
    "created_at": "2010-01-12T04:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7900#issuecomment-68590",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [mercurial-variables-to-commands.patch](tarball://root/attachments/some-uuid/ticket7900/mercurial-variables-to-commands.patch) by drkirkby created at 2010-01-12 04:11:49



---

archive/issue_comments_068591.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-12T04:15:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7900#issuecomment-68591",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068592.json:
```json
{
    "body": "The new package looks good. Positive review.\n\nJaap",
    "created_at": "2010-01-12T11:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7900#issuecomment-68592",
    "user": "https://github.com/jaapspies"
}
```

The new package looks good. Positive review.

Jaap



---

archive/issue_comments_068593.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-12T11:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7900#issuecomment-68593",
    "user": "https://github.com/jaapspies"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008115.json:
```json
{
    "actor": "@rlmill",
    "created_at": "2010-01-14T02:58:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7900",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7900#event-8115"
}
```



---

archive/issue_comments_068594.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-14T02:58:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7900#issuecomment-68594",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
