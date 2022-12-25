# Issue 5187: fix optional magma doctests that changed in magma-2.15

archive/issues_005187.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe latest version of Magma is Magma-2.15, and there are doctests all over that now slightly fail because the output format of certain things in Magma has changed.  \n\nThe file at http://sage.math.washington.edu/home/was/patches/magma-2.15.txt lists all the doctest failures.  It was got by running this script:\n\n```\n        sage -t -only_optional=magma \"devel/sage/sage/rings/polynomial/multi_polynomial_ring_generic.pyx\"\n        sage -t -only_optional=magma \"devel/sage/sage/rings/polynomial/term_order.py\"\n        sage -t -only_optional=magma \"devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\"\n        sage -t -only_optional=magma \"devel/sage/sage/crypto/mq/mpolynomialsystem.py\"\n        sage -t -only_optional=magma \"devel/sage/sage/interfaces/magma.py\"\n\n```\n\non eno, which has Magma-2.15.\n\nI think all the changes are purely cosmetic, so this should be very straightforward (but tedious).\n\nIssue created by migration from https://trac.sagemath.org/ticket/5187\n\n",
    "created_at": "2009-02-05T21:30:50Z",
    "labels": [
        "component: interfaces",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "fix optional magma doctests that changed in magma-2.15",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5187",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

The latest version of Magma is Magma-2.15, and there are doctests all over that now slightly fail because the output format of certain things in Magma has changed.  

The file at http://sage.math.washington.edu/home/was/patches/magma-2.15.txt lists all the doctest failures.  It was got by running this script:

```
        sage -t -only_optional=magma "devel/sage/sage/rings/polynomial/multi_polynomial_ring_generic.pyx"
        sage -t -only_optional=magma "devel/sage/sage/rings/polynomial/term_order.py"
        sage -t -only_optional=magma "devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py"
        sage -t -only_optional=magma "devel/sage/sage/crypto/mq/mpolynomialsystem.py"
        sage -t -only_optional=magma "devel/sage/sage/interfaces/magma.py"

```

on eno, which has Magma-2.15.

I think all the changes are purely cosmetic, so this should be very straightforward (but tedious).

Issue created by migration from https://trac.sagemath.org/ticket/5187





---

archive/issue_comments_039705.json:
```json
{
    "body": "It all seems to be \n\n```\nGraded Reverse Lexicographical Order\n```\n\nvs\n\n```\nOrder: Graded Reverse Lexicographical\n```\n\nand \n\n```\nLexicographical Order\n```\n\nvs\n\n```\nOrder: Lexicographical\n```\n\n\nThe question is: Do we make 2.15 the only officially blessed release or do we add a sufficient amount of dots to make the tests also pass with 2.13 to 2.14?\n\nCheers,\n\nMichael",
    "created_at": "2009-02-05T21:39:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5187#issuecomment-39705",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

It all seems to be 

```
Graded Reverse Lexicographical Order
```

vs

```
Order: Graded Reverse Lexicographical
```

and 

```
Lexicographical Order
```

vs

```
Order: Lexicographical
```


The question is: Do we make 2.15 the only officially blessed release or do we add a sufficient amount of dots to make the tests also pass with 2.13 to 2.14?

Cheers,

Michael



---

archive/issue_comments_039706.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-05-24T20:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5187#issuecomment-39706",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_039707.json:
```json
{
    "body": "I believe this ticket can be closed as it is superceded by #7870.",
    "created_at": "2011-05-24T20:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5187#issuecomment-39707",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

I believe this ticket can be closed as it is superceded by #7870.



---

archive/issue_events_005441.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2011-08-23T05:19:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5187",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5187#event-5441"
}
```



---

archive/issue_comments_039708.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-08-23T05:19:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5187#issuecomment-39708",
    "user": "https://github.com/williamstein"
}
```

Resolution: duplicate



---

archive/issue_comments_039709.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd32\".",
    "created_at": "2011-08-24T23:45:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5187#issuecomment-39709",
    "user": "https://github.com/williamstein"
}
```

Changing keywords from "" to "sd32".
