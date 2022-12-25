# Issue 5967: ElementWrapper: A class for wrapping Sage or Python objects as Sage elements

archive/issues_005967.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat\n\nThis patch implements a simple class ElementWrapper for wrapping Sage\nor Python objects as Sage elements, with reasonable default\nimplementations of repr, cmp, hash, etc. The typical use case is for\ntrivially constructing new element classes from preexisting Sage or\nPython classes, with a containment relation.\n\nThis class is used extensively in the examples of the upcoming category framework patch #5891.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5967\n\n",
    "created_at": "2009-05-03T01:26:19Z",
    "labels": [
        "component: misc"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "ElementWrapper: A class for wrapping Sage or Python objects as Sage elements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5967",
    "user": "https://github.com/nthiery"
}
```
Assignee: @nthiery

CC:  sage-combinat

This patch implements a simple class ElementWrapper for wrapping Sage
or Python objects as Sage elements, with reasonable default
implementations of repr, cmp, hash, etc. The typical use case is for
trivially constructing new element classes from preexisting Sage or
Python classes, with a containment relation.

This class is used extensively in the examples of the upcoming category framework patch #5891.


Issue created by migration from https://trac.sagemath.org/ticket/5967





---

archive/issue_comments_047188.json:
```json
{
    "body": "This is broken:\n\n```\n \t129\t            sage: cmp(l11, l12), cmp(l12, l11)   # values differ \n \t130\t            (-1, 1) \n \t131\t            sage: cmp(l11, l21), cmp(l21, l11)   # parents differ \n \t132\t            (-1, 1) \n```\n**Never** check the return value of `cmp` to be -1 or 1, but always write\n\n```\nsage: cmp(l11, l21) in [-1,1]\nTrue\n```\nsince the value depends on memory location. I have had to fix this literally dozens of times in doctests.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-03T01:55:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5967#issuecomment-47188",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is broken:

```
 	129	            sage: cmp(l11, l12), cmp(l12, l11)   # values differ 
 	130	            (-1, 1) 
 	131	            sage: cmp(l11, l21), cmp(l21, l11)   # parents differ 
 	132	            (-1, 1) 
```
**Never** check the return value of `cmp` to be -1 or 1, but always write

```
sage: cmp(l11, l21) in [-1,1]
True
```
since the value depends on memory location. I have had to fix this literally dozens of times in doctests.

Cheers,

Michael



---

archive/issue_comments_047189.json:
```json
{
    "body": "This ticket also needs to be properly market with a marker so it is picked up for review.\n\nAnother thing to fix is to get this file into the documentation. Unless it is in the documentation the vast majority of people will never know of its existence. Current policy is that every file that is well documented and 100% doctested belongs in the documentation. \n\nCheers,\n\nMichael",
    "created_at": "2009-05-03T01:57:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5967#issuecomment-47189",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This ticket also needs to be properly market with a marker so it is picked up for review.

Another thing to fix is to get this file into the documentation. Unless it is in the documentation the vast majority of people will never know of its existence. Current policy is that every file that is well documented and 100% doctested belongs in the documentation. 

Cheers,

Michael



---

archive/issue_comments_047190.json:
```json
{
    "body": "Replying to [comment:1 mabshoff]:\n> This is broken:\n> \n> ```\n>  \t129\t            sage: cmp(l11, l12), cmp(l12, l11)   # values differ \n>  \t130\t            (-1, 1) \n>  \t131\t            sage: cmp(l11, l21), cmp(l21, l11)   # parents differ \n>  \t132\t            (-1, 1) \n> ```\n> **Never** check the return value of `cmp` to be -1 or 1, but always write\n> \n> ```\n> sage: cmp(l11, l21) in [-1,1]\n> True\n> ```\n> since the value depends on memory location. I have had to fix this literally dozens of times in doctests.\n\n\nOk, will do.",
    "created_at": "2009-05-03T02:25:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5967#issuecomment-47190",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:1 mabshoff]:
> This is broken:
> 
> ```
>  	129	            sage: cmp(l11, l12), cmp(l12, l11)   # values differ 
>  	130	            (-1, 1) 
>  	131	            sage: cmp(l11, l21), cmp(l21, l11)   # parents differ 
>  	132	            (-1, 1) 
> ```
> **Never** check the return value of `cmp` to be -1 or 1, but always write
> 
> ```
> sage: cmp(l11, l21) in [-1,1]
> True
> ```
> since the value depends on memory location. I have had to fix this literally dozens of times in doctests.


Ok, will do.



---

archive/issue_comments_047191.json:
```json
{
    "body": "Replying to [comment:2 mabshoff]:\n> This ticket also needs to be properly market with a marker so it is picked up for review.\n\n\nAny suggestion for that marker?\n\n> Another thing to fix is to get this file into the documentation. Unless it is in the documentation the vast majority of people will never know of its existence. Current policy is that every file that is well documented and 100% doctested belongs in the documentation. \n\n\nOk, will do.",
    "created_at": "2009-05-03T02:25:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5967#issuecomment-47191",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:2 mabshoff]:
> This ticket also needs to be properly market with a marker so it is picked up for review.


Any suggestion for that marker?

> Another thing to fix is to get this file into the documentation. Unless it is in the documentation the vast majority of people will never know of its existence. Current policy is that every file that is well documented and 100% doctested belongs in the documentation. 


Ok, will do.



---

archive/issue_comments_047192.json:
```json
{
    "body": "Replying to [comment:4 nthiery]:\n> Replying to [comment:2 mabshoff]:\n> > This ticket also needs to be properly market with a marker so it is picked up for review.\n\n> \n> Any suggestion for that marker?\n\n\nI meant the standard \"[with patch, needs review]\" :)\n\nCheers,\n\nMichael",
    "created_at": "2009-05-03T02:29:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5967#issuecomment-47192",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:4 nthiery]:
> Replying to [comment:2 mabshoff]:
> > This ticket also needs to be properly market with a marker so it is picked up for review.

> 
> Any suggestion for that marker?


I meant the standard "[with patch, needs review]" :)

Cheers,

Michael



---

archive/issue_comments_047193.json:
```json
{
    "body": "Replying to [comment:5 mabshoff]:\n> I meant the standard \"[with patch, needs review]\" :)\n\n\nOops, I was sure I had done this!",
    "created_at": "2009-05-03T02:33:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5967#issuecomment-47193",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:5 mabshoff]:
> I meant the standard "[with patch, needs review]" :)


Oops, I was sure I had done this!



---

archive/issue_comments_047194.json:
```json
{
    "body": "Done, and patch updated. Thanks Michael for your suggestions.",
    "created_at": "2009-05-03T03:02:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5967#issuecomment-47194",
    "user": "https://github.com/nthiery"
}
```

Done, and patch updated. Thanks Michael for your suggestions.



---

archive/issue_comments_047195.json:
```json
{
    "body": "The tests of the patch pass when applied to sage-3.4.2.\n\nBesides the application to the category framework #5891,\nthis patch will be useful for crystals. For example the\nclass Letter(Element):\nin /combinat/crystals/letters.py\ncan be shortened by inheriting from ElementWrapper.\n\nI give this patch a positive review!",
    "created_at": "2009-05-07T03:50:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5967#issuecomment-47195",
    "user": "https://github.com/anneschilling"
}
```

The tests of the patch pass when applied to sage-3.4.2.

Besides the application to the category framework #5891,
this patch will be useful for crystals. For example the
class Letter(Element):
in /combinat/crystals/letters.py
can be shortened by inheriting from ElementWrapper.

I give this patch a positive review!



---

archive/issue_comments_047196.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-19T06:25:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5967#issuecomment-47196",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to assigned.



---

archive/issue_comments_047197.json:
```json
{
    "body": "Has anybody non-combinat signed off on this? Not that I don't trust Anne, but ... ;)\n\nCheers,\n\nMichael",
    "created_at": "2009-05-22T14:20:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5967#issuecomment-47197",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Has anybody non-combinat signed off on this? Not that I don't trust Anne, but ... ;)

Cheers,

Michael



---

archive/issue_comments_047198.json:
```json
{
    "body": "The uploaded patch adds a warning about the probable little change of interface in the near future (but after integration of the category patch).\nRobert promised to have a look at this shortly.",
    "created_at": "2009-05-23T07:41:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5967#issuecomment-47198",
    "user": "https://github.com/nthiery"
}
```

The uploaded patch adds a warning about the probable little change of interface in the near future (but after integration of the category patch).
Robert promised to have a look at this shortly.



---

archive/issue_comments_047199.json:
```json
{
    "body": "I agree this looks good. The only caveat is that the docstring reads \n\n```\nTherefore, ``o`` does inherit the string\n```\n\nwhere it probably should be \"does not.\"",
    "created_at": "2009-05-23T08:55:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5967#issuecomment-47199",
    "user": "https://github.com/robertwb"
}
```

I agree this looks good. The only caveat is that the docstring reads 

```
Therefore, ``o`` does inherit the string
```

where it probably should be "does not."



---

archive/issue_comments_047200.json:
```json
{
    "body": "Attachment [element_wrapper-5967-submitted.patch](tarball://root/attachments/some-uuid/ticket5967/element_wrapper-5967-submitted.patch) by @nthiery created at 2009-05-23 15:40:38",
    "created_at": "2009-05-23T15:40:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5967#issuecomment-47200",
    "user": "https://github.com/nthiery"
}
```

Attachment [element_wrapper-5967-submitted.patch](tarball://root/attachments/some-uuid/ticket5967/element_wrapper-5967-submitted.patch) by @nthiery created at 2009-05-23 15:40:38



---

archive/issue_comments_047201.json:
```json
{
    "body": "Replying to [comment:12 robertwb]:\n> I agree this looks good. The only caveat is that the docstring reads \n> \n> \n> ```\n> Therefore, ``o`` does inherit the string\n> ```\n> \n> where it probably should be \"does not.\"\n\n\nOops, indeed! Thanks. Patch updated.",
    "created_at": "2009-05-23T15:49:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5967#issuecomment-47201",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:12 robertwb]:
> I agree this looks good. The only caveat is that the docstring reads 
> 
> 
> ```
> Therefore, ``o`` does inherit the string
> ```
> 
> where it probably should be "does not."


Oops, indeed! Thanks. Patch updated.



---

archive/issue_comments_047202.json:
```json
{
    "body": "Merged in 4.0.1.alpha0.",
    "created_at": "2009-05-31T23:40:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5967#issuecomment-47202",
    "user": "https://github.com/mwhansen"
}
```

Merged in 4.0.1.alpha0.



---

archive/issue_comments_047203.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-31T23:40:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5967#issuecomment-47203",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_014008.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-05-31T23:40:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5967",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5967#event-14008"
}
```
