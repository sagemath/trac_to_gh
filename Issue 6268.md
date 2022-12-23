# Issue 6268: Typesetting of sec(x), csc(x), cot(x) are broken

archive/issues_006268.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  ncalexan\n\nTypesettings of sec(x), csc(x), cot(x) are broken. It puts an\nextra \"\\mbox\" around them. However, typesetting for sin(x), \ncos(x), tan(x) works as expected.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6268\n\n",
    "created_at": "2009-06-12T15:25:27Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "Typesetting of sec(x), csc(x), cot(x) are broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6268",
    "user": "gmhossain"
}
```
Assignee: cwitty

CC:  ncalexan

Typesettings of sec(x), csc(x), cot(x) are broken. It puts an
extra "\mbox" around them. However, typesetting for sin(x), 
cos(x), tan(x) works as expected.

Issue created by migration from https://trac.sagemath.org/ticket/6268





---

archive/issue_comments_050065.json:
```json
{
    "body": "\n```\n[mvngu@sage sage-4.0.1]$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: # the following work as expected\nsage: latex(sec)\n\\sec\nsage: latex(csc)\n\\csc\nsage: latex(cot)\n\\cot\nsage: # but the following have extra \"\\mbox\" around the trig function name\nsage: latex(sec(x))\n\\mbox{\\sec}\\left(x\\right)\nsage: latex(csc(x))\n\\mbox{\\csc}\\left(x\\right)\nsage: latex(cot(x))\n\\mbox{\\cot}\\left(x\\right)\n```\n",
    "created_at": "2009-06-12T19:22:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6268#issuecomment-50065",
    "user": "mvngu"
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

archive/issue_comments_050066.json:
```json
{
    "body": "Is this a bug in ginac/pynac?  Look at this:\n\n```\nsage: SR\nSymbolic Ring\nsage: SR._latex_element_(sin(x))\n'\\\\sin\\\\left(x\\\\right)'\nsage: SR._latex_element_(sec(x))\n'\\\\mbox{\\\\sec}\\\\left(x\\\\right)'\n```\n\nThe method `_latex_element_` is a one-liner:\n\n```\n        return GEx_to_str_latex(&x._gobj)\n```\n\nand I think GEx_to_str_latex is a ginac/pynac thing.  At least, I found it in sage/libs/ginac/decl.pxi.\n\nIt's possible to work around it, I think, with a patch like the attached, but I'm not at all convinced that this is the right way to fix it.  If you think it's okay, feel free to review it, but since I'm not sure, I've labeled it as \"not read for review\".",
    "created_at": "2009-06-12T20:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6268#issuecomment-50066",
    "user": "jhpalmieri"
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

archive/issue_comments_050067.json:
```json
{
    "body": "Attachment\n\nThe rebased patch for the ticket\n\nhttp://trac.sagemath.org/sage_trac/ticket/5711\n\nwill resolve this issue as an un-intended consequence.",
    "created_at": "2009-06-12T22:35:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6268#issuecomment-50067",
    "user": "gmhossain"
}
```

Attachment

The rebased patch for the ticket

http://trac.sagemath.org/sage_trac/ticket/5711

will resolve this issue as an un-intended consequence.



---

archive/issue_comments_050068.json:
```json
{
    "body": "new patch, apply only this one",
    "created_at": "2009-06-14T22:16:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6268#issuecomment-50068",
    "user": "burcin"
}
```

new patch, apply only this one



---

archive/issue_comments_050069.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-14T22:17:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6268#issuecomment-50069",
    "user": "burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_050070.json:
```json
{
    "body": "Changing assignee from cwitty to burcin.",
    "created_at": "2009-06-14T22:17:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6268#issuecomment-50070",
    "user": "burcin"
}
```

Changing assignee from cwitty to burcin.



---

archive/issue_comments_050071.json:
```json
{
    "body": "Changing component from misc to symbolics.",
    "created_at": "2009-06-14T22:17:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6268#issuecomment-50071",
    "user": "burcin"
}
```

Changing component from misc to symbolics.



---

archive/issue_comments_050072.json:
```json
{
    "body": "Attachment\n\nattachment:trac_6268-py_print_latex.patch fixes the reported problem. Apply only this patch.",
    "created_at": "2009-06-14T22:17:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6268#issuecomment-50072",
    "user": "burcin"
}
```

Attachment

attachment:trac_6268-py_print_latex.patch fixes the reported problem. Apply only this patch.



---

archive/issue_comments_050073.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-14T22:21:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6268#issuecomment-50073",
    "user": "ncalexan"
}
```

Resolution: fixed
