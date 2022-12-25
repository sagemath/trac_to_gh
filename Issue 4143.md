# Issue 4143: injvar() docstring should be the same as inject_variables()

archive/issues_004143.json:
```json
{
    "body": "Assignee: tbd\n\nThe `injvar()` command has no docstring. Maybe depreciate it and use the docstring of `inject_variables()` ?\n\n```\nR = PolynomialRing( GF(Integer(2)), ['a%s'%i for i in range(Integer(93))] + ['b%s'%i for i in range(Integer(84))], order='degrevlex' )\n\nR.injvar?\nType:           builtin_function_or_method\nBase Class:     <type 'builtin_function_or_method'>\nString Form:    <built-in method injvar of sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular object at 0xb1c32414>\nNamespace:      Interactive\nDocstring:\n    <no docstring>\nClass Docstring:\n    <attribute '__doc__' of 'builtin_function_or_method' objects>\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4143\n\n",
    "created_at": "2008-09-18T10:23:39Z",
    "labels": [
        "component: algebra",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "injvar() docstring should be the same as inject_variables()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4143",
    "user": "https://github.com/haraldschilly"
}
```
Assignee: tbd

The `injvar()` command has no docstring. Maybe depreciate it and use the docstring of `inject_variables()` ?

```
R = PolynomialRing( GF(Integer(2)), ['a%s'%i for i in range(Integer(93))] + ['b%s'%i for i in range(Integer(84))], order='degrevlex' )

R.injvar?
Type:           builtin_function_or_method
Base Class:     <type 'builtin_function_or_method'>
String Form:    <built-in method injvar of sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular object at 0xb1c32414>
Namespace:      Interactive
Docstring:
    <no docstring>
Class Docstring:
    <attribute '__doc__' of 'builtin_function_or_method' objects>
```


Issue created by migration from https://trac.sagemath.org/ticket/4143





---

archive/issue_comments_030022.json:
```json
{
    "body": "> There should be one-- and preferably only one --obvious way to do it.\n\n(http://www.python.org/dev/peps/pep-0020/)\n\nI vote for deprecation of `injvar`.",
    "created_at": "2008-09-18T10:43:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4143#issuecomment-30022",
    "user": "https://github.com/malb"
}
```

> There should be one-- and preferably only one --obvious way to do it.

(http://www.python.org/dev/peps/pep-0020/)

I vote for deprecation of `injvar`.



---

archive/issue_comments_030023.json:
```json
{
    "body": "Attachment [4143.patch](tarball://root/attachments/some-uuid/ticket4143/4143.patch) by @jhpalmieri created at 2008-12-10 21:07:41\n\nThis patch deprecates injvar.",
    "created_at": "2008-12-10T21:07:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4143#issuecomment-30023",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [4143.patch](tarball://root/attachments/some-uuid/ticket4143/4143.patch) by @jhpalmieri created at 2008-12-10 21:07:41

This patch deprecates injvar.



---

archive/issue_comments_030024.json:
```json
{
    "body": "I agree with deprecating this, and the patch looks good to me.",
    "created_at": "2008-12-12T01:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4143#issuecomment-30024",
    "user": "https://github.com/robertwb"
}
```

I agree with deprecating this, and the patch looks good to me.



---

archive/issue_comments_030025.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-12T06:32:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4143#issuecomment-30025",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_009432.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-12T06:32:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4143",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4143#event-9432"
}
```



---

archive/issue_comments_030026.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha2",
    "created_at": "2008-12-12T06:32:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4143#issuecomment-30026",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.2.alpha2
