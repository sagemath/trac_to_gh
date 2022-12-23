# Issue 6950: computing algebraic immunity

archive/issues_006950.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  malb\n\nIt would be nice to have an efficient implementation for computing the algebraic immunity of a Boolean function and finding annihilators.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6950\n\n",
    "created_at": "2009-09-17T19:28:30Z",
    "labels": [
        "cryptography",
        "major",
        "enhancement"
    ],
    "title": "computing algebraic immunity",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6950",
    "user": "ylchapuy"
}
```
Assignee: somebody

CC:  malb

It would be nice to have an efficient implementation for computing the algebraic immunity of a Boolean function and finding annihilators.

Issue created by migration from https://trac.sagemath.org/ticket/6950





---

archive/issue_comments_057474.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2009-09-17T19:34:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6950#issuecomment-57474",
    "user": "ylchapuy"
}
```

Changing priority from major to minor.



---

archive/issue_comments_057475.json:
```json
{
    "body": "This is a toy implementation, but still better than nothing. I also added a way of constructing a random Boolean function, I hope it's ok to put both in this ticket.\n\nPS: Is it ok if I cc you Martin?",
    "created_at": "2009-09-17T19:34:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6950#issuecomment-57475",
    "user": "ylchapuy"
}
```

This is a toy implementation, but still better than nothing. I also added a way of constructing a random Boolean function, I hope it's ok to put both in this ticket.

PS: Is it ok if I cc you Martin?



---

archive/issue_comments_057476.json:
```json
{
    "body": "Of course, its okay :) I'll try to do the review before I go on holiday on Saturday.",
    "created_at": "2009-09-17T20:33:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6950#issuecomment-57476",
    "user": "malb"
}
```

Of course, its okay :) I'll try to do the review before I go on holiday on Saturday.



---

archive/issue_comments_057477.json:
```json
{
    "body": "I noticed `def random_BooleanFunction(n)` while skimming the patch, the convention seems to be `random_boolean_function`, i.e. lower case for functions.",
    "created_at": "2009-09-17T20:34:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6950#issuecomment-57477",
    "user": "malb"
}
```

I noticed `def random_BooleanFunction(n)` while skimming the patch, the convention seems to be `random_boolean_function`, i.e. lower case for functions.



---

archive/issue_comments_057478.json:
```json
{
    "body": "Patch updated.",
    "created_at": "2009-09-17T20:54:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6950#issuecomment-57478",
    "user": "ylchapuy"
}
```

Patch updated.



---

archive/issue_comments_057479.json:
```json
{
    "body": "**Review**\n\n* patch applies cleanly against alpha1\n* you shouldn't need `#random` in the doctest because the random seed should be reset before each doctest to make sure that the result is reproducible. \n* there are some very minor line break problems in the HTML reference manual: http://sage.math.washington.edu/home/malb/scratch/sage-4.1.2.alpha1/devel/sage/doc/output/html/en/reference/sage/crypto/boolean_function.html\n* also `..math::` is not properly typesetted (cf. same link)\n* doctests pass on sage.math\n\nSo almost positive review, module the nitpicks above. Feel free to change it to a positive review once those are addressed.",
    "created_at": "2009-09-17T21:50:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6950#issuecomment-57479",
    "user": "malb"
}
```

**Review**

* patch applies cleanly against alpha1
* you shouldn't need `#random` in the doctest because the random seed should be reset before each doctest to make sure that the result is reproducible. 
* there are some very minor line break problems in the HTML reference manual: http://sage.math.washington.edu/home/malb/scratch/sage-4.1.2.alpha1/devel/sage/doc/output/html/en/reference/sage/crypto/boolean_function.html
* also `..math::` is not properly typesetted (cf. same link)
* doctests pass on sage.math

So almost positive review, module the nitpicks above. Feel free to change it to a positive review once those are addressed.



---

archive/issue_comments_057480.json:
```json
{
    "body": "based on sage 4.1.2.alpha0 (needs #6877)",
    "created_at": "2009-09-17T22:44:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6950#issuecomment-57480",
    "user": "ylchapuy"
}
```

based on sage 4.1.2.alpha0 (needs #6877)



---

archive/issue_comments_057481.json:
```json
{
    "body": "Attachment\n\nThanks for that quick review, and enjoy your holidays!",
    "created_at": "2009-09-17T22:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6950#issuecomment-57481",
    "user": "ylchapuy"
}
```

Attachment

Thanks for that quick review, and enjoy your holidays!



---

archive/issue_comments_057482.json:
```json
{
    "body": "See #6953 for a follow-up to this ticket.",
    "created_at": "2009-09-18T02:10:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6950#issuecomment-57482",
    "user": "mvngu"
}
```

See #6953 for a follow-up to this ticket.



---

archive/issue_comments_057483.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-18T02:10:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6950#issuecomment-57483",
    "user": "mvngu"
}
```

Resolution: fixed
