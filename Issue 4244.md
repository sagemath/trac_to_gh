# Issue 4244: [with patch, needs review] pynac interface enhancements, symbolic functions

archive/issues_004244.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @williamstein @mwhansen\n\nKeywords: pynac, symbolics\n\nThe patches attached contain various enhancements to the pynac interface:\n* variables.patch - adds a .variables() method to sage.symbolic.expression.Expression\n* custom_eval_func.patch - allows the user to set custom python functions to perform evaluation, numeric evaluation, derivation, series expansion etc. on the given function (sage.symbolic.function.SFunction).\n\nChanges in custom_eval_func.patch depend on the package at #4243, which in turn depends on #3872.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4244\n\n",
    "created_at": "2008-10-04T20:36:40Z",
    "labels": [
        "calculus",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with patch, needs review] pynac interface enhancements, symbolic functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4244",
    "user": "@burcin"
}
```
Assignee: @burcin

CC:  @williamstein @mwhansen

Keywords: pynac, symbolics

The patches attached contain various enhancements to the pynac interface:
* variables.patch - adds a .variables() method to sage.symbolic.expression.Expression
* custom_eval_func.patch - allows the user to set custom python functions to perform evaluation, numeric evaluation, derivation, series expansion etc. on the given function (sage.symbolic.function.SFunction).

Changes in custom_eval_func.patch depend on the package at #4243, which in turn depends on #3872.

Issue created by migration from https://trac.sagemath.org/ticket/4244





---

archive/issue_comments_030846.json:
```json
{
    "body": "Attachment [variables.patch](tarball://root/attachments/some-uuid/ticket4244/variables.patch) by @burcin created at 2008-10-04 20:37:42\n\nadd .variables() function to sage.symbolic.expression.Expression",
    "created_at": "2008-10-04T20:37:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4244#issuecomment-30846",
    "user": "@burcin"
}
```

Attachment [variables.patch](tarball://root/attachments/some-uuid/ticket4244/variables.patch) by @burcin created at 2008-10-04 20:37:42

add .variables() function to sage.symbolic.expression.Expression



---

archive/issue_comments_030847.json:
```json
{
    "body": "Attachment [custom_eval_func.patch](tarball://root/attachments/some-uuid/ticket4244/custom_eval_func.patch) by @burcin created at 2008-10-04 20:38:40\n\nallow sage.symbolic.function.SFunction to use custom python function for evalution, series expansion, derivation, etc.",
    "created_at": "2008-10-04T20:38:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4244#issuecomment-30847",
    "user": "@burcin"
}
```

Attachment [custom_eval_func.patch](tarball://root/attachments/some-uuid/ticket4244/custom_eval_func.patch) by @burcin created at 2008-10-04 20:38:40

allow sage.symbolic.function.SFunction to use custom python function for evalution, series expansion, derivation, etc.



---

archive/issue_comments_030848.json:
```json
{
    "body": "fix some problems with modular coefficients",
    "created_at": "2008-10-15T09:10:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4244#issuecomment-30848",
    "user": "@burcin"
}
```

fix some problems with modular coefficients



---

archive/issue_comments_030849.json:
```json
{
    "body": "Attachment [symbolics_modular.patch](tarball://root/attachments/some-uuid/ticket4244/symbolics_modular.patch) by @burcin created at 2008-10-15 09:16:08\n\nNote that you need the package at #4243 to try these patches.",
    "created_at": "2008-10-15T09:16:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4244#issuecomment-30849",
    "user": "@burcin"
}
```

Attachment [symbolics_modular.patch](tarball://root/attachments/some-uuid/ticket4244/symbolics_modular.patch) by @burcin created at 2008-10-15 09:16:08

Note that you need the package at #4243 to try these patches.



---

archive/issue_comments_030850.json:
```json
{
    "body": "I went over this with Burcin at SD10.  Positive review.",
    "created_at": "2008-10-18T09:36:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4244#issuecomment-30850",
    "user": "@mwhansen"
}
```

I went over this with Burcin at SD10.  Positive review.



---

archive/issue_comments_030851.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-18T13:05:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4244#issuecomment-30851",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030852.json:
```json
{
    "body": "Merged all three patches in Sage 3.2.alpha0",
    "created_at": "2008-10-18T13:05:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4244#issuecomment-30852",
    "user": "mabshoff"
}
```

Merged all three patches in Sage 3.2.alpha0
