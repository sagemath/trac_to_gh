# Issue 4582: use Singular's capabilities for computing over fraction fields

archive/issues_004582.json:
```json
{
    "body": "Assignee: @malb\n\nGuillaume Moroz wrote on [sage-devel]:\n\n\"\nit seems that the sage interface to singular is not aware that Singular handles multivariate polynomial rings with coefficients in a fraction field.\n\n\n```\nsage: from sage.rings.polynomial.polynomial_singular_interface import\ncan_convert_to_singular\nsage: r=Frac(QQ['a,b'])['x,y']\nsage: can_convert_to_singular(r)\nFalse\n```\n\n\nHowever, it is possible to define it in Singular: in this case, it would be\n\n\n```\nring R=(0,a,b),(x,y),dp;\n```\n\n\n(following the syntax 2. given at http://www.singular.uni-kl.de/Manual/latest/sing_30.htm#SEC40)\n\nIn particular, Gr\u00f6bner basis can be computed by Singular in these polynomial rings more efficiently than the toy algorithm currently used.\n\"\n\n\nI hope this can help!\n\nBest regards,\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4582\n\n",
    "created_at": "2008-11-22T12:01:16Z",
    "labels": [
        "component: commutative algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "use Singular's capabilities for computing over fraction fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4582",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

Guillaume Moroz wrote on [sage-devel]:

"
it seems that the sage interface to singular is not aware that Singular handles multivariate polynomial rings with coefficients in a fraction field.


```
sage: from sage.rings.polynomial.polynomial_singular_interface import
can_convert_to_singular
sage: r=Frac(QQ['a,b'])['x,y']
sage: can_convert_to_singular(r)
False
```


However, it is possible to define it in Singular: in this case, it would be


```
ring R=(0,a,b),(x,y),dp;
```


(following the syntax 2. given at http://www.singular.uni-kl.de/Manual/latest/sing_30.htm#SEC40)

In particular, Gröbner basis can be computed by Singular in these polynomial rings more efficiently than the toy algorithm currently used.
"


I hope this can help!

Best regards,


Issue created by migration from https://trac.sagemath.org/ticket/4582





---

archive/issue_comments_034289.json:
```json
{
    "body": "Patch resolution via pexpect",
    "created_at": "2008-11-26T23:56:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4582#issuecomment-34289",
    "user": "https://trac.sagemath.org/admin/accounts/users/gmoroz"
}
```

Patch resolution via pexpect



---

archive/issue_comments_034290.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-27T00:04:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4582#issuecomment-34290",
    "user": "https://trac.sagemath.org/admin/accounts/users/gmoroz"
}
```

Resolution: fixed



---

archive/issue_comments_034291.json:
```json
{
    "body": "Attachment [patch_polynomial.txt](tarball://root/attachments/some-uuid/ticket4582/patch_polynomial.txt) by gmoroz created at 2008-11-27 00:04:54\n\nThe attached patch should satisfy the requierement",
    "created_at": "2008-11-27T00:04:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4582#issuecomment-34291",
    "user": "https://trac.sagemath.org/admin/accounts/users/gmoroz"
}
```

Attachment [patch_polynomial.txt](tarball://root/attachments/some-uuid/ticket4582/patch_polynomial.txt) by gmoroz created at 2008-11-27 00:04:54

The attached patch should satisfy the requierement



---

archive/issue_events_004829.json:
```json
{
    "actor": "gmoroz",
    "created_at": "2008-11-27T00:04:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4582",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4582#event-4829"
}
```



---

archive/issue_comments_034292.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-11-27T00:08:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4582#issuecomment-34292",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_034293.json:
```json
{
    "body": "Hi,\n\nplease don't close tickets. A ticket is only closed once it has been merged by the release manager. \n\nPlease make sure to read http://wiki.sagemath.org/TracGuidelines since it explains the process.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-27T00:08:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4582#issuecomment-34293",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi,

please don't close tickets. A ticket is only closed once it has been merged by the release manager. 

Please make sure to read http://wiki.sagemath.org/TracGuidelines since it explains the process.

Cheers,

Michael



---

archive/issue_comments_034294.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-11-27T00:08:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4582#issuecomment-34294",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_events_004830.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-11-27T00:08:56Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/4582",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4582#event-4830"
}
```



---

archive/issue_comments_034295.json:
```json
{
    "body": "And one more thing: Please make sure to attach the file with the ending \".patch\". The current attachment is a plain diff, so in case you use mercurial commit and do an \"hg export tip\" to create an hg patch. That patch automatically gives credit to you in the hg changelog for example and also has a number of different advantages. If you have trouble using hg we can discuss it either in IRC or on [sage-support].\n\nCheers,\n\nMichael",
    "created_at": "2008-11-27T00:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4582#issuecomment-34295",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

And one more thing: Please make sure to attach the file with the ending ".patch". The current attachment is a plain diff, so in case you use mercurial commit and do an "hg export tip" to create an hg patch. That patch automatically gives credit to you in the hg changelog for example and also has a number of different advantages. If you have trouble using hg we can discuss it either in IRC or on [sage-support].

Cheers,

Michael



---

archive/issue_comments_034296.json:
```json
{
    "body": "Yes sorry, I realized this too late.\n\nIt is the first time I use mercurial and just piped the output of 'sage -hg diff' in the text file: I'll check the export mercurial function and send a normal patch in some days.",
    "created_at": "2008-11-27T00:23:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4582#issuecomment-34296",
    "user": "https://trac.sagemath.org/admin/accounts/users/gmoroz"
}
```

Yes sorry, I realized this too late.

It is the first time I use mercurial and just piped the output of 'sage -hg diff' in the text file: I'll check the export mercurial function and send a normal patch in some days.



---

archive/issue_comments_034297.json:
```json
{
    "body": "Replying to [comment:4 gmoroz]:\n> Yes sorry, I realized this too late.\n\nNo problem, plenty of us have made that mistake :)\n\n> It is the first time I use mercurial and just piped the output of 'sage -hg diff' in the text file: I'll check the export mercurial function and send a normal patch in some days.\n\nCool. Welcome aboard Sage development.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-27T00:26:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4582#issuecomment-34297",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:4 gmoroz]:
> Yes sorry, I realized this too late.

No problem, plenty of us have made that mistake :)

> It is the first time I use mercurial and just piped the output of 'sage -hg diff' in the text file: I'll check the export mercurial function and send a normal patch in some days.

Cool. Welcome aboard Sage development.

Cheers,

Michael



---

archive/issue_comments_034298.json:
```json
{
    "body": "Standard mercurial patch",
    "created_at": "2008-11-28T22:57:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4582#issuecomment-34298",
    "user": "https://trac.sagemath.org/admin/accounts/users/gmoroz"
}
```

Standard mercurial patch



---

archive/issue_comments_034299.json:
```json
{
    "body": "Attachment [fraction_field.patch](tarball://root/attachments/some-uuid/ticket4582/fraction_field.patch) by @malb created at 2008-11-30 21:53:53\n\nPatch applies cleanly against 3.2, doctests in `sage.rings` pass, patch contains doctest.",
    "created_at": "2008-11-30T21:53:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4582#issuecomment-34299",
    "user": "https://github.com/malb"
}
```

Attachment [fraction_field.patch](tarball://root/attachments/some-uuid/ticket4582/fraction_field.patch) by @malb created at 2008-11-30 21:53:53

Patch applies cleanly against 3.2, doctests in `sage.rings` pass, patch contains doctest.



---

archive/issue_comments_034300.json:
```json
{
    "body": "Merged fraction_field.patch in Sage 3.2.1.rc1",
    "created_at": "2008-11-30T23:12:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4582#issuecomment-34300",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged fraction_field.patch in Sage 3.2.1.rc1



---

archive/issue_comments_034301.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-30T23:12:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4582#issuecomment-34301",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004831.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-11-30T23:12:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4582",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4582#event-4831"
}
```
