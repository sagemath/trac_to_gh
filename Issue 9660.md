# Issue 9660: Obtaining the string representation of a number field ideal takes too long

archive/issues_009660.json:
```json
{
    "body": "Assignee: @loefflerd\n\nIn order to obtain the string representation of an NumberFieldFractionalIdeal, the class group of the number field is computed to determine whether or not the ideal is principal.  This can take a very long time.  For example, the following is essentially immediate:\n\n```\nsage: K.<zeta> = CyclotomicField(23)\nsage: F = K.ideal(2).factor()\n```\n\nBut now, doing\n\n```\nsage: F\n```\n\ntakes a very long time.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9660\n\n",
    "created_at": "2010-08-01T15:52:53Z",
    "labels": [
        "number fields",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Obtaining the string representation of a number field ideal takes too long",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9660",
    "user": "@jdemeyer"
}
```
Assignee: @loefflerd

In order to obtain the string representation of an NumberFieldFractionalIdeal, the class group of the number field is computed to determine whether or not the ideal is principal.  This can take a very long time.  For example, the following is essentially immediate:

```
sage: K.<zeta> = CyclotomicField(23)
sage: F = K.ideal(2).factor()
```

But now, doing

```
sage: F
```

takes a very long time.

Issue created by migration from https://trac.sagemath.org/ticket/9660





---

archive/issue_comments_093772.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-09-10T12:27:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9660#issuecomment-93772",
    "user": "mvngu"
}
```

Resolution: invalid
