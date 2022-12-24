# Issue 955: Singular interface (and possibly others) can lose synchronization due to GC

archive/issues_000955.json:
```json
{
    "body": "Assignee: was\n\nI'm going to describe the problem in terms of the Singular interface, but I think probably at least some other interfaces are similarly vulnerable.\n\nThe bad sequence of events is:\n\n 1) Some Singular computation is requested, by calling Singular.eval().\n\n 2) Singular.eval() calls Expect.eval().\n\n 3) Expect.eval() sends a command to Singular, to perform the requested computation.\n\n 4) A Python garbage collection is triggered.\n\n 5) One of the collected objects is a Singular wrapper object (of type SingularElement).\n\n 6) Singular.clear() is called on this object.\n\n 7) Singular.clear() calls Singular.eval() to kill the Singular variable corresponding to this object.\n\n 8) Singular.eval() calls Expect.eval().\n\n 9) Expect.eval() sends the kill command to Singular.\n\n 10) Expect.eval() waits for a response from Singular.  Unfortunately, the next response it sees from Singular is the response to the command sent in step 3), from the mathematical computation.\n\n 11) Expect.eval() returns this response to Singular.eval().\n\n 12) Singular.eval() returns this response to Singular.clear().\n\n 13) Singular.clear() discards the response.\n\n 14) Garbage collection completes.\n\n 15) Expect.eval() waits for a response from Singular.  Unfortunately, the next response it sees from Singular is the null response from the kill command.\n\n 16) Expect.eval() returns this response to Singular.eval().\n\n 17) Singular.eval() returns this null response as the result of the requested computation.\n\nI'll attach two log files to this ticket; log7027 shows the interface working, and log7028 shows the interface failing because the print(sage10); command is interrupted by the command to kill sage7.\n\nIssue created by migration from https://trac.sagemath.org/ticket/955\n\n",
    "created_at": "2007-10-21T03:50:22Z",
    "labels": [
        "interfaces",
        "critical",
        "bug"
    ],
    "title": "Singular interface (and possibly others) can lose synchronization due to GC",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/955",
    "user": "cwitty"
}
```
Assignee: was

I'm going to describe the problem in terms of the Singular interface, but I think probably at least some other interfaces are similarly vulnerable.

The bad sequence of events is:

 1) Some Singular computation is requested, by calling Singular.eval().

 2) Singular.eval() calls Expect.eval().

 3) Expect.eval() sends a command to Singular, to perform the requested computation.

 4) A Python garbage collection is triggered.

 5) One of the collected objects is a Singular wrapper object (of type SingularElement).

 6) Singular.clear() is called on this object.

 7) Singular.clear() calls Singular.eval() to kill the Singular variable corresponding to this object.

 8) Singular.eval() calls Expect.eval().

 9) Expect.eval() sends the kill command to Singular.

 10) Expect.eval() waits for a response from Singular.  Unfortunately, the next response it sees from Singular is the response to the command sent in step 3), from the mathematical computation.

 11) Expect.eval() returns this response to Singular.eval().

 12) Singular.eval() returns this response to Singular.clear().

 13) Singular.clear() discards the response.

 14) Garbage collection completes.

 15) Expect.eval() waits for a response from Singular.  Unfortunately, the next response it sees from Singular is the null response from the kill command.

 16) Expect.eval() returns this response to Singular.eval().

 17) Singular.eval() returns this null response as the result of the requested computation.

I'll attach two log files to this ticket; log7027 shows the interface working, and log7028 shows the interface failing because the print(sage10); command is interrupted by the command to kill sage7.

Issue created by migration from https://trac.sagemath.org/ticket/955





---

archive/issue_comments_005817.json:
```json
{
    "body": "Attachment [log7027](tarball://root/attachments/some-uuid/ticket955/log7027) by cwitty created at 2007-10-21 03:50:36",
    "created_at": "2007-10-21T03:50:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/955#issuecomment-5817",
    "user": "cwitty"
}
```

Attachment [log7027](tarball://root/attachments/some-uuid/ticket955/log7027) by cwitty created at 2007-10-21 03:50:36



---

archive/issue_comments_005818.json:
```json
{
    "body": "Attachment [log7028](tarball://root/attachments/some-uuid/ticket955/log7028) by cwitty created at 2007-10-21 03:50:45",
    "created_at": "2007-10-21T03:50:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/955#issuecomment-5818",
    "user": "cwitty"
}
```

Attachment [log7028](tarball://root/attachments/some-uuid/ticket955/log7028) by cwitty created at 2007-10-21 03:50:45



---

archive/issue_comments_005819.json:
```json
{
    "body": "See rings/morphism.pyx for an example of this that is # not tested right now.",
    "created_at": "2007-10-21T06:22:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/955#issuecomment-5819",
    "user": "was"
}
```

See rings/morphism.pyx for an example of this that is # not tested right now.



---

archive/issue_comments_005820.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-25T05:34:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/955#issuecomment-5820",
    "user": "cwitty"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005821.json:
```json
{
    "body": "Changing assignee from was to cwitty.",
    "created_at": "2007-10-25T05:34:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/955#issuecomment-5821",
    "user": "cwitty"
}
```

Changing assignee from was to cwitty.



---

archive/issue_comments_005822.json:
```json
{
    "body": "Release 2.8.8 had a patch for this that fixed most or all of the issues with Singular.  However, other interfaces are still vulnerable to the same problem.  All interfaces should be audited and fixed.",
    "created_at": "2007-10-25T05:41:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/955#issuecomment-5822",
    "user": "cwitty"
}
```

Release 2.8.8 had a patch for this that fixed most or all of the issues with Singular.  However, other interfaces are still vulnerable to the same problem.  All interfaces should be audited and fixed.



---

archive/issue_comments_005823.json:
```json
{
    "body": "Attachment [7176.patch](tarball://root/attachments/some-uuid/ticket955/7176.patch) by cwitty created at 2007-10-27 18:02:30\n\nI've fixed several places that looked slightly dubious, although I could have missed something.\n\nThe attached patch will be in 2.8.10.",
    "created_at": "2007-10-27T18:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/955#issuecomment-5823",
    "user": "cwitty"
}
```

Attachment [7176.patch](tarball://root/attachments/some-uuid/ticket955/7176.patch) by cwitty created at 2007-10-27 18:02:30

I've fixed several places that looked slightly dubious, although I could have missed something.

The attached patch will be in 2.8.10.



---

archive/issue_comments_005824.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-27T18:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/955#issuecomment-5824",
    "user": "cwitty"
}
```

Resolution: fixed
