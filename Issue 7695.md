# Issue 7695: naming of the variable in subfields of cyclotomic fields

archive/issues_007695.json:
```json
{
    "body": "Assignee: @loefflerd\n\nKeywords: cyclotomic fields, subfields\n\n\n```\nsage: F = CyclotomicField(7)\nsage: K = F.subfields(3)[0][0]\nsage: K\nNumber Field in zeta70 with defining polynomial x^3 + x^2 - 2*x - 1\n```\n\n\nI think this convention of adding a 0 to the variable name, as nice and practicle as it is in general, is not good in this case. The resulting algebraic element is not a 70th root of unity as the name would suggest.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7695\n\n",
    "created_at": "2009-12-16T00:33:08Z",
    "labels": [
        "component: number fields",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.1",
    "title": "naming of the variable in subfields of cyclotomic fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7695",
    "user": "https://github.com/categorie"
}
```
Assignee: @loefflerd

Keywords: cyclotomic fields, subfields


```
sage: F = CyclotomicField(7)
sage: K = F.subfields(3)[0][0]
sage: K
Number Field in zeta70 with defining polynomial x^3 + x^2 - 2*x - 1
```


I think this convention of adding a 0 to the variable name, as nice and practicle as it is in general, is not good in this case. The resulting algebraic element is not a 70th root of unity as the name would suggest.

Issue created by migration from https://trac.sagemath.org/ticket/7695





---

archive/issue_comments_065900.json:
```json
{
    "body": "exported against 4.5.2.alpha1; but must be applied after #9407",
    "created_at": "2010-07-30T17:22:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7695#issuecomment-65900",
    "user": "https://github.com/categorie"
}
```

exported against 4.5.2.alpha1; but must be applied after #9407



---

archive/issue_comments_065901.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-30T17:24:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7695#issuecomment-65901",
    "user": "https://github.com/categorie"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065902.json:
```json
{
    "body": "Attachment [trac_7695.patch](tarball://root/attachments/some-uuid/ticket7695/trac_7695.patch) by @categorie created at 2010-07-30 17:24:15\n\nThis is ready for review but depends on #9407.\n\nOf course, this is not the only solution, but it eliminates the cases that bother me.",
    "created_at": "2010-07-30T17:24:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7695#issuecomment-65902",
    "user": "https://github.com/categorie"
}
```

Attachment [trac_7695.patch](tarball://root/attachments/some-uuid/ticket7695/trac_7695.patch) by @categorie created at 2010-07-30 17:24:15

This is ready for review but depends on #9407.

Of course, this is not the only solution, but it eliminates the cases that bother me.



---

archive/issue_comments_065903.json:
```json
{
    "body": "I rebased it and removed the useless dependency. This is really a trivial change.",
    "created_at": "2013-12-30T12:13:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7695#issuecomment-65903",
    "user": "https://github.com/categorie"
}
```

I rebased it and removed the useless dependency. This is really a trivial change.



---

archive/issue_comments_065904.json:
```json
{
    "body": "New commits:",
    "created_at": "2013-12-30T12:15:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7695#issuecomment-65904",
    "user": "https://github.com/categorie"
}
```

New commits:



---

archive/issue_comments_065905.json:
```json
{
    "body": "I think it would be better to add the underscore in all cases where the generator ends with a digit.",
    "created_at": "2013-12-30T12:34:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7695#issuecomment-65905",
    "user": "https://github.com/jdemeyer"
}
```

I think it would be better to add the underscore in all cases where the generator ends with a digit.



---

archive/issue_comments_065906.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-12-30T12:34:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7695#issuecomment-65906",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_065907.json:
```json
{
    "body": "I agree. Here is the change. I am running the tests now to see if there are any other corrections in the documentation to make.",
    "created_at": "2013-12-30T16:29:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7695#issuecomment-65907",
    "user": "https://github.com/categorie"
}
```

I agree. Here is the change. I am running the tests now to see if there are any other corrections in the documentation to make.



---

archive/issue_comments_065908.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2013-12-30T16:29:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7695#issuecomment-65908",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065909.json:
```json
{
    "body": "a little bit annoying that the push resets the dependency again. what did i do wrong ?",
    "created_at": "2013-12-30T16:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7695#issuecomment-65909",
    "user": "https://github.com/categorie"
}
```

a little bit annoying that the push resets the dependency again. what did i do wrong ?



---

archive/issue_comments_065910.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-12-30T19:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7695#issuecomment-65910",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_065911.json:
```json
{
    "body": "Replying to [comment:13 wuthrich]:\n> a little bit annoying that the push resets the dependency again. what did i do wrong ?\n`sage --dev` has its own local version of the dependencies.  I think that when the local and remote dependencies are different, it is supposed to ask if you want to upload or download the dependency list or to leave the two lists different.",
    "created_at": "2013-12-30T21:54:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7695#issuecomment-65911",
    "user": "https://github.com/pjbruin"
}
```

Replying to [comment:13 wuthrich]:
> a little bit annoying that the push resets the dependency again. what did i do wrong ?
`sage --dev` has its own local version of the dependencies.  I think that when the local and remote dependencies are different, it is supposed to ask if you want to upload or download the dependency list or to leave the two lists different.



---

archive/issue_comments_065912.json:
```json
{
    "body": "Patch looks good, running doctests now...",
    "created_at": "2013-12-31T10:13:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7695#issuecomment-65912",
    "user": "https://github.com/jdemeyer"
}
```

Patch looks good, running doctests now...



---

archive/issue_comments_065913.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-12-31T11:14:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7695#issuecomment-65913",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065914.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-01-05T00:32:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7695#issuecomment-65914",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
