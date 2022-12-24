# Issue 2274: guava->python, 1

archive/issues_002274.json:
```json
{
    "body": "Assignee: rlm\n\nFor various reasons, ease of maintenance among others, the coding theory functions in SAGE which are GAP wrappers for GUAVA functions will be moved over to pure Python/SAGE. This is just a \"first installment\". In this patch (to be attached once the testall suite is completed)\n\nHammingCode, CyclicCode, dual_code, put_standard_form,\n\nare moved over and the simple function LinearCodeFromCheckMatrix is added.\nThe amusing utility function \"permutation_action\" is needed, which provides a\n(left) action of SymmetricGroup(n) on a list/vector/sequence/matrix of\nlength n.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2274\n\n",
    "created_at": "2008-02-23T02:50:35Z",
    "labels": [
        "coding theory",
        "minor",
        "enhancement"
    ],
    "title": "guava->python, 1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2274",
    "user": "wdj"
}
```
Assignee: rlm

For various reasons, ease of maintenance among others, the coding theory functions in SAGE which are GAP wrappers for GUAVA functions will be moved over to pure Python/SAGE. This is just a "first installment". In this patch (to be attached once the testall suite is completed)

HammingCode, CyclicCode, dual_code, put_standard_form,

are moved over and the simple function LinearCodeFromCheckMatrix is added.
The amusing utility function "permutation_action" is needed, which provides a
(left) action of SymmetricGroup(n) on a list/vector/sequence/matrix of
length n.

Issue created by migration from https://trac.sagemath.org/ticket/2274





---

archive/issue_comments_015079.json:
```json
{
    "body": "The bundle was too large to post for some reason. It is at\nhttp://sage.math.washington.edu/home/wdj/patches/coding_23-02-2008.hg\nModified were the files \nall.py (moved HammingCode from guava to code_constructions, etc)\nlinear_code.py (rewrote standard_form and dual_code in python, so they do not call GAP)\nguava.py (deleted HammingCode and CyclicCode)\ncode_constructions.py (added pure python functions HammingCode, CyclicCodeFromGeneratorPolynomial, CyclicCodeFromCheckPolynomial, LinearCodeFromCheckMatrix, and some utility functions)",
    "created_at": "2008-02-23T14:46:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2274#issuecomment-15079",
    "user": "wdj"
}
```

The bundle was too large to post for some reason. It is at
http://sage.math.washington.edu/home/wdj/patches/coding_23-02-2008.hg
Modified were the files 
all.py (moved HammingCode from guava to code_constructions, etc)
linear_code.py (rewrote standard_form and dual_code in python, so they do not call GAP)
guava.py (deleted HammingCode and CyclicCode)
code_constructions.py (added pure python functions HammingCode, CyclicCodeFromGeneratorPolynomial, CyclicCodeFromCheckPolynomial, LinearCodeFromCheckMatrix, and some utility functions)



---

archive/issue_comments_015080.json:
```json
{
    "body": "I'm sorry, I should add that this passes sage -testall, except for the file const.tex. I'll fix this separately. (There is no way I know of to create a mercurial bundle containing both code patches and doc fixes.)",
    "created_at": "2008-02-23T14:48:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2274#issuecomment-15080",
    "user": "wdj"
}
```

I'm sorry, I should add that this passes sage -testall, except for the file const.tex. I'll fix this separately. (There is no way I know of to create a mercurial bundle containing both code patches and doc fixes.)



---

archive/issue_comments_015081.json:
```json
{
    "body": "I am dubious about any bundle larger than a couple dozen kilobytes, especially for something like this. In comparison David Roe's padics bundle topped out at about 150kb with a hundred+ commits. I will have a look, but it sounds like you need to do this again with a clean 2.10.2 and your code applied.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-23T15:01:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2274#issuecomment-15081",
    "user": "mabshoff"
}
```

I am dubious about any bundle larger than a couple dozen kilobytes, especially for something like this. In comparison David Roe's padics bundle topped out at about 150kb with a hundred+ commits. I will have a look, but it sounds like you need to do this again with a clean 2.10.2 and your code applied.

Cheers,

Michael



---

archive/issue_comments_015082.json:
```json
{
    "body": "Replying to [comment:2 wdj]:\n> I'm sorry, I should add that this passes sage -testall, except for the file const.tex. I'll fix this separately. (There is no way I know of to create a mercurial bundle containing both code patches and doc fixes.)\n\nSince the code for documentation and the sage library are in different repos you cannot submit a bundle that contains changesets from both repos. I would also plead you once more to use the export command, if needed via the command line, i.e. `hg export $CHANGESET` because there are clearly some issues with the way you do bundle :(\n\nCheers,\n\nMichael",
    "created_at": "2008-02-23T15:03:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2274#issuecomment-15082",
    "user": "mabshoff"
}
```

Replying to [comment:2 wdj]:
> I'm sorry, I should add that this passes sage -testall, except for the file const.tex. I'll fix this separately. (There is no way I know of to create a mercurial bundle containing both code patches and doc fixes.)

Since the code for documentation and the sage library are in different repos you cannot submit a bundle that contains changesets from both repos. I would also plead you once more to use the export command, if needed via the command line, i.e. `hg export $CHANGESET` because there are clearly some issues with the way you do bundle :(

Cheers,

Michael



---

archive/issue_comments_015083.json:
```json
{
    "body": "I don't know how to export a doc bundle (and I've tried many different ways). I'm attaching the patch, just in case.",
    "created_at": "2008-02-23T15:11:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2274#issuecomment-15083",
    "user": "wdj"
}
```

I don't know how to export a doc bundle (and I've tried many different ways). I'm attaching the patch, just in case.



---

archive/issue_comments_015084.json:
```json
{
    "body": "Attachment [8672.patch](tarball://root/attachments/some-uuid/ticket2274/8672.patch) by wdj created at 2008-02-23 15:12:06",
    "created_at": "2008-02-23T15:12:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2274#issuecomment-15084",
    "user": "wdj"
}
```

Attachment [8672.patch](tarball://root/attachments/some-uuid/ticket2274/8672.patch) by wdj created at 2008-02-23 15:12:06



---

archive/issue_comments_015085.json:
```json
{
    "body": "I just figured out how to export a doc bundle to a patch. It's actually obvious and easy, so I don't know what the problem was before. It is attached too. \n\nCan you tell me if these are acceptable or if they need to be redone?",
    "created_at": "2008-02-23T15:18:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2274#issuecomment-15085",
    "user": "wdj"
}
```

I just figured out how to export a doc bundle to a patch. It's actually obvious and easy, so I don't know what the problem was before. It is attached too. 

Can you tell me if these are acceptable or if they need to be redone?



---

archive/issue_comments_015086.json:
```json
{
    "body": "Attachment [435.patch](tarball://root/attachments/some-uuid/ticket2274/435.patch) by wdj created at 2008-02-23 15:18:48",
    "created_at": "2008-02-23T15:18:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2274#issuecomment-15086",
    "user": "wdj"
}
```

Attachment [435.patch](tarball://root/attachments/some-uuid/ticket2274/435.patch) by wdj created at 2008-02-23 15:18:48



---

archive/issue_comments_015087.json:
```json
{
    "body": "Replying to [comment:5 wdj]:\n> I don't know how to export a doc bundle (and I've tried many different ways). I'm attaching the patch, just in case.\n\nThe patch looks good and does apply cleanly against my 2.10.3.alpha0. That isn't a formal review, just a technical observation. The reason the bundle is so large because William hasn't pushed out the changes from 2.10.2 to the repos and it contains every commit from 2.10.1 onward. So in the end it is all William's fault :)\n\nTo export the doc patch go into `$SAGE_ROOT/devel/doc` and us hg to do an `hg export tip` (at least for the last commit). You can do the same using Sage's hg interface to the doc repo, i.e. do `hg_doc.log()` to see the changelog.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-23T15:20:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2274#issuecomment-15087",
    "user": "mabshoff"
}
```

Replying to [comment:5 wdj]:
> I don't know how to export a doc bundle (and I've tried many different ways). I'm attaching the patch, just in case.

The patch looks good and does apply cleanly against my 2.10.3.alpha0. That isn't a formal review, just a technical observation. The reason the bundle is so large because William hasn't pushed out the changes from 2.10.2 to the repos and it contains every commit from 2.10.1 onward. So in the end it is all William's fault :)

To export the doc patch go into `$SAGE_ROOT/devel/doc` and us hg to do an `hg export tip` (at least for the last commit). You can do the same using Sage's hg interface to the doc repo, i.e. do `hg_doc.log()` to see the changelog.

Cheers,

Michael



---

archive/issue_comments_015088.json:
```json
{
    "body": "Replying to [comment:6 wdj]:\n> I just figured out how to export a doc bundle to a patch. It's actually obvious and easy, so I don't know what the problem was before. It is attached too. \n> \n> Can you tell me if these are acceptable or if they need to be redone?\n\nI can now see that we crossed paths while I wrote the answer to your initial question. Both patches look correct and apply cleanly against my current repo. So once they get positively reviewed (by rlm?) they can go in.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-23T15:22:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2274#issuecomment-15088",
    "user": "mabshoff"
}
```

Replying to [comment:6 wdj]:
> I just figured out how to export a doc bundle to a patch. It's actually obvious and easy, so I don't know what the problem was before. It is attached too. 
> 
> Can you tell me if these are acceptable or if they need to be redone?

I can now see that we crossed paths while I wrote the answer to your initial question. Both patches look correct and apply cleanly against my current repo. So once they get positively reviewed (by rlm?) they can go in.

Cheers,

Michael



---

archive/issue_comments_015089.json:
```json
{
    "body": "- I noticed that you changed many instances of `from blah import *` to `from blah import one_specific_thing`. Awesome!\n- Since you did testall, I just tested the `sage/coding` module, and everything seems fine.\n- I strongly support the move from Guava to Python for this functionality. Tom Boothby and I are going to start working on something similar for permutation groups (not just elements).",
    "created_at": "2008-02-24T19:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2274#issuecomment-15089",
    "user": "rlm"
}
```

- I noticed that you changed many instances of `from blah import *` to `from blah import one_specific_thing`. Awesome!
- Since you did testall, I just tested the `sage/coding` module, and everything seems fine.
- I strongly support the move from Guava to Python for this functionality. Tom Boothby and I are going to start working on something similar for permutation groups (not just elements).



---

archive/issue_comments_015090.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-25T02:29:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2274#issuecomment-15090",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015091.json:
```json
{
    "body": "Both patches merged in Sage 2.10.3.alpha0",
    "created_at": "2008-02-25T02:29:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2274#issuecomment-15091",
    "user": "mabshoff"
}
```

Both patches merged in Sage 2.10.3.alpha0
