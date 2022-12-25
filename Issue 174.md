# Issue 174: [with patch; positive review] Implement a modular Hermite Normal Form algorithm

archive/issues_000174.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @burcin\n\nHermite Normal form is the analogue of echelon form over the integers.\nIt's crucial for almost all efficient computations with Z-modules (infinite \nabelian groups, finite abelian groups, lattices, modular abelian varieties\nvia lattices, etc).  \n\nMAGMA is 50 times faster even for small examples, and asymptotically\nmuch faster than GAP, PARI, and NTL. \n\nSee this page http://magma.maths.usyd.edu.au/users/allan/mat/hermite.html\nwhich is mirrored here:\nhttp://sage.math.washington.edu/sage/misc/hermite.html\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/174\n\n",
    "closed_at": "2008-02-21T03:10:40Z",
    "created_at": "2006-12-01T02:15:15Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "[with patch; positive review] Implement a modular Hermite Normal Form algorithm",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/174",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  @burcin

Hermite Normal form is the analogue of echelon form over the integers.
It's crucial for almost all efficient computations with Z-modules (infinite 
abelian groups, finite abelian groups, lattices, modular abelian varieties
via lattices, etc).  

MAGMA is 50 times faster even for small examples, and asymptotically
much faster than GAP, PARI, and NTL. 

See this page http://magma.maths.usyd.edu.au/users/allan/mat/hermite.html
which is mirrored here:
http://sage.math.washington.edu/sage/misc/hermite.html




Issue created by migration from https://trac.sagemath.org/ticket/174





---

archive/issue_comments_000795.json:
```json
{
    "body": "a student paper on fast HNF algorithms (and there are other papers out there)",
    "created_at": "2006-12-01T02:16:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/174#issuecomment-795",
    "user": "https://github.com/williamstein"
}
```

a student paper on fast HNF algorithms (and there are other papers out there)



---

archive/issue_comments_000796.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-01-13T01:44:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/174#issuecomment-796",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_000797.json:
```json
{
    "body": "Attachment [HermiteNormalForm_1.tex](tarball://root/attachments/some-uuid/ticket174/HermiteNormalForm_1.tex) by @williamstein created at 2007-01-13 01:44:45",
    "created_at": "2007-01-13T01:44:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/174#issuecomment-797",
    "user": "https://github.com/williamstein"
}
```

Attachment [HermiteNormalForm_1.tex](tarball://root/attachments/some-uuid/ticket174/HermiteNormalForm_1.tex) by @williamstein created at 2007-01-13 01:44:45



---

archive/issue_comments_000798.json:
```json
{
    "body": "The attached paper by students describes the super-fast algorithm in MAGMA, and should\nbe reasonably easy to implement in SAGE given what we now have.",
    "created_at": "2007-03-08T10:09:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/174#issuecomment-798",
    "user": "https://github.com/williamstein"
}
```

The attached paper by students describes the super-fast algorithm in MAGMA, and should
be reasonably easy to implement in SAGE given what we now have.



---

archive/issue_events_000324.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-09-10T02:57:48Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/174",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/174#event-324"
}
```



---

archive/issue_comments_000799.json:
```json
{
    "body": "Attachment [trac-174.patch](tarball://root/attachments/some-uuid/ticket174/trac-174.patch) by @williamstein created at 2008-02-08 16:08:15",
    "created_at": "2008-02-08T16:08:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/174#issuecomment-799",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-174.patch](tarball://root/attachments/some-uuid/ticket174/trac-174.patch) by @williamstein created at 2008-02-08 16:08:15



---

archive/issue_comments_000800.json:
```json
{
    "body": "Attachment [hnfrow.sage](tarball://root/attachments/some-uuid/ticket174/hnfrow.sage) by @williamstein created at 2008-02-08 16:11:31",
    "created_at": "2008-02-08T16:11:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/174#issuecomment-800",
    "user": "https://github.com/williamstein"
}
```

Attachment [hnfrow.sage](tarball://root/attachments/some-uuid/ticket174/hnfrow.sage) by @williamstein created at 2008-02-08 16:11:31



---

archive/issue_comments_000801.json:
```json
{
    "body": "Attachment [trac-174-part2.patch](tarball://root/attachments/some-uuid/ticket174/trac-174-part2.patch) by @williamstein created at 2008-02-08 16:11:49",
    "created_at": "2008-02-08T16:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/174#issuecomment-801",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-174-part2.patch](tarball://root/attachments/some-uuid/ticket174/trac-174-part2.patch) by @williamstein created at 2008-02-08 16:11:49



---

archive/issue_comments_000802.json:
```json
{
    "body": "Attachment [trac-174-part3.patch](tarball://root/attachments/some-uuid/ticket174/trac-174-part3.patch) by @williamstein created at 2008-02-17 01:14:22\n\nI've put the final hnf.hg bundle here:\n\n  http://sage.math.washington.edu/home/was/patches/hnf.hg\n\nThis is a bundle that I made by cleanly applying all my relevant\npatches to 2.10.2.alpha0, then do hg_sage.send(...). \n\nThe code is well documented, works well (very well tested with\nautomated testing and doctstrings), but has a HUGE MEMORY LEAK somewhere:\n\n```\nsage: a = random_matrix(ZZ,200,x=0,y=9)\nsage: a._clear_cache(); e = a.hermite_form(proof=False); get_memory_usage()\n'234M+'\nsage: a._clear_cache(); e = a.hermite_form(proof=False); get_memory_usage()\n'239M+'\nsage: a._clear_cache(); e = a.hermite_form(proof=False); get_memory_usage()\n'244M+'\nsage: a._clear_cache(); e = a.hermite_form(proof=False); get_memory_usage()\n'249M+'\n```\n\nI suspect the memleak is in the optimized GMP code I added to matrix_integer_dense, and will find out soon...",
    "created_at": "2008-02-17T01:14:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/174#issuecomment-802",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-174-part3.patch](tarball://root/attachments/some-uuid/ticket174/trac-174-part3.patch) by @williamstein created at 2008-02-17 01:14:22

I've put the final hnf.hg bundle here:

  http://sage.math.washington.edu/home/was/patches/hnf.hg

This is a bundle that I made by cleanly applying all my relevant
patches to 2.10.2.alpha0, then do hg_sage.send(...). 

The code is well documented, works well (very well tested with
automated testing and doctstrings), but has a HUGE MEMORY LEAK somewhere:

```
sage: a = random_matrix(ZZ,200,x=0,y=9)
sage: a._clear_cache(); e = a.hermite_form(proof=False); get_memory_usage()
'234M+'
sage: a._clear_cache(); e = a.hermite_form(proof=False); get_memory_usage()
'239M+'
sage: a._clear_cache(); e = a.hermite_form(proof=False); get_memory_usage()
'244M+'
sage: a._clear_cache(); e = a.hermite_form(proof=False); get_memory_usage()
'249M+'
```

I suspect the memleak is in the optimized GMP code I added to matrix_integer_dense, and will find out soon...



---

archive/issue_events_000325.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-02-17T01:28:28Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/174",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/174#event-325"
}
```



---

archive/issue_events_000326.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-02-17T01:28:28Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/174",
    "milestone": "sage-2.10.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/174#event-326"
}
```



---

archive/issue_comments_000803.json:
```json
{
    "body": "Here's a big leak:\n\n```\nsage: a = random_matrix(ZZ,200,x=0,y=9); e = a.hermite_form(proof=False); p = a.pivots()\nsage: get_memory_usage()\n'192M+'\nsage: w = e._add_row_and_maintain_echelon_form(random_matrix(ZZ,1,200), p)\nsage: get_memory_usage()\n'210M+'\n```",
    "created_at": "2008-02-17T01:28:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/174#issuecomment-803",
    "user": "https://github.com/williamstein"
}
```

Here's a big leak:

```
sage: a = random_matrix(ZZ,200,x=0,y=9); e = a.hermite_form(proof=False); p = a.pivots()
sage: get_memory_usage()
'192M+'
sage: w = e._add_row_and_maintain_echelon_form(random_matrix(ZZ,1,200), p)
sage: get_memory_usage()
'210M+'
```



---

archive/issue_comments_000804.json:
```json
{
    "body": "ok, the file at http://sage.math.washington.edu/home/was/patches/hnf.hg has all the HNF stuff all working with no known issues.\n\n finally!",
    "created_at": "2008-02-17T03:46:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/174#issuecomment-804",
    "user": "https://github.com/williamstein"
}
```

ok, the file at http://sage.math.washington.edu/home/was/patches/hnf.hg has all the HNF stuff all working with no known issues.

 finally!



---

archive/issue_comments_000805.json:
```json
{
    "body": "Ok, running the final bundle under valgrind with \n\n```\nsage: a = random_matrix(ZZ,200,x=0,y=9)\nsage: a._clear_cache(); e = a.hermite_form(proof=False); get_memory_usage()\nsage: a._clear_cache(); e = a.hermite_form(proof=False); get_memory_usage()\nsage: a._clear_cache(); e = a.hermite_form(proof=False); get_memory_usage()\n```\ndoesn't leak at all. Excellent. So positive review on memory leak issues.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-17T03:52:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/174#issuecomment-805",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, running the final bundle under valgrind with 

```
sage: a = random_matrix(ZZ,200,x=0,y=9)
sage: a._clear_cache(); e = a.hermite_form(proof=False); get_memory_usage()
sage: a._clear_cache(); e = a.hermite_form(proof=False); get_memory_usage()
sage: a._clear_cache(); e = a.hermite_form(proof=False); get_memory_usage()
```
doesn't leak at all. Excellent. So positive review on memory leak issues.

Cheers,

Michael



---

archive/issue_comments_000806.json:
```json
{
    "body": "FYI: The code has been merged, but still needs \"official\" review by a third party.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-17T11:55:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/174#issuecomment-806",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

FYI: The code has been merged, but still needs "official" review by a third party.

Cheers,

Michael



---

archive/issue_comments_000807.json:
```json
{
    "body": "The bundle has been extensively tested and I have verified via valgrind that it doesn't leak memory. While nobody external ever did a formal review  I am giving this a positive review due to the excessive amount of testing. Feel free to do a formal review, but please open another ticket in case  you come up with any issues.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-21T03:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/174#issuecomment-807",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The bundle has been extensively tested and I have verified via valgrind that it doesn't leak memory. While nobody external ever did a formal review  I am giving this a positive review due to the excessive amount of testing. Feel free to do a formal review, but please open another ticket in case  you come up with any issues.

Cheers,

Michael



---

archive/issue_comments_000808.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha1",
    "created_at": "2008-02-21T03:10:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/174#issuecomment-808",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha1



---

archive/issue_comments_000809.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-21T03:10:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/174#issuecomment-809",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_000327.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-21T03:10:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/174",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/174#event-327"
}
```
