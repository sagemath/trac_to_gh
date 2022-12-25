# Issue 2551: `__getitem__` for relative number field elements is ... surprising

archive/issues_002551.json:
```json
{
    "body": "Assignee: @williamstein\n\nIndexing into a relative number field element does unexpected things:\n\n\n```\nsage: K\n Number Field in b with defining polynomial x^3 - 5 over its base field\nsage: K([1,2,3])\n 3*b^2 + (-6*a + 2)*b - 2*a + 7\nsage: K([1,2,3])[0]\n 1\nsage: K([1,2,3])[1]\n 2\n\nsage: K([1,2,3]).list()\n [-2*a + 7, -6*a + 2, 3]\nsage: K([1,2,3]).list()[0]\n -2*a + 7\n\nsage: K([1,2,3]).polynomial()\n 3*x^2 + 2*x + 1\n```\n\n\nThe issue is that it's giving you the entries in the representation of the element as an *absolute* number field element. It should be fixed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2551\n\n",
    "created_at": "2008-03-16T21:10:56Z",
    "labels": [
        "component: number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "`__getitem__` for relative number field elements is ... surprising",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2551",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @williamstein

Indexing into a relative number field element does unexpected things:


```
sage: K
 Number Field in b with defining polynomial x^3 - 5 over its base field
sage: K([1,2,3])
 3*b^2 + (-6*a + 2)*b - 2*a + 7
sage: K([1,2,3])[0]
 1
sage: K([1,2,3])[1]
 2

sage: K([1,2,3]).list()
 [-2*a + 7, -6*a + 2, 3]
sage: K([1,2,3]).list()[0]
 -2*a + 7

sage: K([1,2,3]).polynomial()
 3*x^2 + 2*x + 1
```


The issue is that it's giving you the entries in the representation of the element as an *absolute* number field element. It should be fixed.

Issue created by migration from https://trac.sagemath.org/ticket/2551





---

archive/issue_comments_017381.json:
```json
{
    "body": "This is sorted out by the patch in #5508, in particular the changes  there to `__getitem__` for the class `NumberFieldElement_relative` in `sage/rings/number_field/number_field_element.pyx`.",
    "created_at": "2009-03-13T18:54:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2551#issuecomment-17381",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

This is sorted out by the patch in #5508, in particular the changes  there to `__getitem__` for the class `NumberFieldElement_relative` in `sage/rings/number_field/number_field_element.pyx`.



---

archive/issue_comments_017382.json:
```json
{
    "body": "To close this we would need a doctest.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T08:55:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2551#issuecomment-17382",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

To close this we would need a doctest.

Cheers,

Michael



---

archive/issue_comments_017383.json:
```json
{
    "body": "Replying to [comment:2 mabshoff]:\n> To close this we would need a doctest.\n\nSee lines 2421 to 2445 of sage/rings/number_field/number_field_element.pyx as patched by #5508:\n\n```\n        EXAMPLES::\n        \n            sage: K.<a, b> = NumberField([x^3 - 5, x^2 + 3])\n            sage: c = (a + b)^3; c\n            3*b*a^2 - 9*a - 3*b + 5\n            sage: c[0]\n            -3*b + 5\n        \n        We illustrate bounds checking::\n        \n            sage: c[-1]\n            Traceback (most recent call last):\n            ...\n            IndexError: index must be between 0 and the relative degree minus 1.\n            sage: c[4]\n            Traceback (most recent call last):\n            ...\n            IndexError: index must be between 0 and the relative degree minus 1.\n        \n        The list method implicitly calls ``__getitem__``::\n        \n            sage: list(c)\n            [-3*b + 5, -9, 3*b]\n            sage: K(list(c)) == c\n            True\n```\n",
    "created_at": "2009-03-26T08:59:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2551#issuecomment-17383",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Replying to [comment:2 mabshoff]:
> To close this we would need a doctest.

See lines 2421 to 2445 of sage/rings/number_field/number_field_element.pyx as patched by #5508:

```
        EXAMPLES::
        
            sage: K.<a, b> = NumberField([x^3 - 5, x^2 + 3])
            sage: c = (a + b)^3; c
            3*b*a^2 - 9*a - 3*b + 5
            sage: c[0]
            -3*b + 5
        
        We illustrate bounds checking::
        
            sage: c[-1]
            Traceback (most recent call last):
            ...
            IndexError: index must be between 0 and the relative degree minus 1.
            sage: c[4]
            Traceback (most recent call last):
            ...
            IndexError: index must be between 0 and the relative degree minus 1.
        
        The list method implicitly calls ``__getitem__``::
        
            sage: list(c)
            [-3*b + 5, -9, 3*b]
            sage: K(list(c)) == c
            True
```




---

archive/issue_comments_017384.json:
```json
{
    "body": "Fixed in Sage 3.4.1.alpha0 via #5508. Thanks Francis :)\n\nCheers,\n\nMichael",
    "created_at": "2009-03-26T20:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2551#issuecomment-17384",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed in Sage 3.4.1.alpha0 via #5508. Thanks Francis :)

Cheers,

Michael



---

archive/issue_comments_017385.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-26T20:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2551#issuecomment-17385",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
