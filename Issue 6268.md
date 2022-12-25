# Issue 6268: Typesetting of sec(x), csc(x), cot(x) are broken

archive/issues_006268.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  @ncalexan\n\nTypesettings of sec(x), csc(x), cot(x) are broken. It puts an\nextra \"\\mbox\" around them. However, typesetting for sin(x), \ncos(x), tan(x) works as expected.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6268\n\n",
    "created_at": "2009-06-12T15:25:27Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "Typesetting of sec(x), csc(x), cot(x) are broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6268",
    "user": "https://github.com/golam-m-hossain"
}
```
Assignee: cwitty

CC:  @ncalexan

Typesettings of sec(x), csc(x), cot(x) are broken. It puts an
extra "\mbox" around them. However, typesetting for sin(x), 
cos(x), tan(x) works as expected.

Issue created by migration from https://trac.sagemath.org/ticket/6268





---

archive/issue_comments_049969.json:
```json
{
    "body": "\n```\n[mvngu@sage sage-4.0.1]$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: # the following work as expected\nsage: latex(sec)\n\\sec\nsage: latex(csc)\n\\csc\nsage: latex(cot)\n\\cot\nsage: # but the following have extra \"\\mbox\" around the trig function name\nsage: latex(sec(x))\n\\mbox{\\sec}\\left(x\\right)\nsage: latex(csc(x))\n\\mbox{\\csc}\\left(x\\right)\nsage: latex(cot(x))\n\\mbox{\\cot}\\left(x\\right)\n```\n",
    "created_at": "2009-06-12T19:22:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6268#issuecomment-49969",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```


```
[mvngu@sage sage-4.0.1]$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: # the following work as expected
sage: latex(sec)
\sec
sage: latex(csc)
\csc
sage: latex(cot)
\cot
sage: # but the following have extra "\mbox" around the trig function name
sage: latex(sec(x))
\mbox{\sec}\left(x\right)
sage: latex(csc(x))
\mbox{\csc}\left(x\right)
sage: latex(cot(x))
\mbox{\cot}\left(x\right)
```




---

archive/issue_comments_049970.json:
```json
{
    "body": "Is this a bug in ginac/pynac?  Look at this:\n\n```\nsage: SR\nSymbolic Ring\nsage: SR._latex_element_(sin(x))\n'\\\\sin\\\\left(x\\\\right)'\nsage: SR._latex_element_(sec(x))\n'\\\\mbox{\\\\sec}\\\\left(x\\\\right)'\n```\n\nThe method `_latex_element_` is a one-liner:\n\n```\n        return GEx_to_str_latex(&x._gobj)\n```\n\nand I think GEx_to_str_latex is a ginac/pynac thing.  At least, I found it in sage/libs/ginac/decl.pxi.\n\nIt's possible to work around it, I think, with a patch like the attached, but I'm not at all convinced that this is the right way to fix it.  If you think it's okay, feel free to review it, but since I'm not sure, I've labeled it as \"not read for review\".",
    "created_at": "2009-06-12T20:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6268#issuecomment-49970",
    "user": "https://github.com/jhpalmieri"
}
```

Is this a bug in ginac/pynac?  Look at this:

```
sage: SR
Symbolic Ring
sage: SR._latex_element_(sin(x))
'\\sin\\left(x\\right)'
sage: SR._latex_element_(sec(x))
'\\mbox{\\sec}\\left(x\\right)'
```

The method `_latex_element_` is a one-liner:

```
        return GEx_to_str_latex(&x._gobj)
```

and I think GEx_to_str_latex is a ginac/pynac thing.  At least, I found it in sage/libs/ginac/decl.pxi.

It's possible to work around it, I think, with a patch like the attached, but I'm not at all convinced that this is the right way to fix it.  If you think it's okay, feel free to review it, but since I'm not sure, I've labeled it as "not read for review".



---

archive/issue_comments_049971.json:
```json
{
    "body": "Attachment [trac_6268.patch](tarball://root/attachments/some-uuid/ticket6268/trac_6268.patch) by @golam-m-hossain created at 2009-06-12 22:35:18\n\nThe rebased patch for the ticket\n\nhttp://trac.sagemath.org/sage_trac/ticket/5711\n\nwill resolve this issue as an un-intended consequence.",
    "created_at": "2009-06-12T22:35:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6268#issuecomment-49971",
    "user": "https://github.com/golam-m-hossain"
}
```

Attachment [trac_6268.patch](tarball://root/attachments/some-uuid/ticket6268/trac_6268.patch) by @golam-m-hossain created at 2009-06-12 22:35:18

The rebased patch for the ticket

http://trac.sagemath.org/sage_trac/ticket/5711

will resolve this issue as an un-intended consequence.



---

archive/issue_comments_049972.json:
```json
{
    "body": "new patch, apply only this one",
    "created_at": "2009-06-14T22:16:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6268#issuecomment-49972",
    "user": "https://github.com/burcin"
}
```

new patch, apply only this one



---

archive/issue_comments_049973.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-14T22:17:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6268#issuecomment-49973",
    "user": "https://github.com/burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_049974.json:
```json
{
    "body": "Changing assignee from cwitty to @burcin.",
    "created_at": "2009-06-14T22:17:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6268#issuecomment-49974",
    "user": "https://github.com/burcin"
}
```

Changing assignee from cwitty to @burcin.



---

archive/issue_comments_049975.json:
```json
{
    "body": "Changing component from misc to symbolics.",
    "created_at": "2009-06-14T22:17:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6268#issuecomment-49975",
    "user": "https://github.com/burcin"
}
```

Changing component from misc to symbolics.



---

archive/issue_comments_049976.json:
```json
{
    "body": "Attachment [trac_6268-py_print_latex.patch](tarball://root/attachments/some-uuid/ticket6268/trac_6268-py_print_latex.patch) by @burcin created at 2009-06-14 22:17:42\n\nattachment:trac_6268-py_print_latex.patch fixes the reported problem. Apply only this patch.",
    "created_at": "2009-06-14T22:17:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6268#issuecomment-49976",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_6268-py_print_latex.patch](tarball://root/attachments/some-uuid/ticket6268/trac_6268-py_print_latex.patch) by @burcin created at 2009-06-14 22:17:42

attachment:trac_6268-py_print_latex.patch fixes the reported problem. Apply only this patch.



---

archive/issue_events_006512.json:
```json
{
    "actor": "@ncalexan",
    "created_at": "2009-06-14T22:21:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6268",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6268#event-6512"
}
```



---

archive/issue_comments_049977.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-14T22:21:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6268#issuecomment-49977",
    "user": "https://github.com/ncalexan"
}
```

Resolution: fixed
