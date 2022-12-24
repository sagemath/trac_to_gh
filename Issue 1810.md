# Issue 1810: [with patch] refactoring to improve finite field reference manual

archive/issues_001810.json:
```json
{
    "body": "Assignee: tba\n\nThe patch removes `FiniteField_prime_modn` from `finite_field.py` because it was odd that this implementation was the only showing up in the reference manual. Also, `GF` is now defined in `rings.all` rather than in `rings.finite_field` to avoid that the documentation for it shows up twice. Finally, a more verbose description of the finite field module is given at the top of the `finite_field.py` file and some doctests were added to `FiniteField_prime_modn`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1810\n\n",
    "created_at": "2008-01-17T21:29:21Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "[with patch] refactoring to improve finite field reference manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1810",
    "user": "malb"
}
```
Assignee: tba

The patch removes `FiniteField_prime_modn` from `finite_field.py` because it was odd that this implementation was the only showing up in the reference manual. Also, `GF` is now defined in `rings.all` rather than in `rings.finite_field` to avoid that the documentation for it shows up twice. Finally, a more verbose description of the finite field module is given at the top of the `finite_field.py` file and some doctests were added to `FiniteField_prime_modn`.

Issue created by migration from https://trac.sagemath.org/ticket/1810





---

archive/issue_comments_011440.json:
```json
{
    "body": "Attachment [finite_field_refactor_doc.patch](tarball://root/attachments/some-uuid/ticket1810/finite_field_refactor_doc.patch) by malb created at 2008-01-17 21:29:32",
    "created_at": "2008-01-17T21:29:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1810#issuecomment-11440",
    "user": "malb"
}
```

Attachment [finite_field_refactor_doc.patch](tarball://root/attachments/some-uuid/ticket1810/finite_field_refactor_doc.patch) by malb created at 2008-01-17 21:29:32



---

archive/issue_comments_011441.json:
```json
{
    "body": "I get the following on a clean 2.10.2 install:\n\n\n```\napplying /home/mike/Desktop/finite_field_refactor_doc.patch\npatching file sage/rings/finite_field.py\nHunk #1 succeeded at 1 with fuzz 2 (offset -2 lines).\nHunk #5 FAILED at 147\n1 out of 13 hunks FAILED -- saving rejects to file sage/rings/finite_field.py.rej\nabort: unable to find sage/rings/padics/eisenstein_extension_generic_element.py or sage/rings/padics/eisenstein_extension_generic_element.py for patching\n\n```\n",
    "created_at": "2008-02-27T18:21:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1810#issuecomment-11441",
    "user": "mhansen"
}
```

I get the following on a clean 2.10.2 install:


```
applying /home/mike/Desktop/finite_field_refactor_doc.patch
patching file sage/rings/finite_field.py
Hunk #1 succeeded at 1 with fuzz 2 (offset -2 lines).
Hunk #5 FAILED at 147
1 out of 13 hunks FAILED -- saving rejects to file sage/rings/finite_field.py.rej
abort: unable to find sage/rings/padics/eisenstein_extension_generic_element.py or sage/rings/padics/eisenstein_extension_generic_element.py for patching

```




---

archive/issue_comments_011442.json:
```json
{
    "body": "I am rebasing right now. `make test` is running and looking good. Then, I'm afraid I'll have to check if I can apply the patch against 2.10.3.alpha0.",
    "created_at": "2008-02-27T18:38:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1810#issuecomment-11442",
    "user": "malb"
}
```

I am rebasing right now. `make test` is running and looking good. Then, I'm afraid I'll have to check if I can apply the patch against 2.10.3.alpha0.



---

archive/issue_comments_011443.json:
```json
{
    "body": "rebased against 2.10.2",
    "created_at": "2008-02-27T18:46:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1810#issuecomment-11443",
    "user": "malb"
}
```

rebased against 2.10.2



---

archive/issue_comments_011444.json:
```json
{
    "body": "Attachment [finite_field_refactor_doc.2.patch](tarball://root/attachments/some-uuid/ticket1810/finite_field_refactor_doc.2.patch) by malb created at 2008-02-27 20:24:05\n\nrebased against 2.10.3.alpha3",
    "created_at": "2008-02-27T20:24:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1810#issuecomment-11444",
    "user": "malb"
}
```

Attachment [finite_field_refactor_doc.2.patch](tarball://root/attachments/some-uuid/ticket1810/finite_field_refactor_doc.2.patch) by malb created at 2008-02-27 20:24:05

rebased against 2.10.3.alpha3



---

archive/issue_comments_011445.json:
```json
{
    "body": "Attachment [finite_field_refactor_doc.3.patch](tarball://root/attachments/some-uuid/ticket1810/finite_field_refactor_doc.3.patch) by malb created at 2008-02-28 00:25:27\n\nadd this on top of the 2.10.3.alpha0 patch, I forgot to hg add a file",
    "created_at": "2008-02-28T00:25:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1810#issuecomment-11445",
    "user": "malb"
}
```

Attachment [finite_field_refactor_doc.3.patch](tarball://root/attachments/some-uuid/ticket1810/finite_field_refactor_doc.3.patch) by malb created at 2008-02-28 00:25:27

add this on top of the 2.10.3.alpha0 patch, I forgot to hg add a file



---

archive/issue_comments_011446.json:
```json
{
    "body": "Attachment [gfp.patch](tarball://root/attachments/some-uuid/ticket1810/gfp.patch) by malb created at 2008-02-28 00:26:34\n\nAdd `gfp.patch` on top of `finite_field_refactor_doc.3.patch`, I forgot to `hg add finite_field_prime_modn.py`",
    "created_at": "2008-02-28T00:26:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1810#issuecomment-11446",
    "user": "malb"
}
```

Attachment [gfp.patch](tarball://root/attachments/some-uuid/ticket1810/gfp.patch) by malb created at 2008-02-28 00:26:34

Add `gfp.patch` on top of `finite_field_refactor_doc.3.patch`, I forgot to `hg add finite_field_prime_modn.py`



---

archive/issue_comments_011447.json:
```json
{
    "body": "Attachment [guava_fix.patch](tarball://root/attachments/some-uuid/ticket1810/guava_fix.patch) by malb created at 2008-02-28 01:14:45\n\nguava_fix.patch needs also to be applied after the other patches",
    "created_at": "2008-02-28T01:14:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1810#issuecomment-11447",
    "user": "malb"
}
```

Attachment [guava_fix.patch](tarball://root/attachments/some-uuid/ticket1810/guava_fix.patch) by malb created at 2008-02-28 01:14:45

guava_fix.patch needs also to be applied after the other patches



---

archive/issue_comments_011448.json:
```json
{
    "body": "Applies cleanly to 2.10.3.alpha0 and passes tests for me.  \n\nTo apply the patch, do the following,\n\n1) Apply finite_field_refactor_doc.3.patch\n\n2) Apply gfp.patch\n\n3) hg add finite_field_prime_modn.py\n\n4) Apply guava_fix.patch",
    "created_at": "2008-02-28T08:37:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1810#issuecomment-11448",
    "user": "mhansen"
}
```

Applies cleanly to 2.10.3.alpha0 and passes tests for me.  

To apply the patch, do the following,

1) Apply finite_field_refactor_doc.3.patch

2) Apply gfp.patch

3) hg add finite_field_prime_modn.py

4) Apply guava_fix.patch



---

archive/issue_comments_011449.json:
```json
{
    "body": "Merged finite_field_refactor_doc.3.patch, gfp.patch and guava_fix.patch in Sage 2.10.3.rc1",
    "created_at": "2008-03-02T22:51:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1810#issuecomment-11449",
    "user": "mabshoff"
}
```

Merged finite_field_refactor_doc.3.patch, gfp.patch and guava_fix.patch in Sage 2.10.3.rc1



---

archive/issue_comments_011450.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-02T22:51:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1810#issuecomment-11450",
    "user": "mabshoff"
}
```

Resolution: fixed
