# Issue 3105: [with patch, needs review]  new  _latex_  and modified  __repr__  for elements of relative number fields

archive/issues_003105.json:
```json
{
    "body": "Assignee: was\n\nCC:  f.clarke@swansea.ac.uk\n\nPatch by Francis Clarke. He should fill in the details once his new trac account works.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3105\n\n",
    "created_at": "2008-05-05T12:56:27Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review]  new  _latex_  and modified  __repr__  for elements of relative number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3105",
    "user": "mabshoff"
}
```
Assignee: was

CC:  f.clarke@swansea.ac.uk

Patch by Francis Clarke. He should fill in the details once his new trac account works.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3105





---

archive/issue_comments_021456.json:
```json
{
    "body": "Attachment\n\nThis patch appliesw fine to 3.0.1 and the doctests in sage/rings/number_field all pass.\n\nIt looks fine to me.",
    "created_at": "2008-05-05T16:14:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3105#issuecomment-21456",
    "user": "cremona"
}
```

Attachment

This patch appliesw fine to 3.0.1 and the doctests in sage/rings/number_field all pass.

It looks fine to me.



---

archive/issue_comments_021457.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha0",
    "created_at": "2008-05-05T20:35:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3105#issuecomment-21457",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.2.alpha0



---

archive/issue_comments_021458.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-05T20:35:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3105#issuecomment-21458",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021459.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-05-06T09:13:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3105#issuecomment-21459",
    "user": "fwclarke"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_021460.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-05-06T09:13:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3105#issuecomment-21460",
    "user": "fwclarke"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_021461.json:
```json
{
    "body": "\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.0, Release Date: 2008-04-21                         |\n| Type notebook() for the GUI, and license() for information.        |\nsage: A.<a> = CyclotomicField(3)\nsage: P.<x> = PolynomialRing(A)\nsage: B.<b> = NumberField(x^2 - 5)\nsage: (a + b)^2\n2*a*b - a + 4\nsage: latex((a + b)^2)\n\\frac{4}{23} b^{3} - \\frac{29}{23} b^{2} - \\frac{8}{23} b + \\frac{212}{23}\n```\n\n\nThis is clearly wrong.  What is happening is the element is being \nrepresented in the absolute number field, but using the variable \nappropriate to the relative field:\n\n\n```\nsage: C.<c> = B.absolute_field()\nsage: from_abs, to_abs = C.structure()\nsage: to_abs((a + b)^2)\n4/23*c^3 - 29/23*c^2 - 8/23*c + 212/23\nsage: latex(to_abs((a + b)^2))\n\\frac{4}{23} c^{3} - \\frac{29}{23} c^{2} - \\frac{8}{23} c + \\frac{212}{23}\n```\n\n\nThe patch below fixes this by providing a  _latex_  function for elements of \nrelative number fields.\n\nIt also simplifies  !__repr!__  for such elements slightly.",
    "created_at": "2008-05-06T09:37:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3105#issuecomment-21461",
    "user": "fwclarke"
}
```


```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0, Release Date: 2008-04-21                         |
| Type notebook() for the GUI, and license() for information.        |
sage: A.<a> = CyclotomicField(3)
sage: P.<x> = PolynomialRing(A)
sage: B.<b> = NumberField(x^2 - 5)
sage: (a + b)^2
2*a*b - a + 4
sage: latex((a + b)^2)
\frac{4}{23} b^{3} - \frac{29}{23} b^{2} - \frac{8}{23} b + \frac{212}{23}
```


This is clearly wrong.  What is happening is the element is being 
represented in the absolute number field, but using the variable 
appropriate to the relative field:


```
sage: C.<c> = B.absolute_field()
sage: from_abs, to_abs = C.structure()
sage: to_abs((a + b)^2)
4/23*c^3 - 29/23*c^2 - 8/23*c + 212/23
sage: latex(to_abs((a + b)^2))
\frac{4}{23} c^{3} - \frac{29}{23} c^{2} - \frac{8}{23} c + \frac{212}{23}
```


The patch below fixes this by providing a  _latex_  function for elements of 
relative number fields.

It also simplifies  !__repr!__  for such elements slightly.



---

archive/issue_comments_021462.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-06T09:37:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3105#issuecomment-21462",
    "user": "fwclarke"
}
```

Resolution: fixed
