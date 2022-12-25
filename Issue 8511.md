# Issue 8511: docstring fix for symbolic expressions

archive/issues_008511.json:
```json
{
    "body": "Assignee: @burcin\n\nAttached is a trivial fix to make the docstring for the `substitute` method for symbolic expressions look right.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8511\n\n",
    "created_at": "2010-03-12T20:24:55Z",
    "labels": [
        "component: symbolics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "docstring fix for symbolic expressions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8511",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @burcin

Attached is a trivial fix to make the docstring for the `substitute` method for symbolic expressions look right.

Issue created by migration from https://trac.sagemath.org/ticket/8511





---

archive/issue_comments_076724.json:
```json
{
    "body": "Attachment [trac_8511-subs.patch](tarball://root/attachments/some-uuid/ticket8511/trac_8511-subs.patch) by @jhpalmieri created at 2010-03-12 20:25:59",
    "created_at": "2010-03-12T20:25:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8511#issuecomment-76724",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_8511-subs.patch](tarball://root/attachments/some-uuid/ticket8511/trac_8511-subs.patch) by @jhpalmieri created at 2010-03-12 20:25:59



---

archive/issue_comments_076725.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-12T20:34:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8511#issuecomment-76725",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076726.json:
```json
{
    "body": "Changing component from symbolics to documentation.",
    "created_at": "2010-03-12T23:27:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8511#issuecomment-76726",
    "user": "https://github.com/jhpalmieri"
}
```

Changing component from symbolics to documentation.



---

archive/issue_comments_076727.json:
```json
{
    "body": "apply only this patch",
    "created_at": "2010-03-12T23:28:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8511#issuecomment-76727",
    "user": "https://github.com/jhpalmieri"
}
```

apply only this patch



---

archive/issue_comments_076728.json:
```json
{
    "body": "Attachment [trac_8511-unexpected-indentation.patch](tarball://root/attachments/some-uuid/ticket8511/trac_8511-unexpected-indentation.patch) by mvngu created at 2010-03-13 00:22:05\n\nreviewer patch; apply on top of previous",
    "created_at": "2010-03-13T00:22:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8511#issuecomment-76728",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8511-unexpected-indentation.patch](tarball://root/attachments/some-uuid/ticket8511/trac_8511-unexpected-indentation.patch) by mvngu created at 2010-03-13 00:22:05

reviewer patch; apply on top of previous



---

archive/issue_comments_076729.json:
```json
{
    "body": "Attachment [trac_8511-reviewer.patch](tarball://root/attachments/some-uuid/ticket8511/trac_8511-reviewer.patch) by @jhpalmieri created at 2010-03-13 00:22:50\n\nWith this patch, plus the ones at #8457 and #8492, the reference manual builds with no warnings.",
    "created_at": "2010-03-13T00:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8511#issuecomment-76729",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_8511-reviewer.patch](tarball://root/attachments/some-uuid/ticket8511/trac_8511-reviewer.patch) by @jhpalmieri created at 2010-03-13 00:22:50

With this patch, plus the ones at #8457 and #8492, the reference manual builds with no warnings.



---

archive/issue_comments_076730.json:
```json
{
    "body": "Changing assignee from @burcin to @jhpalmieri.",
    "created_at": "2010-03-13T00:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8511#issuecomment-76730",
    "user": "https://github.com/jhpalmieri"
}
```

Changing assignee from @burcin to @jhpalmieri.



---

archive/issue_comments_076731.json:
```json
{
    "body": "Changing priority from minor to critical.",
    "created_at": "2010-03-13T00:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8511#issuecomment-76731",
    "user": "https://github.com/jhpalmieri"
}
```

Changing priority from minor to critical.



---

archive/issue_comments_076732.json:
```json
{
    "body": "The patch [trac_8511-unexpected-indentation.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8511/trac_8511-unexpected-indentation.patch) solves the three warnings reported at #8492. However, note that the formatting in the following snippet won't properly render in the HTML version as one would expect TESTS and EXAMPLES block to render:\n\n```diff\ndiff -r 29c870e0a9e4 -r 8851bfe046d1 sage/symbolic/expression.pyx\n--- a/sage/symbolic/expression.pyx\tMon Mar 08 20:51:26 2010 -0800\n+++ b/sage/symbolic/expression.pyx\tFri Mar 12 15:12:47 2010 -0800\n@@ -3151,7 +3151,8 @@\n             sage: t.subs({a:b, b:c})\n             (x + y)^3 + b^2 + c^2\n \n-        TESTS:\n+        TESTS::\n+\n             # no arguments return the same expression\n             sage: t.subs()\n             (x + y)^3 + a^2 + b^2\n```\nThis is due to the comment\n\n```\n# no arguments return the same expression\n```\nTo get this TESTS block to render with colours as one would expect of a TESTS block, prefix that comment with \"sage: \". The reviewer patch [trac_8511-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8511/trac_8511-reviewer.patch) takes care of that. So only my patch needs review by anyone but me. If it gets a positive review, the whole ticket is good to go into Sage 4.3.4.rc0.",
    "created_at": "2010-03-13T00:30:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8511#issuecomment-76732",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The patch [trac_8511-unexpected-indentation.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8511/trac_8511-unexpected-indentation.patch) solves the three warnings reported at #8492. However, note that the formatting in the following snippet won't properly render in the HTML version as one would expect TESTS and EXAMPLES block to render:

```diff
diff -r 29c870e0a9e4 -r 8851bfe046d1 sage/symbolic/expression.pyx
--- a/sage/symbolic/expression.pyx	Mon Mar 08 20:51:26 2010 -0800
+++ b/sage/symbolic/expression.pyx	Fri Mar 12 15:12:47 2010 -0800
@@ -3151,7 +3151,8 @@
             sage: t.subs({a:b, b:c})
             (x + y)^3 + b^2 + c^2
 
-        TESTS:
+        TESTS::
+
             # no arguments return the same expression
             sage: t.subs()
             (x + y)^3 + a^2 + b^2
```
This is due to the comment

```
# no arguments return the same expression
```
To get this TESTS block to render with colours as one would expect of a TESTS block, prefix that comment with "sage: ". The reviewer patch [trac_8511-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8511/trac_8511-reviewer.patch) takes care of that. So only my patch needs review by anyone but me. If it gets a positive review, the whole ticket is good to go into Sage 4.3.4.rc0.



---

archive/issue_comments_076733.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-13T00:53:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8511#issuecomment-76733",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076734.json:
```json
{
    "body": "Looks good to me.  The TESTS block now looks right, and doctests pass.",
    "created_at": "2010-03-13T00:53:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8511#issuecomment-76734",
    "user": "https://github.com/jhpalmieri"
}
```

Looks good to me.  The TESTS block now looks right, and doctests pass.



---

archive/issue_events_020436.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-03-14T08:28:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8511",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8511#event-20436"
}
```



---

archive/issue_comments_076735.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-14T08:28:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8511#issuecomment-76735",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_076736.json:
```json
{
    "body": "Merged in this order:\n\n1. [trac_8511-unexpected-indentation.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8511/trac_8511-unexpected-indentation.patch)\n2. [trac_8511-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8511/trac_8511-reviewer.patch)",
    "created_at": "2010-03-14T08:28:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8511#issuecomment-76736",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged in this order:

1. [trac_8511-unexpected-indentation.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8511/trac_8511-unexpected-indentation.patch)
2. [trac_8511-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8511/trac_8511-reviewer.patch)
