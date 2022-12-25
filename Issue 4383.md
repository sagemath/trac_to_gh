# Issue 4383: composition_series() returns no generators for trivial subgroup

archive/issues_004383.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: composition series, generators\n\nAt the tail end of a composition series of a group, the trivial subgroup has no generators, rather than the identity permutation as a generator.  This appears unacceptable to GAP for subsequent computations.\n\nOn 3.1.4 built from source on x86.\n\n\n```\nsage: G=CyclicPermutationGroup(2)\nsage: comps\n```\n\n\n\n```\n[Permutation Group with generators [(1,2)],\n Permutation Group with generators []]\n```\n\n\n\n```\nsage: comps[1].order()\n```\n\n\n\n```\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"/home/rob/.sage/sage_notebook/worksheets/admin/48/code/5.py\", line 7, in <module>\n    comps[_sage_const_1 ].order()\n  File \"/opt/sage-3.1.4/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/\", line 1, in <module>\n    \n  File \"/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py\", line 770, in order\n    return Integer(self._gap_().Size())\n  File \"sage_object.pyx\", line 270, in sage.structure.sage_object.SageObject._gap_ (sage/structure/sage_object.c:2442)\n  File \"sage_object.pyx\", line 246, in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:2186)\n  File \"/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 965, in __call__\n    return cls(self, x, name=name)\n  File \"/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 1283, in __init__\n    raise TypeError, x\nTypeError: Gap produced error output\nError, usage: Group(<gen>,...), Group(<gens>), Group(<gens>,<id>)\n\n   executing $sage6:=Group([]);;\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4383\n\n",
    "created_at": "2008-10-30T04:02:58Z",
    "labels": [
        "component: group theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "composition_series() returns no generators for trivial subgroup",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4383",
    "user": "https://github.com/rbeezer"
}
```
Assignee: somebody

Keywords: composition series, generators

At the tail end of a composition series of a group, the trivial subgroup has no generators, rather than the identity permutation as a generator.  This appears unacceptable to GAP for subsequent computations.

On 3.1.4 built from source on x86.


```
sage: G=CyclicPermutationGroup(2)
sage: comps
```



```
[Permutation Group with generators [(1,2)],
 Permutation Group with generators []]
```



```
sage: comps[1].order()
```



```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/rob/.sage/sage_notebook/worksheets/admin/48/code/5.py", line 7, in <module>
    comps[_sage_const_1 ].order()
  File "/opt/sage-3.1.4/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/", line 1, in <module>
    
  File "/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py", line 770, in order
    return Integer(self._gap_().Size())
  File "sage_object.pyx", line 270, in sage.structure.sage_object.SageObject._gap_ (sage/structure/sage_object.c:2442)
  File "sage_object.pyx", line 246, in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:2186)
  File "/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 965, in __call__
    return cls(self, x, name=name)
  File "/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1283, in __init__
    raise TypeError, x
TypeError: Gap produced error output
Error, usage: Group(<gen>,...), Group(<gens>), Group(<gens>,<id>)

   executing $sage6:=Group([]);;
```


Issue created by migration from https://trac.sagemath.org/ticket/4383





---

archive/issue_comments_032181.json:
```json
{
    "body": "First bit of code above lost the middle line, which should read\n\n\n```\nsage: comps=G.composition_series()\n```\n",
    "created_at": "2008-10-30T04:06:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4383#issuecomment-32181",
    "user": "https://github.com/rbeezer"
}
```

First bit of code above lost the middle line, which should read


```
sage: comps=G.composition_series()
```




---

archive/issue_comments_032182.json:
```json
{
    "body": "I'm guessing that this this ticket is not named accurately. \n\nIt appears the problem isn't with the composition series but with the order function:\n\n\n```\nsage: G = PermutationGroup([])\nsage: G.order()\nERROR: An unexpected error occurred while tokenizing input\n<snip>\n```\n\nThis will possibly raise the issue of whether the trivial group should be PermutationGroup([]) (as it is now) or PermutationGroup([()]) (for which order works). According to Rotman, the group whose generating set is the empty set is the trivial group, so I think they way we have it is fine. Therefore, I elected to simply fix this bug in the order method. \nPatch attached is based on sage-3.2.alpha1 and pases sage -t.",
    "created_at": "2008-10-30T19:15:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4383#issuecomment-32182",
    "user": "https://github.com/wdjoyner"
}
```

I'm guessing that this this ticket is not named accurately. 

It appears the problem isn't with the composition series but with the order function:


```
sage: G = PermutationGroup([])
sage: G.order()
ERROR: An unexpected error occurred while tokenizing input
<snip>
```

This will possibly raise the issue of whether the trivial group should be PermutationGroup([]) (as it is now) or PermutationGroup([()]) (for which order works). According to Rotman, the group whose generating set is the empty set is the trivial group, so I think they way we have it is fine. Therefore, I elected to simply fix this bug in the order method. 
Patch attached is based on sage-3.2.alpha1 and pases sage -t.



---

archive/issue_comments_032183.json:
```json
{
    "body": "Attachment [trac_4383-order-trivial-permgp.patch](tarball://root/attachments/some-uuid/ticket4383/trac_4383-order-trivial-permgp.patch) by @wdjoyner created at 2008-10-30 19:15:43\n\nbased on 3.2.alpha1",
    "created_at": "2008-10-30T19:15:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4383#issuecomment-32183",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [trac_4383-order-trivial-permgp.patch](tarball://root/attachments/some-uuid/ticket4383/trac_4383-order-trivial-permgp.patch) by @wdjoyner created at 2008-10-30 19:15:43

based on 3.2.alpha1



---

archive/issue_comments_032184.json:
```json
{
    "body": "This patch needs a doctest.\n\nPlease also stick with the standard tags for patches.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-30T19:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4383#issuecomment-32184",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch needs a doctest.

Please also stick with the standard tags for patches.

Cheers,

Michael



---

archive/issue_comments_032185.json:
```json
{
    "body": "Sorry - I added a doctest in the 2nd patch. I could not figure out what I did wrong with the tags (whatever they are - I could not find them in http://wiki.sagemath.org/TracGuidelines, but could have easily missed something).",
    "created_at": "2008-10-30T19:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4383#issuecomment-32185",
    "user": "https://github.com/wdjoyner"
}
```

Sorry - I added a doctest in the 2nd patch. I could not figure out what I did wrong with the tags (whatever they are - I could not find them in http://wiki.sagemath.org/TracGuidelines, but could have easily missed something).



---

archive/issue_comments_032186.json:
```json
{
    "body": "Attachment [trac_4383-order-trivial-permgp2.patch](tarball://root/attachments/some-uuid/ticket4383/trac_4383-order-trivial-permgp2.patch) by @wdjoyner created at 2008-10-30 19:55:50\n\nbased on 3.2.alpha1 - apply after the first patch",
    "created_at": "2008-10-30T19:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4383#issuecomment-32186",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [trac_4383-order-trivial-permgp2.patch](tarball://root/attachments/some-uuid/ticket4383/trac_4383-order-trivial-permgp2.patch) by @wdjoyner created at 2008-10-30 19:55:50

based on 3.2.alpha1 - apply after the first patch



---

archive/issue_comments_032187.json:
```json
{
    "body": "I agree that a constructor with an empty list should be interpreted as the trivial subgroup, but it seems that passing this to GAP will cause an error.  On 3.1.4 I get a different error message than David, which suggests that GAP doesn't like the construction.\n\nCalling other commands on a group with no generators (such as exponent() or is_simple() or derived_series()), yields an error similar (or identical) to the one from a call to order().\n\nFurthermore, it appears that until recently composition_series() returned a trivial subgroup with the identity element as a generator for the tail end of the series.  For example, see sample output in [3364](http://trac.sagemath.org/sage_trac/ticket/3364).\n\nIt seems to me that having the output of one command be acceptable to all subsequent commands is preferable.  The experiment below suggests to me that GAP doesn't like an empty list of generators.\n\n\n\n```\nsage: gap.eval(\"G := Group(())\")\n'Group(())'\n\nsage: gap.eval(\"G := Group()\")\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"/home/rob/.sage/sage_notebook/worksheets/admin/48/code/17.py\", line 6, in <module>\n    gap.eval(\"G := Group()\")\n  File \"/opt/sage-3.1.4/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/\", line 1, in <module>\n    \n  File \"/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/interfaces/gap.py\", line 404, in eval\n    s = Expect.eval(self, x)\n  File \"/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 937, in eval\n    return '\\n'.join([self._eval_line(L, **kwds) for L in code.split('\\n') if L != ''])\n  File \"/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/interfaces/gap.py\", line 627, in _eval_line\n    raise RuntimeError, message\nRuntimeError: Gap produced error output\nError, usage: Group(<gen>,...), Group(<gens>), Group(<gens>,<id>)\n\n   executing G := Group();\n```\n",
    "created_at": "2008-10-31T02:40:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4383#issuecomment-32187",
    "user": "https://github.com/rbeezer"
}
```

I agree that a constructor with an empty list should be interpreted as the trivial subgroup, but it seems that passing this to GAP will cause an error.  On 3.1.4 I get a different error message than David, which suggests that GAP doesn't like the construction.

Calling other commands on a group with no generators (such as exponent() or is_simple() or derived_series()), yields an error similar (or identical) to the one from a call to order().

Furthermore, it appears that until recently composition_series() returned a trivial subgroup with the identity element as a generator for the tail end of the series.  For example, see sample output in [3364](http://trac.sagemath.org/sage_trac/ticket/3364).

It seems to me that having the output of one command be acceptable to all subsequent commands is preferable.  The experiment below suggests to me that GAP doesn't like an empty list of generators.



```
sage: gap.eval("G := Group(())")
'Group(())'

sage: gap.eval("G := Group()")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/rob/.sage/sage_notebook/worksheets/admin/48/code/17.py", line 6, in <module>
    gap.eval("G := Group()")
  File "/opt/sage-3.1.4/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/", line 1, in <module>
    
  File "/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/interfaces/gap.py", line 404, in eval
    s = Expect.eval(self, x)
  File "/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 937, in eval
    return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
  File "/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/interfaces/gap.py", line 627, in _eval_line
    raise RuntimeError, message
RuntimeError: Gap produced error output
Error, usage: Group(<gen>,...), Group(<gens>), Group(<gens>,<id>)

   executing G := Group();
```




---

archive/issue_comments_032188.json:
```json
{
    "body": "(a) Maybe I'm wrong, I see this as a different issue form the bug you opened the ticket for. \n(b) It seems you are suggesting that all the methods should work for groups constructed using both PermutationGroup([()]) and PermutationGroup([]), and give the same result. This seems reasonable to me. However, it seems like it should be opened as a separate ticket, which a suitably descriptive title.",
    "created_at": "2008-10-31T10:05:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4383#issuecomment-32188",
    "user": "https://github.com/wdjoyner"
}
```

(a) Maybe I'm wrong, I see this as a different issue form the bug you opened the ticket for. 
(b) It seems you are suggesting that all the methods should work for groups constructed using both PermutationGroup([()]) and PermutationGroup([]), and give the same result. This seems reasonable to me. However, it seems like it should be opened as a separate ticket, which a suitably descriptive title.



---

archive/issue_comments_032189.json:
```json
{
    "body": "With regards to (b), I'm suggesting the opposite.  Seems easier, and more consistent, to return composition_series() to its previous behavior, rather than having it generate objects that subsequently GAP cannot digest.  In other words, adjust only the behavior of composition_series().   I am NOT suggesting that all the methods acting on groups be adjusted to accept a trivial subgroup specified with no generators.\n\nSo I guess I'm suggesting more broadly that an empty list of generators not be possible (even if it makes sense mathematically).  I don't have enough experience with the other parts of Sage to know how it is handled for other objects (like rings).  But if GAP isn't happy with an empty list, then I think the effort should be made to make sure the output of methods for groups produces items appropriate as input to other commands using GAP to do their work.  Or maybe the interface to GAP should convert empty lists to a list with the identity?  That would be another solution.\n\nOne possibility would be to have the constructors for groups recognize and convert an empty list of generators into a list holding just the identity permutation.  But again, I don't have enough experience to know if this would be feasible or desirable.\n\nRob",
    "created_at": "2008-10-31T14:17:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4383#issuecomment-32189",
    "user": "https://github.com/rbeezer"
}
```

With regards to (b), I'm suggesting the opposite.  Seems easier, and more consistent, to return composition_series() to its previous behavior, rather than having it generate objects that subsequently GAP cannot digest.  In other words, adjust only the behavior of composition_series().   I am NOT suggesting that all the methods acting on groups be adjusted to accept a trivial subgroup specified with no generators.

So I guess I'm suggesting more broadly that an empty list of generators not be possible (even if it makes sense mathematically).  I don't have enough experience with the other parts of Sage to know how it is handled for other objects (like rings).  But if GAP isn't happy with an empty list, then I think the effort should be made to make sure the output of methods for groups produces items appropriate as input to other commands using GAP to do their work.  Or maybe the interface to GAP should convert empty lists to a list with the identity?  That would be another solution.

One possibility would be to have the constructors for groups recognize and convert an empty list of generators into a list holding just the identity permutation.  But again, I don't have enough experience to know if this would be feasible or desirable.

Rob



---

archive/issue_comments_032190.json:
```json
{
    "body": "This last patch seems to do what you want.",
    "created_at": "2008-11-01T02:07:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4383#issuecomment-32190",
    "user": "https://github.com/wdjoyner"
}
```

This last patch seems to do what you want.



---

archive/issue_comments_032191.json:
```json
{
    "body": "Thanks, David.\n\nRob",
    "created_at": "2008-11-01T19:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4383#issuecomment-32191",
    "user": "https://github.com/rbeezer"
}
```

Thanks, David.

Rob



---

archive/issue_comments_032192.json:
```json
{
    "body": "REFEREE REPORT:\n\nHuh?  \n\n\n* trac_4383-order-trivial-permgp.patch + trac_4383-order-trivial-permgp2.patch  make some sense to me with the second patch fixing a bug introduced in the first and adding doctests.\n\n* trac_4383-order-trivial-permgp3.patch looks to me like exactly the same (?) as the first buggy patch!  So maybe you forgot to attach the right patch?\n\nPlease clarify and ping me.",
    "created_at": "2008-11-28T22:37:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4383#issuecomment-32192",
    "user": "https://github.com/williamstein"
}
```

REFEREE REPORT:

Huh?  


* trac_4383-order-trivial-permgp.patch + trac_4383-order-trivial-permgp2.patch  make some sense to me with the second patch fixing a bug introduced in the first and adding doctests.

* trac_4383-order-trivial-permgp3.patch looks to me like exactly the same (?) as the first buggy patch!  So maybe you forgot to attach the right patch?

Please clarify and ping me.



---

archive/issue_comments_032193.json:
```json
{
    "body": "Attachment [trac_4383-order-trivial-permgp3.patch](tarball://root/attachments/some-uuid/ticket4383/trac_4383-order-trivial-permgp3.patch) by @wdjoyner created at 2008-11-28 22:56:25",
    "created_at": "2008-11-28T22:56:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4383#issuecomment-32193",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [trac_4383-order-trivial-permgp3.patch](tarball://root/attachments/some-uuid/ticket4383/trac_4383-order-trivial-permgp3.patch) by @wdjoyner created at 2008-11-28 22:56:25



---

archive/issue_comments_032194.json:
```json
{
    "body": "REPORT:\n\nLooks good.   Mabshoff, apply the following patches in order (to 3.2.1.alpha):\n\n\n```\ntrac_4383-order-trivial-permgp.patch \ntrac_4383-order-trivial-permgp2.patch\ntrac_4383-order-trivial-permgp3-REBASE.patch\n```\n",
    "created_at": "2008-11-29T01:49:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4383#issuecomment-32194",
    "user": "https://github.com/williamstein"
}
```

REPORT:

Looks good.   Mabshoff, apply the following patches in order (to 3.2.1.alpha):


```
trac_4383-order-trivial-permgp.patch 
trac_4383-order-trivial-permgp2.patch
trac_4383-order-trivial-permgp3-REBASE.patch
```




---

archive/issue_comments_032195.json:
```json
{
    "body": "Attachment [trac_4383-order-trivial-permgp3-REBASE.patch](tarball://root/attachments/some-uuid/ticket4383/trac_4383-order-trivial-permgp3-REBASE.patch) by @williamstein created at 2008-11-29 01:50:12",
    "created_at": "2008-11-29T01:50:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4383#issuecomment-32195",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_4383-order-trivial-permgp3-REBASE.patch](tarball://root/attachments/some-uuid/ticket4383/trac_4383-order-trivial-permgp3-REBASE.patch) by @williamstein created at 2008-11-29 01:50:12



---

archive/issue_comments_032196.json:
```json
{
    "body": "One trivial doctesting failure is to fix:\n\n```\nsage -t -long \"devel/sage/sage/combinat/designs/incidence_structures.py\"\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.1.alpha3/devel/sage/sage/combinat/designs/incidence_structures.py\", line 174:\n    sage: G = BD.automorphism_group(); G\nExpected:\n    Permutation Group with generators []\nGot:\n    Permutation Group with generators [()]\n```\n",
    "created_at": "2008-11-29T02:27:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4383#issuecomment-32196",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

One trivial doctesting failure is to fix:

```
sage -t -long "devel/sage/sage/combinat/designs/incidence_structures.py"
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha3/devel/sage/sage/combinat/designs/incidence_structures.py", line 174:
    sage: G = BD.automorphism_group(); G
Expected:
    Permutation Group with generators []
Got:
    Permutation Group with generators [()]
```




---

archive/issue_comments_032197.json:
```json
{
    "body": "Another doctest failure:\n\n```\nFile \"/home/was/build/sage-3.2.1.alpha1/devel/sage-review/sage/combinat/designs/incidence_structures.py\", line 174:\n    sage: G = BD.automorphism_group(); G\nExpected:\n    Permutation Group with generators []\nGot:\n    Permutation Group with generators [()]\n```\n",
    "created_at": "2008-11-29T02:34:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4383#issuecomment-32197",
    "user": "https://github.com/williamstein"
}
```

Another doctest failure:

```
File "/home/was/build/sage-3.2.1.alpha1/devel/sage-review/sage/combinat/designs/incidence_structures.py", line 174:
    sage: G = BD.automorphism_group(); G
Expected:
    Permutation Group with generators []
Got:
    Permutation Group with generators [()]
```




---

archive/issue_comments_032198.json:
```json
{
    "body": "Attachment [trac_4383-order-trivial-permgp4.patch](tarball://root/attachments/some-uuid/ticket4383/trac_4383-order-trivial-permgp4.patch) by mabshoff created at 2008-11-29 03:30:51",
    "created_at": "2008-11-29T03:30:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4383#issuecomment-32198",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4383-order-trivial-permgp4.patch](tarball://root/attachments/some-uuid/ticket4383/trac_4383-order-trivial-permgp4.patch) by mabshoff created at 2008-11-29 03:30:51



---

archive/issue_comments_032199.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-29T03:31:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4383#issuecomment-32199",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032200.json:
```json
{
    "body": "Merged\n\n```\ntrac_4383-order-trivial-permgp.patch \ntrac_4383-order-trivial-permgp2.patch\ntrac_4383-order-trivial-permgp3-REBASE.patch\ntrac_4383-order-trivial-permgp4.patch\n```\n\nin Sage 3.2.1.rc0\n\nCheers,\n\nMichael",
    "created_at": "2008-11-29T03:31:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4383#issuecomment-32200",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged

```
trac_4383-order-trivial-permgp.patch 
trac_4383-order-trivial-permgp2.patch
trac_4383-order-trivial-permgp3-REBASE.patch
trac_4383-order-trivial-permgp4.patch
```

in Sage 3.2.1.rc0

Cheers,

Michael



---

archive/issue_events_009904.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-29T03:31:41Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4383",
    "milestone": "sage-3.2.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4383#event-9904"
}
```



---

archive/issue_events_009905.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-29T03:31:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4383",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4383#event-9905"
}
```
