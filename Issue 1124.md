# Issue 1124: ModularSymbol.complement crashes on full subspaces

archive/issues_001124.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: zero_subspace\n\nHere is a bug in modular symbols code:\n\n``` \nsage: M=ModularSymbols(11,2,1)\nsage: M.complement()\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/net/mathserv/1/home/syazdani/research/programs/<ipython console> in <module>()\n\n/home/syazdani/sage/local/lib/python2.5/site-packages/sage/modular/hecke/ambient_module.py in complement(self)\n     96         Return the largest Hecke-stable complement of this space.\n     97         \"\"\"\n---> 98         return self.zero_subspace()\n     99\n    100     def decomposition_matrix(self):\n\n<type 'exceptions.AttributeError'>: 'ModularSymbolsAmbient_wt2_g0' object has no attribute 'zero_subspace'\n```\n\n\nThe problem is that zero_subspace is not implemented. Although zero_submodule is.\nOne possible fix is to change self.zero_subspace to self.zero_submodule(). That's the included patch.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1124\n\n",
    "created_at": "2007-11-07T18:07:46Z",
    "labels": [
        "component: modular forms",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.13",
    "title": "ModularSymbol.complement crashes on full subspaces",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1124",
    "user": "https://github.com/syazdani77"
}
```
Assignee: @williamstein

Keywords: zero_subspace

Here is a bug in modular symbols code:

``` 
sage: M=ModularSymbols(11,2,1)
sage: M.complement()
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/net/mathserv/1/home/syazdani/research/programs/<ipython console> in <module>()

/home/syazdani/sage/local/lib/python2.5/site-packages/sage/modular/hecke/ambient_module.py in complement(self)
     96         Return the largest Hecke-stable complement of this space.
     97         """
---> 98         return self.zero_subspace()
     99
    100     def decomposition_matrix(self):

<type 'exceptions.AttributeError'>: 'ModularSymbolsAmbient_wt2_g0' object has no attribute 'zero_subspace'
```


The problem is that zero_subspace is not implemented. Although zero_submodule is.
One possible fix is to change self.zero_subspace to self.zero_submodule(). That's the included patch.

Issue created by migration from https://trac.sagemath.org/ticket/1124





---

archive/issue_comments_006768.json:
```json
{
    "body": "trivial patch",
    "created_at": "2007-11-07T18:08:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1124#issuecomment-6768",
    "user": "https://github.com/syazdani77"
}
```

trivial patch



---

archive/issue_comments_006769.json:
```json
{
    "body": "Attachment [zero_submodule](tarball://root/attachments/some-uuid/ticket1124/zero_submodule) by @syazdani77 created at 2007-11-07 18:15:36\n\n[with patch]",
    "created_at": "2007-11-07T18:15:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1124#issuecomment-6769",
    "user": "https://github.com/syazdani77"
}
```

Attachment [zero_submodule](tarball://root/attachments/some-uuid/ticket1124/zero_submodule) by @syazdani77 created at 2007-11-07 18:15:36

[with patch]



---

archive/issue_events_003002.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-07T18:18:47Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1124",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1124#event-3002"
}
```



---

archive/issue_comments_006770.json:
```json
{
    "body": "Added doctest for complement. Both patches should be applied.",
    "created_at": "2007-11-07T18:25:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1124#issuecomment-6770",
    "user": "https://github.com/syazdani77"
}
```

Added doctest for complement. Both patches should be applied.



---

archive/issue_comments_006771.json:
```json
{
    "body": "Attachment [doctest](tarball://root/attachments/some-uuid/ticket1124/doctest) by mabshoff created at 2007-11-16 11:56:26",
    "created_at": "2007-11-16T11:56:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1124#issuecomment-6771",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [doctest](tarball://root/attachments/some-uuid/ticket1124/doctest) by mabshoff created at 2007-11-16 11:56:26



---

archive/issue_events_003003.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-16T11:56:26Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1124",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1124#event-3003"
}
```



---

archive/issue_events_003004.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-16T11:56:26Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1124",
    "milestone": "sage-2.8.13",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1124#event-3004"
}
```



---

archive/issue_comments_006772.json:
```json
{
    "body": "** \"I have reviewed this patch and it agree with it.\"",
    "created_at": "2007-11-18T03:55:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1124#issuecomment-6772",
    "user": "https://github.com/williamstein"
}
```

** "I have reviewed this patch and it agree with it."



---

archive/issue_events_003005.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-18T14:22:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1124",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1124#event-3005"
}
```



---

archive/issue_comments_006773.json:
```json
{
    "body": "Merged in 2.8.13.alpha0.",
    "created_at": "2007-11-18T14:22:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1124#issuecomment-6773",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.13.alpha0.



---

archive/issue_comments_006774.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-18T14:22:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1124#issuecomment-6774",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
