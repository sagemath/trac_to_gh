# Issue 2978: Rstats -- make it build with png support

archive/issues_002978.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  jdemeyer\n\nOn most platforms R with Sage does *not* build with png support.  Fix this and revert #2974 once this is fixed. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2978\n\n",
    "created_at": "2008-04-21T02:34:11Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "Rstats -- make it build with png support",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2978",
    "user": "was"
}
```
Assignee: mabshoff

CC:  jdemeyer

On most platforms R with Sage does *not* build with png support.  Fix this and revert #2974 once this is fixed. 

Issue created by migration from https://trac.sagemath.org/ticket/2978





---

archive/issue_comments_020509.json:
```json
{
    "body": "Now that we build libpng dynamically on all systems including OSX this seems like a good idea. This is also required to make the optional doctests in rpy pass.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-02T02:28:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2978#issuecomment-20509",
    "user": "mabshoff"
}
```

Now that we build libpng dynamically on all systems including OSX this seems like a good idea. This is also required to make the optional doctests in rpy pass.

Cheers,

Michael



---

archive/issue_comments_020510.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-02T02:28:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2978#issuecomment-20510",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020511.json:
```json
{
    "body": "Changing assignee from mabshoff to jason.",
    "created_at": "2009-09-16T16:35:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2978#issuecomment-20511",
    "user": "jason"
}
```

Changing assignee from mabshoff to jason.



---

archive/issue_comments_020512.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2009-09-16T16:35:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2978#issuecomment-20512",
    "user": "jason"
}
```

Changing status from assigned to new.



---

archive/issue_comments_020513.json:
```json
{
    "body": "To release manager: This ticket is no longer valid.  There are still some issues with R and graphics on minimal Linux installs without certain libraries, but we have marked such doctests optional and have open tickets for re-enabling this in those cases.    \n\nSee for instance #8868 (most relevant) as well as #11249 and #11266.",
    "created_at": "2011-06-28T16:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2978#issuecomment-20513",
    "user": "kcrisman"
}
```

To release manager: This ticket is no longer valid.  There are still some issues with R and graphics on minimal Linux installs without certain libraries, but we have marked such doctests optional and have open tickets for re-enabling this in those cases.    

See for instance #8868 (most relevant) as well as #11249 and #11266.



---

archive/issue_comments_020514.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-06-28T16:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2978#issuecomment-20514",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_020515.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-06-28T16:30:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2978#issuecomment-20515",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_020516.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2011-07-05T10:07:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2978#issuecomment-20516",
    "user": "jdemeyer"
}
```

Resolution: worksforme
