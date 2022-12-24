# Issue 6780: Stability improvement for lattice_polytope

archive/issues_006780.json:
```json
{
    "body": "Assignee: mhampton\n\nAs it was already observed before, there are problems with using LatticePolytope for polytopes with many vertices/points. The problem occurs during pipe calls to PALP for single polytopes and can be avoided using lattice_polytope.all_* functions which work with files. \n\nThis patch switches all interaction with PALP to files by default, while allowing the old method as an option.\n\nIt may affect the speed, but I cannot detect the difference on sage.math. On the other hand, in many cases I had to deal with polytopes which worked fine and fast through files and lead to hang-ups with pipes.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6780\n\n",
    "created_at": "2009-08-20T03:30:22Z",
    "labels": [
        "geometry",
        "major",
        "enhancement"
    ],
    "title": "Stability improvement for lattice_polytope",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6780",
    "user": "novoselt"
}
```
Assignee: mhampton

As it was already observed before, there are problems with using LatticePolytope for polytopes with many vertices/points. The problem occurs during pipe calls to PALP for single polytopes and can be avoided using lattice_polytope.all_* functions which work with files. 

This patch switches all interaction with PALP to files by default, while allowing the old method as an option.

It may affect the speed, but I cannot detect the difference on sage.math. On the other hand, in many cases I had to deal with polytopes which worked fine and fast through files and lead to hang-ups with pipes.

Issue created by migration from https://trac.sagemath.org/ticket/6780





---

archive/issue_comments_055836.json:
```json
{
    "body": "Attachment [trac_6780_stability_improvement_for_lattice_polytope.patch](tarball://root/attachments/some-uuid/ticket6780/trac_6780_stability_improvement_for_lattice_polytope.patch) by novoselt created at 2009-08-20 03:32:14",
    "created_at": "2009-08-20T03:32:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6780#issuecomment-55836",
    "user": "novoselt"
}
```

Attachment [trac_6780_stability_improvement_for_lattice_polytope.patch](tarball://root/attachments/some-uuid/ticket6780/trac_6780_stability_improvement_for_lattice_polytope.patch) by novoselt created at 2009-08-20 03:32:14



---

archive/issue_comments_055837.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-24T15:25:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6780#issuecomment-55837",
    "user": "mhampton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_055838.json:
```json
{
    "body": "This passes all tests and definitely seems like an improvement.  The solution does seem a little complicated, and it seems unlikely that the always_use_files(False) option will be used by anyone, but that's OK.  Its always hard to say what people actually use, so leaving that in as an option is good.",
    "created_at": "2009-10-24T15:25:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6780#issuecomment-55838",
    "user": "mhampton"
}
```

This passes all tests and definitely seems like an improvement.  The solution does seem a little complicated, and it seems unlikely that the always_use_files(False) option will be used by anyone, but that's OK.  Its always hard to say what people actually use, so leaving that in as an option is good.



---

archive/issue_comments_055839.json:
```json
{
    "body": "This patch is included as a part of a rebased patch for #6831.",
    "created_at": "2009-10-30T05:35:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6780#issuecomment-55839",
    "user": "novoselt"
}
```

This patch is included as a part of a rebased patch for #6831.



---

archive/issue_comments_055840.json:
```json
{
    "body": "Fixed in #6831.",
    "created_at": "2009-11-02T04:36:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6780#issuecomment-55840",
    "user": "mhansen"
}
```

Fixed in #6831.



---

archive/issue_comments_055841.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-02T04:36:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6780#issuecomment-55841",
    "user": "mhansen"
}
```

Resolution: fixed
