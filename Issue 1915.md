# Issue 1915: infinity doesn't behave well

archive/issues_001915.json:
```json
{
    "body": "Assignee: cwitty\n\nThe default model for handling infinity in Sage is not very user friendly.\n\nHere is an example from Mathematica:\n\n\n```\nmathematica: Gamma[0]\nComplexInfinity\n\nmathematica: 1/Gamma[0]\n0\n\nmathematica: 1 + 1/Gamma[0]\n1\n```\n\n\nAnd an example from sage:\n\n\n```\nsage: 1/Infinity\nZero\n\nsage: 1 + 1/Infinity\nA positive finite number\n```\n\n\nIn Sage `1/Infinity` should be `0` in some numeric domain. Returning `Zero` in `The Infinity Ring`  results in everything coercing to `The Infinity Ring`. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1915\n\n",
    "created_at": "2008-01-24T17:35:48Z",
    "labels": [
        "misc",
        "critical",
        "bug"
    ],
    "title": "infinity doesn't behave well",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1915",
    "user": "burcin"
}
```
Assignee: cwitty

The default model for handling infinity in Sage is not very user friendly.

Here is an example from Mathematica:


```
mathematica: Gamma[0]
ComplexInfinity

mathematica: 1/Gamma[0]
0

mathematica: 1 + 1/Gamma[0]
1
```


And an example from sage:


```
sage: 1/Infinity
Zero

sage: 1 + 1/Infinity
A positive finite number
```


In Sage `1/Infinity` should be `0` in some numeric domain. Returning `Zero` in `The Infinity Ring`  results in everything coercing to `The Infinity Ring`. 

Issue created by migration from https://trac.sagemath.org/ticket/1915





---

archive/issue_comments_012130.json:
```json
{
    "body": "See the attached patch.  I am making 1/Infinity return the integer 0, since that should coerce without problems into any place one wants to do arithmetic.",
    "created_at": "2008-09-07T02:59:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1915#issuecomment-12130",
    "user": "AlexGhitza"
}
```

See the attached patch.  I am making 1/Infinity return the integer 0, since that should coerce without problems into any place one wants to do arithmetic.



---

archive/issue_comments_012131.json:
```json
{
    "body": "Overall, I like this. However, and this is not entirely the fault of your patch, I have an issue here. First, in the docs at the top of the file infinity.py, oo is defined to be `UnsignedInfinityRing.0`, and then later it is defined to be `InfinityRing.0`; however, oo is already defined (in sage.all). It seems bad to define it (since it's already defined), and it also makes the documentation really hard to read, since as it currently stands, sometimes oo means (unsigned) infinity, and sometimes it means +Infinity. If you're doing a quick skim (as I just was), you can get really confused.\n\nFurthermore, in a fresh copy of sage:\n\n```\nsage: InfinityRing.0 == oo\nTrue\nsage: UnsignedInfinityRing.0 == oo\nTrue\nsage: 1 / (UnsignedInfinityRing.0)     \nA number less than infinity\nsage: 1 / oo                      \n0\n```\n\nI don't like the fact that although these various infinities are ==, they don't behave the same when they are denominators.\n\nPerhaps this could be fixed by:\n\n1. having your patch return 0 for quotients like `1 / (UnsignedInfinityRing.0)` (or did you have a reason for not making `1 / (UnsignedInfinityRing.0)` return 0?), and\n\n2. not defining oo in the documentation, but instead verify in the examples that `oo == UnsignedInfinityRing.0` and `oo == InfinityRing.0` both return True. (Or if the generator `UnsignedInfinityRing.0` really needs a name in the docs, give it a different one. Same for `InfinityRing.0`, so the two elements can be easily distinguished when reading the docs.)",
    "created_at": "2008-09-11T22:05:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1915#issuecomment-12131",
    "user": "jhpalmieri"
}
```

Overall, I like this. However, and this is not entirely the fault of your patch, I have an issue here. First, in the docs at the top of the file infinity.py, oo is defined to be `UnsignedInfinityRing.0`, and then later it is defined to be `InfinityRing.0`; however, oo is already defined (in sage.all). It seems bad to define it (since it's already defined), and it also makes the documentation really hard to read, since as it currently stands, sometimes oo means (unsigned) infinity, and sometimes it means +Infinity. If you're doing a quick skim (as I just was), you can get really confused.

Furthermore, in a fresh copy of sage:

```
sage: InfinityRing.0 == oo
True
sage: UnsignedInfinityRing.0 == oo
True
sage: 1 / (UnsignedInfinityRing.0)     
A number less than infinity
sage: 1 / oo                      
0
```

I don't like the fact that although these various infinities are ==, they don't behave the same when they are denominators.

Perhaps this could be fixed by:

1. having your patch return 0 for quotients like `1 / (UnsignedInfinityRing.0)` (or did you have a reason for not making `1 / (UnsignedInfinityRing.0)` return 0?), and

2. not defining oo in the documentation, but instead verify in the examples that `oo == UnsignedInfinityRing.0` and `oo == InfinityRing.0` both return True. (Or if the generator `UnsignedInfinityRing.0` really needs a name in the docs, give it a different one. Same for `InfinityRing.0`, so the two elements can be easily distinguished when reading the docs.)



---

archive/issue_comments_012132.json:
```json
{
    "body": "Attachment\n\nThanks for catching the bug involving unsigned infinity.  I have replaced the patch with one that hopefully addresses the (very justified!) objections.  I chose to explain how oo relates to InfinityRing.0 and to UnsignedInfinity.0, and to replace oo by unsigned_oo in the docstrings related to the unsigned infinity ring.",
    "created_at": "2008-09-12T05:25:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1915#issuecomment-12132",
    "user": "AlexGhitza"
}
```

Attachment

Thanks for catching the bug involving unsigned infinity.  I have replaced the patch with one that hopefully addresses the (very justified!) objections.  I chose to explain how oo relates to InfinityRing.0 and to UnsignedInfinity.0, and to replace oo by unsigned_oo in the docstrings related to the unsigned infinity ring.



---

archive/issue_comments_012133.json:
```json
{
    "body": "Looks good to me. I like the new comparisons using == and `is` at the top, too.",
    "created_at": "2008-09-12T16:26:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1915#issuecomment-12133",
    "user": "jhpalmieri"
}
```

Looks good to me. I like the new comparisons using == and `is` at the top, too.



---

archive/issue_comments_012134.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-15T03:54:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1915#issuecomment-12134",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012135.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc4",
    "created_at": "2008-09-15T03:54:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1915#issuecomment-12135",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc4
