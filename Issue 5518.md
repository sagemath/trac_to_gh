# Issue 5518: Improve efficiency of multiplcative_order() for number field elements

archive/issues_005518.json:
```json
{
    "body": "Assignee: was\n\nKeywords: number field multiplicative order\n\nThe attached patch vastly improves the efficiency of the multiplicative_order() function for number field elements.  Before, this example:\n\n```\n sage: x = polygen(QQ)\n            sage: K.<a>=NumberField(x^40 - x^20 + 4)\n            sage: u = 1/4*a^30 + 1/4*a^10 + 1/2\n            sage: u.multiplicative_order()\n            6\n            sage: a.multiplicative_order()\n            +Infinity\n```\n\nwould have required raising a to the power 2**40 (I'm serious).  Now it just works (fast).\n\nIssue created by migration from https://trac.sagemath.org/ticket/5518\n\n",
    "created_at": "2009-03-14T18:53:55Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "Improve efficiency of multiplcative_order() for number field elements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5518",
    "user": "cremona"
}
```
Assignee: was

Keywords: number field multiplicative order

The attached patch vastly improves the efficiency of the multiplicative_order() function for number field elements.  Before, this example:

```
 sage: x = polygen(QQ)
            sage: K.<a>=NumberField(x^40 - x^20 + 4)
            sage: u = 1/4*a^30 + 1/4*a^10 + 1/2
            sage: u.multiplicative_order()
            6
            sage: a.multiplicative_order()
            +Infinity
```

would have required raising a to the power 2**40 (I'm serious).  Now it just works (fast).

Issue created by migration from https://trac.sagemath.org/ticket/5518





---

archive/issue_comments_042888.json:
```json
{
    "body": "Attachment [multiplicative_order.patch](tarball://root/attachments/some-uuid/ticket5518/multiplicative_order.patch) by cremona created at 2009-03-14 20:35:19",
    "created_at": "2009-03-14T20:35:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5518#issuecomment-42888",
    "user": "cremona"
}
```

Attachment [multiplicative_order.patch](tarball://root/attachments/some-uuid/ticket5518/multiplicative_order.patch) by cremona created at 2009-03-14 20:35:19



---

archive/issue_comments_042889.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2009-03-14T20:35:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5518#issuecomment-42889",
    "user": "cremona"
}
```

Changing priority from major to minor.



---

archive/issue_comments_042890.json:
```json
{
    "body": "This is excellent.  A great speed up, and it gives the right answer!  \n\nI would suggest adding the doctest\n\n```\nsage: K.<a, b> = NumberField([x^2 + x + 1, x^2 - 3])\nsage: z = (a - 1)*b/3\nsage: z.multiplicative_order()\n12\n```\n\nbecause sage-3.4 says the order is `+infinity`.",
    "created_at": "2009-03-17T20:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5518#issuecomment-42890",
    "user": "fwclarke"
}
```

This is excellent.  A great speed up, and it gives the right answer!  

I would suggest adding the doctest

```
sage: K.<a, b> = NumberField([x^2 + x + 1, x^2 - 3])
sage: z = (a - 1)*b/3
sage: z.multiplicative_order()
12
```

because sage-3.4 says the order is `+infinity`.



---

archive/issue_comments_042891.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2009-03-17T20:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5518#issuecomment-42891",
    "user": "fwclarke"
}
```

Changing priority from minor to major.



---

archive/issue_comments_042892.json:
```json
{
    "body": "Attachment [trac_5518.patch](tarball://root/attachments/some-uuid/ticket5518/trac_5518.patch) by cremona created at 2009-03-17 22:10:29\n\nI added a small patch with the additional doctest as suggested.",
    "created_at": "2009-03-17T22:10:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5518#issuecomment-42892",
    "user": "cremona"
}
```

Attachment [trac_5518.patch](tarball://root/attachments/some-uuid/ticket5518/trac_5518.patch) by cremona created at 2009-03-17 22:10:29

I added a small patch with the additional doctest as suggested.



---

archive/issue_comments_042893.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-25T09:24:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5518#issuecomment-42893",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_042894.json:
```json
{
    "body": "Merged both patches in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T09:24:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5518#issuecomment-42894",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.4.1.alpha0.

Cheers,

Michael
