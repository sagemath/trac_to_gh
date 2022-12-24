# Issue 8283: A better Carmichael lambda function

archive/issues_008283.json:
```json
{
    "body": "Assignee: mvngu\n\nReported by ylchapuy:\n\nHere is another implementation:\n\n {{{\n\n def carmichael_lambda(n):\n    n = Integer(n)\n\n    if n < 1:\n        raise ValueError(\"Input n must be a positive integer.\")\n\n    F = n.factor()\n    L = []\n\n    # first get rid of the even part\n    if n & 1 == 0:\n        e = F[0][1]\n        F = F[1:]\n        if e < 3:\n            e = e-1\n        else:\n            e = e-2\n        L.append(1<<e)\n\n    # then other prime factors\n    L += [ p**(k-1)*(p-1) for p,k in F]\n\n    # finish the job\n    return lcm(L)\n\n }}}\n\nThis is a bit faster than the current implementation and, if you replace lcm with sage.rings.integer.LCM_list, it is even faster.\n\nA bug with the current function is that the output is not always an integer: e.g., carmichael_lambda(16) is of type sage.rings.rational.Rational .\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8283\n\n",
    "created_at": "2010-02-16T16:36:13Z",
    "labels": [
        "cryptography",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "A better Carmichael lambda function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8283",
    "user": "wdj"
}
```
Assignee: mvngu

Reported by ylchapuy:

Here is another implementation:

 {{{

 def carmichael_lambda(n):
    n = Integer(n)

    if n < 1:
        raise ValueError("Input n must be a positive integer.")

    F = n.factor()
    L = []

    # first get rid of the even part
    if n & 1 == 0:
        e = F[0][1]
        F = F[1:]
        if e < 3:
            e = e-1
        else:
            e = e-2
        L.append(1<<e)

    # then other prime factors
    L += [ p**(k-1)*(p-1) for p,k in F]

    # finish the job
    return lcm(L)

 }}}

This is a bit faster than the current implementation and, if you replace lcm with sage.rings.integer.LCM_list, it is even faster.

A bug with the current function is that the output is not always an integer: e.g., carmichael_lambda(16) is of type sage.rings.rational.Rational .


Issue created by migration from https://trac.sagemath.org/ticket/8283





---

archive/issue_comments_073333.json:
```json
{
    "body": "based on 4.3.3",
    "created_at": "2010-03-01T10:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8283#issuecomment-73333",
    "user": "ylchapuy"
}
```

based on 4.3.3



---

archive/issue_comments_073334.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-01T10:10:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8283#issuecomment-73334",
    "user": "ylchapuy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073335.json:
```json
{
    "body": "Attachment [trac_8283-improve_carmichael_lambda.patch](tarball://root/attachments/some-uuid/ticket8283/trac_8283-improve_carmichael_lambda.patch) by ylchapuy created at 2010-03-01 10:10:29\n\nI don't use `sage.rings.integer.LCM_list` because I think it's less readable.",
    "created_at": "2010-03-01T10:10:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8283#issuecomment-73335",
    "user": "ylchapuy"
}
```

Attachment [trac_8283-improve_carmichael_lambda.patch](tarball://root/attachments/some-uuid/ticket8283/trac_8283-improve_carmichael_lambda.patch) by ylchapuy created at 2010-03-01 10:10:29

I don't use `sage.rings.integer.LCM_list` because I think it's less readable.



---

archive/issue_comments_073336.json:
```json
{
    "body": "Applies okay to 10.26.2 mac and passes sage -testall.\n\nOkay with me. Minh, what do you think?",
    "created_at": "2010-03-02T21:41:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8283#issuecomment-73336",
    "user": "wdj"
}
```

Applies okay to 10.26.2 mac and passes sage -testall.

Okay with me. Minh, what do you think?



---

archive/issue_comments_073337.json:
```json
{
    "body": "apply on top of previous one",
    "created_at": "2010-03-03T13:21:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8283#issuecomment-73337",
    "user": "mvngu"
}
```

apply on top of previous one



---

archive/issue_comments_073338.json:
```json
{
    "body": "Attachment [trac_8283-reviewer.patch](tarball://root/attachments/some-uuid/ticket8283/trac_8283-reviewer.patch) by mvngu created at 2010-03-03 13:38:24\n\nReplying to [comment:2 wdj]:\n> Okay with me. Minh, what do you think?\n\nI agree with Yann's rewrite. It's much more compact than the previous version. However, I have attached the reviewer patch [trac_8283-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8283/trac_8283-reviewer.patch), whose changes include:\n\n* Remove the import statements\n {{{\nfrom sage.rings.arith import factor\nfrom sage.structure.element import generic_power\n }}}\n These import statements are no longer required due to Yann's rewrite of the Carmichael lambda function.\n* Move the import statement\n {{{\nimport sage.rings.integer\n }}}\n to the module preamble, so that it now reads\n {{{\nfrom sage.rings.integer import Integer\n }}}\n This has the effect of importing only what is required, i.e. the class `Integer`, instead of importing the whole module `sage.rings.integer`.\n* Some typo fixes.\n* Clean up \u00e0 la [PEP8](http://www.python.org/dev/peps/pep-0008/).\n* Removing a redundant `lambda` construct by replacing\n {{{\nlambda x: int(x)\n }}}\n with the more compact\n {{{\nint\n }}}\n\nOnly my patch needs review by anyone but me. If it's OK, then the whole ticket gets a positive review.",
    "created_at": "2010-03-03T13:38:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8283#issuecomment-73338",
    "user": "mvngu"
}
```

Attachment [trac_8283-reviewer.patch](tarball://root/attachments/some-uuid/ticket8283/trac_8283-reviewer.patch) by mvngu created at 2010-03-03 13:38:24

Replying to [comment:2 wdj]:
> Okay with me. Minh, what do you think?

I agree with Yann's rewrite. It's much more compact than the previous version. However, I have attached the reviewer patch [trac_8283-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8283/trac_8283-reviewer.patch), whose changes include:

* Remove the import statements
 {{{
from sage.rings.arith import factor
from sage.structure.element import generic_power
 }}}
 These import statements are no longer required due to Yann's rewrite of the Carmichael lambda function.
* Move the import statement
 {{{
import sage.rings.integer
 }}}
 to the module preamble, so that it now reads
 {{{
from sage.rings.integer import Integer
 }}}
 This has the effect of importing only what is required, i.e. the class `Integer`, instead of importing the whole module `sage.rings.integer`.
* Some typo fixes.
* Clean up à la [PEP8](http://www.python.org/dev/peps/pep-0008/).
* Removing a redundant `lambda` construct by replacing
 {{{
lambda x: int(x)
 }}}
 with the more compact
 {{{
int
 }}}

Only my patch needs review by anyone but me. If it's OK, then the whole ticket gets a positive review.



---

archive/issue_comments_073339.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-04T01:17:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8283#issuecomment-73339",
    "user": "wdj"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073340.json:
```json
{
    "body": "I read this over - looks good. I also installed it on top of the previous patch - passed sage -t devel/sage/sage/crypto/util.py. Is that enough, or it sage -testall necessary? If that is okay, positive review from me.",
    "created_at": "2010-03-04T01:17:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8283#issuecomment-73340",
    "user": "wdj"
}
```

I read this over - looks good. I also installed it on top of the previous patch - passed sage -t devel/sage/sage/crypto/util.py. Is that enough, or it sage -testall necessary? If that is okay, positive review from me.



---

archive/issue_comments_073341.json:
```json
{
    "body": "Replying to [comment:4 wdj]:\n> I read this over - looks good. I also installed it on top of the previous patch - passed sage -t devel/sage/sage/crypto/util.py. Is that enough, or it sage -testall necessary?\n\nRunning all doctests in the cryptography module subdirectory would be nice. Something like:\n\n```\n./sage -t -long devel/sage-main/sage/crypto/\n```\n\nThe module `sage/crypto/util.py` is at least used by the Blum-Goldwasser class under `sage/crypto/public_key/`. So naturally one would like to know how the above two patches would affect any other modules under the cryptography subdirectory.",
    "created_at": "2010-03-04T01:31:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8283#issuecomment-73341",
    "user": "mvngu"
}
```

Replying to [comment:4 wdj]:
> I read this over - looks good. I also installed it on top of the previous patch - passed sage -t devel/sage/sage/crypto/util.py. Is that enough, or it sage -testall necessary?

Running all doctests in the cryptography module subdirectory would be nice. Something like:

```
./sage -t -long devel/sage-main/sage/crypto/
```

The module `sage/crypto/util.py` is at least used by the Blum-Goldwasser class under `sage/crypto/public_key/`. So naturally one would like to know how the above two patches would affect any other modules under the cryptography subdirectory.



---

archive/issue_comments_073342.json:
```json
{
    "body": "Done. All tests passed!",
    "created_at": "2010-03-04T01:46:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8283#issuecomment-73342",
    "user": "wdj"
}
```

Done. All tests passed!



---

archive/issue_comments_073343.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-06T08:36:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8283#issuecomment-73343",
    "user": "mhansen"
}
```

Resolution: fixed
