# Issue 3779: inconsistency for variables method, leads to errors in differentiation

archive/issues_003779.json:
```json
{
    "body": "Assignee: gfurnish\n\n\n```\n\nHi William:\n\nI was running Sage 3.0.2 on Linux when the error occurred.  Just now i\nupgraded to 'sage-3.0.6-i686-Linux-debian-intel' without problems, ran\nthe same code (in a notebook and on the command line), and got the\nsame error.  Hmm, i don't understand why Sage can do 'diff(f*SR(2),x)'\nbut not 'diff(f*SR(1),x)'.\n\nAlex\n```\n\n\nThis boils down to the fact that some symbolic objects take an extra argument in their `variables` method. It is unclear what the meaning of this argument is (couldn't find any examples) and if it should be removed, or added, to make things consistent. (I'd guess removed, but I don't want to break things.) \n\nIssue created by migration from https://trac.sagemath.org/ticket/3779\n\n",
    "created_at": "2008-08-06T04:29:22Z",
    "labels": [
        "calculus",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "inconsistency for variables method, leads to errors in differentiation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3779",
    "user": "robertwb"
}
```
Assignee: gfurnish


```

Hi William:

I was running Sage 3.0.2 on Linux when the error occurred.  Just now i
upgraded to 'sage-3.0.6-i686-Linux-debian-intel' without problems, ran
the same code (in a notebook and on the command line), and got the
same error.  Hmm, i don't understand why Sage can do 'diff(f*SR(2),x)'
but not 'diff(f*SR(1),x)'.

Alex
```


This boils down to the fact that some symbolic objects take an extra argument in their `variables` method. It is unclear what the meaning of this argument is (couldn't find any examples) and if it should be removed, or added, to make things consistent. (I'd guess removed, but I don't want to break things.) 

Issue created by migration from https://trac.sagemath.org/ticket/3779





---

archive/issue_comments_026868.json:
```json
{
    "body": "The argument doesn't exist in symbolics, so I'm in favor of removal (and I have no idea what it does either)",
    "created_at": "2008-08-06T06:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3779#issuecomment-26868",
    "user": "gfurnish"
}
```

The argument doesn't exist in symbolics, so I'm in favor of removal (and I have no idea what it does either)



---

archive/issue_comments_026869.json:
```json
{
    "body": "Changing assignee from gfurnish to mhansen.",
    "created_at": "2008-08-06T20:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3779#issuecomment-26869",
    "user": "mhansen"
}
```

Changing assignee from gfurnish to mhansen.



---

archive/issue_comments_026870.json:
```json
{
    "body": "The argument was used to pass in additional variables to the variables method which would then be subsequently returned.  This functionality was never used, and I can't / couldn't think of a case where it would be needed.  So, I do think the correct fix is to remove it.  I've attached a patch which does that and passes tests.",
    "created_at": "2008-08-06T20:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3779#issuecomment-26870",
    "user": "mhansen"
}
```

The argument was used to pass in additional variables to the variables method which would then be subsequently returned.  This functionality was never used, and I can't / couldn't think of a case where it would be needed.  So, I do think the correct fix is to remove it.  I've attached a patch which does that and passes tests.



---

archive/issue_comments_026871.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-08-06T20:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3779#issuecomment-26871",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_026872.json:
```json
{
    "body": "Attachment [trac_3779.patch](tarball://root/attachments/some-uuid/ticket3779/trac_3779.patch) by robertwb created at 2008-08-07 02:02:48\n\nLooks good to me, and fixes the bug. The only question I had is why you wrote tuple([]) rather than (), but I'm OK with that.",
    "created_at": "2008-08-07T02:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3779#issuecomment-26872",
    "user": "robertwb"
}
```

Attachment [trac_3779.patch](tarball://root/attachments/some-uuid/ticket3779/trac_3779.patch) by robertwb created at 2008-08-07 02:02:48

Looks good to me, and fixes the bug. The only question I had is why you wrote tuple([]) rather than (), but I'm OK with that.



---

archive/issue_comments_026873.json:
```json
{
    "body": "There's no real reason -- it's just what I happened to type :-)",
    "created_at": "2008-08-07T02:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3779#issuecomment-26873",
    "user": "mhansen"
}
```

There's no real reason -- it's just what I happened to type :-)



---

archive/issue_comments_026874.json:
```json
{
    "body": "Attachment [trac_3779-2.patch](tarball://root/attachments/some-uuid/ticket3779/trac_3779-2.patch) by mhansen created at 2008-08-10 06:13:37",
    "created_at": "2008-08-10T06:13:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3779#issuecomment-26874",
    "user": "mhansen"
}
```

Attachment [trac_3779-2.patch](tarball://root/attachments/some-uuid/ticket3779/trac_3779-2.patch) by mhansen created at 2008-08-10 06:13:37



---

archive/issue_comments_026875.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-10T06:33:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3779#issuecomment-26875",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026876.json:
```json
{
    "body": "Merged both patches in Sage 3.1.alpha1",
    "created_at": "2008-08-10T06:33:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3779#issuecomment-26876",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.1.alpha1
