# Issue 5542: [with patch, positive review] more docstring fixes for permgroup.py

archive/issues_005542.json:
```json
{
    "body": "Assignee: tba\n\nKeywords: permgroup.py, docstring\n\nWhile reviewing the patch on ticket #5536, I noticed that there are more formatting issues in `sage/groups/perm_gps/permgroup.py`. This is a follow up to that ticket.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5542\n\n",
    "closed_at": "2009-03-20T21:20:04Z",
    "created_at": "2009-03-17T05:45:48Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, positive review] more docstring fixes for permgroup.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5542",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: tba

Keywords: permgroup.py, docstring

While reviewing the patch on ticket #5536, I noticed that there are more formatting issues in `sage/groups/perm_gps/permgroup.py`. This is a follow up to that ticket.

Issue created by migration from https://trac.sagemath.org/ticket/5542





---

archive/issue_comments_043039.json:
```json
{
    "body": "Attachment [trac_5542-docstring-fixes.patch](tarball://root/attachments/some-uuid/ticket5542/trac_5542-docstring-fixes.patch) by mvngu created at 2009-03-17 07:54:23\n\nThe patch **trac_5542-docstring-fixes.patch** fixes formatting problems I found while reviewing ticket #5536. This patch depends on #5536, and the patch at #5536 should be applied first.",
    "created_at": "2009-03-17T07:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5542#issuecomment-43039",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_5542-docstring-fixes.patch](tarball://root/attachments/some-uuid/ticket5542/trac_5542-docstring-fixes.patch) by mvngu created at 2009-03-17 07:54:23

The patch **trac_5542-docstring-fixes.patch** fixes formatting problems I found while reviewing ticket #5536. This patch depends on #5536, and the patch at #5536 should be applied first.



---

archive/issue_comments_043040.json:
```json
{
    "body": "Looks good, mostly.  I'm attaching a new patch to fix a few issues; positive review for everything else.  (So if my new patch is okay, the whole thing gets a positive review.)",
    "created_at": "2009-03-17T16:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5542#issuecomment-43040",
    "user": "https://github.com/jhpalmieri"
}
```

Looks good, mostly.  I'm attaching a new patch to fix a few issues; positive review for everything else.  (So if my new patch is okay, the whole thing gets a positive review.)



---

archive/issue_comments_043041.json:
```json
{
    "body": "For the patch **5542-referee.patch**, everything looks good except for this line:\n\n```\n2017\t        The normal subgroups of `H = PSL(2,7) \\times PSL(2,7)` are\n```\nThe LaTeX macro `\\times` is meant to render as a multiplication symbol that looks like this \"x\". But after applying **5542-referee.patch** on top of **trac_5542-docstring-fixes.patch** and rebuilding the HTML version of the reference manual, the said macro doesn't render as expected; see the rebuilt ref manual at\n\n\n\nhttp://sage.math.washington.edu/home/mvngu/scratch/sage-3.4/devel/sage-5542/doc/output/html/en/reference/sage/groups/perm_gps/permgroup.html#sage.groups.perm_gps.permgroup.PermutationGroup_generic.normal_subgroups\n\n\n\nto see what it's rendered as.",
    "created_at": "2009-03-18T09:52:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5542#issuecomment-43041",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

For the patch **5542-referee.patch**, everything looks good except for this line:

```
2017	        The normal subgroups of `H = PSL(2,7) \times PSL(2,7)` are
```
The LaTeX macro `\times` is meant to render as a multiplication symbol that looks like this "x". But after applying **5542-referee.patch** on top of **trac_5542-docstring-fixes.patch** and rebuilding the HTML version of the reference manual, the said macro doesn't render as expected; see the rebuilt ref manual at



http://sage.math.washington.edu/home/mvngu/scratch/sage-3.4/devel/sage-5542/doc/output/html/en/reference/sage/groups/perm_gps/permgroup.html#sage.groups.perm_gps.permgroup.PermutationGroup_generic.normal_subgroups



to see what it's rendered as.



---

archive/issue_comments_043042.json:
```json
{
    "body": "Should have been `\\\\times` instead.  Here's a replacement patch.",
    "created_at": "2009-03-18T16:22:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5542#issuecomment-43042",
    "user": "https://github.com/jhpalmieri"
}
```

Should have been `\\times` instead.  Here's a replacement patch.



---

archive/issue_comments_043043.json:
```json
{
    "body": "Attachment [5542-referee.patch](tarball://root/attachments/some-uuid/ticket5542/5542-referee.patch) by mvngu created at 2009-03-18 23:24:25\n\nOK, the (new) patch **5542-referee.patch** applies fine against Sage 3.4, all doctests passed, the HTML version of the reference manual builds without problems, and the macro `\\\\times` now renders as expected. The HTML manual page for `sage/groups/perm_gps/permgroup.py` now looks ridiculously beautiful :-)  Positive review.",
    "created_at": "2009-03-18T23:24:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5542#issuecomment-43043",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [5542-referee.patch](tarball://root/attachments/some-uuid/ticket5542/5542-referee.patch) by mvngu created at 2009-03-18 23:24:25

OK, the (new) patch **5542-referee.patch** applies fine against Sage 3.4, all doctests passed, the HTML version of the reference manual builds without problems, and the macro `\\times` now renders as expected. The HTML manual page for `sage/groups/perm_gps/permgroup.py` now looks ridiculously beautiful :-)  Positive review.



---

archive/issue_comments_043044.json:
```json
{
    "body": "For the record, here's the order in which patches should be applied:\n1. First apply the patch on ticket #5536.\n2. Then apply `trac_5542-docstring-fixes.patch`.\n3. And finally, apply `5542-referee.patch`.",
    "created_at": "2009-03-18T23:33:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5542#issuecomment-43044",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

For the record, here's the order in which patches should be applied:
1. First apply the patch on ticket #5536.
2. Then apply `trac_5542-docstring-fixes.patch`.
3. And finally, apply `5542-referee.patch`.



---

archive/issue_comments_043045.json:
```json
{
    "body": "Merged both patches in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-20T21:20:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5542#issuecomment-43045",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_events_013006.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-20T21:20:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5542",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5542#event-13006"
}
```



---

archive/issue_comments_043046.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-20T21:20:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5542#issuecomment-43046",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
