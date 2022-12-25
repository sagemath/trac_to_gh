# Issue 8022: ref manual for 4.3.1: fix warning about misc/attach.rst

archive/issues_008022.json:
```json
{
    "body": "Assignee: mvngu\n\nWhen building the reference manual, I get this warning (among others):\n\n```\n.../devel/sage/doc/en/reference/sage/misc/attach.rst:: WARNING: document isn't included in any toctree\n```\nThe fix is easy: delete (by hand) the file `SAGE_ROOT/devel/sage/doc/en/reference/sage/misc/attach.rst`.  (This file is not under revision control, so can't be removed by a patch.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/8022\n\n",
    "created_at": "2010-01-21T06:31:45Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "ref manual for 4.3.1: fix warning about misc/attach.rst",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8022",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: mvngu

When building the reference manual, I get this warning (among others):

```
.../devel/sage/doc/en/reference/sage/misc/attach.rst:: WARNING: document isn't included in any toctree
```
The fix is easy: delete (by hand) the file `SAGE_ROOT/devel/sage/doc/en/reference/sage/misc/attach.rst`.  (This file is not under revision control, so can't be removed by a patch.)

Issue created by migration from https://trac.sagemath.org/ticket/8022





---

archive/issue_comments_069970.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-21T06:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8022",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8022#issuecomment-69970",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069971.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-31T01:30:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8022",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8022#issuecomment-69971",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069972.json:
```json
{
    "body": "Also, `polytope.rst`?  To be sure, do `rm -rf SAGE_DOC/en/reference/sage*` and rebuild...",
    "created_at": "2010-01-31T01:45:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8022",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8022#issuecomment-69972",
    "user": "https://github.com/qed777"
}
```

Also, `polytope.rst`?  To be sure, do `rm -rf SAGE_DOC/en/reference/sage*` and rebuild...



---

archive/issue_comments_069973.json:
```json
{
    "body": "Replying to [comment:3 mpatel]:\n> Also, `polytope.rst`?  To be sure, do `rm -rf SAGE_DOC/en/reference/sage*` and rebuild...\n\n\nYes, it looks like polytope.rst was removed from the reference manual in #7109.  Let's delete that file, too; I'll change the description of this ticket to reflect this.",
    "created_at": "2010-01-31T06:26:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8022",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8022#issuecomment-69973",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:3 mpatel]:
> Also, `polytope.rst`?  To be sure, do `rm -rf SAGE_DOC/en/reference/sage*` and rebuild...


Yes, it looks like polytope.rst was removed from the reference manual in #7109.  Let's delete that file, too; I'll change the description of this ticket to reflect this.



---

archive/issue_comments_069974.json:
```json
{
    "body": "There are no patches to merge, so I \"merged\" as follows:\n\n* `rm -rf SAGE_ROOT/devel/sage-main/doc/en/reference/sage`\n\nFor Sage 4.3.2.alpha1, originally the number of warnings for building the reference manual was 157. After following the above deletion step, the total number of warnings dropped down to 155.",
    "created_at": "2010-02-01T22:31:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8022",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8022#issuecomment-69974",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There are no patches to merge, so I "merged" as follows:

* `rm -rf SAGE_ROOT/devel/sage-main/doc/en/reference/sage`

For Sage 4.3.2.alpha1, originally the number of warnings for building the reference manual was 157. After following the above deletion step, the total number of warnings dropped down to 155.



---

archive/issue_events_019218.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-02-01T22:31:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8022",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8022#event-19218"
}
```



---

archive/issue_comments_069975.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-01T22:31:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8022",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8022#issuecomment-69975",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_069976.json:
```json
{
    "body": "**Correction:** I only removed the file `polytope.rst`:\n\n* `rm SAGE_ROOT/devel/sage-main/doc/en/reference/sage/geometry/polytope.rst`",
    "created_at": "2010-02-04T01:36:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8022",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8022#issuecomment-69976",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

**Correction:** I only removed the file `polytope.rst`:

* `rm SAGE_ROOT/devel/sage-main/doc/en/reference/sage/geometry/polytope.rst`
