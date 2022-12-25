# Issue 5910: move logic module boolopt.py to another enhancement ticket

archive/issues_005910.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: Quine-McCluskey, logic\n\nThis is a followup to #545. As discussed at #545, the module `boolopt.py` is moved to this enhancement ticket. So basically, #545 no longer requires boolopt.py to reach 100% doctest coverage in order to be merged into Sage. Thus the only work needed to be done here is to bring coverage of boolopt.py to 100%.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5910\n\n",
    "created_at": "2009-04-27T11:53:41Z",
    "labels": [
        "component: basic arithmetic"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "move logic module boolopt.py to another enhancement ticket",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5910",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: somebody

Keywords: Quine-McCluskey, logic

This is a followup to #545. As discussed at #545, the module `boolopt.py` is moved to this enhancement ticket. So basically, #545 no longer requires boolopt.py to reach 100% doctest coverage in order to be merged into Sage. Thus the only work needed to be done here is to bring coverage of boolopt.py to 100%.

Issue created by migration from https://trac.sagemath.org/ticket/5910





---

archive/issue_comments_046614.json:
```json
{
    "body": "Attachment [trac_5910-doctest-simplify.patch](tarball://root/attachments/some-uuid/ticket5910/trac_5910-doctest-simplify.patch) by mvngu created at 2009-04-27 13:20:57\n\nRestore the method simplify() and its doctests",
    "created_at": "2009-04-27T13:20:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5910#issuecomment-46614",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_5910-doctest-simplify.patch](tarball://root/attachments/some-uuid/ticket5910/trac_5910-doctest-simplify.patch) by mvngu created at 2009-04-27 13:20:57

Restore the method simplify() and its doctests



---

archive/issue_comments_046615.json:
```json
{
    "body": "Please make sure to convert the newlines to standard Unix convention since it seems that some newlines are in Windows format. It would also be good to get all this restified, get the coverage of logic.py up and get the code into the reference manual post ReST conversion - not that this all has to happen on this ticket. I am just glad we are done wioth #545 :)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T03:30:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5910#issuecomment-46615",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Please make sure to convert the newlines to standard Unix convention since it seems that some newlines are in Windows format. It would also be good to get all this restified, get the coverage of logic.py up and get the code into the reference manual post ReST conversion - not that this all has to happen on this ticket. I am just glad we are done wioth #545 :)

Cheers,

Michael



---

archive/issue_comments_046616.json:
```json
{
    "body": "with Unix newline",
    "created_at": "2009-05-05T06:24:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5910#issuecomment-46616",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

with Unix newline



---

archive/issue_comments_046617.json:
```json
{
    "body": "Attachment [trac_5910-boolopt.patch](tarball://root/attachments/some-uuid/ticket5910/trac_5910-boolopt.patch) by @aghitza created at 2010-01-02 03:18:33",
    "created_at": "2010-01-02T03:18:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5910#issuecomment-46617",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_5910-boolopt.patch](tarball://root/attachments/some-uuid/ticket5910/trac_5910-boolopt.patch) by @aghitza created at 2010-01-02 03:18:33



---

archive/issue_comments_046618.json:
```json
{
    "body": "Changing component from basic arithmetic to misc.",
    "created_at": "2010-01-02T03:18:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5910#issuecomment-46618",
    "user": "https://github.com/aghitza"
}
```

Changing component from basic arithmetic to misc.



---

archive/issue_comments_046619.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-07-23T14:55:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5910#issuecomment-46619",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid



---

archive/issue_comments_046620.json:
```json
{
    "body": "Given http://comments.gmane.org/gmane.comp.mathematics.sage.devel/67430 , I think we can close this.  The file is still here for reference if we ever need it.",
    "created_at": "2013-07-23T14:55:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5910#issuecomment-46620",
    "user": "https://github.com/mwhansen"
}
```

Given http://comments.gmane.org/gmane.comp.mathematics.sage.devel/67430 , I think we can close this.  The file is still here for reference if we ever need it.
