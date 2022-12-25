# Issue 4312: [with patch; with positive review] major @paralllel (hence pyprocessing) new bug in 3.1.3, still in 3.1.4

archive/issues_004312.json:
```json
{
    "body": "Assignee: cwitty\n\nIn 3.1.2 this worked fine. It's totally broken in 3.1.4.\n\n```\nsage@modular:~/build/sage-3.1.4$ more a.sage\n@parallel(8)\ndef f(p):\n    print p\n    t = cputime()\n    M = ModularSymbols(p^2,sign=1)\n    w = M.atkin_lehner_operator(p)\n    K = (w-1).kernel()\n    N = K.new_subspace()\n    D = N.decomposition()\n    print cputime(t)\n    M.save(str(p))\n    save(D, '%s-decomp'%p)\n\n\n\nsage@modular:~/build/sage-3.1.4$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.1.4, Release Date: 2008-10-16                       |\n| Type notebook() for the GUI, and license() for information.        |\nsage: load a.sage\nsage: list(f([11,17]))\n17\n11\n---------------------------------------------------------------------------\nNameError                                 Traceback (most recent call last)\n\n/home2/sage/.sage/temp/modular/25347/_home2_sage_build_sage_3_1_4_a_sage_0.py in <module>()\n----> 1\n      2\n      3\n      4\n      5\n\n/home2/sage/build/sage-3.1.4/local/lib/python2.5/site-packages/sage/parallel/multiprocessing.pyc in parallel_iter(processes, f, inputs)\n     64\n     65     result = p.imapUnordered(call_pickled_function, [ (fp, t) for t in inputs ])\n---> 66     for res in result:\n     67         yield res\n     68\n\n/home2/sage/build/sage-3.1.4/local/lib/python2.5/site-packages/processing/pool.pyc in next(self, timeout)\n    468         if success:\n    469             return value\n--> 470         raise value\n    471\n    472     def _set(self, i, obj):\n\nNameError: global name '_sage_const_2' is not defined\nsage:           \n```\n\nThis is a pyprocessing problem since:\n\n```\nsage: load a.sage\nsage: f(11)\n11\n0.168011\nsage: f(13)\n13\n0.244015\nsage:              \n```\n}}}\n\nIssue created by migration from https://trac.sagemath.org/ticket/4312\n\n",
    "closed_at": "2008-11-18T18:17:21Z",
    "created_at": "2008-10-17T12:52:39Z",
    "labels": [
        "component: misc",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with patch; with positive review] major @paralllel (hence pyprocessing) new bug in 3.1.3, still in 3.1.4",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4312",
    "user": "https://github.com/williamstein"
}
```
Assignee: cwitty

In 3.1.2 this worked fine. It's totally broken in 3.1.4.

```
sage@modular:~/build/sage-3.1.4$ more a.sage
@parallel(8)
def f(p):
    print p
    t = cputime()
    M = ModularSymbols(p^2,sign=1)
    w = M.atkin_lehner_operator(p)
    K = (w-1).kernel()
    N = K.new_subspace()
    D = N.decomposition()
    print cputime(t)
    M.save(str(p))
    save(D, '%s-decomp'%p)



sage@modular:~/build/sage-3.1.4$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.4, Release Date: 2008-10-16                       |
| Type notebook() for the GUI, and license() for information.        |
sage: load a.sage
sage: list(f([11,17]))
17
11
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/home2/sage/.sage/temp/modular/25347/_home2_sage_build_sage_3_1_4_a_sage_0.py in <module>()
----> 1
      2
      3
      4
      5

/home2/sage/build/sage-3.1.4/local/lib/python2.5/site-packages/sage/parallel/multiprocessing.pyc in parallel_iter(processes, f, inputs)
     64
     65     result = p.imapUnordered(call_pickled_function, [ (fp, t) for t in inputs ])
---> 66     for res in result:
     67         yield res
     68

/home2/sage/build/sage-3.1.4/local/lib/python2.5/site-packages/processing/pool.pyc in next(self, timeout)
    468         if success:
    469             return value
--> 470         raise value
    471
    472     def _set(self, i, obj):

NameError: global name '_sage_const_2' is not defined
sage:           
```

This is a pyprocessing problem since:

```
sage: load a.sage
sage: f(11)
11
0.168011
sage: f(13)
13
0.244015
sage:              
```
}}}

Issue created by migration from https://trac.sagemath.org/ticket/4312





---

archive/issue_comments_031508.json:
```json
{
    "body": "So does this issue have anything to do with `@`interact?  Or is it `@`parallel that has the problem?",
    "created_at": "2008-10-17T14:12:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4312",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4312#issuecomment-31508",
    "user": "https://github.com/jasongrout"
}
```

So does this issue have anything to do with `@`interact?  Or is it `@`parallel that has the problem?



---

archive/issue_comments_031509.json:
```json
{
    "body": "Bug Day 15 material? This certainly should get fixed in 3.2.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-30T05:55:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4312",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4312#issuecomment-31509",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Bug Day 15 material? This certainly should get fixed in 3.2.

Cheers,

Michael



---

archive/issue_events_009744.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-30T05:55:12Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4312",
    "milestone": "sage-3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4312#event-9744"
}
```



---

archive/issue_events_009745.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-15T10:29:41Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4312",
    "milestone": "sage-3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4312#event-9745"
}
```



---

archive/issue_events_009746.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-15T10:29:41Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4312",
    "milestone": "sage-3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4312#event-9746"
}
```



---

archive/issue_comments_031510.json:
```json
{
    "body": "I've posted a hack-ish patch that at least fixes this problem.  Something better might be to modify `@`parallel to more properly transfer all _sage_const*'s to subprocesses or something.",
    "created_at": "2008-11-16T20:05:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4312",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4312#issuecomment-31510",
    "user": "https://github.com/williamstein"
}
```

I've posted a hack-ish patch that at least fixes this problem.  Something better might be to modify `@`parallel to more properly transfer all _sage_const*'s to subprocesses or something.



---

archive/issue_comments_031511.json:
```json
{
    "body": "Attachment [sage-4312.patch](tarball://root/attachments/some-uuid/ticket4312/sage-4312.patch) by @williamstein created at 2008-11-16 20:06:33",
    "created_at": "2008-11-16T20:06:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4312",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4312#issuecomment-31511",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-4312.patch](tarball://root/attachments/some-uuid/ticket4312/sage-4312.patch) by @williamstein created at 2008-11-16 20:06:33



---

archive/issue_comments_031512.json:
```json
{
    "body": "Attachment [sage-4312-edited.patch](tarball://root/attachments/some-uuid/ticket4312/sage-4312-edited.patch) by @craigcitro created at 2008-11-18 09:39:10",
    "created_at": "2008-11-18T09:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4312",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4312#issuecomment-31512",
    "user": "https://github.com/craigcitro"
}
```

Attachment [sage-4312-edited.patch](tarball://root/attachments/some-uuid/ticket4312/sage-4312-edited.patch) by @craigcitro created at 2008-11-18 09:39:10



---

archive/issue_comments_031513.json:
```json
{
    "body": "Looks good. \n\nI made a new ticket to have someone find an **actual** fix, which is #4545. I also edited the patch to have this info in it, and posted that above.",
    "created_at": "2008-11-18T09:40:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4312",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4312#issuecomment-31513",
    "user": "https://github.com/craigcitro"
}
```

Looks good. 

I made a new ticket to have someone find an **actual** fix, which is #4545. I also edited the patch to have this info in it, and posted that above.



---

archive/issue_events_009747.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-18T18:17:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4312",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4312#event-9747"
}
```



---

archive/issue_comments_031514.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-18T18:17:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4312",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4312#issuecomment-31514",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_031515.json:
```json
{
    "body": "Merged sage-4312-edited.patch in Sage 3.2.rc2",
    "created_at": "2008-11-18T18:17:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4312",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4312#issuecomment-31515",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged sage-4312-edited.patch in Sage 3.2.rc2
