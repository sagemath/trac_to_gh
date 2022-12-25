# Issue 8411: Branching rule fix and doc revision

archive/issues_008411.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat brant@math.ucdavis.edu\n\nThis corrects a minor problem with branching rules in weyl_characters.py.\n\nPreviously branching rules SO(m+n)->SO(m)xSO(n) were implemented using\nrule=\"extended\", and similarly for symplectic groups. However there is one\ncase where this does not meet the definition of the extended rule, namely\nSO(2n+2m+2)->SO(2n+1)xSO(2m+1). Indeed, the extended rule checks\nto see if the ranks are equal, which they are not in this case.\n\nI thought the cleanest fix was to implement a new rule called \"orthogonal_sum\"\nfor such cases.\n\nI also took the chance to revise the documentation since what was said\nbefore about rule=\"symmetric\" was misleading.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8411\n\n",
    "created_at": "2010-03-01T19:42:24Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Branching rule fix and doc revision",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8411",
    "user": "https://github.com/dwbump"
}
```
Assignee: sage-combinat

CC:  sage-combinat brant@math.ucdavis.edu

This corrects a minor problem with branching rules in weyl_characters.py.

Previously branching rules SO(m+n)->SO(m)xSO(n) were implemented using
rule="extended", and similarly for symplectic groups. However there is one
case where this does not meet the definition of the extended rule, namely
SO(2n+2m+2)->SO(2n+1)xSO(2m+1). Indeed, the extended rule checks
to see if the ranks are equal, which they are not in this case.

I thought the cleanest fix was to implement a new rule called "orthogonal_sum"
for such cases.

I also took the chance to revise the documentation since what was said
before about rule="symmetric" was misleading.

Issue created by migration from https://trac.sagemath.org/ticket/8411





---

archive/issue_comments_075230.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-01T19:45:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8411#issuecomment-75230",
    "user": "https://github.com/dwbump"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075231.json:
```json
{
    "body": "All test pass on 4.3.4 and, from a technical point of view, the patch\nlooks good.\n\nSo it is good to go as soon as someone more knowledgeable with\nbranching rules will have double check the mathematics? Well, of\ncourse, the expert is Dan :-) Maybe Brant?",
    "created_at": "2010-04-18T15:30:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8411#issuecomment-75231",
    "user": "https://github.com/nthiery"
}
```

All test pass on 4.3.4 and, from a technical point of view, the patch
looks good.

So it is good to go as soon as someone more knowledgeable with
branching rules will have double check the mathematics? Well, of
course, the expert is Dan :-) Maybe Brant?



---

archive/issue_comments_075232.json:
```json
{
    "body": "Changing keywords from \"\" to \"Branching rules\".",
    "created_at": "2010-04-18T15:34:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8411#issuecomment-75232",
    "user": "https://github.com/nthiery"
}
```

Changing keywords from "" to "Branching rules".



---

archive/issue_comments_075233.json:
```json
{
    "body": "jhpalmieri objected in #8414 to the fact that the patch there did not contain\nmercurial headers information.\n\nI therefore remade this patch. There is no change to the content of the patch.",
    "created_at": "2010-04-18T17:32:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8411#issuecomment-75233",
    "user": "https://github.com/dwbump"
}
```

jhpalmieri objected in #8414 to the fact that the patch there did not contain
mercurial headers information.

I therefore remade this patch. There is no change to the content of the patch.



---

archive/issue_comments_075234.json:
```json
{
    "body": "Please also include the ticket number in the patch title!\n\n#8411: Branching rule fix and doc revision\n\nSorry for the extra bother ...",
    "created_at": "2010-04-18T17:44:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8411#issuecomment-75234",
    "user": "https://github.com/nthiery"
}
```

Please also include the ticket number in the patch title!

#8411: Branching rule fix and doc revision

Sorry for the extra bother ...



---

archive/issue_comments_075235.json:
```json
{
    "body": "Branching rule fix and revised doc in weyl_characters.py",
    "created_at": "2010-04-19T01:29:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8411#issuecomment-75235",
    "user": "https://github.com/dwbump"
}
```

Branching rule fix and revised doc in weyl_characters.py



---

archive/issue_comments_075236.json:
```json
{
    "body": "Attachment [trac_8411_branching_rules.patch](tarball://root/attachments/some-uuid/ticket8411/trac_8411_branching_rules.patch) by @dwbump created at 2010-04-19 01:31:11\n\n> Please also include the ticket number in the patch title!\n>\n> #8411: Branching rule fix and doc revision\n>\n> Sorry for the extra bother ...\n\nOK, I changed the patch description to begin #8411.",
    "created_at": "2010-04-19T01:31:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8411#issuecomment-75236",
    "user": "https://github.com/dwbump"
}
```

Attachment [trac_8411_branching_rules.patch](tarball://root/attachments/some-uuid/ticket8411/trac_8411_branching_rules.patch) by @dwbump created at 2010-04-19 01:31:11

> Please also include the ticket number in the patch title!
>
> #8411: Branching rule fix and doc revision
>
> Sorry for the extra bother ...

OK, I changed the patch description to begin #8411.



---

archive/issue_comments_075237.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-20T16:32:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8411#issuecomment-75237",
    "user": "https://trac.sagemath.org/admin/accounts/users/brant.c.jones"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075238.json:
```json
{
    "body": "This is a positive review for trac_8411.\n\nPrior to this patch, sage would not branch e.g. SO(3) x SO(3) -> SO(6) because this would embed a rank 2 group in a rank 3 group, and the get_branching_rule() code required the ranks to be equal.  After applying this patch, the \"orthogonal_sum\" rule will allow such branching (as the identity map) between types B/D, and within type C (only).\n\nThis patch correctly implements useful mathematics.\n\n-- Brant Jones",
    "created_at": "2010-04-20T16:32:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8411#issuecomment-75238",
    "user": "https://trac.sagemath.org/admin/accounts/users/brant.c.jones"
}
```

This is a positive review for trac_8411.

Prior to this patch, sage would not branch e.g. SO(3) x SO(3) -> SO(6) because this would embed a rank 2 group in a rank 3 group, and the get_branching_rule() code required the ranks to be equal.  After applying this patch, the "orthogonal_sum" rule will allow such branching (as the identity map) between types B/D, and within type C (only).

This patch correctly implements useful mathematics.

-- Brant Jones



---

archive/issue_comments_075239.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-23T17:10:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8411#issuecomment-75239",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_075240.json:
```json
{
    "body": "Merged into 4.4.alpha2.",
    "created_at": "2010-04-23T17:10:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8411#issuecomment-75240",
    "user": "https://github.com/jhpalmieri"
}
```

Merged into 4.4.alpha2.
