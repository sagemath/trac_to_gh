# Issue 5576: [with patch, needs review] MPolynomialSystem cleanup

archive/issues_005576.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @mwhansen\n\nKeywords: crypto\n\n* clean up of ReST in `mq.MPolynomialSystem`\n* improved documentation of `mq.MPolynomialSystem`\n* deprecated `mq.MPolynomialSystem_gf2e.change_ring()`\n* added `mq.MPolynomialSystem_gf2e.weil_restriction()`\n* added `mq.MPolynomialSystem.connected_components()`\n* added `mq.MPolynomialSystem.connection_graph()`\n* added `mq.MPolynomialSystem_gf2.eliminate_linear_variables()`\n\nIssue created by migration from https://trac.sagemath.org/ticket/5576\n\n",
    "created_at": "2009-03-20T13:39:50Z",
    "labels": [
        "component: commutative algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "[with patch, needs review] MPolynomialSystem cleanup",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5576",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  @mwhansen

Keywords: crypto

* clean up of ReST in `mq.MPolynomialSystem`
* improved documentation of `mq.MPolynomialSystem`
* deprecated `mq.MPolynomialSystem_gf2e.change_ring()`
* added `mq.MPolynomialSystem_gf2e.weil_restriction()`
* added `mq.MPolynomialSystem.connected_components()`
* added `mq.MPolynomialSystem.connection_graph()`
* added `mq.MPolynomialSystem_gf2.eliminate_linear_variables()`

Issue created by migration from https://trac.sagemath.org/ticket/5576





---

archive/issue_comments_043393.json:
```json
{
    "body": "The attached patch depends on #5569",
    "created_at": "2009-03-20T13:41:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5576#issuecomment-43393",
    "user": "https://github.com/malb"
}
```

The attached patch depends on #5569



---

archive/issue_comments_043394.json:
```json
{
    "body": "First I applied the patch at #5569 against Sage 3.4, then I applied the patch on this ticket. Doctesting gave me timed out errors:\n\n```\n[mvngu@sage sage-3.4]$ sage -t -long devel/sage-5576/sage/crypto/mq/\nsage -t -long \"devel/sage-5576/sage/crypto/mq/sbox.py\"      \n         [11.3 s]\nsage -t -long \"devel/sage-5576/sage/crypto/mq/mpolynomialsystemgenerator.py\"\n         [7.6 s]\nsage -t -long \"devel/sage-5576/sage/crypto/mq/sr.py\"        \n*** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n*** *** Error: TIMED OUT! *** ***\n*** *** Error: TIMED OUT! *** ***\n         [1800.5 s]\nsage -t -long \"devel/sage-5576/sage/crypto/mq/mpolynomialsystem.py\"\n         [24.4 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t -long \"devel/sage-5576/sage/crypto/mq/sr.py\"\nTotal time for all tests: 1843.9 seconds\n```\n",
    "created_at": "2009-03-27T06:13:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5576#issuecomment-43394",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

First I applied the patch at #5569 against Sage 3.4, then I applied the patch on this ticket. Doctesting gave me timed out errors:

```
[mvngu@sage sage-3.4]$ sage -t -long devel/sage-5576/sage/crypto/mq/
sage -t -long "devel/sage-5576/sage/crypto/mq/sbox.py"      
         [11.3 s]
sage -t -long "devel/sage-5576/sage/crypto/mq/mpolynomialsystemgenerator.py"
         [7.6 s]
sage -t -long "devel/sage-5576/sage/crypto/mq/sr.py"        
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
*** *** Error: TIMED OUT! *** ***
         [1800.5 s]
sage -t -long "devel/sage-5576/sage/crypto/mq/mpolynomialsystem.py"
         [24.4 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage-5576/sage/crypto/mq/sr.py"
Total time for all tests: 1843.9 seconds
```




---

archive/issue_comments_043395.json:
```json
{
    "body": "I can reproduce your problem and I'll look into it. Thanks.",
    "created_at": "2009-03-27T11:04:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5576#issuecomment-43395",
    "user": "https://github.com/malb"
}
```

I can reproduce your problem and I'll look into it. Thanks.



---

archive/issue_comments_043396.json:
```json
{
    "body": "I fixed the underlying issue and will raise a question on [sage-devel] how to deal with the API change that caused it.",
    "created_at": "2009-03-27T11:11:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5576#issuecomment-43396",
    "user": "https://github.com/malb"
}
```

I fixed the underlying issue and will raise a question on [sage-devel] how to deal with the API change that caused it.



---

archive/issue_comments_043397.json:
```json
{
    "body": "With the latest stable version sage-3.4.2, i.e. the \"post-final\" 3.4.2 version, I get the following hunk failures:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: 5576\nsage: hg_sage.apply(\"/home/mvngu/patch/5576/mpolynomialsystem_rest.patch\")\ncd \"/scratch/mvngu/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage\" && hg status\ncd \"/scratch/mvngu/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage\" && hg status\ncd \"/scratch/mvngu/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage\" && hg import   \"/home/mvngu/patch/5576/mpolynomialsystem_rest.patch\"\napplying /home/mvngu/patch/5576/mpolynomialsystem_rest.patch\npatching file sage/crypto/mq/mpolynomialsystem.py\nHunk #7 FAILED at 262\nHunk #8 FAILED at 277\nHunk #9 FAILED at 314\nHunk #22 FAILED at 652\n4 out of 51 hunks FAILED -- saving rejects to file sage/crypto/mq/mpolynomialsystem.py.rej\nabort: patch failed to apply\n```\n",
    "created_at": "2009-05-08T01:16:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5576#issuecomment-43397",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

With the latest stable version sage-3.4.2, i.e. the "post-final" 3.4.2 version, I get the following hunk failures:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: 5576
sage: hg_sage.apply("/home/mvngu/patch/5576/mpolynomialsystem_rest.patch")
cd "/scratch/mvngu/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage" && hg status
cd "/scratch/mvngu/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage" && hg status
cd "/scratch/mvngu/sage-3.4.2-sage.math-only-x86_64-Linux/devel/sage" && hg import   "/home/mvngu/patch/5576/mpolynomialsystem_rest.patch"
applying /home/mvngu/patch/5576/mpolynomialsystem_rest.patch
patching file sage/crypto/mq/mpolynomialsystem.py
Hunk #7 FAILED at 262
Hunk #8 FAILED at 277
Hunk #9 FAILED at 314
Hunk #22 FAILED at 652
4 out of 51 hunks FAILED -- saving rejects to file sage/crypto/mq/mpolynomialsystem.py.rej
abort: patch failed to apply
```




---

archive/issue_comments_043398.json:
```json
{
    "body": "I rebased the patch.",
    "created_at": "2009-05-12T00:07:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5576#issuecomment-43398",
    "user": "https://github.com/malb"
}
```

I rebased the patch.



---

archive/issue_comments_043399.json:
```json
{
    "body": "Attachment [mpolynomialsystem_rest.patch](tarball://root/attachments/some-uuid/ticket5576/mpolynomialsystem_rest.patch) by @malb created at 2009-05-12 00:34:04",
    "created_at": "2009-05-12T00:34:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5576#issuecomment-43399",
    "user": "https://github.com/malb"
}
```

Attachment [mpolynomialsystem_rest.patch](tarball://root/attachments/some-uuid/ticket5576/mpolynomialsystem_rest.patch) by @malb created at 2009-05-12 00:34:04



---

archive/issue_comments_043400.json:
```json
{
    "body": "\n```\n[01:15] <mhansen> malb: You need to fix the REFERENCES section in eliminate_linear_variables([01:16] <malb> what about it?\n[01:18] <mhansen> The text after the .. should all be aligned.\n[01:18] <mhansen> (on the left.\n```\n\n\nfixed in updated patch.",
    "created_at": "2009-05-12T00:35:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5576#issuecomment-43400",
    "user": "https://github.com/malb"
}
```


```
[01:15] <mhansen> malb: You need to fix the REFERENCES section in eliminate_linear_variables([01:16] <malb> what about it?
[01:18] <mhansen> The text after the .. should all be aligned.
[01:18] <mhansen> (on the left.
```


fixed in updated patch.



---

archive/issue_comments_043401.json:
```json
{
    "body": "Patch looks good, doctests pass.",
    "created_at": "2009-05-12T14:33:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5576#issuecomment-43401",
    "user": "https://github.com/burcin"
}
```

Patch looks good, doctests pass.



---

archive/issue_comments_043402.json:
```json
{
    "body": "Merged in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-12T17:15:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5576#issuecomment-43402",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_events_005821.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-05-12T17:15:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5576",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5576#event-5821"
}
```



---

archive/issue_comments_043403.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-12T17:15:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5576#issuecomment-43403",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
