# Issue 2526: switch charpoly mod p back to linbox as default

archive/issues_002526.json:
```json
{
    "body": "Assignee: @williamstein\n\nDue to problems with LinBox's charpoly mod p we switched the default implementation to use in 2.10.3 to the native Sage version. Since Linbox is about three times as fast switch back the default.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2526\n\n",
    "created_at": "2008-03-15T02:08:59Z",
    "labels": [
        "basic arithmetic",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "switch charpoly mod p back to linbox as default",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2526",
    "user": "mabshoff"
}
```
Assignee: @williamstein

Due to problems with LinBox's charpoly mod p we switched the default implementation to use in 2.10.3 to the native Sage version. Since Linbox is about three times as fast switch back the default.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/2526





---

archive/issue_comments_017228.json:
```json
{
    "body": "This depends on #2525 to be merged.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-15T02:09:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2526#issuecomment-17228",
    "user": "mabshoff"
}
```

This depends on #2525 to be merged.

Cheers,

Michael



---

archive/issue_comments_017229.json:
```json
{
    "body": "this patch straight up revers #2453",
    "created_at": "2008-03-15T05:19:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2526#issuecomment-17229",
    "user": "mabshoff"
}
```

this patch straight up revers #2453



---

archive/issue_comments_017230.json:
```json
{
    "body": "Attachment [trac_2526.patch](tarball://root/attachments/some-uuid/ticket2526/trac_2526.patch) by mabshoff created at 2008-03-15 05:19:32",
    "created_at": "2008-03-15T05:19:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2526#issuecomment-17230",
    "user": "mabshoff"
}
```

Attachment [trac_2526.patch](tarball://root/attachments/some-uuid/ticket2526/trac_2526.patch) by mabshoff created at 2008-03-15 05:19:32



---

archive/issue_comments_017231.json:
```json
{
    "body": "As I don't know what the problems were with the linbox function originally, or whether that problem has been fixed, I don't know whether switching the default back to linbox is a good idea!",
    "created_at": "2008-03-27T17:24:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2526#issuecomment-17231",
    "user": "@JohnCremona"
}
```

As I don't know what the problems were with the linbox function originally, or whether that problem has been fixed, I don't know whether switching the default back to linbox is a good idea!



---

archive/issue_comments_017232.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2008-03-27T17:34:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2526#issuecomment-17232",
    "user": "mabshoff"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_comments_017233.json:
```json
{
    "body": "Replying to [comment:4 cremona]:\n> As I don't know what the problems were with the linbox function originally, or whether that problem has been fixed, I don't know whether switching the default back to linbox is a good idea!\n\nHi John,\n\nthe bug in LinBox still hasn't been fixed. Hence this patch will not be applied until the LinBox.spkg with the bug fix will be merged in Sage. It looked initially that this would happen quickly, but that didn't go as planned. Since the bug is trivial and has a positive review it can be instantly merged once the upstream fix in LinBox has happened.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-27T17:34:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2526#issuecomment-17233",
    "user": "mabshoff"
}
```

Replying to [comment:4 cremona]:
> As I don't know what the problems were with the linbox function originally, or whether that problem has been fixed, I don't know whether switching the default back to linbox is a good idea!

Hi John,

the bug in LinBox still hasn't been fixed. Hence this patch will not be applied until the LinBox.spkg with the bug fix will be merged in Sage. It looked initially that this would happen quickly, but that didn't go as planned. Since the bug is trivial and has a positive review it can be instantly merged once the upstream fix in LinBox has happened.

Cheers,

Michael



---

archive/issue_comments_017234.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-27T17:34:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2526#issuecomment-17234",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_017235.json:
```json
{
    "body": "Sounds good -as long as it doesn't get forgotten!",
    "created_at": "2008-03-27T17:51:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2526#issuecomment-17235",
    "user": "@JohnCremona"
}
```

Sounds good -as long as it doesn't get forgotten!



---

archive/issue_comments_017236.json:
```json
{
    "body": "Replying to [comment:6 cremona]:\n> Sounds good -as long as it doesn't get forgotten!\n\nNah, it is actually listed on my internal ToDo list. And I am sure Clement and William will also remember. Since it has a positive review it always pops up when I look for tickets than can be merged.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-28T08:09:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2526#issuecomment-17236",
    "user": "mabshoff"
}
```

Replying to [comment:6 cremona]:
> Sounds good -as long as it doesn't get forgotten!

Nah, it is actually listed on my internal ToDo list. And I am sure Clement and William will also remember. Since it has a positive review it always pops up when I look for tickets than can be merged.

Cheers,

Michael



---

archive/issue_comments_017237.json:
```json
{
    "body": "An equivalent patch was merged in Sage 3.0.alpha0",
    "created_at": "2008-04-04T01:09:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2526#issuecomment-17237",
    "user": "mabshoff"
}
```

An equivalent patch was merged in Sage 3.0.alpha0



---

archive/issue_comments_017238.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-04T01:09:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2526#issuecomment-17238",
    "user": "mabshoff"
}
```

Resolution: fixed
