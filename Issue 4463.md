# Issue 4463: modular/abvar/homspace.py doctests are long

archive/issues_004463.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @williamstein\n\nKeywords: abvar, homspace, long\n\nThe doctests in modular/abvar/homspace.py timeout on my PPC mac, so something in there takes long enough that it should get the \"# long time\" comment.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4463\n\n",
    "created_at": "2008-11-07T17:08:32Z",
    "labels": [
        "component: doctest",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "modular/abvar/homspace.py doctests are long",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4463",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: mabshoff

CC:  @williamstein

Keywords: abvar, homspace, long

The doctests in modular/abvar/homspace.py timeout on my PPC mac, so something in there takes long enough that it should get the "# long time" comment.

Issue created by migration from https://trac.sagemath.org/ticket/4463





---

archive/issue_comments_032889.json:
```json
{
    "body": "This ought to get fixed in Sage 3.2.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-16T08:59:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4463#issuecomment-32889",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This ought to get fixed in Sage 3.2.

Cheers,

Michael



---

archive/issue_comments_032890.json:
```json
{
    "body": "Attachment [trac-4463.patch](tarball://root/attachments/some-uuid/ticket4463/trac-4463.patch) by @craigcitro created at 2008-11-23 11:12:04",
    "created_at": "2008-11-23T11:12:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4463#issuecomment-32890",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-4463.patch](tarball://root/attachments/some-uuid/ticket4463/trac-4463.patch) by @craigcitro created at 2008-11-23 11:12:04



---

archive/issue_comments_032891.json:
```json
{
    "body": "Changing assignee from mabshoff to @craigcitro.",
    "created_at": "2008-11-23T11:14:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4463#issuecomment-32891",
    "user": "https://github.com/craigcitro"
}
```

Changing assignee from mabshoff to @craigcitro.



---

archive/issue_comments_032892.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-23T11:14:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4463#issuecomment-32892",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032893.json:
```json
{
    "body": "Some speedups for computation of endomorphism rings of modular abelian varieties. This patch just makes one or two easy changes; much work remains. However, it gives a noticeable speedup (at least on my machine): testing `sage/modular/abvar/homspace.py` drops from ~150s to ~100s. This should at least stop the timeouts people keep running into.",
    "created_at": "2008-11-23T11:14:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4463#issuecomment-32893",
    "user": "https://github.com/craigcitro"
}
```

Some speedups for computation of endomorphism rings of modular abelian varieties. This patch just makes one or two easy changes; much work remains. However, it gives a noticeable speedup (at least on my machine): testing `sage/modular/abvar/homspace.py` drops from ~150s to ~100s. This should at least stop the timeouts people keep running into.



---

archive/issue_comments_032894.json:
```json
{
    "body": "Changing component from doctest to modular forms.",
    "created_at": "2008-11-23T11:14:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4463#issuecomment-32894",
    "user": "https://github.com/craigcitro"
}
```

Changing component from doctest to modular forms.



---

archive/issue_comments_032895.json:
```json
{
    "body": "For the record, the two optimizations in the above patch:\n\n* for computing endomorphism ring generators for a one dimensional abelian variety, simply return the answer, and \n* if we're intersecting a space of modular symbols with `ZZ^n`, simply take the appropriate submodule instead of doing any linear algebra.",
    "created_at": "2008-11-23T11:17:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4463#issuecomment-32895",
    "user": "https://github.com/craigcitro"
}
```

For the record, the two optimizations in the above patch:

* for computing endomorphism ring generators for a one dimensional abelian variety, simply return the answer, and 
* if we're intersecting a space of modular symbols with `ZZ^n`, simply take the appropriate submodule instead of doing any linear algebra.



---

archive/issue_comments_032896.json:
```json
{
    "body": "Well, initially this was all about making some doctests \"#long time\", but speeding things up is obviously better :)\n\nCheers,\n\nMichael",
    "created_at": "2008-11-23T11:18:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4463#issuecomment-32896",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Well, initially this was all about making some doctests "#long time", but speeding things up is obviously better :)

Cheers,

Michael



---

archive/issue_comments_032897.json:
```json
{
    "body": "Works and seems sensible.  Makes the test take half the time on one of my test machines.",
    "created_at": "2008-11-23T21:59:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4463#issuecomment-32897",
    "user": "https://github.com/williamstein"
}
```

Works and seems sensible.  Makes the test take half the time on one of my test machines.



---

archive/issue_comments_032898.json:
```json
{
    "body": "There is one doctest failure issue here:\n\n```\nsage -t -long devel/sage/sage/modules/free_module.py        \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage/sage/modules/free_module.py\", line 1164:\n    sage: K = S.integral_structure(); K\nExpected:\n    Free module of degree 19 and rank 8 over Integer Ring\n    Echelon basis matrix:\n    [ 0  1  0  0 -1  0  0  0  0  0  0  0  0  0  0  0  0  0  0]\n    ...\nGot:\n    Free module of degree 19 and rank 8 over Integer Ring\n    User basis matrix:\n    [ 0  1  0  0 -1  0  0  0  0  0  0  0  0  0  0  0  0  0  0]\n    [ 0  0  1  0 -1  0  0  0  0  0  0  0  0  0  0  0  0  0  0]\n    [ 0  0  0  0  0  1  0  0  0 -1  0  0  0  0  0  0  0  0  0]\n    [ 0  0  0  0  0  0  1  0  0  0 -1  0  0  0  0  0  0  0  0]\n    [ 0  0  0  0  0  0  0  1  0 -1  0  0  0  0  0  0  0  0  0]\n    [ 0  0  0  0  0  0  0  0  1  0 -1  0  0  0  0  0  0  0  0]\n    [ 0  0  0  0  0  0  0  0  0  0  0  1  0 -1  0  0  0 -1  1]\n    [ 0  0  0  0  0  0  0  0  0  0  0  0  1  0 -1  0  0  1 -1]\n**********************************************************************\n```\n\nChanging this is simple, but I would like to know if the experts think this change is justified.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-23T23:44:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4463#issuecomment-32898",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

There is one doctest failure issue here:

```
sage -t -long devel/sage/sage/modules/free_module.py        
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage/sage/modules/free_module.py", line 1164:
    sage: K = S.integral_structure(); K
Expected:
    Free module of degree 19 and rank 8 over Integer Ring
    Echelon basis matrix:
    [ 0  1  0  0 -1  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
    ...
Got:
    Free module of degree 19 and rank 8 over Integer Ring
    User basis matrix:
    [ 0  1  0  0 -1  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
    [ 0  0  1  0 -1  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
    [ 0  0  0  0  0  1  0  0  0 -1  0  0  0  0  0  0  0  0  0]
    [ 0  0  0  0  0  0  1  0  0  0 -1  0  0  0  0  0  0  0  0]
    [ 0  0  0  0  0  0  0  1  0 -1  0  0  0  0  0  0  0  0  0]
    [ 0  0  0  0  0  0  0  0  1  0 -1  0  0  0  0  0  0  0  0]
    [ 0  0  0  0  0  0  0  0  0  0  0  1  0 -1  0  0  0 -1  1]
    [ 0  0  0  0  0  0  0  0  0  0  0  0  1  0 -1  0  0  1 -1]
**********************************************************************
```

Changing this is simple, but I would like to know if the experts think this change is justified.

Cheers,

Michael



---

archive/issue_comments_032899.json:
```json
{
    "body": "Craig mentioned in IRC that some more work needs to be done here.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-23T23:53:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4463#issuecomment-32899",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Craig mentioned in IRC that some more work needs to be done here.

Cheers,

Michael



---

archive/issue_comments_032900.json:
```json
{
    "body": "Attachment [trac-4463-pt2.patch](tarball://root/attachments/some-uuid/ticket4463/trac-4463-pt2.patch) by @craigcitro created at 2008-11-24 04:31:16\n\nAdded a new patch that fixes the doctest failure. It was just a question of calling the free module constructor appropriately; this version is even ever so slightly faster than before.",
    "created_at": "2008-11-24T04:31:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4463#issuecomment-32900",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-4463-pt2.patch](tarball://root/attachments/some-uuid/ticket4463/trac-4463-pt2.patch) by @craigcitro created at 2008-11-24 04:31:16

Added a new patch that fixes the doctest failure. It was just a question of calling the free module constructor appropriately; this version is even ever so slightly faster than before.



---

archive/issue_comments_032901.json:
```json
{
    "body": "Merged both patches in Sage 3.2.1.alpha1",
    "created_at": "2008-11-24T19:35:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4463#issuecomment-32901",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.2.1.alpha1



---

archive/issue_comments_032902.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-24T19:35:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4463#issuecomment-32902",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
