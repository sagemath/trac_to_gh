# Issue 1189: update sympy to 0.5.7, patch to make SymPy and SAGE work nicely

archive/issues_001189.json:
```json
{
    "body": "Assignee: was\n\nPlease update to sympy 0.5.7 using the attached spkg.\n\nThen apply the attached patch that will allow SAGE to freely mix SymPy and SAGE expressions.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1189\n\n",
    "created_at": "2007-11-17T00:15:13Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "update sympy to 0.5.7, patch to make SymPy and SAGE work nicely",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1189",
    "user": "certik"
}
```
Assignee: was

Please update to sympy 0.5.7 using the attached spkg.

Then apply the attached patch that will allow SAGE to freely mix SymPy and SAGE expressions.

Issue created by migration from https://trac.sagemath.org/ticket/1189





---

archive/issue_comments_007356.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-11-17T00:18:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7356",
    "user": "certik"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_007357.json:
```json
{
    "body": "Attachment\n\nHere is the link to the new sympy spkg:\n\nhttp://dakol.fsik.cvut.cz/~ondra/sympy-0.5.7.spkg\n\nPlease update this first, only then use the patch above.",
    "created_at": "2007-11-17T00:18:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7357",
    "user": "certik"
}
```

Attachment

Here is the link to the new sympy spkg:

http://dakol.fsik.cvut.cz/~ondra/sympy-0.5.7.spkg

Please update this first, only then use the patch above.



---

archive/issue_comments_007358.json:
```json
{
    "body": "Changing component from algebraic geometry to calculus.",
    "created_at": "2007-11-17T00:18:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7358",
    "user": "certik"
}
```

Changing component from algebraic geometry to calculus.



---

archive/issue_comments_007359.json:
```json
{
    "body": "After upgrading the spkg and applying the patch, please check, that everything works as it should by:\n\n$ ./sage -t devel/sage/sage/calculus/test_sympy.py \nsage -t  devel/sage-main/sage/calculus/test_sympy.py        \n         [2.9 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 2.9 seconds",
    "created_at": "2007-11-17T00:26:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7359",
    "user": "certik"
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

archive/issue_comments_007360.json:
```json
{
    "body": "Changelog of the spkg:\n\n* Script \"get-hg\" for getting hg sources added\n* get-orig-sources updated to download SymPy 0.5.7\n\nChangelog of the patch:\n\n* basic SymPy and SAGE objects can now be freely mixed",
    "created_at": "2007-11-17T23:20:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7360",
    "user": "certik"
}
```

Changelog of the spkg:

* Script "get-hg" for getting hg sources added
* get-orig-sources updated to download SymPy 0.5.7

Changelog of the patch:

* basic SymPy and SAGE objects can now be freely mixed



---

archive/issue_comments_007361.json:
```json
{
    "body": "Once again, this time with correct formatting.\n\nChangelog of the spkg:\n\n* Script \"get-hg\" for getting hg sources added\n\n\n* \"get-orig-sources\" updated to download SymPy 0.5.7\n\nChangelog of the patch:\n\n* basic SymPy and SAGE objects can now be freely mixed",
    "created_at": "2007-11-17T23:23:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7361",
    "user": "certik"
}
```

Once again, this time with correct formatting.

Changelog of the spkg:

* Script "get-hg" for getting hg sources added


* "get-orig-sources" updated to download SymPy 0.5.7

Changelog of the patch:

* basic SymPy and SAGE objects can now be freely mixed



---

archive/issue_comments_007362.json:
```json
{
    "body": "Merged in 2.8.13.alpha0.",
    "created_at": "2007-11-18T06:15:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7362",
    "user": "mabshoff"
}
```

Merged in 2.8.13.alpha0.



---

archive/issue_comments_007363.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-18T06:15:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7363",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007364.json:
```json
{
    "body": "Arrg, the bit of the patch in coerce.pyx causes segfaults. So the patch is backed out, but the spkg is still in.\n\nOndrej: Either open a new ticket and resubmit the patch or reopen this ticket.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-18T13:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7364",
    "user": "mabshoff"
}
```

Arrg, the bit of the patch in coerce.pyx causes segfaults. So the patch is backed out, but the spkg is still in.

Ondrej: Either open a new ticket and resubmit the patch or reopen this ticket.

Cheers,

Michael



---

archive/issue_comments_007365.json:
```json
{
    "body": "Oops. I only executed the tests in calculus/test_sympy.py.\n\nI am openning the ticket, but leaving it to a later milestone, because I don't have time at the moment to fix that. Is there someone more experienced to maybe see immediatelly what is wrong?\n\nI run \"./sage -t *\" and indeed I am getting these errors:\n\nsage -t  devel/sage-main/sage/schemes/generic/spec.py       sh: line 1:  9143 Segmentation fault      /home/ondra/ext/sage-2.8.12-debian32-i686-Linux/local/bin/python .doctest_spec.py >.doctest/out 2>.doctest/err\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n\n\nsage -t  devel/sage-main/sage/rings/number_field/order.py   sh: line 1:  9354 Segmentation fault      /home/ondra/ext/sage-2.8.12-debian32-i686-Linux/local/bin/python .doctest_order.py >.doctest/out 2>.doctest/err\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n\nsage -t  devel/sage-main/sage/rings/integer_ring.pyx        sh: line 1:  9855 Segmentation fault      /home/ondra/ext/sage-2.8.12-debian32-i686-Linux/local/bin/python .doctest_integer_ring.py >.doctest/out 2>.doctest/err\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n\n\nsage -t  devel/sage-main/sage/rings/complex_field.py        sh: line 1:  9919 Segmentation fault      /home/ondra/ext/sage-2.8.12-debian32-i686-Linux/local/bin/python .doctest_complex_field.py >.doctest/out 2>.doctest/err\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n\nsage -t  devel/sage-main/sage/rings/quotient_ring.py        sh: line 1:  9934 Segmentation fault      /home/ondra/ext/sage-2.8.12-debian32-i686-Linux/local/bin/python .doctest_quotient_ring.py >.doctest/out 2>.doctest/err\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n\n\nsage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial_ideal.pysh: line 1: 10028 Segmentation fault      /home/ondra/ext/sage-2.8.12-debian32-i686-Linux/local/bin/python .doctest_multi_polynomial_ideal.py >.doctest/out 2>.doctest/err\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n\nsage -t  devel/sage-main/sage/rings/real_rqdf.pyx           sh: line 1: 10557 Segmentation fault      /home/ondra/ext/sage-2.8.12-debian32-i686-Linux/local/bin/python .doctest_real_rqdf.py >.doctest/out 2>.doctest/err\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n\n...",
    "created_at": "2007-11-18T13:59:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7365",
    "user": "certik"
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

archive/issue_comments_007366.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-11-18T13:59:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7366",
    "user": "certik"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_007367.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-11-18T13:59:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7367",
    "user": "certik"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_007368.json:
```json
{
    "body": "Hehe, I assumed you ran testall, especially after touching coerce.pyx. I tagged this against 2.9 for now. It will automatically get moved forward every time we complete a milestone.\n\nI also changed the summary to reflect the remaining issue.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-18T14:03:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7368",
    "user": "mabshoff"
}
```

Hehe, I assumed you ran testall, especially after touching coerce.pyx. I tagged this against 2.9 for now. It will automatically get moved forward every time we complete a milestone.

I also changed the summary to reflect the remaining issue.

Cheers,

Michael



---

archive/issue_comments_007369.json:
```json
{
    "body": "> Hehe, I assumed you ran testall, especially after touching coerce.pyx.\n\nYeah, I am still learning how to properly contribute to SAGE. :)",
    "created_at": "2007-11-19T08:40:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7369",
    "user": "certik"
}
```

> Hehe, I assumed you ran testall, especially after touching coerce.pyx.

Yeah, I am still learning how to properly contribute to SAGE. :)



---

archive/issue_comments_007370.json:
```json
{
    "body": "Attachment\n\nThe patch was fixed, now it passes all tests:\n\nhttp://sagetrac.org/sage_trac/attachment/ticket/1189/sympy2.patch\n\nBut probably needs some review before committing.",
    "created_at": "2007-11-26T01:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7370",
    "user": "certik"
}
```

Attachment

The patch was fixed, now it passes all tests:

http://sagetrac.org/sage_trac/attachment/ticket/1189/sympy2.patch

But probably needs some review before committing.



---

archive/issue_comments_007371.json:
```json
{
    "body": "I was not able to apply sympy2.patch cleanly against Sage 2.8.14. \n\nThat said, I think _verify_canonical_coercion_c is the wrong thing to call here--please see the attached change which should fix the segfault issue in a much cleaner way and allow stuff like\n \n\n```\nsage: Integer(1) + sympy.Symbol(\"x\")\nx + 1\n```\n",
    "created_at": "2007-11-27T03:43:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7371",
    "user": "robertwb"
}
```

I was not able to apply sympy2.patch cleanly against Sage 2.8.14. 

That said, I think _verify_canonical_coercion_c is the wrong thing to call here--please see the attached change which should fix the segfault issue in a much cleaner way and allow stuff like
 

```
sage: Integer(1) + sympy.Symbol("x")
x + 1
```




---

archive/issue_comments_007372.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-11-27T03:43:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7372",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_007373.json:
```json
{
    "body": "Unfortunately, I don't have time to do it (leaving to Spain tomorrow). But please use the original sympy.patch + sympy-coerce.patch from Robert, that should do the job.\n\nThanks a lot.",
    "created_at": "2007-11-27T17:10:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7373",
    "user": "certik"
}
```

Unfortunately, I don't have time to do it (leaving to Spain tomorrow). But please use the original sympy.patch + sympy-coerce.patch from Robert, that should do the job.

Thanks a lot.



---

archive/issue_comments_007374.json:
```json
{
    "body": "Merged in 2.8.15.rc0 - finally ;)",
    "created_at": "2007-12-02T23:23:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7374",
    "user": "mabshoff"
}
```

Merged in 2.8.15.rc0 - finally ;)



---

archive/issue_comments_007375.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-02T23:23:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7375",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007376.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-12-03T00:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7376",
    "user": "mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_007377.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-12-03T00:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7377",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_007378.json:
```json
{
    "body": "On sage.math the above two patches cause doctest failures in rings/polynomial/multi_polynomial_ideal.py - so reopen.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-03T00:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7378",
    "user": "mabshoff"
}
```

On sage.math the above two patches cause doctest failures in rings/polynomial/multi_polynomial_ideal.py - so reopen.

Cheers,

Michael



---

archive/issue_comments_007379.json:
```json
{
    "body": "This is probably not the patches direct fault, but we need to fix the other segfault first before merging this. Sage not working on sage.math isn't really an option.\n\nSorry, Ondrej.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-06T02:40:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7379",
    "user": "mabshoff"
}
```

This is probably not the patches direct fault, but we need to fix the other segfault first before merging this. Sage not working on sage.math isn't really an option.

Sorry, Ondrej.

Cheers,

Michael



---

archive/issue_comments_007380.json:
```json
{
    "body": "I wasn't able to reproduce the errors in rings/polynomial/multi_polynomial_ideal.py, or anywhere for that matter. Could you clarify? \n\nStill running testall...",
    "created_at": "2007-12-06T21:41:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7380",
    "user": "robertwb"
}
```

I wasn't able to reproduce the errors in rings/polynomial/multi_polynomial_ideal.py, or anywhere for that matter. Could you clarify? 

Still running testall...



---

archive/issue_comments_007381.json:
```json
{
    "body": "Testall succeeded for me with these patches.",
    "created_at": "2007-12-06T22:37:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7381",
    "user": "robertwb"
}
```

Testall succeeded for me with these patches.



---

archive/issue_comments_007382.json:
```json
{
    "body": "Well, the segfault happened to me on sage.math. \n\nCheers,\n\nMichael",
    "created_at": "2007-12-09T12:50:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7382",
    "user": "mabshoff"
}
```

Well, the segfault happened to me on sage.math. 

Cheers,

Michael



---

archive/issue_comments_007383.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-10T22:30:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7383",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007384.json:
```json
{
    "body": "Finally merged in 2.9.alpha5 :)",
    "created_at": "2007-12-10T22:30:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1189#issuecomment-7384",
    "user": "mabshoff"
}
```

Finally merged in 2.9.alpha5 :)
