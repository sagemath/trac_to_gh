# Issue 7363: print symbolic fractions more naturally: print 2/(x+2) instead of 2 (1/(x+2))

archive/issues_007363.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @burcin\n\nSee http://groups.google.com/group/sage-devel/browse_frm/thread/9d58693356e11947\n\nIssue created by migration from https://trac.sagemath.org/ticket/7363\n\n",
    "created_at": "2009-10-31T14:44:49Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "print symbolic fractions more naturally: print 2/(x+2) instead of 2 (1/(x+2))",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7363",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @burcin

CC:  @burcin

See http://groups.google.com/group/sage-devel/browse_frm/thread/9d58693356e11947

Issue created by migration from https://trac.sagemath.org/ticket/7363





---

archive/issue_comments_061580.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2009-10-31T14:45:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7363#issuecomment-61580",
    "user": "https://github.com/jasongrout"
}
```

Changing priority from major to minor.



---

archive/issue_comments_061581.json:
```json
{
    "body": "add doctests",
    "created_at": "2010-01-17T07:20:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7363#issuecomment-61581",
    "user": "https://github.com/burcin"
}
```

add doctests



---

archive/issue_comments_061582.json:
```json
{
    "body": "Attachment [trac_7363-mul_coeff.patch](tarball://root/attachments/some-uuid/ticket7363/trac_7363-mul_coeff.patch) by @burcin created at 2010-01-17 07:22:12\n\nNext pynac release will have a patch for this. attachment:trac_7363-mul_coeff.patch fixes some doctests and adds a couple more.",
    "created_at": "2010-01-17T07:22:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7363#issuecomment-61582",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_7363-mul_coeff.patch](tarball://root/attachments/some-uuid/ticket7363/trac_7363-mul_coeff.patch) by @burcin created at 2010-01-17 07:22:12

Next pynac release will have a patch for this. attachment:trac_7363-mul_coeff.patch fixes some doctests and adds a couple more.



---

archive/issue_comments_061583.json:
```json
{
    "body": "Changing keywords from \"\" to \"pynac\".",
    "created_at": "2010-01-17T07:22:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7363#issuecomment-61583",
    "user": "https://github.com/burcin"
}
```

Changing keywords from "" to "pynac".



---

archive/issue_comments_061584.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-01-17T07:22:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7363#issuecomment-61584",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_061585.json:
```json
{
    "body": "New pynac package available here:\n\nhttp://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.11.spkg\n\nThe package contains fixes for #7822, #6961, #7876, #7363, #6465 and #6559. Apart from this ticket, #7876 contains printing changes. Doctests should be run with the patch from that ticket applied as well.",
    "created_at": "2010-01-19T22:50:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7363#issuecomment-61585",
    "user": "https://github.com/burcin"
}
```

New pynac package available here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.11.spkg

The package contains fixes for #7822, #6961, #7876, #7363, #6465 and #6559. Apart from this ticket, #7876 contains printing changes. Doctests should be run with the patch from that ticket applied as well.



---

archive/issue_comments_061586.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-19T22:50:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7363#issuecomment-61586",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061587.json:
```json
{
    "body": "This seems to work well, but I do not know enough C++ to review http://pynac.sagemath.org/hg/rev/5ea74f619c01, unfortunately.  Partial positive review?",
    "created_at": "2010-01-28T21:17:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7363#issuecomment-61587",
    "user": "https://github.com/kcrisman"
}
```

This seems to work well, but I do not know enough C++ to review http://pynac.sagemath.org/hg/rev/5ea74f619c01, unfortunately.  Partial positive review?



---

archive/issue_comments_061588.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-15T14:06:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7363#issuecomment-61588",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061589.json:
```json
{
    "body": "Changing keywords from \"pynac\" to \"pynac, symbolic, print\".",
    "created_at": "2010-02-15T14:06:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7363#issuecomment-61589",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Changing keywords from "pynac" to "pynac, symbolic, print".



---

archive/issue_comments_061590.json:
```json
{
    "body": "Im also not qualified to review the C++ code but the (representative) examples below indicate the code satisfies the objectives so Im giving it a positive review (which someone can reverse if they discover a counterexample)\n\n\n\n```\n# Note: division is left associative: 12/3/4 = (12/3)/4\nsage: 12/3/4 \n1\n\nsage: var('x y z')\n(x, y, z)\n\nsage: 2/(x+1) # the motivating example\n2/(x + 1)\n\nsage: 1/(2*y)\n1/2/y\n\nsage: 1/(1/2*y)\n2/y\n\nsage: x/2/y\n1/2*x/y\n\nsage: .5*x/y\n0.500000000000000*x/y\n\nsage: .5/x/y\n0.500000000000000/(x*y)\n\nsage: 1/2/x/y\n1/2/(x*y)\n\nsage: 1/x/2\n1/2/x\n```\n",
    "created_at": "2010-02-15T14:06:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7363#issuecomment-61590",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Im also not qualified to review the C++ code but the (representative) examples below indicate the code satisfies the objectives so Im giving it a positive review (which someone can reverse if they discover a counterexample)



```
# Note: division is left associative: 12/3/4 = (12/3)/4
sage: 12/3/4 
1

sage: var('x y z')
(x, y, z)

sage: 2/(x+1) # the motivating example
2/(x + 1)

sage: 1/(2*y)
1/2/y

sage: 1/(1/2*y)
2/y

sage: x/2/y
1/2*x/y

sage: .5*x/y
0.500000000000000*x/y

sage: .5/x/y
0.500000000000000/(x*y)

sage: 1/2/x/y
1/2/(x*y)

sage: 1/x/2
1/2/x
```




---

archive/issue_comments_061591.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-18T21:43:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7363#issuecomment-61591",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
