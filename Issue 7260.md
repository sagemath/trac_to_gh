# Issue 7260: [with patch; needs review] Inverse mod number field ideals: deal with several remaining problems

archive/issues_007260.json:
```json
{
    "body": "Assignee: @loefflerd\n\nCC:  mtaranes @JohnCremona\n\nKeywords: inverse_mod\n\nAt present the function `inverse_mod` (which computes the inverse of \nelements of number fields modulo integral ideals) suffers from several \ndefects.\n\n1.  It does not work for elements of relative number fields, though it \ndoes for an element of the rings of integers of such a number field.\n\n2.  The behaviour is different depending whether the element's parent is \nthe number field or the maximal order.  Thus with 4.1.2:\n\n```\nsage: k.<a> = NumberField(x^3 + 11)\nsage: R = k.ring_of_integers()\nsage: (a + 13).inverse_mod(k.ideal(a^2))\n-3*a - 5\nsage: R(a + 13).inverse_mod(k.ideal(a^2))\n-123*a^2 + 8*a - 104\n```\n\nThis is because the field version of the function applies `small_residue` \nto the results of the computation, while the order versions do not.\nMoreover\n\n```\nsage: R(a + 13).inverse_mod(k.ideal(a^2)).parent() == k\nTrue\n```\n\nwhen it would make more sense if the inverse of an element of R was an \nelement of R.\n\n3.  Error messages are inconsistent.\n\nThe attached patch deals with these defects and also makes the code run a \nbit faster in some cases.  \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7260\n\n",
    "created_at": "2009-10-21T08:54:00Z",
    "labels": [
        "component: number fields",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "[with patch; needs review] Inverse mod number field ideals: deal with several remaining problems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7260",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```
Assignee: @loefflerd

CC:  mtaranes @JohnCremona

Keywords: inverse_mod

At present the function `inverse_mod` (which computes the inverse of 
elements of number fields modulo integral ideals) suffers from several 
defects.

1.  It does not work for elements of relative number fields, though it 
does for an element of the rings of integers of such a number field.

2.  The behaviour is different depending whether the element's parent is 
the number field or the maximal order.  Thus with 4.1.2:

```
sage: k.<a> = NumberField(x^3 + 11)
sage: R = k.ring_of_integers()
sage: (a + 13).inverse_mod(k.ideal(a^2))
-3*a - 5
sage: R(a + 13).inverse_mod(k.ideal(a^2))
-123*a^2 + 8*a - 104
```

This is because the field version of the function applies `small_residue` 
to the results of the computation, while the order versions do not.
Moreover

```
sage: R(a + 13).inverse_mod(k.ideal(a^2)).parent() == k
True
```

when it would make more sense if the inverse of an element of R was an 
element of R.

3.  Error messages are inconsistent.

The attached patch deals with these defects and also makes the code run a 
bit faster in some cases.  



Issue created by migration from https://trac.sagemath.org/ticket/7260





---

archive/issue_comments_060186.json:
```json
{
    "body": "Attachment [trac_7260.patch](tarball://root/attachments/some-uuid/ticket7260/trac_7260.patch) by fwclarke created at 2009-10-21 08:55:01",
    "created_at": "2009-10-21T08:55:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7260#issuecomment-60186",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Attachment [trac_7260.patch](tarball://root/attachments/some-uuid/ticket7260/trac_7260.patch) by fwclarke created at 2009-10-21 08:55:01



---

archive/issue_comments_060187.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-31T21:46:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7260#issuecomment-60187",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060188.json:
```json
{
    "body": "This looks good to me.  It applies fine to 4.3.alpha0 and all tests in rings/number_field pass.  I also tested modular/modsym since p1list_nf.py is one place where this code is used and that was fine too.",
    "created_at": "2009-11-22T17:26:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7260#issuecomment-60188",
    "user": "https://github.com/JohnCremona"
}
```

This looks good to me.  It applies fine to 4.3.alpha0 and all tests in rings/number_field pass.  I also tested modular/modsym since p1list_nf.py is one place where this code is used and that was fine too.



---

archive/issue_comments_060189.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-22T17:26:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7260#issuecomment-60189",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060190.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-29T05:12:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7260#issuecomment-60190",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
