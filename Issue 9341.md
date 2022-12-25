# Issue 9341: K.S_units doesn't check for repeated entries

archive/issues_009341.json:
```json
{
    "body": "Assignee: @loefflerd\n\nCC:  @rlmill @robertwb\n\nKeywords: S_units\n\nHere is a stupid example:\n\n```\nsage: _.<t>=QQ[]\nsage: K.<T>=NumberField(t-1)\nsage: I = K.ideal(2)\nsage: K.S_units([I])\n[2, -1]\nsage: K.S_units([I, I])\n[2, 2, -1]\n```\n\nLooking at the code, this seems to be an upstream issue with gp as well.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9341\n\n",
    "created_at": "2010-06-25T20:54:29Z",
    "labels": [
        "component: number fields",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.2",
    "title": "K.S_units doesn't check for repeated entries",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9341",
    "user": "https://github.com/syazdani77"
}
```
Assignee: @loefflerd

CC:  @rlmill @robertwb

Keywords: S_units

Here is a stupid example:

```
sage: _.<t>=QQ[]
sage: K.<T>=NumberField(t-1)
sage: I = K.ideal(2)
sage: K.S_units([I])
[2, -1]
sage: K.S_units([I, I])
[2, 2, -1]
```

Looking at the code, this seems to be an upstream issue with gp as well.

Issue created by migration from https://trac.sagemath.org/ticket/9341





---

archive/issue_comments_088106.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-04-18T00:39:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9341#issuecomment-88106",
    "user": "https://github.com/aghitza"
}
```

New commits:



---

archive/issue_comments_088107.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-04-18T00:39:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9341#issuecomment-88107",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_088108.json:
```json
{
    "body": "It doesn't seem very robust to rely on a duplicate in the list of prime ideals yielding the *same* *S*-unit twice, rather than two (or more) different but linearly dependent *S*-units.  PARI's algorithm probably assumes that the input is a list of pairwise distinct prime ideals, so I would guess it is safer to apply `uniq()` to the input instead of the output.\n\n[Edit: it may even be wise to do this in `_S_class_group_and_units()`.]",
    "created_at": "2014-04-18T12:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9341#issuecomment-88108",
    "user": "https://github.com/pjbruin"
}
```

It doesn't seem very robust to rely on a duplicate in the list of prime ideals yielding the *same* *S*-unit twice, rather than two (or more) different but linearly dependent *S*-units.  PARI's algorithm probably assumes that the input is a list of pairwise distinct prime ideals, so I would guess it is safer to apply `uniq()` to the input instead of the output.

[Edit: it may even be wise to do this in `_S_class_group_and_units()`.]



---

archive/issue_comments_088109.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-04-18T22:25:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9341#issuecomment-88109",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_088110.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-04-18T22:28:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9341#issuecomment-88110",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_088111.json:
```json
{
    "body": "Peter is of course right.  I have modified the fix so that it uniq-fies the input list of primes instead, and I have put it into the helper function.\n\nSorry about this minor fix now being spread across 3 git commits, still getting the hang of the \"new\" workflow.  Is there a way to flatten the commits into one?  (After having pushed to the trac server?)",
    "created_at": "2014-04-18T22:31:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9341#issuecomment-88111",
    "user": "https://github.com/aghitza"
}
```

Peter is of course right.  I have modified the fix so that it uniq-fies the input list of primes instead, and I have put it into the helper function.

Sorry about this minor fix now being spread across 3 git commits, still getting the hang of the "new" workflow.  Is there a way to flatten the commits into one?  (After having pushed to the trac server?)



---

archive/issue_comments_088112.json:
```json
{
    "body": "It is not necessary to flatten the commits, imho. If you prefer less commits, you should rather flatten them before pushing to trac (for example using `git rebase -i develop`).",
    "created_at": "2014-04-20T09:00:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9341#issuecomment-88112",
    "user": "https://github.com/fchapoton"
}
```

It is not necessary to flatten the commits, imho. If you prefer less commits, you should rather flatten them before pushing to trac (for example using `git rebase -i develop`).



---

archive/issue_comments_088113.json:
```json
{
    "body": "OK, looks good and all tests pass.  The only comment I have is that `TEST:` should only have a single colon, since there is no doctest directly following it.\n\nIf you want to flatten the commits into one, the easiest way is `git reset develop` (this forgets that you have made the commits, but keeps the edits) followed by `git commit -a` and then do a forced push.  I agree that you shouldn't do this in general, but in this case I think it is fine; I don't expect people have already started to base new work on this.\n\nWhen you have done one or both of these things, feel free to set this to positive review.",
    "created_at": "2014-04-21T10:23:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9341#issuecomment-88113",
    "user": "https://github.com/pjbruin"
}
```

OK, looks good and all tests pass.  The only comment I have is that `TEST:` should only have a single colon, since there is no doctest directly following it.

If you want to flatten the commits into one, the easiest way is `git reset develop` (this forgets that you have made the commits, but keeps the edits) followed by `git commit -a` and then do a forced push.  I agree that you shouldn't do this in general, but in this case I think it is fine; I don't expect people have already started to base new work on this.

When you have done one or both of these things, feel free to set this to positive review.



---

archive/issue_comments_088114.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-04-22T22:12:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9341#issuecomment-88114",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_088115.json:
```json
{
    "body": "I fixed the docstring issue.",
    "created_at": "2014-04-22T22:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9341#issuecomment-88115",
    "user": "https://github.com/aghitza"
}
```

I fixed the docstring issue.



---

archive/issue_comments_088116.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-04-22T22:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9341#issuecomment-88116",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_088117.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-04-25T14:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9341#issuecomment-88117",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
