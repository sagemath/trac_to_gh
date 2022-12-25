# Issue 2060: Update PolyBoRi spkg to 0.2

archive/issues_002060.json:
```json
{
    "body": "Assignee: @burcin\n\n\n```\nThe first release candidate of PolyBoRi 0.2 is available in the download area.\nThis version comes with refined Gr\u00f6bner algorithms and several stability\nimprovements. Also new procedures for interpolation of Boolean polynomials\nhave been added.\n```\n\nhttp://polybori.sourceforge.net/\n\nIssue created by migration from https://trac.sagemath.org/ticket/2060\n\n",
    "created_at": "2008-02-05T17:35:05Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "Update PolyBoRi spkg to 0.2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2060",
    "user": "https://github.com/malb"
}
```
Assignee: @burcin


```
The first release candidate of PolyBoRi 0.2 is available in the download area.
This version comes with refined Gröbner algorithms and several stability
improvements. Also new procedures for interpolation of Boolean polynomials
have been added.
```

http://polybori.sourceforge.net/

Issue created by migration from https://trac.sagemath.org/ticket/2060





---

archive/issue_comments_013309.json:
```json
{
    "body": "Note that #1611 is the ticket to split out and use the dynamic version of libm4ri. \n\nCheers,\n\nMichael",
    "created_at": "2008-02-17T19:57:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2060#issuecomment-13309",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Note that #1611 is the ticket to split out and use the dynamic version of libm4ri. 

Cheers,

Michael



---

archive/issue_comments_013310.json:
```json
{
    "body": "Attachment [2060-polybori_interface_update_0.3.1.patch](tarball://root/attachments/some-uuid/ticket2060/2060-polybori_interface_update_0.3.1.patch) by @burcin created at 2008-03-25 20:36:44\n\nupdate polybori interface to version 0.3.1",
    "created_at": "2008-03-25T20:36:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2060#issuecomment-13310",
    "user": "https://github.com/burcin"
}
```

Attachment [2060-polybori_interface_update_0.3.1.patch](tarball://root/attachments/some-uuid/ticket2060/2060-polybori_interface_update_0.3.1.patch) by @burcin created at 2008-03-25 20:36:44

update polybori interface to version 0.3.1



---

archive/issue_comments_013311.json:
```json
{
    "body": "attachment:2060-polybori_interface_update_0.3.1.patch includes the changes to the polybori wrapper for version 0.3.1, the corresponding package is here:\n\nhttp://www.risc.uni-linz.ac.at/people/berocal/sage/polybori-0.3.1.spkg",
    "created_at": "2008-03-25T20:42:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2060#issuecomment-13311",
    "user": "https://github.com/burcin"
}
```

attachment:2060-polybori_interface_update_0.3.1.patch includes the changes to the polybori wrapper for version 0.3.1, the corresponding package is here:

http://www.risc.uni-linz.ac.at/people/berocal/sage/polybori-0.3.1.spkg



---

archive/issue_comments_013312.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-25T20:42:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2060#issuecomment-13312",
    "user": "https://github.com/burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_013313.json:
```json
{
    "body": "The SPKG installs fine but I cannot apply the patch neither against my modified copy of Sage (which is expected) nor a vanilla 2.10.4, which is unexpected. I've attached the reject files for both.",
    "created_at": "2008-03-26T21:21:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2060#issuecomment-13313",
    "user": "https://github.com/malb"
}
```

The SPKG installs fine but I cannot apply the patch neither against my modified copy of Sage (which is expected) nor a vanilla 2.10.4, which is unexpected. I've attached the reject files for both.



---

archive/issue_comments_013314.json:
```json
{
    "body": "FYI, this patch still applies against 2.11:\n\n```\napplying /home/malb/2060-polybori_interface_update_0.3.1.patch?format=raw\npatching file sage/rings/polynomial/pbori.pyx\nHunk #1 succeeded at 148 with fuzz 1 (offset 100 lines).\n```\n",
    "created_at": "2008-04-01T13:03:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2060#issuecomment-13314",
    "user": "https://github.com/malb"
}
```

FYI, this patch still applies against 2.11:

```
applying /home/malb/2060-polybori_interface_update_0.3.1.patch?format=raw
patching file sage/rings/polynomial/pbori.pyx
Hunk #1 succeeded at 148 with fuzz 1 (offset 100 lines).
```




---

archive/issue_comments_013315.json:
```json
{
    "body": "Attachment [polybori_0.3.1_doctest_coverage_48.patch](tarball://root/attachments/some-uuid/ticket2060/polybori_0.3.1_doctest_coverage_48.patch) by @malb created at 2008-04-01 16:15:45\n\nThe attached patch (`polybori_0.3.1_doctest_coverage_48.patch`) which is to be applied on top of `2060-polybori_interface_update_0.3.1.patch` increases the doctest coverage to 47%.\n\n\n```\npbori.pyx\nSCORE pbori.pyx: 47% (98 of 205)\n```\n\n\nBefore both patches the coverage was at:\n\n\n```\npbori.pyx\nSCORE pbori.pyx: 33% (52 of 157)\n```\n\n\nand thus this is an improvement over vanilla 2.11 too.\n\n* I give Burcin's patch a positive review: doctests pass and we **need** `PolyBoRi` 0.3.1\n* someone should review my patch\n* if my patch gets a positive review both patches should be applied, since then not only is the functionality improved but also the doctest coverage which should make the everything-new-needs-doctest faction happy.\n* Burcin's patch was also doctested with the `PolyBoRi` test suite by him, so there is even an undocumented extra level of assurance.\n* In any case: We'll be working on getting the coverage close to 100% in the very near future.",
    "created_at": "2008-04-01T16:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2060#issuecomment-13315",
    "user": "https://github.com/malb"
}
```

Attachment [polybori_0.3.1_doctest_coverage_48.patch](tarball://root/attachments/some-uuid/ticket2060/polybori_0.3.1_doctest_coverage_48.patch) by @malb created at 2008-04-01 16:15:45

The attached patch (`polybori_0.3.1_doctest_coverage_48.patch`) which is to be applied on top of `2060-polybori_interface_update_0.3.1.patch` increases the doctest coverage to 47%.


```
pbori.pyx
SCORE pbori.pyx: 47% (98 of 205)
```


Before both patches the coverage was at:


```
pbori.pyx
SCORE pbori.pyx: 33% (52 of 157)
```


and thus this is an improvement over vanilla 2.11 too.

* I give Burcin's patch a positive review: doctests pass and we **need** `PolyBoRi` 0.3.1
* someone should review my patch
* if my patch gets a positive review both patches should be applied, since then not only is the functionality improved but also the doctest coverage which should make the everything-new-needs-doctest faction happy.
* Burcin's patch was also doctested with the `PolyBoRi` test suite by him, so there is even an undocumented extra level of assurance.
* In any case: We'll be working on getting the coverage close to 100% in the very near future.



---

archive/issue_comments_013316.json:
```json
{
    "body": "I agree that waiting to add doctests to each wrapped function from polybori will hold up the patch unnecessarily. The `PolyBoRi` test suite stresses the (yet) undocumented functions thoroughly.\n\nI give Martin's patch a positive review, both patches should be applied",
    "created_at": "2008-04-01T21:41:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2060#issuecomment-13316",
    "user": "https://github.com/burcin"
}
```

I agree that waiting to add doctests to each wrapped function from polybori will hold up the patch unnecessarily. The `PolyBoRi` test suite stresses the (yet) undocumented functions thoroughly.

I give Martin's patch a positive review, both patches should be applied



---

archive/issue_comments_013317.json:
```json
{
    "body": "Merged in Sage 3.0.alpha0",
    "created_at": "2008-04-01T22:14:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2060#issuecomment-13317",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha0



---

archive/issue_comments_013318.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-01T22:14:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2060#issuecomment-13318",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
