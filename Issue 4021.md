# Issue 4021: [with patch, needs review] MPolynomial_libsingular over ZZ

archive/issues_004021.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @williamstein\n\nKeywords: libsingular, singular, ZZ, multivariate\n\nThere it is.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4021\n\n",
    "created_at": "2008-08-31T17:08:10Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "[with patch, needs review] MPolynomial_libsingular over ZZ",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4021",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  @williamstein

Keywords: libsingular, singular, ZZ, multivariate

There it is.

Issue created by migration from https://trac.sagemath.org/ticket/4021





---

archive/issue_comments_028940.json:
```json
{
    "body": "Attachment [mpolynomial_libsingular_zz.patch](tarball://root/attachments/some-uuid/ticket4021/mpolynomial_libsingular_zz.patch) by @malb created at 2008-08-31 17:09:27\n\nthe attached patch depends on #686",
    "created_at": "2008-08-31T17:09:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4021#issuecomment-28940",
    "user": "https://github.com/malb"
}
```

Attachment [mpolynomial_libsingular_zz.patch](tarball://root/attachments/some-uuid/ticket4021/mpolynomial_libsingular_zz.patch) by @malb created at 2008-08-31 17:09:27

the attached patch depends on #686



---

archive/issue_comments_028941.json:
```json
{
    "body": "On [sage-devel] Oliver Wienand (author of the upcoming Singular implementation for GBs over rings) wrote:\n\n> I have just glimpsed over the code. But maybe it is worth stating in\n> the comments, that the reduce impl. only returns unqiue answer against\n> strong Gr\u00f6bner basis.\n\n> Gr\u00f6bner basis G of I <=> the leading ideal of G generates all leading\n> terms of I\n> strong % of I <=> for every leading term t of I there exists an\n> element g of G, such that the leading term of g divides t.\n\n> (leading terms means coef * product of variables)\n\n> Otherwise the reduce code shown in\n> http://trac.sagemath.org/sage_trac/attachment/ticket/4021/mpolynomial_libsingular_zz.patch\n> looks fine.",
    "created_at": "2008-09-01T12:40:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4021#issuecomment-28941",
    "user": "https://github.com/malb"
}
```

On [sage-devel] Oliver Wienand (author of the upcoming Singular implementation for GBs over rings) wrote:

> I have just glimpsed over the code. But maybe it is worth stating in
> the comments, that the reduce impl. only returns unqiue answer against
> strong Gröbner basis.

> Gröbner basis G of I <=> the leading ideal of G generates all leading
> terms of I
> strong % of I <=> for every leading term t of I there exists an
> element g of G, such that the leading term of g divides t.

> (leading terms means coef * product of variables)

> Otherwise the reduce code shown in
> http://trac.sagemath.org/sage_trac/attachment/ticket/4021/mpolynomial_libsingular_zz.patch
> looks fine.



---

archive/issue_comments_028942.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-20T15:46:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4021#issuecomment-28942",
    "user": "https://github.com/malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_028943.json:
```json
{
    "body": "Attachment [mpolynomial_zz_reduce_doc.patch](tarball://root/attachments/some-uuid/ticket4021/mpolynomial_zz_reduce_doc.patch) by @malb created at 2008-09-24 11:30:58\n\nThe second patch addresses the review of Oliver Wienand on [sage-devel]:\n\n```\nI have just glimpsed over the code. But maybe it is worth stating in\nthe comments, that the reduce impl. only returns unqiue answer against\nstrong Gr\u00f6bner basis.\n\nGr\u00f6bner basis G of I <=> the leading ideal of G generates all leading\nterms of I\nstrong % of I <=> for every leading term t of I there exists an\nelement g of G, such that the leading term of g divides t.\n\n(leading terms meaans coef * product of variables)\n\nOtherwise the reduce code shown in\nhttp://trac.sagemath.org/sage_trac/attachment/ticket/4021/mpolynomial_libsingular_zz.patch\nlooks fine.\n```\n",
    "created_at": "2008-09-24T11:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4021#issuecomment-28943",
    "user": "https://github.com/malb"
}
```

Attachment [mpolynomial_zz_reduce_doc.patch](tarball://root/attachments/some-uuid/ticket4021/mpolynomial_zz_reduce_doc.patch) by @malb created at 2008-09-24 11:30:58

The second patch addresses the review of Oliver Wienand on [sage-devel]:

```
I have just glimpsed over the code. But maybe it is worth stating in
the comments, that the reduce impl. only returns unqiue answer against
strong Gröbner basis.

Gröbner basis G of I <=> the leading ideal of G generates all leading
terms of I
strong % of I <=> for every leading term t of I there exists an
element g of G, such that the leading term of g divides t.

(leading terms meaans coef * product of variables)

Otherwise the reduce code shown in
http://trac.sagemath.org/sage_trac/attachment/ticket/4021/mpolynomial_libsingular_zz.patch
looks fine.
```




---

archive/issue_comments_028944.json:
```json
{
    "body": "Attachment [trac4021-doctest-fix.patch](tarball://root/attachments/some-uuid/ticket4021/trac4021-doctest-fix.patch) by @aghitza created at 2008-09-28 06:45:20\n\nApplies cleanly on 3.1.3.alpha1 + the patch at #686, except for a reject in rings/polynomial/multi_polynomial_libsingular.pyx, which can be ignored.\n\nThere is a tiny doctest failure in rings/polynomial/multi_polynomial_element.py which is fixed by the attached patch.",
    "created_at": "2008-09-28T06:45:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4021#issuecomment-28944",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac4021-doctest-fix.patch](tarball://root/attachments/some-uuid/ticket4021/trac4021-doctest-fix.patch) by @aghitza created at 2008-09-28 06:45:20

Applies cleanly on 3.1.3.alpha1 + the patch at #686, except for a reject in rings/polynomial/multi_polynomial_libsingular.pyx, which can be ignored.

There is a tiny doctest failure in rings/polynomial/multi_polynomial_element.py which is fixed by the attached patch.



---

archive/issue_comments_028945.json:
```json
{
    "body": "Merged all three patches in Sage 3.1.3.alpha2",
    "created_at": "2008-09-28T18:15:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4021#issuecomment-28945",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all three patches in Sage 3.1.3.alpha2



---

archive/issue_comments_028946.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-28T19:22:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4021#issuecomment-28946",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_028947.json:
```json
{
    "body": "Merged all three patches in Sage 3.1.3.alpha2 and this time I closed the ticket :)",
    "created_at": "2008-09-28T19:22:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4021#issuecomment-28947",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all three patches in Sage 3.1.3.alpha2 and this time I closed the ticket :)
