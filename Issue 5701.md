# Issue 5701: Remove Guava from standard Sage

archive/issues_005701.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  wdj\n\nWe currently ship Guava per default in the GAP.spkg. But Guava is limited in functionality, i.e. compared to Magma see http://wiki.sagemath.org/magma#CodingTheory for a list by wdj, and tends to crash at exit, too.  \n\nThe following doctests fail when guava is removed from the GAP spkg. \n\n```\n\tsage -t -long \"devel/sage/sage/combinat/combinat.py\"\n\tsage -t -long \"devel/sage/sage/combinat/designs/block_design.py\"\n\tsage -t -long \"devel/sage/sage/coding/linear_code.py\"\n\tsage -t -long \"devel/sage/sage/coding/code_bounds.py\"\n\tsage -t -long \"devel/sage/sage/coding/code_constructions.py\"\n\tsage -t -long \"devel/sage/sage/coding/guava.py\"\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5701\n\n",
    "created_at": "2009-04-06T21:57:46Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "Remove Guava from standard Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5701",
    "user": "mabshoff"
}
```
Assignee: rlm

CC:  wdj

We currently ship Guava per default in the GAP.spkg. But Guava is limited in functionality, i.e. compared to Magma see http://wiki.sagemath.org/magma#CodingTheory for a list by wdj, and tends to crash at exit, too.  

The following doctests fail when guava is removed from the GAP spkg. 

```
	sage -t -long "devel/sage/sage/combinat/combinat.py"
	sage -t -long "devel/sage/sage/combinat/designs/block_design.py"
	sage -t -long "devel/sage/sage/coding/linear_code.py"
	sage -t -long "devel/sage/sage/coding/code_bounds.py"
	sage -t -long "devel/sage/sage/coding/code_constructions.py"
	sage -t -long "devel/sage/sage/coding/guava.py"
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5701





---

archive/issue_comments_044557.json:
```json
{
    "body": "Attachment [trac_5701-guava-extraction.patch](tarball://root/attachments/some-uuid/ticket5701/trac_5701-guava-extraction.patch) by wdj created at 2009-05-20 18:28:08\n\nbased on 4.0.a0",
    "created_at": "2009-05-20T18:28:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5701#issuecomment-44557",
    "user": "wdj"
}
```

Attachment [trac_5701-guava-extraction.patch](tarball://root/attachments/some-uuid/ticket5701/trac_5701-guava-extraction.patch) by wdj created at 2009-05-20 18:28:08

based on 4.0.a0



---

archive/issue_comments_044558.json:
```json
{
    "body": "Attachment [trac_5701-ref-suggestions.patch](tarball://root/attachments/some-uuid/ticket5701/trac_5701-ref-suggestions.patch) by rlm created at 2009-05-20 18:34:06\n\nI have run tests and checked the code here, and everything seems fine, with the following caveat: I did not run tests on a fresh install, i.e. I ran tests on a system with Guava still installed.\n\nI will give this a positive review, pending the tests passing on a system with the right GAP spkg and workspace setup, and  wdj will follow up on #6094.",
    "created_at": "2009-05-20T18:34:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5701#issuecomment-44558",
    "user": "rlm"
}
```

Attachment [trac_5701-ref-suggestions.patch](tarball://root/attachments/some-uuid/ticket5701/trac_5701-ref-suggestions.patch) by rlm created at 2009-05-20 18:34:06

I have run tests and checked the code here, and everything seems fine, with the following caveat: I did not run tests on a fresh install, i.e. I ran tests on a system with Guava still installed.

I will give this a positive review, pending the tests passing on a system with the right GAP spkg and workspace setup, and  wdj will follow up on #6094.



---

archive/issue_comments_044559.json:
```json
{
    "body": "Attachment [trac_5701-guava-extraction2.patch](tarball://root/attachments/some-uuid/ticket5701/trac_5701-guava-extraction2.patch) by wdj created at 2009-05-25 23:28:32\n\nto be applied after the other 2 patches (all three can be based on 4.0.rc0)",
    "created_at": "2009-05-25T23:28:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5701#issuecomment-44559",
    "user": "wdj"
}
```

Attachment [trac_5701-guava-extraction2.patch](tarball://root/attachments/some-uuid/ticket5701/trac_5701-guava-extraction2.patch) by wdj created at 2009-05-25 23:28:32

to be applied after the other 2 patches (all three can be based on 4.0.rc0)



---

archive/issue_comments_044560.json:
```json
{
    "body": "I just added a third patch. If you remove guava from gap*/pkg, reset the GAP workspace, and then apply these three patches then all tests pass on a 64bit ubuntu 9.04 machine.",
    "created_at": "2009-05-26T02:08:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5701#issuecomment-44560",
    "user": "wdj"
}
```

I just added a third patch. If you remove guava from gap*/pkg, reset the GAP workspace, and then apply these three patches then all tests pass on a 64bit ubuntu 9.04 machine.



---

archive/issue_comments_044561.json:
```json
{
    "body": "Since you are adding an input to `wtdist_gap`, you also need to add a description to the INPUT section.",
    "created_at": "2009-05-26T06:36:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5701#issuecomment-44561",
    "user": "rlm"
}
```

Since you are adding an input to `wtdist_gap`, you also need to add a description to the INPUT section.



---

archive/issue_comments_044562.json:
```json
{
    "body": "Attachment [trac_5701-ref-suggestions2.patch](tarball://root/attachments/some-uuid/ticket5701/trac_5701-ref-suggestions2.patch) by wdj created at 2009-06-05 11:54:57\n\nto be applied after the others.",
    "created_at": "2009-06-05T11:54:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5701#issuecomment-44562",
    "user": "wdj"
}
```

Attachment [trac_5701-ref-suggestions2.patch](tarball://root/attachments/some-uuid/ticket5701/trac_5701-ref-suggestions2.patch) by wdj created at 2009-06-05 11:54:57

to be applied after the others.



---

archive/issue_comments_044563.json:
```json
{
    "body": "Adds 2 line description to linear_code.py docstring following referees suggestion.",
    "created_at": "2009-06-05T11:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5701#issuecomment-44563",
    "user": "wdj"
}
```

Adds 2 line description to linear_code.py docstring following referees suggestion.



---

archive/issue_comments_044564.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-12T07:34:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5701#issuecomment-44564",
    "user": "ncalexan"
}
```

Resolution: fixed
