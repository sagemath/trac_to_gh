# Issue 6763: [with patch, needs review]  Bin Packing (uses Linear Programming)

archive/issues_006763.json:
```json
{
    "body": "Assignee: jkantor\n\nThis patch implements a solver for the Bin Packing problem using Linear Programming.. Sorry again, but to test this you will have to first install GLPK (just type sage -i glpk 4.38) and the patch AllMIP #6502 ;-)\n\nI hope you will like the documentation, I tried to make it clean ;-)\n\nIssue created by migration from https://trac.sagemath.org/ticket/6763\n\n",
    "created_at": "2009-08-16T16:14:34Z",
    "labels": [
        "component: numerical"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "[with patch, needs review]  Bin Packing (uses Linear Programming)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6763",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: jkantor

This patch implements a solver for the Bin Packing problem using Linear Programming.. Sorry again, but to test this you will have to first install GLPK (just type sage -i glpk 4.38) and the patch AllMIP #6502 ;-)

I hope you will like the documentation, I tried to make it clean ;-)

Issue created by migration from https://trac.sagemath.org/ticket/6763





---

archive/issue_comments_055573.json:
```json
{
    "body": "As the functions dealing with LP have not been reviewed, I prefer to rewrite the MIP class for Sage to make it easier to use. I will post a new version of the MIP patch as soon as possible, along with all the patches for functions using it.\n\nSorry for the trouble, I'll try to make it quick !\n\nNathann",
    "created_at": "2009-08-31T15:55:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6763#issuecomment-55573",
    "user": "https://github.com/nathanncohen"
}
```

As the functions dealing with LP have not been reviewed, I prefer to rewrite the MIP class for Sage to make it easier to use. I will post a new version of the MIP patch as soon as possible, along with all the patches for functions using it.

Sorry for the trouble, I'll try to make it quick !

Nathann



---

archive/issue_comments_055574.json:
```json
{
    "body": "New version, ready for review !!!!\n\nNathann",
    "created_at": "2009-09-06T16:56:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6763#issuecomment-55574",
    "user": "https://github.com/nathanncohen"
}
```

New version, ready for review !!!!

Nathann



---

archive/issue_comments_055575.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-20T10:13:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6763#issuecomment-55575",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_055576.json:
```json
{
    "body": "What is the output format? You should include several more examples. Also, unless success returns True, it's better to raise an error on failure than return False.",
    "created_at": "2010-01-20T10:13:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6763#issuecomment-55576",
    "user": "https://github.com/robertwb"
}
```

What is the output format? You should include several more examples. Also, unless success returns True, it's better to raise an error on failure than return False.



---

archive/issue_comments_055577.json:
```json
{
    "body": "updated... This patch was 5 months old and was not working anymore ;-)\n\nNathann",
    "created_at": "2010-01-21T14:27:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6763#issuecomment-55577",
    "user": "https://github.com/nathanncohen"
}
```

updated... This patch was 5 months old and was not working anymore ;-)

Nathann



---

archive/issue_comments_055578.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-21T14:27:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6763#issuecomment-55578",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_055579.json:
```json
{
    "body": "Thanks, that clarifies things more. I would raise a ValueError rather than a generic exception. Also, you still need more examples. (You never actually even show the output.)",
    "created_at": "2010-01-21T20:07:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6763#issuecomment-55579",
    "user": "https://github.com/robertwb"
}
```

Thanks, that clarifies things more. I would raise a ValueError rather than a generic exception. Also, you still need more examples. (You never actually even show the output.)



---

archive/issue_comments_055580.json:
```json
{
    "body": "Well, maybe you can help me for the output : I deliberately avoided to show it as a valid solution [A,B] could be returned [B, A], for example... It depends on the solvers you use, but also on the platform (hashing functions depend on it, I learnt that recently from William and it was breaking som eof my docstring). How do you think we could avoid it ? :-)\n\nNathann",
    "created_at": "2010-01-22T06:59:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6763#issuecomment-55580",
    "user": "https://github.com/nathanncohen"
}
```

Well, maybe you can help me for the output : I deliberately avoided to show it as a valid solution [A,B] could be returned [B, A], for example... It depends on the solvers you use, but also on the platform (hashing functions depend on it, I learnt that recently from William and it was breaking som eof my docstring). How do you think we could avoid it ? :-)

Nathann



---

archive/issue_comments_055581.json:
```json
{
    "body": "Sort the result before printing.",
    "created_at": "2010-01-22T07:28:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6763#issuecomment-55581",
    "user": "https://github.com/robertwb"
}
```

Sort the result before printing.



---

archive/issue_comments_055582.json:
```json
{
    "body": "Done",
    "created_at": "2010-01-22T08:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6763#issuecomment-55582",
    "user": "https://github.com/nathanncohen"
}
```

Done



---

archive/issue_comments_055583.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-11T09:49:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6763#issuecomment-55583",
    "user": "https://trac.sagemath.org/admin/accounts/users/jsyri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_055584.json:
```json
{
    "body": "Attachment [binpacking.patch](tarball://root/attachments/some-uuid/ticket6763/binpacking.patch) by jsyri created at 2010-05-11 09:49:26\n\nI think check should be added to make sure all weights are <= max. At the moment\n\n\n```\nbinpacking([1,2,3],2)\n```\n\ncauses infinite loop. Otherwise code seems fine.",
    "created_at": "2010-05-11T09:49:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6763#issuecomment-55584",
    "user": "https://trac.sagemath.org/admin/accounts/users/jsyri"
}
```

Attachment [binpacking.patch](tarball://root/attachments/some-uuid/ticket6763/binpacking.patch) by jsyri created at 2010-05-11 09:49:26

I think check should be added to make sure all weights are <= max. At the moment


```
binpacking([1,2,3],2)
```

causes infinite loop. Otherwise code seems fine.



---

archive/issue_comments_055585.json:
```json
{
    "body": "Patch updated !! With a few other modifications, as this patch is one of the first LP patches Trac received, and is even older than the 8 months this ticket indicates... I'm not sorry to see it finally reviewed ! :-)\n\nBy the way, if you like Linear Programming and have some time to spend on trac tickets... I desperately need some help with LP patches in the Graph Theory section ;-)\n\nThank you very much !\n\nNathann",
    "created_at": "2010-05-11T21:00:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6763#issuecomment-55585",
    "user": "https://github.com/nathanncohen"
}
```

Patch updated !! With a few other modifications, as this patch is one of the first LP patches Trac received, and is even older than the 8 months this ticket indicates... I'm not sorry to see it finally reviewed ! :-)

By the way, if you like Linear Programming and have some time to spend on trac tickets... I desperately need some help with LP patches in the Graph Theory section ;-)

Thank you very much !

Nathann



---

archive/issue_comments_055586.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-11T21:00:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6763#issuecomment-55586",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_055587.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-12T11:07:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6763#issuecomment-55587",
    "user": "https://trac.sagemath.org/admin/accounts/users/jsyri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_055588.json:
```json
{
    "body": "One last thing, I'm sorry I didn't catch it first time around. Documentation for the parameter 'k'  claims function will return false if solution doesn't exist. Instead exception is raised if no solution exists.",
    "created_at": "2010-05-12T11:07:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6763#issuecomment-55588",
    "user": "https://trac.sagemath.org/admin/accounts/users/jsyri"
}
```

One last thing, I'm sorry I didn't catch it first time around. Documentation for the parameter 'k'  claims function will return false if solution doesn't exist. Instead exception is raised if no solution exists.



---

archive/issue_comments_055589.json:
```json
{
    "body": "Fixed.",
    "created_at": "2010-05-12T17:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6763#issuecomment-55589",
    "user": "https://github.com/nathanncohen"
}
```

Fixed.



---

archive/issue_comments_055590.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-12T17:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6763#issuecomment-55590",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_055591.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-12T18:03:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6763#issuecomment-55591",
    "user": "https://trac.sagemath.org/admin/accounts/users/jsyri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_055592.json:
```json
{
    "body": "Attachment [trac_6763.patch](tarball://root/attachments/some-uuid/ticket6763/trac_6763.patch) by jsyri created at 2010-05-12 18:03:38\n\nEverything seems to be in order. Positive review.",
    "created_at": "2010-05-12T18:03:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6763#issuecomment-55592",
    "user": "https://trac.sagemath.org/admin/accounts/users/jsyri"
}
```

Attachment [trac_6763.patch](tarball://root/attachments/some-uuid/ticket6763/trac_6763.patch) by jsyri created at 2010-05-12 18:03:38

Everything seems to be in order. Positive review.



---

archive/issue_comments_055593.json:
```json
{
    "body": "Thank youuuuuuuuu :-)\n\nNathann",
    "created_at": "2010-05-12T18:09:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6763#issuecomment-55593",
    "user": "https://github.com/nathanncohen"
}
```

Thank youuuuuuuuu :-)

Nathann



---

archive/issue_comments_055594.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-07T04:52:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6763#issuecomment-55594",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
