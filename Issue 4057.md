# Issue 4057: Possible improvements to ? and ?? for R functions

archive/issues_004057.json:
```json
{
    "body": "Assignee: @williamstein\n\nThings are different in notebook and console:\n\n* Because of underline trick, in notebook headings in docstring consists of only underline!\n* Source display in console would look better with additional new line char and one empty line after source output and before \"Constructor Docstring\", the docstring in console is better, underline trick works as expected, but there could also be one empty line before \"Constructor Docstring\"\n  * btw - is Constructor Docstring really needed? I think the source is enough and we don't have to include same docstring for every R function, it's already available as docstring for r interpreter itself... it's not included in docstring in notebook so I guess we could live without it, if it is the case, no need to add empty line before it!\n* getting source of R function through notebook by ?? don't work at all...\n\nIssue created by migration from https://trac.sagemath.org/ticket/4057\n\n",
    "created_at": "2008-09-04T03:13:47Z",
    "labels": [
        "component: interfaces",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "Possible improvements to ? and ?? for R functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4057",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```
Assignee: @williamstein

Things are different in notebook and console:

* Because of underline trick, in notebook headings in docstring consists of only underline!
* Source display in console would look better with additional new line char and one empty line after source output and before "Constructor Docstring", the docstring in console is better, underline trick works as expected, but there could also be one empty line before "Constructor Docstring"
  * btw - is Constructor Docstring really needed? I think the source is enough and we don't have to include same docstring for every R function, it's already available as docstring for r interpreter itself... it's not included in docstring in notebook so I guess we could live without it, if it is the case, no need to add empty line before it!
* getting source of R function through notebook by ?? don't work at all...

Issue created by migration from https://trac.sagemath.org/ticket/4057





---

archive/issue_comments_029175.json:
```json
{
    "body": "a simple (and probably not best) way to deal with \"underline only\" problem in notebook docstring for R functions",
    "created_at": "2008-09-04T03:15:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4057#issuecomment-29175",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

a simple (and probably not best) way to deal with "underline only" problem in notebook docstring for R functions



---

archive/issue_comments_029176.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-09-04T03:15:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4057#issuecomment-29176",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: invalid



---

archive/issue_events_009262.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-04T03:15:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4057",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4057#event-9262"
}
```



---

archive/issue_comments_029177.json:
```json
{
    "body": "Attachment [underline_trick.patch](tarball://root/attachments/some-uuid/ticket4057/underline_trick.patch) by mabshoff created at 2008-09-04 03:15:50\n\nHi,\n\nthis is some laundry list of things and should be first discussed on sage-devel before opening clearly defined tickets. Trac is not a discussion forum :)\n\nInvalid.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-04T03:15:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4057#issuecomment-29177",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [underline_trick.patch](tarball://root/attachments/some-uuid/ticket4057/underline_trick.patch) by mabshoff created at 2008-09-04 03:15:50

Hi,

this is some laundry list of things and should be first discussed on sage-devel before opening clearly defined tickets. Trac is not a discussion forum :)

Invalid.

Cheers,

Michael



---

archive/issue_events_009263.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-04T03:25:45Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4057",
    "milestone": "sage-3.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4057#event-9263"
}
```



---

archive/issue_comments_029178.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-09-04T03:25:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4057#issuecomment-29178",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_events_009264.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-04T03:25:45Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/4057",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4057#event-9264"
}
```



---

archive/issue_comments_029179.json:
```json
{
    "body": "Resolution changed from invalid to ",
    "created_at": "2008-09-04T03:25:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4057#issuecomment-29179",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution changed from invalid to 



---

archive/issue_comments_029180.json:
```json
{
    "body": "when limited to one issue, defect seems to fit better to this one...",
    "created_at": "2008-09-04T03:34:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4057#issuecomment-29180",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

when limited to one issue, defect seems to fit better to this one...



---

archive/issue_comments_029181.json:
```json
{
    "body": "Changing type from enhancement to defect.",
    "created_at": "2008-09-04T03:34:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4057#issuecomment-29181",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

Changing type from enhancement to defect.



---

archive/issue_comments_029182.json:
```json
{
    "body": "Changing status from reopened to new.",
    "created_at": "2008-09-04T04:15:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4057#issuecomment-29182",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

Changing status from reopened to new.



---

archive/issue_comments_029183.json:
```json
{
    "body": "Changing assignee from @williamstein to aginiewicz.",
    "created_at": "2008-09-04T04:15:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4057#issuecomment-29183",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

Changing assignee from @williamstein to aginiewicz.



---

archive/issue_comments_029184.json:
```json
{
    "body": "(forgot to assign ticket to myself)",
    "created_at": "2008-09-04T04:15:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4057#issuecomment-29184",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

(forgot to assign ticket to myself)



---

archive/issue_comments_029185.json:
```json
{
    "body": "See http://sage.math.washington.edu/home/tclemans/R_docstring_before_after.png for the before and after screenshots.",
    "created_at": "2008-09-08T11:45:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4057#issuecomment-29185",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

See http://sage.math.washington.edu/home/tclemans/R_docstring_before_after.png for the before and after screenshots.



---

archive/issue_comments_029186.json:
```json
{
    "body": "better solution to problem",
    "created_at": "2008-09-15T21:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4057#issuecomment-29186",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

better solution to problem



---

archive/issue_comments_029187.json:
```json
{
    "body": "Attachment [underline_trick.2.patch](tarball://root/attachments/some-uuid/ticket4057/underline_trick.2.patch) by aginiewicz created at 2008-09-15 21:16:22\n\nI attached better fix of problem, it fixes not only the r.sth? notation but also not fixed by previous - r.help(\"sth\") - also it doesn't add check related to R in generic module so I guess previous was bad",
    "created_at": "2008-09-15T21:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4057#issuecomment-29187",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

Attachment [underline_trick.2.patch](tarball://root/attachments/some-uuid/ticket4057/underline_trick.2.patch) by aginiewicz created at 2008-09-15 21:16:22

I attached better fix of problem, it fixes not only the r.sth? notation but also not fixed by previous - r.help("sth") - also it doesn't add check related to R in generic module so I guess previous was bad



---

archive/issue_comments_029188.json:
```json
{
    "body": "apply this and the patch right above this.",
    "created_at": "2008-11-27T18:31:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4057#issuecomment-29188",
    "user": "https://github.com/williamstein"
}
```

apply this and the patch right above this.



---

archive/issue_comments_029189.json:
```json
{
    "body": "Attachment [sage-4057-part2.patch](tarball://root/attachments/some-uuid/ticket4057/sage-4057-part2.patch) by @williamstein created at 2008-11-27 18:32:09\n\nREFEREE REPORT:\n\nLooks good, but needs to *only* delete the underline in embedded mode.  I've attached a patch to do that.",
    "created_at": "2008-11-27T18:32:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4057#issuecomment-29189",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-4057-part2.patch](tarball://root/attachments/some-uuid/ticket4057/sage-4057-part2.patch) by @williamstein created at 2008-11-27 18:32:09

REFEREE REPORT:

Looks good, but needs to *only* delete the underline in embedded mode.  I've attached a patch to do that.



---

archive/issue_events_009265.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-28T21:52:04Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4057",
    "milestone": "sage-3.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4057#event-9265"
}
```



---

archive/issue_events_009266.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-28T21:52:04Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4057",
    "milestone": "sage-3.2.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4057#event-9266"
}
```



---

archive/issue_comments_029190.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-28T21:52:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4057#issuecomment-29190",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_009267.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-28T21:52:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4057",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4057#event-9267"
}
```



---

archive/issue_comments_029191.json:
```json
{
    "body": "Merged underline_trick.2.patch and sage-4057-part2.patch in Sage 3.2.1.rc0.\n\nAndrzej: Your patch was a diff, please make sure to post proper hg patches in the future. I have committed this patch in your name to the repo for proper credit.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-28T21:52:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4057#issuecomment-29191",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged underline_trick.2.patch and sage-4057-part2.patch in Sage 3.2.1.rc0.

Andrzej: Your patch was a diff, please make sure to post proper hg patches in the future. I have committed this patch in your name to the repo for proper credit.

Cheers,

Michael



---

archive/issue_comments_029192.json:
```json
{
    "body": "I know, the patch was attached before the one from which I found out earlier you prefer hg patch :)...\n\nthanks for including this anyway,\ncheers,\nAndrzej.",
    "created_at": "2008-11-28T23:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4057#issuecomment-29192",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

I know, the patch was attached before the one from which I found out earlier you prefer hg patch :)...

thanks for including this anyway,
cheers,
Andrzej.
