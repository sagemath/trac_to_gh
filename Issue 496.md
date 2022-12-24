# Issue 496: In several places the generic powering and n*x code is stupid.

archive/issues_000496.json:
```json
{
    "body": "Assignee: boothby\n\n* In rings/arith.py the code for generic powering does an extra multiply the last time through the loop.\nThis can take a huge amount of extra time on big powering.\n\n* In structure/element.pyx the code for generic n*x (the function cdef ModuleElement _lmul_c_impl(self, RingElement right), around line 1125) does possibly an extra add.\n\n\nTo fix this either rewrite or refactor the above code to be more like the __pow__ that is around\nline 1057 of element.pyx.  Also, write *lots of doctests* to make sure you're really computing\nthe right thing. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/496\n\n",
    "created_at": "2007-08-27T21:26:34Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "In several places the generic powering and n*x code is stupid.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/496",
    "user": "was"
}
```
Assignee: boothby

* In rings/arith.py the code for generic powering does an extra multiply the last time through the loop.
This can take a huge amount of extra time on big powering.

* In structure/element.pyx the code for generic n*x (the function cdef ModuleElement _lmul_c_impl(self, RingElement right), around line 1125) does possibly an extra add.


To fix this either rewrite or refactor the above code to be more like the __pow__ that is around
line 1057 of element.pyx.  Also, write *lots of doctests* to make sure you're really computing
the right thing. 


Issue created by migration from https://trac.sagemath.org/ticket/496





---

archive/issue_comments_002474.json:
```json
{
    "body": "Attachment [arith_496.hg](tarball://root/attachments/some-uuid/ticket496/arith_496.hg) by boothby created at 2007-08-28 06:43:29\n\nAttached patch fixes the problem.",
    "created_at": "2007-08-28T06:43:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/496#issuecomment-2474",
    "user": "boothby"
}
```

Attachment [arith_496.hg](tarball://root/attachments/some-uuid/ticket496/arith_496.hg) by boothby created at 2007-08-28 06:43:29

Attached patch fixes the problem.



---

archive/issue_comments_002475.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-28T06:43:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/496#issuecomment-2475",
    "user": "boothby"
}
```

Resolution: fixed



---

archive/issue_comments_002476.json:
```json
{
    "body": "Hello,\n\nI think that bugs should only be closed as fixed once the patch has made it into the Repo. While this might be the case at least to the outside world this changeset is not visible yet. So I would suggest adding in Action an option \"fix attached\" to the resolve option.\n\nCheers,\n\nMichael",
    "created_at": "2007-08-28T07:27:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/496#issuecomment-2476",
    "user": "mabshoff"
}
```

Hello,

I think that bugs should only be closed as fixed once the patch has made it into the Repo. While this might be the case at least to the outside world this changeset is not visible yet. So I would suggest adding in Action an option "fix attached" to the resolve option.

Cheers,

Michael



---

archive/issue_comments_002477.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-08-29T23:16:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/496#issuecomment-2477",
    "user": "boothby"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_002478.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-08-29T23:16:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/496#issuecomment-2478",
    "user": "boothby"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_002479.json:
```json
{
    "body": "Attached file introduces bugs.  Better fix is located at:\n\n[http://sage.math.washington.edu/home/boothby/my_patches/arith_2.8.3.hg](http://sage.math.washington.edu/home/boothby/my_patches/arith_2.8.3.hg)\n\n(patch re-opened due to Michael's suggestion)",
    "created_at": "2007-08-29T23:16:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/496#issuecomment-2479",
    "user": "boothby"
}
```

Attached file introduces bugs.  Better fix is located at:

[http://sage.math.washington.edu/home/boothby/my_patches/arith_2.8.3.hg](http://sage.math.washington.edu/home/boothby/my_patches/arith_2.8.3.hg)

(patch re-opened due to Michael's suggestion)



---

archive/issue_comments_002480.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-31T22:06:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/496#issuecomment-2480",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_002481.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-08-31T22:07:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/496#issuecomment-2481",
    "user": "was"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_002482.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-08-31T22:07:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/496#issuecomment-2482",
    "user": "was"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_002483.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-31T22:45:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/496#issuecomment-2483",
    "user": "boothby"
}
```

Resolution: fixed



---

archive/issue_comments_002484.json:
```json
{
    "body": "Everything seems to check out.  Almost all element classes are now using the generic code, and all tests pass.  The classes which do not use generic code are listed in #503, or have good reason not to use it (for example, integers call mpz library code).",
    "created_at": "2007-08-31T22:45:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/496#issuecomment-2484",
    "user": "boothby"
}
```

Everything seems to check out.  Almost all element classes are now using the generic code, and all tests pass.  The classes which do not use generic code are listed in #503, or have good reason not to use it (for example, integers call mpz library code).
