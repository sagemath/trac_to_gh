# Issue 2781: bool() for SymbolicEquation should raise an error when it doesn't know the answer

archive/issues_002781.json:
```json
{
    "body": "Assignee: @williamstein\n\nCurrently, it returns False, which makes a return value of False fairly worthless.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2781\n\n",
    "created_at": "2008-04-02T21:45:36Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "bool() for SymbolicEquation should raise an error when it doesn't know the answer",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2781",
    "user": "@jasongrout"
}
```
Assignee: @williamstein

Currently, it returns False, which makes a return value of False fairly worthless.

Issue created by migration from https://trac.sagemath.org/ticket/2781





---

archive/issue_comments_019101.json:
```json
{
    "body": "Attachment [trac-2781-symbolic-bool.patch](tarball://root/attachments/some-uuid/ticket2781/trac-2781-symbolic-bool.patch) by @jasongrout created at 2008-04-02 21:47:40\n\nThe patch currently passes minimal doctests, but breaks lots of other doctests.  I've run out of time to work on it now, but will look at this later.",
    "created_at": "2008-04-02T21:47:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2781#issuecomment-19101",
    "user": "@jasongrout"
}
```

Attachment [trac-2781-symbolic-bool.patch](tarball://root/attachments/some-uuid/ticket2781/trac-2781-symbolic-bool.patch) by @jasongrout created at 2008-04-02 21:47:40

The patch currently passes minimal doctests, but breaks lots of other doctests.  I've run out of time to work on it now, but will look at this later.



---

archive/issue_comments_019102.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-04-09T06:16:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2781#issuecomment-19102",
    "user": "@jasongrout"
}
```

Resolution: invalid



---

archive/issue_comments_019103.json:
```json
{
    "body": "After discussion on IRC, the consensus was that this is *not* pythonic (see, for example, the docs for __nonzero__ at http://www.python.org/doc/2.3.5/ref/customization.html )\n\nThis functionality should probably be a different function than the builtin bool function.  The current functionality should stand as it is.\n\nEventually, as we get quantifiers worked into the system, it would be nice to have a function that said if an equation was always true, always false, sometimes true, sometimes false, etc.  Something like Reduce in Mma would be nice.",
    "created_at": "2008-04-09T06:16:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2781#issuecomment-19103",
    "user": "@jasongrout"
}
```

After discussion on IRC, the consensus was that this is *not* pythonic (see, for example, the docs for __nonzero__ at http://www.python.org/doc/2.3.5/ref/customization.html )

This functionality should probably be a different function than the builtin bool function.  The current functionality should stand as it is.

Eventually, as we get quantifiers worked into the system, it would be nice to have a function that said if an equation was always true, always false, sometimes true, sometimes false, etc.  Something like Reduce in Mma would be nice.
