# Issue 3715: trivial to do bug fix

archive/issues_003715.json:
```json
{
    "body": "Assignee: cwitty\n\n\n```\nWhile debugging the new release of the FriCAS optional package Waldek\nHebisch discovered a small bug in the script that starts clisp. There\nare missing argument quotes that can cause problems if some spkg (such\nas fricas-1.0.3.spkg) needs to pass arguments containing spaces.\n\nhttp://sage.math.washington.edu/home/page/packages/lisp.diff\n\n--- lisp.orig   2008-07-20 17:22:27.000000000 -0400\n+++ lisp        2008-07-20 03:04:00.000000000 -0400\n@@ -1,2 +1,2 @@\n #!/bin/sh\n-\"$SAGE_ROOT/local/bin/clisp.bin\" -B \"$SAGE_ROOT/local/lib/clisp-2.46\" $@\n+\"$SAGE_ROOT/local/bin/clisp.bin\" -B \"$SAGE_ROOT/local/lib/clisp-2.46\" \"$@\"\n\n-----\n\nRegards,\nBill Page.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3715\n\n",
    "created_at": "2008-07-23T18:39:20Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.6",
    "title": "trivial to do bug fix",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3715",
    "user": "@williamstein"
}
```
Assignee: cwitty


```
While debugging the new release of the FriCAS optional package Waldek
Hebisch discovered a small bug in the script that starts clisp. There
are missing argument quotes that can cause problems if some spkg (such
as fricas-1.0.3.spkg) needs to pass arguments containing spaces.

http://sage.math.washington.edu/home/page/packages/lisp.diff

--- lisp.orig   2008-07-20 17:22:27.000000000 -0400
+++ lisp        2008-07-20 03:04:00.000000000 -0400
@@ -1,2 +1,2 @@
 #!/bin/sh
-"$SAGE_ROOT/local/bin/clisp.bin" -B "$SAGE_ROOT/local/lib/clisp-2.46" $@
+"$SAGE_ROOT/local/bin/clisp.bin" -B "$SAGE_ROOT/local/lib/clisp-2.46" "$@"

-----

Regards,
Bill Page.
```


Issue created by migration from https://trac.sagemath.org/ticket/3715





---

archive/issue_comments_026365.json:
```json
{
    "body": "The spgk at #3712 fixes the issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-29T16:00:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3715#issuecomment-26365",
    "user": "mabshoff"
}
```

The spgk at #3712 fixes the issue.

Cheers,

Michael



---

archive/issue_comments_026366.json:
```json
{
    "body": "Changing assignee from cwitty to mabshoff.",
    "created_at": "2008-07-29T16:52:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3715#issuecomment-26366",
    "user": "mabshoff"
}
```

Changing assignee from cwitty to mabshoff.



---

archive/issue_comments_026367.json:
```json
{
    "body": "Due to the positive review at #3712 I am changing this ticket to a positive review also.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-29T16:52:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3715#issuecomment-26367",
    "user": "mabshoff"
}
```

Due to the positive review at #3712 I am changing this ticket to a positive review also.

Cheers,

Michael



---

archive/issue_comments_026368.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-07-29T16:52:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3715#issuecomment-26368",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_026369.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-29T16:55:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3715#issuecomment-26369",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026370.json:
```json
{
    "body": "Merged in Sage 3.0.6.final",
    "created_at": "2008-07-29T16:55:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3715#issuecomment-26370",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.6.final
