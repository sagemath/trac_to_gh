# Issue 8630: Cusp forms constructor ignores the character and returns enormous space

archive/issues_008630.json:
```json
{
    "body": "Assignee: craigcitro\n\n\n```\nsage: chi = DirichletGroup(109, CyclotomicField(3)).0\nsage: CuspForms(chi, 2, base_ring = CyclotomicField(9))\nCuspidal subspace of dimension 442 of Modular Forms space of dimension 10, character [zeta3 + 1] and weight 2 over Cyclotomic Field of order 9 and degree6\n```\n\n\n*facepalm*\n\nIssue created by migration from https://trac.sagemath.org/ticket/8630\n\n",
    "created_at": "2010-03-30T11:37:41Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "title": "Cusp forms constructor ignores the character and returns enormous space",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8630",
    "user": "davidloeffler"
}
```
Assignee: craigcitro


```
sage: chi = DirichletGroup(109, CyclotomicField(3)).0
sage: CuspForms(chi, 2, base_ring = CyclotomicField(9))
Cuspidal subspace of dimension 442 of Modular Forms space of dimension 10, character [zeta3 + 1] and weight 2 over Cyclotomic Field of order 9 and degree6
```


*facepalm*

Issue created by migration from https://trac.sagemath.org/ticket/8630





---

archive/issue_comments_078245.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-30T15:32:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8630#issuecomment-78245",
    "user": "davidloeffler"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078246.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-30T16:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8630#issuecomment-78246",
    "user": "davidloeffler"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_078247.json:
```json
{
    "body": "*** wait, it's still wrong in certain nastly cases ***",
    "created_at": "2010-03-30T16:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8630#issuecomment-78247",
    "user": "davidloeffler"
}
```

*** wait, it's still wrong in certain nastly cases ***



---

archive/issue_comments_078248.json:
```json
{
    "body": "Attachment [trac_8630.patch](tarball://root/attachments/some-uuid/ticket8630/trac_8630.patch) by davidloeffler created at 2010-03-30 17:37:31",
    "created_at": "2010-03-30T17:37:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8630#issuecomment-78248",
    "user": "davidloeffler"
}
```

Attachment [trac_8630.patch](tarball://root/attachments/some-uuid/ticket8630/trac_8630.patch) by davidloeffler created at 2010-03-30 17:37:31



---

archive/issue_comments_078249.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-30T17:40:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8630#issuecomment-78249",
    "user": "davidloeffler"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_078250.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-03-30T18:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8630#issuecomment-78250",
    "user": "was"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_078251.json:
```json
{
    "body": "All doctests pass when this is applied against sage-4.3.5.",
    "created_at": "2010-03-31T01:48:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8630#issuecomment-78251",
    "user": "was"
}
```

All doctests pass when this is applied against sage-4.3.5.



---

archive/issue_comments_078252.json:
```json
{
    "body": "1. Below \"ring\" should be \"modular symbols space\":\n\n```\n \t117\t    def change_ring(self, R): \n \t118\t        r\"\"\" \n \t119\t        Return this ring with the base ring changed to the ring R. \n```\n\n\n2. Here I think the sentence should end with ::\n\n\n```\n \t419\t    A more complicated example involving both a nontrivial character, and a \n \t420\t    base field that is not minimal for that character: \n```\n\n\n\nIt's really awesome that you sphinxified a bunch of docs, in addition to fixing the bug in this ticket.",
    "created_at": "2010-03-31T05:02:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8630#issuecomment-78252",
    "user": "was"
}
```

1. Below "ring" should be "modular symbols space":

```
 	117	    def change_ring(self, R): 
 	118	        r""" 
 	119	        Return this ring with the base ring changed to the ring R. 
```


2. Here I think the sentence should end with ::


```
 	419	    A more complicated example involving both a nontrivial character, and a 
 	420	    base field that is not minimal for that character: 
```



It's really awesome that you sphinxified a bunch of docs, in addition to fixing the bug in this ticket.



---

archive/issue_comments_078253.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-31T05:02:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8630#issuecomment-78253",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078254.json:
```json
{
    "body": "Attachment [trac_8630_docfixes.patch](tarball://root/attachments/some-uuid/ticket8630/trac_8630_docfixes.patch) by davidloeffler created at 2010-03-31 11:07:37\n\napply over previous patch",
    "created_at": "2010-03-31T11:07:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8630#issuecomment-78254",
    "user": "davidloeffler"
}
```

Attachment [trac_8630_docfixes.patch](tarball://root/attachments/some-uuid/ticket8630/trac_8630_docfixes.patch) by davidloeffler created at 2010-03-31 11:07:37

apply over previous patch



---

archive/issue_comments_078255.json:
```json
{
    "body": "Here's a tiny patch that corrects the two things you pointed out in the docstrings.",
    "created_at": "2010-03-31T11:08:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8630#issuecomment-78255",
    "user": "davidloeffler"
}
```

Here's a tiny patch that corrects the two things you pointed out in the docstrings.



---

archive/issue_comments_078256.json:
```json
{
    "body": "Merged in 4.4.alpha0:\n- trac_8630.patch\n- trac_8630_docfixes.patch",
    "created_at": "2010-04-16T18:54:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8630#issuecomment-78256",
    "user": "jhpalmieri"
}
```

Merged in 4.4.alpha0:
- trac_8630.patch
- trac_8630_docfixes.patch



---

archive/issue_comments_078257.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-16T18:54:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8630#issuecomment-78257",
    "user": "jhpalmieri"
}
```

Resolution: fixed
