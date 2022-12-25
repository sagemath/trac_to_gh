# Issue 3492: [with patch, needs review] listing finite field embeddings

archive/issues_003492.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: finite field homomorphism\n\nThe attached patch adapts `sage/rings/number_field/morphism.py` so that the syntax for homorphisms of number fields also works for finite fields.  Thus\n\n```\nsage: End(GF(125, 'a')).list()\n\n[\nRing endomorphism of Finite Field in a of size 5^3\n  Defn: a |--> a,\nRing endomorphism of Finite Field in a of size 5^3\n  Defn: a |--> 3*a^2 + 1,\nRing endomorphism of Finite Field in a of size 5^3\n  Defn: a |--> 2*a^2 + 4*a + 4\n]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3492\n\n",
    "created_at": "2008-06-22T22:44:09Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with patch, needs review] listing finite field embeddings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3492",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```
Assignee: tbd

Keywords: finite field homomorphism

The attached patch adapts `sage/rings/number_field/morphism.py` so that the syntax for homorphisms of number fields also works for finite fields.  Thus

```
sage: End(GF(125, 'a')).list()

[
Ring endomorphism of Finite Field in a of size 5^3
  Defn: a |--> a,
Ring endomorphism of Finite Field in a of size 5^3
  Defn: a |--> 3*a^2 + 1,
Ring endomorphism of Finite Field in a of size 5^3
  Defn: a |--> 2*a^2 + 4*a + 4
]
```


Issue created by migration from https://trac.sagemath.org/ticket/3492





---

archive/issue_comments_024544.json:
```json
{
    "body": "Attachment [trac-3493.patch](tarball://root/attachments/some-uuid/ticket3492/trac-3493.patch) by fwclarke created at 2008-06-22 22:45:14",
    "created_at": "2008-06-22T22:45:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3492#issuecomment-24544",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Attachment [trac-3493.patch](tarball://root/attachments/some-uuid/ticket3492/trac-3493.patch) by fwclarke created at 2008-06-22 22:45:14



---

archive/issue_comments_024545.json:
```json
{
    "body": "This is a nice patch. Some issues still to address:\n\n* More doctests please! Still a lot of functions don't have doctests.\n* There's some irrelevant stuff that got copied from the number field case, like the \"H = Hom(ZZ, QQ)\" test, which should be deleted\n* I want to see doctests showing the list of embeddings from a finite field into a larger finite field\n* I want to see doctests showing that there are no embeddings when the characteristics are unequal\n* I want to see doctests showing how to *apply* the homomorphisms to elements of the domain\n* I want to see doctests covering the degenerate case where the domain is the prime field\n* the patch filename is confusing, it has the wrong ticket number :-)",
    "created_at": "2008-06-24T01:12:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3492#issuecomment-24545",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

This is a nice patch. Some issues still to address:

* More doctests please! Still a lot of functions don't have doctests.
* There's some irrelevant stuff that got copied from the number field case, like the "H = Hom(ZZ, QQ)" test, which should be deleted
* I want to see doctests showing the list of embeddings from a finite field into a larger finite field
* I want to see doctests showing that there are no embeddings when the characteristics are unequal
* I want to see doctests showing how to *apply* the homomorphisms to elements of the domain
* I want to see doctests covering the degenerate case where the domain is the prime field
* the patch filename is confusing, it has the wrong ticket number :-)



---

archive/issue_comments_024546.json:
```json
{
    "body": "Attachment [sage-3492-replacement.patch](tarball://root/attachments/some-uuid/ticket3492/sage-3492-replacement.patch) by fwclarke created at 2008-06-25 06:53:20\n\nI've  added several doctests covering the points made by dmharvey.  And \nI've introduced an index function; if you can do `End(GF(27, 'a'))[0]`, \nthen it should also be possible to do the opposite.\n\nAll this is now included in a replacement for the previous patch.  (It has a more appropriate \nname!)",
    "created_at": "2008-06-25T06:53:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3492#issuecomment-24546",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Attachment [sage-3492-replacement.patch](tarball://root/attachments/some-uuid/ticket3492/sage-3492-replacement.patch) by fwclarke created at 2008-06-25 06:53:20

I've  added several doctests covering the points made by dmharvey.  And 
I've introduced an index function; if you can do `End(GF(27, 'a'))[0]`, 
then it should also be possible to do the opposite.

All this is now included in a replacement for the previous patch.  (It has a more appropriate 
name!)



---

archive/issue_comments_024547.json:
```json
{
    "body": "Hi,\n\nI am in the middle of moving apartments so I won't get back to this for at least a week. If someone else wants to take over in the meantime, please go ahead.",
    "created_at": "2008-06-25T11:11:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3492#issuecomment-24547",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Hi,

I am in the middle of moving apartments so I won't get back to this for at least a week. If someone else wants to take over in the meantime, please go ahead.



---

archive/issue_comments_024548.json:
```json
{
    "body": "Excellent.",
    "created_at": "2008-07-02T21:15:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3492#issuecomment-24548",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Excellent.



---

archive/issue_comments_024549.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-03T02:15:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3492#issuecomment-24549",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_024550.json:
```json
{
    "body": "Merged sage-3492-replacement.patch in Sage 3.0.4.alpha2",
    "created_at": "2008-07-03T02:15:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3492#issuecomment-24550",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged sage-3492-replacement.patch in Sage 3.0.4.alpha2
