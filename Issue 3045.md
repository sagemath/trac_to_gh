# Issue 3045: K.gen() where K = GF(p) returns 1, not a primitive element

archive/issues_003045.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: galois field\n\n\n```\nsage: k = GF(7)\nsage: k.gen()\n1\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3045\n\n",
    "created_at": "2008-04-27T15:06:13Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "K.gen() where K = GF(p) returns 1, not a primitive element",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3045",
    "user": "https://trac.sagemath.org/admin/accounts/users/jxxcarlson"
}
```
Assignee: @williamstein

Keywords: galois field


```
sage: k = GF(7)
sage: k.gen()
1
```




Issue created by migration from https://trac.sagemath.org/ticket/3045





---

archive/issue_comments_020924.json:
```json
{
    "body": "This is actually the correct behaviour.  The function that returns a primitive element is K.multiplicative_generator(), not K.gen().  There was some inconsistency in the docstrings of the various types of finite fields, which is fixed by the attached patch.",
    "created_at": "2009-01-23T08:31:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3045#issuecomment-20924",
    "user": "https://github.com/aghitza"
}
```

This is actually the correct behaviour.  The function that returns a primitive element is K.multiplicative_generator(), not K.gen().  There was some inconsistency in the docstrings of the various types of finite fields, which is fixed by the attached patch.



---

archive/issue_comments_020925.json:
```json
{
    "body": "This otherwise deserves a positive review, except that I couldn't verify the claim in the doctest that the outputs of gen() and multiplicative_generator() can vary between runs. Is that really true?",
    "created_at": "2009-01-23T22:20:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3045#issuecomment-20925",
    "user": "https://github.com/kedlaya"
}
```

This otherwise deserves a positive review, except that I couldn't verify the claim in the doctest that the outputs of gen() and multiplicative_generator() can vary between runs. Is that really true?



---

archive/issue_comments_020926.json:
```json
{
    "body": "Attachment [trac_3045.patch](tarball://root/attachments/some-uuid/ticket3045/trac_3045.patch) by @aghitza created at 2009-01-24 00:47:25\n\nKiran, I tried to find some examples and couldn't.  I think the point of the warning in the docstring is that we are not guaranteeing that the finite fields code wouldn't change in the future in such a way that other generators would be returned; or, for that matter, that the same version of Sage running on wildly different architectures won't return different generators.  I modified the docstrings a bit to (hopefully) make that more clear.\n\nNote that multiplicative_generator() calls pari's znprimroot(), so whatever fuzziness there is in pari's finding a generator gets automatically inherited by Sage.",
    "created_at": "2009-01-24T00:47:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3045#issuecomment-20926",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_3045.patch](tarball://root/attachments/some-uuid/ticket3045/trac_3045.patch) by @aghitza created at 2009-01-24 00:47:25

Kiran, I tried to find some examples and couldn't.  I think the point of the warning in the docstring is that we are not guaranteeing that the finite fields code wouldn't change in the future in such a way that other generators would be returned; or, for that matter, that the same version of Sage running on wildly different architectures won't return different generators.  I modified the docstrings a bit to (hopefully) make that more clear.

Note that multiplicative_generator() calls pari's znprimroot(), so whatever fuzziness there is in pari's finding a generator gets automatically inherited by Sage.



---

archive/issue_comments_020927.json:
```json
{
    "body": "Looks good to me.  I think the docstrings are clear enough.",
    "created_at": "2009-01-24T11:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3045#issuecomment-20927",
    "user": "https://github.com/roed314"
}
```

Looks good to me.  I think the docstrings are clear enough.



---

archive/issue_comments_020928.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-25T02:20:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3045#issuecomment-20928",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha2.

Cheers,

Michael



---

archive/issue_comments_020929.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-25T02:20:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3045#issuecomment-20929",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
