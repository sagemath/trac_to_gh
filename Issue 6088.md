# Issue 6088: LatticePolytope: Removed a try/catch which could involuntarily hide exceptions from lower code

archive/issues_006088.json:
```json
{
    "body": "Assignee: nthiery\n\nCC:  sage-combinat\n\nKeywords: lattice polytope, exceptions\n\nThis try catch made it hard to discover a trivial bug in Sequences\nbecause it was catching the corresponding exception.\n\nIts purpose was just to test if some data had already been\ncached. This is not on a critical section, so testing on the existence\nof an attribute is as good, clearer, and safer.\n\nBy the way, I would recommend not to use Sequence for this kind of\napplications, as the overhead in speed and complexity is non trivial,\nwhereas the specific features of Sequence do not seem to be very much\nused here. Plain tuples should probably work as well.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6088\n\n",
    "created_at": "2009-05-20T01:06:58Z",
    "labels": [
        "geometry",
        "trivial",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "LatticePolytope: Removed a try/catch which could involuntarily hide exceptions from lower code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6088",
    "user": "nthiery"
}
```
Assignee: nthiery

CC:  sage-combinat

Keywords: lattice polytope, exceptions

This try catch made it hard to discover a trivial bug in Sequences
because it was catching the corresponding exception.

Its purpose was just to test if some data had already been
cached. This is not on a critical section, so testing on the existence
of an attribute is as good, clearer, and safer.

By the way, I would recommend not to use Sequence for this kind of
applications, as the overhead in speed and complexity is non trivial,
whereas the specific features of Sequence do not seem to be very much
used here. Plain tuples should probably work as well.


Issue created by migration from https://trac.sagemath.org/ticket/6088





---

archive/issue_comments_048503.json:
```json
{
    "body": "Attachment [lattice_polytope-trivialfix-6088-nt.patch](tarball://root/attachments/some-uuid/ticket6088/lattice_polytope-trivialfix-6088-nt.patch) by novoselt created at 2009-05-20 02:34:09\n\nGood change, positive review. I have already learned that it is a bad idea to catch exceptions from a bigger than tiny piece of code.\n\nAnd thanks for the comment on Sequence! (Here it was used only for pretty output with \"cr=True\" but probably should not hurt performance too much since operations with nef partitions are long on their own.)",
    "created_at": "2009-05-20T02:34:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6088#issuecomment-48503",
    "user": "novoselt"
}
```

Attachment [lattice_polytope-trivialfix-6088-nt.patch](tarball://root/attachments/some-uuid/ticket6088/lattice_polytope-trivialfix-6088-nt.patch) by novoselt created at 2009-05-20 02:34:09

Good change, positive review. I have already learned that it is a bad idea to catch exceptions from a bigger than tiny piece of code.

And thanks for the comment on Sequence! (Here it was used only for pretty output with "cr=True" but probably should not hurt performance too much since operations with nef partitions are long on their own.)



---

archive/issue_comments_048504.json:
```json
{
    "body": "Merged in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-21T00:33:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6088#issuecomment-48504",
    "user": "mabshoff"
}
```

Merged in Sage 4.0.rc0.

Cheers,

Michael



---

archive/issue_comments_048505.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-21T00:33:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6088#issuecomment-48505",
    "user": "mabshoff"
}
```

Resolution: fixed
