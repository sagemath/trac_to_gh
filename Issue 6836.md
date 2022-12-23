# Issue 6836: The Sturm bound for modular forms gives the wrong result sometimes

archive/issues_006836.json:
```json
{
    "body": "Assignee: craigcitro\n\nIn the documentation for the Sturm bound, the following appears:\n\n\"Kevin Buzzard pointed out to me (William Stein) in Fall 2002 that the above bound is fine for Gamma1 with character, as one sees by taking a power of `f`. More precisely, if `fcong 0pmod{p}` for first `s` coefficients, then `f^r = 0 pmod{p}` for first `s r` coefficients. Since the weight of `f^r` is `r weight(f)`, it follows that if `s >=` the sturm bound for `Gamma_0` at weight(f), then `f^r` has valuation large enough to be forced to be `0` at `r *` weight(f) by Sturm bound (which is valid if we choose `r` right). Thus `f cong 0 pmod{p}`. Conclusion: For `Gamma_1` with fixed character, the Sturm bound is *exactly* the same as for           `Gamma_0`. \"\n\nHowever, this does not seem to be the case:\n\n\n```\nsage: CuspForms(DG144.1^2,3).sturm_bound()\n3457\nsage: CuspForms(Gamma0(144),3).sturm_bound()\n73\n```\n\n\nI believe that this is due to the following code in the `sturm_bound` method for modular forms:\n\n\n```\nif M is not None:\n            raise NotImplementedError\n        if self.__sturm_bound is None:\n            # the +1 below is because O(q^prec) has precision prec.\n            self.__sturm_bound =      self.group().sturm_bound(self.weight())+1\n        return self.__sturm_bound\n\n```\n\nwhere `self.group()' gives the wrong answer in the case of `Gamma_1` with fixed character, because it returns `Gamma_1` rather than `Gamma_0`.\n\nI propose that the code above should be of the form\n\n```\nif M is not None:\n            raise NotImplementedError\n        if self.__sturm_bound is None:\n            # the +1 below is because O(q^prec) has precision prec.\n            G=self.group()\n            if G=Gamma1(G.level()) and self.character() in DirichletGroup(self.level()):\n                G=Gamma0(G.level())\n            self.__sturm_bound = G.sturm_bound(self.weight())+1\n        return self.__sturm_bound\n```\n\nbefore the sturm_bound variable is set, which would implement the remark of Buzzard given above.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6836\n\n",
    "created_at": "2009-08-28T14:21:35Z",
    "labels": [
        "modular forms",
        "minor",
        "bug"
    ],
    "title": "The Sturm bound for modular forms gives the wrong result sometimes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6836",
    "user": "ljpk"
}
```
Assignee: craigcitro

In the documentation for the Sturm bound, the following appears:

"Kevin Buzzard pointed out to me (William Stein) in Fall 2002 that the above bound is fine for Gamma1 with character, as one sees by taking a power of `f`. More precisely, if `fcong 0pmod{p}` for first `s` coefficients, then `f^r = 0 pmod{p}` for first `s r` coefficients. Since the weight of `f^r` is `r weight(f)`, it follows that if `s >=` the sturm bound for `Gamma_0` at weight(f), then `f^r` has valuation large enough to be forced to be `0` at `r *` weight(f) by Sturm bound (which is valid if we choose `r` right). Thus `f cong 0 pmod{p}`. Conclusion: For `Gamma_1` with fixed character, the Sturm bound is *exactly* the same as for           `Gamma_0`. "

However, this does not seem to be the case:


```
sage: CuspForms(DG144.1^2,3).sturm_bound()
3457
sage: CuspForms(Gamma0(144),3).sturm_bound()
73
```


I believe that this is due to the following code in the `sturm_bound` method for modular forms:


```
if M is not None:
            raise NotImplementedError
        if self.__sturm_bound is None:
            # the +1 below is because O(q^prec) has precision prec.
            self.__sturm_bound =      self.group().sturm_bound(self.weight())+1
        return self.__sturm_bound

```

where `self.group()' gives the wrong answer in the case of `Gamma_1` with fixed character, because it returns `Gamma_1` rather than `Gamma_0`.

I propose that the code above should be of the form

```
if M is not None:
            raise NotImplementedError
        if self.__sturm_bound is None:
            # the +1 below is because O(q^prec) has precision prec.
            G=self.group()
            if G=Gamma1(G.level()) and self.character() in DirichletGroup(self.level()):
                G=Gamma0(G.level())
            self.__sturm_bound = G.sturm_bound(self.weight())+1
        return self.__sturm_bound
```

before the sturm_bound variable is set, which would implement the remark of Buzzard given above.

Issue created by migration from https://trac.sagemath.org/ticket/6836





---

archive/issue_comments_056362.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-03T11:59:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6836#issuecomment-56362",
    "user": "AlexGhitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_056363.json:
```json
{
    "body": "Changing keywords from \"\" to \"sturm bound character\".",
    "created_at": "2010-01-03T11:59:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6836#issuecomment-56363",
    "user": "AlexGhitza"
}
```

Changing keywords from "" to "sturm bound character".



---

archive/issue_comments_056364.json:
```json
{
    "body": "Implemented Lloyd's suggestion (with some changes to the code).  See the patch.",
    "created_at": "2010-01-03T11:59:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6836#issuecomment-56364",
    "user": "AlexGhitza"
}
```

Implemented Lloyd's suggestion (with some changes to the code).  See the patch.



---

archive/issue_comments_056365.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2010-01-03T11:59:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6836#issuecomment-56365",
    "user": "AlexGhitza"
}
```

Changing priority from minor to major.



---

archive/issue_comments_056366.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-01-03T11:59:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6836#issuecomment-56366",
    "user": "AlexGhitza"
}
```

Attachment



---

archive/issue_comments_056367.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-05T13:30:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6836#issuecomment-56367",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_056368.json:
```json
{
    "body": "Looks fine to me, and tests pass on 4.3.5 (with all the other patches in the positive_review pile already applied).",
    "created_at": "2010-04-05T13:30:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6836#issuecomment-56368",
    "user": "davidloeffler"
}
```

Looks fine to me, and tests pass on 4.3.5 (with all the other patches in the positive_review pile already applied).



---

archive/issue_comments_056369.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-04-15T05:34:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6836#issuecomment-56369",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_056370.json:
```json
{
    "body": "Here's a patch to make the docs build without error.",
    "created_at": "2010-04-15T05:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6836#issuecomment-56370",
    "user": "jhpalmieri"
}
```

Here's a patch to make the docs build without error.



---

archive/issue_comments_056371.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T05:57:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6836#issuecomment-56371",
    "user": "jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_056372.json:
```json
{
    "body": "Merged in 4.4.alpha0:\n\n- trac_6836.patch\n- trac_6836-trivial-doc.patch",
    "created_at": "2010-04-15T05:57:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6836#issuecomment-56372",
    "user": "jhpalmieri"
}
```

Merged in 4.4.alpha0:

- trac_6836.patch
- trac_6836-trivial-doc.patch
