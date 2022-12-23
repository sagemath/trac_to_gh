# Issue 6124: Bug in galois_group of a p-adic field extension

archive/issues_006124.json:
```json
{
    "body": "Assignee: was\n\nKeywords: p-adic\n\nA bug in the implementation of p-adic groups.\n\nsage: K.<a> = Qp(2).extension(x^3 + x^2+1)\nsage: K.galois_group()\n---------------------------------------------------------------------------\nImportError                               Traceback (most recent call last)\n\n/Users/jeromelefebvre/.sage/temp/Jerome.local/23278/_Users_jeromelefebvre__sage_init_sage_0.py in <module>()\n\n/Applications/sage/local/lib/python2.5/site-packages/sage/rings/padics/unramified_extension_generic.pyc in galois_group(self)\n     96         ## doing this.\n     97         ##\n---> 98         from sage.groups.perm_gps.permgroup import CyclicPermutationGroup\n     99         return CyclicPermutationGroup(self.modulus().degree())\n    100 \n\nImportError: cannot import name CyclicPermutationGroup\n\n\nWhile, CyclicPermutationGroup does work fine on my machine.\nsage: G=CyclicPermutationGroup(2)\nsage: G.list()\n[(), (1,2)]\n\nIssue created by migration from https://trac.sagemath.org/ticket/6124\n\n",
    "created_at": "2009-05-24T14:41:03Z",
    "labels": [
        "number theory",
        "minor",
        "bug"
    ],
    "title": "Bug in galois_group of a p-adic field extension",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6124",
    "user": "jlefebvre"
}
```
Assignee: was

Keywords: p-adic

A bug in the implementation of p-adic groups.

sage: K.<a> = Qp(2).extension(x^3 + x^2+1)
sage: K.galois_group()
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)

/Users/jeromelefebvre/.sage/temp/Jerome.local/23278/_Users_jeromelefebvre__sage_init_sage_0.py in <module>()

/Applications/sage/local/lib/python2.5/site-packages/sage/rings/padics/unramified_extension_generic.pyc in galois_group(self)
     96         ## doing this.
     97         ##
---> 98         from sage.groups.perm_gps.permgroup import CyclicPermutationGroup
     99         return CyclicPermutationGroup(self.modulus().degree())
    100 

ImportError: cannot import name CyclicPermutationGroup


While, CyclicPermutationGroup does work fine on my machine.
sage: G=CyclicPermutationGroup(2)
sage: G.list()
[(), (1,2)]

Issue created by migration from https://trac.sagemath.org/ticket/6124





---

archive/issue_comments_048932.json:
```json
{
    "body": "Changing assignee from was to roed.",
    "created_at": "2009-05-25T01:53:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6124#issuecomment-48932",
    "user": "AlexGhitza"
}
```

Changing assignee from was to roed.



---

archive/issue_comments_048933.json:
```json
{
    "body": "Changing component from number theory to padics.",
    "created_at": "2009-05-25T01:53:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6124#issuecomment-48933",
    "user": "AlexGhitza"
}
```

Changing component from number theory to padics.



---

archive/issue_comments_048934.json:
```json
{
    "body": "Note that in sage-4.0.rc0, there is no `galois_group` method for an extension of `Qp`:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: K.<a> = Qp(2).extension(x^3 + x^2+1)\nsage: K.g    # tried to tab-complete here:\nK.gcd                   K.gens                  K.get_action            K.get_action_impl       K.ground_ring_of_tower  \nK.gen                   K.gens_dict             K.get_action_c          K.ground_ring           \n```\n",
    "created_at": "2009-05-25T01:53:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6124#issuecomment-48934",
    "user": "AlexGhitza"
}
```

Note that in sage-4.0.rc0, there is no `galois_group` method for an extension of `Qp`:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: K.<a> = Qp(2).extension(x^3 + x^2+1)
sage: K.g    # tried to tab-complete here:
K.gcd                   K.gens                  K.get_action            K.get_action_impl       K.ground_ring_of_tower  
K.gen                   K.gens_dict             K.get_action_c          K.ground_ring           
```




---

archive/issue_comments_048935.json:
```json
{
    "body": "Same thing for Sage 4.0.1. It would be cool if there was some galois group computations, but that's an other issue.\nSo, it looks like this trac should be closed.\nThanks for looking into it.",
    "created_at": "2009-06-11T15:01:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6124#issuecomment-48935",
    "user": "jlefebvre"
}
```

Same thing for Sage 4.0.1. It would be cool if there was some galois group computations, but that's an other issue.
So, it looks like this trac should be closed.
Thanks for looking into it.



---

archive/issue_comments_048936.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-11-09T03:21:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6124#issuecomment-48936",
    "user": "roed"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_048937.json:
```json
{
    "body": "This ticket should be closed.",
    "created_at": "2011-11-09T03:21:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6124#issuecomment-48937",
    "user": "roed"
}
```

This ticket should be closed.



---

archive/issue_comments_048938.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-11-19T04:25:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6124#issuecomment-48938",
    "user": "roed"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_048939.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2011-11-26T13:05:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6124#issuecomment-48939",
    "user": "jdemeyer"
}
```

Resolution: invalid
