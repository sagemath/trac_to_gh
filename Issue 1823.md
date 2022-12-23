# Issue 1823: [with patch] RDF/CDF coverage, consistent hashing

archive/issues_001823.json:
```json
{
    "body": "Assignee: somebody\n\nSome functions, e.g. one-liners and stuff dealing with the RDF pool, are hard or useless to test in the doctest setting. \n\nHashing is now consistent between RDF, RR, CDF, CC, float, and complex. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1823\n\n",
    "created_at": "2008-01-18T02:14:07Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "[with patch] RDF/CDF coverage, consistent hashing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1823",
    "user": "robertwb"
}
```
Assignee: somebody

Some functions, e.g. one-liners and stuff dealing with the RDF pool, are hard or useless to test in the doctest setting. 

Hashing is now consistent between RDF, RR, CDF, CC, float, and complex. 

Issue created by migration from https://trac.sagemath.org/ticket/1823





---

archive/issue_comments_011535.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-01-18T02:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1823#issuecomment-11535",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_011536.json:
```json
{
    "body": "Changing assignee from somebody to robertwb.",
    "created_at": "2008-01-18T02:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1823#issuecomment-11536",
    "user": "robertwb"
}
```

Changing assignee from somebody to robertwb.



---

archive/issue_comments_011537.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-18T02:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1823#issuecomment-11537",
    "user": "robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011538.json:
```json
{
    "body": "I get the following error after the patch:\n\n```\n    sage: whole, parts = q.partial_fraction_decomposition(); parts\nExpected:\n    [(-7.6294e-6*x^2 + 1.0000)/(1.0000*x^4 + 4.0000*x^2 + 4.0000), 1.0000/(1.0000*x - 1.0000)]\nGot:\n    [1.0000/(1.0000*x - 1.0000), (-7.6294e-6*x^2 + 1.0000)/(1.0000*x^4 + 4.0000*x^2 + 4.0000)]\n```\n",
    "created_at": "2008-01-21T05:01:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1823#issuecomment-11538",
    "user": "mhansen"
}
```

I get the following error after the patch:

```
    sage: whole, parts = q.partial_fraction_decomposition(); parts
Expected:
    [(-7.6294e-6*x^2 + 1.0000)/(1.0000*x^4 + 4.0000*x^2 + 4.0000), 1.0000/(1.0000*x - 1.0000)]
Got:
    [1.0000/(1.0000*x - 1.0000), (-7.6294e-6*x^2 + 1.0000)/(1.0000*x^4 + 4.0000*x^2 + 4.0000)]
```




---

archive/issue_comments_011539.json:
```json
{
    "body": "This is just an ordering issue (which is arbitrary), the doctest can be changed.",
    "created_at": "2008-01-22T06:45:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1823#issuecomment-11539",
    "user": "robertwb"
}
```

This is just an ordering issue (which is arbitrary), the doctest can be changed.



---

archive/issue_comments_011540.json:
```json
{
    "body": "Patch looks excellent.  I would like the int(...) and long(...) functions to actually doctest that their output has the expected type, but that's a small issue.\n\nI cannot speak to whether the hashing strategy is a good design decision.",
    "created_at": "2008-01-22T19:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1823#issuecomment-11540",
    "user": "ncalexan"
}
```

Patch looks excellent.  I would like the int(...) and long(...) functions to actually doctest that their output has the expected type, but that's a small issue.

I cannot speak to whether the hashing strategy is a good design decision.



---

archive/issue_comments_011541.json:
```json
{
    "body": "robertwb claims \"Hashing is now consistent between RDF, RR, CDF, CC, float, and complex.\"\n\nIs this doctested?  I don't think so.  It should be.  Should this maybe go in the module level tests for RDF, CDF, or something like that?",
    "created_at": "2008-01-22T19:07:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1823#issuecomment-11541",
    "user": "ncalexan"
}
```

robertwb claims "Hashing is now consistent between RDF, RR, CDF, CC, float, and complex."

Is this doctested?  I don't think so.  It should be.  Should this maybe go in the module level tests for RDF, CDF, or something like that?



---

archive/issue_comments_011542.json:
```json
{
    "body": "Yes, the consistency between RDF, RR, CDF, CC, float, and complex is doctested, the doctests for the `__hash__` functions each test against hashing the native Python type.",
    "created_at": "2008-01-26T08:48:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1823#issuecomment-11542",
    "user": "robertwb"
}
```

Yes, the consistency between RDF, RR, CDF, CC, float, and complex is doctested, the doctests for the `__hash__` functions each test against hashing the native Python type.



---

archive/issue_comments_011543.json:
```json
{
    "body": "Attachment\n\nOnce both rdf-cdf-coverage.diff and rdf-cdf-fixup.patch are applied, all doctests pass on both 32-bit and 64-bit x86 Linux.\n\nThe code looks good.",
    "created_at": "2008-01-27T21:24:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1823#issuecomment-11543",
    "user": "cwitty"
}
```

Attachment

Once both rdf-cdf-coverage.diff and rdf-cdf-fixup.patch are applied, all doctests pass on both 32-bit and 64-bit x86 Linux.

The code looks good.



---

archive/issue_comments_011544.json:
```json
{
    "body": "I had a trivial reject for Robert's patch which I resolved manually. See\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc2/trac_1823_rdf-cdf-coverage-missing-hunk.patch\n\nCheers,\n\nMichael",
    "created_at": "2008-01-27T22:20:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1823#issuecomment-11544",
    "user": "mabshoff"
}
```

I had a trivial reject for Robert's patch which I resolved manually. See

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc2/trac_1823_rdf-cdf-coverage-missing-hunk.patch

Cheers,

Michael



---

archive/issue_comments_011545.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc2",
    "created_at": "2008-01-27T22:21:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1823#issuecomment-11545",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.rc2



---

archive/issue_comments_011546.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-27T22:21:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1823#issuecomment-11546",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011547.json:
```json
{
    "body": "Attachment\n\n\n```\n[23:19] <mabshoff> cwitty: after applying #1823 I have a comple_double.h and complex_double_api.h \n[23:20] <mabshoff> in sage/rings all the sudden.\n[23:20] <mabshoff> And hg claims they are not under revision control. Any idea what is up with that?\n[23:22] <cwitty> mabshoff, strange Cython magic?\n[23:23] <mabshoff> No clue. I grepped the tree for any file including them and there are none.\n[23:23] <cwitty> They're clearly autogenerated, and are probably caused by this:\n[23:23] <cwitty> cdef public api ComplexDoubleElement new_ComplexDoubleElement()\n[23:23] <cwitty> from Robert's patch.\n[23:23] <mabshoff> ok\n[23:23] <cwitty> But I don't know why Robert thought that should be public.\n[23:24] <mabshoff> Maybe something that he will follow up with?\n[23:24] <mabshoff> But what to do? Put them into the repo? I don't think we will get an answer today.\n[23:25] <cwitty> No; I think add them to .hgignore.\n[23:25] <cwitty> (Auto-generated files shouldn't go in the repository.)\n```\n\n\nAd per cwitty suggestion I added the to .hgignore. The patch attached above has one extra, erroneous change (sage->SAGE [damn vi]), that I reverted already in my repo. It is just attached for the record. If adding those two files to `.hgignore` was a mistake please let us know.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-27T22:47:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1823#issuecomment-11547",
    "user": "mabshoff"
}
```

Attachment


```
[23:19] <mabshoff> cwitty: after applying #1823 I have a comple_double.h and complex_double_api.h 
[23:20] <mabshoff> in sage/rings all the sudden.
[23:20] <mabshoff> And hg claims they are not under revision control. Any idea what is up with that?
[23:22] <cwitty> mabshoff, strange Cython magic?
[23:23] <mabshoff> No clue. I grepped the tree for any file including them and there are none.
[23:23] <cwitty> They're clearly autogenerated, and are probably caused by this:
[23:23] <cwitty> cdef public api ComplexDoubleElement new_ComplexDoubleElement()
[23:23] <cwitty> from Robert's patch.
[23:23] <mabshoff> ok
[23:23] <cwitty> But I don't know why Robert thought that should be public.
[23:24] <mabshoff> Maybe something that he will follow up with?
[23:24] <mabshoff> But what to do? Put them into the repo? I don't think we will get an answer today.
[23:25] <cwitty> No; I think add them to .hgignore.
[23:25] <cwitty> (Auto-generated files shouldn't go in the repository.)
```


Ad per cwitty suggestion I added the to .hgignore. The patch attached above has one extra, erroneous change (sage->SAGE [damn vi]), that I reverted already in my repo. It is just attached for the record. If adding those two files to `.hgignore` was a mistake please let us know.

Cheers,

Michael
