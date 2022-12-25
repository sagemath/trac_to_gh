# Issue 1189: update sympy to 0.5.7, patch to make SymPy and SAGE work nicely

archive/issues_001189.json:
```json
{
    "body": "Assignee: @williamstein\n\nPlease update to sympy 0.5.7 using the attached spkg.\n\nThen apply the attached patch that will allow SAGE to freely mix SymPy and SAGE expressions.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1189\n\n",
    "created_at": "2007-11-17T00:15:13Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "update sympy to 0.5.7, patch to make SymPy and SAGE work nicely",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1189",
    "user": "https://github.com/certik"
}
```
Assignee: @williamstein

Please update to sympy 0.5.7 using the attached spkg.

Then apply the attached patch that will allow SAGE to freely mix SymPy and SAGE expressions.

Issue created by migration from https://trac.sagemath.org/ticket/1189





---

archive/issue_comments_007334.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-11-17T00:18:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7334",
    "user": "https://github.com/certik"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_007335.json:
```json
{
    "body": "Attachment [sympy.patch](tarball://root/attachments/some-uuid/ticket1189/sympy.patch) by @certik created at 2007-11-17 00:18:56\n\nHere is the link to the new sympy spkg:\n\nhttp://dakol.fsik.cvut.cz/~ondra/sympy-0.5.7.spkg\n\nPlease update this first, only then use the patch above.",
    "created_at": "2007-11-17T00:18:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7335",
    "user": "https://github.com/certik"
}
```

Attachment [sympy.patch](tarball://root/attachments/some-uuid/ticket1189/sympy.patch) by @certik created at 2007-11-17 00:18:56

Here is the link to the new sympy spkg:

http://dakol.fsik.cvut.cz/~ondra/sympy-0.5.7.spkg

Please update this first, only then use the patch above.



---

archive/issue_comments_007336.json:
```json
{
    "body": "Changing component from algebraic geometry to calculus.",
    "created_at": "2007-11-17T00:18:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7336",
    "user": "https://github.com/certik"
}
```

Changing component from algebraic geometry to calculus.



---

archive/issue_comments_007337.json:
```json
{
    "body": "After upgrading the spkg and applying the patch, please check, that everything works as it should by:\n\n$ ./sage -t devel/sage/sage/calculus/test_sympy.py \nsage -t  devel/sage-main/sage/calculus/test_sympy.py        \n         [2.9 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 2.9 seconds",
    "created_at": "2007-11-17T00:26:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7337",
    "user": "https://github.com/certik"
}
```

After upgrading the spkg and applying the patch, please check, that everything works as it should by:

$ ./sage -t devel/sage/sage/calculus/test_sympy.py 
sage -t  devel/sage-main/sage/calculus/test_sympy.py        
         [2.9 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 2.9 seconds



---

archive/issue_comments_007338.json:
```json
{
    "body": "Changelog of the spkg:\n\n* Script \"get-hg\" for getting hg sources added\n* get-orig-sources updated to download SymPy 0.5.7\n\nChangelog of the patch:\n\n* basic SymPy and SAGE objects can now be freely mixed",
    "created_at": "2007-11-17T23:20:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7338",
    "user": "https://github.com/certik"
}
```

Changelog of the spkg:

* Script "get-hg" for getting hg sources added
* get-orig-sources updated to download SymPy 0.5.7

Changelog of the patch:

* basic SymPy and SAGE objects can now be freely mixed



---

archive/issue_comments_007339.json:
```json
{
    "body": "Once again, this time with correct formatting.\n\nChangelog of the spkg:\n\n* Script \"get-hg\" for getting hg sources added\n\n\n* \"get-orig-sources\" updated to download SymPy 0.5.7\n\nChangelog of the patch:\n\n* basic SymPy and SAGE objects can now be freely mixed",
    "created_at": "2007-11-17T23:23:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7339",
    "user": "https://github.com/certik"
}
```

Once again, this time with correct formatting.

Changelog of the spkg:

* Script "get-hg" for getting hg sources added


* "get-orig-sources" updated to download SymPy 0.5.7

Changelog of the patch:

* basic SymPy and SAGE objects can now be freely mixed



---

archive/issue_comments_007340.json:
```json
{
    "body": "Merged in 2.8.13.alpha0.",
    "created_at": "2007-11-18T06:15:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7340",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.13.alpha0.



---

archive/issue_comments_007341.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-18T06:15:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7341",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001321.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-11-18T06:15:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1189#event-1321"
}
```



---

archive/issue_comments_007342.json:
```json
{
    "body": "Arrg, the bit of the patch in coerce.pyx causes segfaults. So the patch is backed out, but the spkg is still in.\n\nOndrej: Either open a new ticket and resubmit the patch or reopen this ticket.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-18T13:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7342",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Arrg, the bit of the patch in coerce.pyx causes segfaults. So the patch is backed out, but the spkg is still in.

Ondrej: Either open a new ticket and resubmit the patch or reopen this ticket.

Cheers,

Michael



---

archive/issue_comments_007343.json:
```json
{
    "body": "Oops. I only executed the tests in calculus/test_sympy.py.\n\nI am openning the ticket, but leaving it to a later milestone, because I don't have time at the moment to fix that. Is there someone more experienced to maybe see immediatelly what is wrong?\n\nI run \"./sage -t *\" and indeed I am getting these errors:\n\nsage -t  devel/sage-main/sage/schemes/generic/spec.py       sh: line 1:  9143 Segmentation fault      /home/ondra/ext/sage-2.8.12-debian32-i686-Linux/local/bin/python .doctest_spec.py >.doctest/out 2>.doctest/err\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n\n\nsage -t  devel/sage-main/sage/rings/number_field/order.py   sh: line 1:  9354 Segmentation fault      /home/ondra/ext/sage-2.8.12-debian32-i686-Linux/local/bin/python .doctest_order.py >.doctest/out 2>.doctest/err\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n\nsage -t  devel/sage-main/sage/rings/integer_ring.pyx        sh: line 1:  9855 Segmentation fault      /home/ondra/ext/sage-2.8.12-debian32-i686-Linux/local/bin/python .doctest_integer_ring.py >.doctest/out 2>.doctest/err\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n\n\nsage -t  devel/sage-main/sage/rings/complex_field.py        sh: line 1:  9919 Segmentation fault      /home/ondra/ext/sage-2.8.12-debian32-i686-Linux/local/bin/python .doctest_complex_field.py >.doctest/out 2>.doctest/err\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n\nsage -t  devel/sage-main/sage/rings/quotient_ring.py        sh: line 1:  9934 Segmentation fault      /home/ondra/ext/sage-2.8.12-debian32-i686-Linux/local/bin/python .doctest_quotient_ring.py >.doctest/out 2>.doctest/err\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n\n\nsage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial_ideal.pysh: line 1: 10028 Segmentation fault      /home/ondra/ext/sage-2.8.12-debian32-i686-Linux/local/bin/python .doctest_multi_polynomial_ideal.py >.doctest/out 2>.doctest/err\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n\nsage -t  devel/sage-main/sage/rings/real_rqdf.pyx           sh: line 1: 10557 Segmentation fault      /home/ondra/ext/sage-2.8.12-debian32-i686-Linux/local/bin/python .doctest_real_rqdf.py >.doctest/out 2>.doctest/err\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n\n...",
    "created_at": "2007-11-18T13:59:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7343",
    "user": "https://github.com/certik"
}
```

Oops. I only executed the tests in calculus/test_sympy.py.

I am openning the ticket, but leaving it to a later milestone, because I don't have time at the moment to fix that. Is there someone more experienced to maybe see immediatelly what is wrong?

I run "./sage -t *" and indeed I am getting these errors:

sage -t  devel/sage-main/sage/schemes/generic/spec.py       sh: line 1:  9143 Segmentation fault      /home/ondra/ext/sage-2.8.12-debian32-i686-Linux/local/bin/python .doctest_spec.py >.doctest/out 2>.doctest/err

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.


sage -t  devel/sage-main/sage/rings/number_field/order.py   sh: line 1:  9354 Segmentation fault      /home/ondra/ext/sage-2.8.12-debian32-i686-Linux/local/bin/python .doctest_order.py >.doctest/out 2>.doctest/err

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.

sage -t  devel/sage-main/sage/rings/integer_ring.pyx        sh: line 1:  9855 Segmentation fault      /home/ondra/ext/sage-2.8.12-debian32-i686-Linux/local/bin/python .doctest_integer_ring.py >.doctest/out 2>.doctest/err

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.


sage -t  devel/sage-main/sage/rings/complex_field.py        sh: line 1:  9919 Segmentation fault      /home/ondra/ext/sage-2.8.12-debian32-i686-Linux/local/bin/python .doctest_complex_field.py >.doctest/out 2>.doctest/err

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.

sage -t  devel/sage-main/sage/rings/quotient_ring.py        sh: line 1:  9934 Segmentation fault      /home/ondra/ext/sage-2.8.12-debian32-i686-Linux/local/bin/python .doctest_quotient_ring.py >.doctest/out 2>.doctest/err

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.


sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial_ideal.pysh: line 1: 10028 Segmentation fault      /home/ondra/ext/sage-2.8.12-debian32-i686-Linux/local/bin/python .doctest_multi_polynomial_ideal.py >.doctest/out 2>.doctest/err

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.

sage -t  devel/sage-main/sage/rings/real_rqdf.pyx           sh: line 1: 10557 Segmentation fault      /home/ondra/ext/sage-2.8.12-debian32-i686-Linux/local/bin/python .doctest_real_rqdf.py >.doctest/out 2>.doctest/err

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.

...



---

archive/issue_comments_007344.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-11-18T13:59:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7344",
    "user": "https://github.com/certik"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_007345.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-11-18T13:59:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7345",
    "user": "https://github.com/certik"
}
```

Changing status from closed to reopened.



---

archive/issue_events_001322.json:
```json
{
    "actor": "@certik",
    "created_at": "2007-11-18T13:59:08Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1189#event-1322"
}
```



---

archive/issue_comments_007346.json:
```json
{
    "body": "Hehe, I assumed you ran testall, especially after touching coerce.pyx. I tagged this against 2.9 for now. It will automatically get moved forward every time we complete a milestone.\n\nI also changed the summary to reflect the remaining issue.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-18T14:03:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7346",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hehe, I assumed you ran testall, especially after touching coerce.pyx. I tagged this against 2.9 for now. It will automatically get moved forward every time we complete a milestone.

I also changed the summary to reflect the remaining issue.

Cheers,

Michael



---

archive/issue_comments_007347.json:
```json
{
    "body": "> Hehe, I assumed you ran testall, especially after touching coerce.pyx.\n\nYeah, I am still learning how to properly contribute to SAGE. :)",
    "created_at": "2007-11-19T08:40:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7347",
    "user": "https://github.com/certik"
}
```

> Hehe, I assumed you ran testall, especially after touching coerce.pyx.

Yeah, I am still learning how to properly contribute to SAGE. :)



---

archive/issue_comments_007348.json:
```json
{
    "body": "Attachment [sympy2.patch](tarball://root/attachments/some-uuid/ticket1189/sympy2.patch) by @certik created at 2007-11-26 01:19:11\n\nThe patch was fixed, now it passes all tests:\n\nhttp://sagetrac.org/sage_trac/attachment/ticket/1189/sympy2.patch\n\nBut probably needs some review before committing.",
    "created_at": "2007-11-26T01:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7348",
    "user": "https://github.com/certik"
}
```

Attachment [sympy2.patch](tarball://root/attachments/some-uuid/ticket1189/sympy2.patch) by @certik created at 2007-11-26 01:19:11

The patch was fixed, now it passes all tests:

http://sagetrac.org/sage_trac/attachment/ticket/1189/sympy2.patch

But probably needs some review before committing.



---

archive/issue_comments_007349.json:
```json
{
    "body": "I was not able to apply sympy2.patch cleanly against Sage 2.8.14. \n\nThat said, I think _verify_canonical_coercion_c is the wrong thing to call here--please see the attached change which should fix the segfault issue in a much cleaner way and allow stuff like\n \n\n```\nsage: Integer(1) + sympy.Symbol(\"x\")\nx + 1\n```\n",
    "created_at": "2007-11-27T03:43:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7349",
    "user": "https://github.com/robertwb"
}
```

I was not able to apply sympy2.patch cleanly against Sage 2.8.14. 

That said, I think _verify_canonical_coercion_c is the wrong thing to call here--please see the attached change which should fix the segfault issue in a much cleaner way and allow stuff like
 

```
sage: Integer(1) + sympy.Symbol("x")
x + 1
```




---

archive/issue_comments_007350.json:
```json
{
    "body": "Attachment [sympy-coerce.patch](tarball://root/attachments/some-uuid/ticket1189/sympy-coerce.patch) by @robertwb created at 2007-11-27 03:43:53",
    "created_at": "2007-11-27T03:43:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7350",
    "user": "https://github.com/robertwb"
}
```

Attachment [sympy-coerce.patch](tarball://root/attachments/some-uuid/ticket1189/sympy-coerce.patch) by @robertwb created at 2007-11-27 03:43:53



---

archive/issue_comments_007351.json:
```json
{
    "body": "Unfortunately, I don't have time to do it (leaving to Spain tomorrow). But please use the original sympy.patch + sympy-coerce.patch from Robert, that should do the job.\n\nThanks a lot.",
    "created_at": "2007-11-27T17:10:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7351",
    "user": "https://github.com/certik"
}
```

Unfortunately, I don't have time to do it (leaving to Spain tomorrow). But please use the original sympy.patch + sympy-coerce.patch from Robert, that should do the job.

Thanks a lot.



---

archive/issue_comments_007352.json:
```json
{
    "body": "Merged in 2.8.15.rc0 - finally ;)",
    "created_at": "2007-12-02T23:23:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7352",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.15.rc0 - finally ;)



---

archive/issue_events_001323.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-12-02T23:23:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1189#event-1323"
}
```



---

archive/issue_comments_007353.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-02T23:23:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7353",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007354.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-12-03T00:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7354",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_007355.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-12-03T00:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7355",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_events_001324.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-12-03T00:30:05Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1189#event-1324"
}
```



---

archive/issue_comments_007356.json:
```json
{
    "body": "On sage.math the above two patches cause doctest failures in rings/polynomial/multi_polynomial_ideal.py - so reopen.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-03T00:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7356",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

On sage.math the above two patches cause doctest failures in rings/polynomial/multi_polynomial_ideal.py - so reopen.

Cheers,

Michael



---

archive/issue_comments_007357.json:
```json
{
    "body": "This is probably not the patches direct fault, but we need to fix the other segfault first before merging this. Sage not working on sage.math isn't really an option.\n\nSorry, Ondrej.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-06T02:40:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7357",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is probably not the patches direct fault, but we need to fix the other segfault first before merging this. Sage not working on sage.math isn't really an option.

Sorry, Ondrej.

Cheers,

Michael



---

archive/issue_comments_007358.json:
```json
{
    "body": "I wasn't able to reproduce the errors in rings/polynomial/multi_polynomial_ideal.py, or anywhere for that matter. Could you clarify? \n\nStill running testall...",
    "created_at": "2007-12-06T21:41:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7358",
    "user": "https://github.com/robertwb"
}
```

I wasn't able to reproduce the errors in rings/polynomial/multi_polynomial_ideal.py, or anywhere for that matter. Could you clarify? 

Still running testall...



---

archive/issue_comments_007359.json:
```json
{
    "body": "Testall succeeded for me with these patches.",
    "created_at": "2007-12-06T22:37:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7359",
    "user": "https://github.com/robertwb"
}
```

Testall succeeded for me with these patches.



---

archive/issue_comments_007360.json:
```json
{
    "body": "Well, the segfault happened to me on sage.math. \n\nCheers,\n\nMichael",
    "created_at": "2007-12-09T12:50:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7360",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Well, the segfault happened to me on sage.math. 

Cheers,

Michael



---

archive/issue_events_001325.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-12-10T22:30:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1189#event-1325"
}
```



---

archive/issue_comments_007361.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-10T22:30:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7361",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007362.json:
```json
{
    "body": "Finally merged in 2.9.alpha5 :)",
    "created_at": "2007-12-10T22:30:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7362",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Finally merged in 2.9.alpha5 :)
