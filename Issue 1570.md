# Issue 1570: typo in sage/rings/number_field/number_field.py

archive/issues_001570.json:
```json
{
    "body": "Assignee: tba\n\nReported by Francis Clarke\n\n```\n--- a/sage/rings/number_field/number_field.py   Sun Dec 16 06:37:16\n2007 -0800\n+++ b/sage/rings/number_field/number_field.py   Wed Dec 19 18:54:54\n2007 +0000\n@@ -751,7 +751,7 @@ class NumberField_generic(number_field_b\n\n         You can also view a number field as having a different\n         generator by just chosing the input to generate the\n-        whole filed; for that it is better to use\n+        whole field; for that it is better to use\n         \\code{self.change_generator}, which gives isomorphisms\n         in both directions.\n         \"\"\" \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1570\n\n",
    "created_at": "2007-12-20T01:30:55Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "typo in sage/rings/number_field/number_field.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1570",
    "user": "mabshoff"
}
```
Assignee: tba

Reported by Francis Clarke

```
--- a/sage/rings/number_field/number_field.py   Sun Dec 16 06:37:16
2007 -0800
+++ b/sage/rings/number_field/number_field.py   Wed Dec 19 18:54:54
2007 +0000
@@ -751,7 +751,7 @@ class NumberField_generic(number_field_b

         You can also view a number field as having a different
         generator by just chosing the input to generate the
-        whole filed; for that it is better to use
+        whole field; for that it is better to use
         \code{self.change_generator}, which gives isomorphisms
         in both directions.
         """ 
```


Issue created by migration from https://trac.sagemath.org/ticket/1570





---

archive/issue_comments_009999.json:
```json
{
    "body": "Attachment [Sage.2.10.alpha3-fix-typo-in-numberfield.py.patch](tarball://root/attachments/some-uuid/ticket1570/Sage.2.10.alpha3-fix-typo-in-numberfield.py.patch) by mabshoff created at 2008-01-13 17:48:43",
    "created_at": "2008-01-13T17:48:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1570#issuecomment-9999",
    "user": "mabshoff"
}
```

Attachment [Sage.2.10.alpha3-fix-typo-in-numberfield.py.patch](tarball://root/attachments/some-uuid/ticket1570/Sage.2.10.alpha3-fix-typo-in-numberfield.py.patch) by mabshoff created at 2008-01-13 17:48:43



---

archive/issue_comments_010000.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-13T17:49:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1570#issuecomment-10000",
    "user": "mabshoff"
}
```

Resolution: fixed
