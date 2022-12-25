# Issue 3284: [with patch, needs work, SEGFAULTs!] use weakref for PolyBoRi

archive/issues_003284.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @burcin polybori\n\nKeywords: PolyBoRi, segfault\n\n**First: Do not apply this patch unless you want to fix it, it SEGFAULTs**\n\nThis patch makes sure only one `BooleanPolynomialRing` per parameter set is created by returning a reference to a prior created object if there is such a reference. However, as a consequence the following happens:\n\n\n```\n$ sage -t -verbose sage/rings/polynomial/pbori.pyx   \n...\nTrying:\n    m = M._coerce_(N(y*z)); m###line 1261:_sage_    >>> m = M._coerce_(N(y*z)); m\nExpecting:\n    y*z\nOperands come from different manager.\n```\n\n\nI don't know where to look for a solution here. So I'm putting the patch up here in the hope that Burcin, Michael, Alexander or someone else doesn't have such a hard time finding the cause of this bug.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3284\n\n",
    "created_at": "2008-05-23T17:15:34Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with patch, needs work, SEGFAULTs!] use weakref for PolyBoRi",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3284",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  @burcin polybori

Keywords: PolyBoRi, segfault

**First: Do not apply this patch unless you want to fix it, it SEGFAULTs**

This patch makes sure only one `BooleanPolynomialRing` per parameter set is created by returning a reference to a prior created object if there is such a reference. However, as a consequence the following happens:


```
$ sage -t -verbose sage/rings/polynomial/pbori.pyx   
...
Trying:
    m = M._coerce_(N(y*z)); m###line 1261:_sage_    >>> m = M._coerce_(N(y*z)); m
Expecting:
    y*z
Operands come from different manager.
```


I don't know where to look for a solution here. So I'm putting the patch up here in the hope that Burcin, Michael, Alexander or someone else doesn't have such a hard time finding the cause of this bug.

Issue created by migration from https://trac.sagemath.org/ticket/3284





---

archive/issue_comments_022676.json:
```json
{
    "body": "Hello again,\n\"Operands come from different manager.\" is an error message from the deep of the BDD-package behind the PolyBoRi data structures. It means, that one tries to do a binary operation with elements from two different rings. But operation does not necessary mean the y*z operation, it maybe triggered by something else in N() oder _coerce_\n\nBest regards,\n  Alexander",
    "created_at": "2008-05-23T21:51:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3284#issuecomment-22676",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

Hello again,
"Operands come from different manager." is an error message from the deep of the BDD-package behind the PolyBoRi data structures. It means, that one tries to do a binary operation with elements from two different rings. But operation does not necessary mean the y*z operation, it maybe triggered by something else in N() oder _coerce_

Best regards,
  Alexander



---

archive/issue_comments_022677.json:
```json
{
    "body": "My guess is that we somewhere forget to set the global ring maybe?",
    "created_at": "2008-05-25T12:57:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3284#issuecomment-22677",
    "user": "https://github.com/malb"
}
```

My guess is that we somewhere forget to set the global ring maybe?



---

archive/issue_comments_022678.json:
```json
{
    "body": "Attachment [pbori_weakref.patch](tarball://root/attachments/some-uuid/ticket3284/pbori_weakref.patch) by @malb created at 2008-05-25 16:09:12\n\nthis patch is supposed to work",
    "created_at": "2008-05-25T16:09:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3284#issuecomment-22678",
    "user": "https://github.com/malb"
}
```

Attachment [pbori_weakref.patch](tarball://root/attachments/some-uuid/ticket3284/pbori_weakref.patch) by @malb created at 2008-05-25 16:09:12

this patch is supposed to work



---

archive/issue_comments_022679.json:
```json
{
    "body": "Changing keywords from \"PolyBoRi, segfault\" to \"PolyBoRi\".",
    "created_at": "2008-05-25T16:09:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3284#issuecomment-22679",
    "user": "https://github.com/malb"
}
```

Changing keywords from "PolyBoRi, segfault" to "PolyBoRi".



---

archive/issue_comments_022680.json:
```json
{
    "body": "Please review the updated patch which fixes the doctest failure.",
    "created_at": "2008-05-25T16:10:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3284#issuecomment-22680",
    "user": "https://github.com/malb"
}
```

Please review the updated patch which fixes the doctest failure.



---

archive/issue_comments_022681.json:
```json
{
    "body": "I don't see why the changes to pbori.pyx other than the addition of the R._pbring.activate() at line 4131 are necessary. \n\nIn `BooleanPolynomialRing_constructor`, the if statement (including the elif) at line 430 seems to be redundant, since normalize_names already returns a tuple. It could be that I'm reading the source of normalize_names wrong though.",
    "created_at": "2008-06-04T22:33:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3284#issuecomment-22681",
    "user": "https://github.com/burcin"
}
```

I don't see why the changes to pbori.pyx other than the addition of the R._pbring.activate() at line 4131 are necessary. 

In `BooleanPolynomialRing_constructor`, the if statement (including the elif) at line 430 seems to be redundant, since normalize_names already returns a tuple. It could be that I'm reading the source of normalize_names wrong though.



---

archive/issue_comments_022682.json:
```json
{
    "body": "True, it is unrelated to this particular weakref patch. I mixed up two things. The renaming only cleans up since vars is a built-in identifier and it is considered bad practice to use it like we used to use it.",
    "created_at": "2008-06-04T22:36:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3284#issuecomment-22682",
    "user": "https://github.com/malb"
}
```

True, it is unrelated to this particular weakref patch. I mixed up two things. The renaming only cleans up since vars is a built-in identifier and it is considered bad practice to use it like we used to use it.



---

archive/issue_comments_022683.json:
```json
{
    "body": "Changing keywords from \"PolyBoRi\" to \"PolyBoRi, editor_malb\".",
    "created_at": "2008-06-15T21:48:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3284#issuecomment-22683",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "PolyBoRi" to "PolyBoRi, editor_malb".



---

archive/issue_comments_022684.json:
```json
{
    "body": "BooleanPolynomialRing user friendly names",
    "created_at": "2008-06-20T03:46:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3284#issuecomment-22684",
    "user": "https://github.com/burcin"
}
```

BooleanPolynomialRing user friendly names



---

archive/issue_comments_022685.json:
```json
{
    "body": "Attachment [trac3284_BooleanPolynomialRing_normalize_names.patch](tarball://root/attachments/some-uuid/ticket3284/trac3284_BooleanPolynomialRing_normalize_names.patch) by @burcin created at 2008-06-20 03:53:34\n\n`BooleanPolynomialRing_constructor` in malb's original patch fails when only names are provided, attachment:trac3284_BooleanPolynomialRing_normalize_names.patch fixes this case.\n\nI give malb's patch (followed by mine) a positive review. Someone should review my patch, especially the change to `normalize_names`.",
    "created_at": "2008-06-20T03:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3284#issuecomment-22685",
    "user": "https://github.com/burcin"
}
```

Attachment [trac3284_BooleanPolynomialRing_normalize_names.patch](tarball://root/attachments/some-uuid/ticket3284/trac3284_BooleanPolynomialRing_normalize_names.patch) by @burcin created at 2008-06-20 03:53:34

`BooleanPolynomialRing_constructor` in malb's original patch fails when only names are provided, attachment:trac3284_BooleanPolynomialRing_normalize_names.patch fixes this case.

I give malb's patch (followed by mine) a positive review. Someone should review my patch, especially the change to `normalize_names`.



---

archive/issue_comments_022686.json:
```json
{
    "body": "Burcin's patch looks good and passes doctests.",
    "created_at": "2008-06-24T06:44:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3284#issuecomment-22686",
    "user": "https://github.com/malb"
}
```

Burcin's patch looks good and passes doctests.



---

archive/issue_comments_022687.json:
```json
{
    "body": "All doctests pass with the patch applied and valgrind gives pbori.pyx a clean bill of health.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-25T02:13:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3284#issuecomment-22687",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

All doctests pass with the patch applied and valgrind gives pbori.pyx a clean bill of health.

Cheers,

Michael



---

archive/issue_comments_022688.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-25T02:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3284#issuecomment-22688",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022689.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha1",
    "created_at": "2008-06-25T02:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3284#issuecomment-22689",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha1



---

archive/issue_events_003503.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-25T02:13:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3284",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3284#event-3503"
}
```
