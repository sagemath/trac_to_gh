# Issue 3719: bug in group cohomology

archive/issues_003719.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  alexghitza\n\nAs reported by Ursula Whitcher\n\n\n```\nsage: G = SymmetricGroup(4)\nsage: G.cohomology(1,2)\n```\n\nyields an error. The problem is a bug in the current version of the GAP package HAP, version 1.8.5. The latest version 1.8.7 but there the bug still exists\n\n\n```\ngap> G := SymmetricGroup(4);\nSym( [ 1 .. 4 ] )\ngap> GroupCohomology(G,1); ## an improvement over 1.8.5\n[  ]\ngap> GroupCohomology(G,1,2);\nList Element: <position> must be a positive integer (not a integer) at\nif IsInt( C!.fpIntHom[n] )  then\n...\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3719\n\n",
    "created_at": "2008-07-24T11:16:49Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "bug in group cohomology",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3719",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: tbd

CC:  alexghitza

As reported by Ursula Whitcher


```
sage: G = SymmetricGroup(4)
sage: G.cohomology(1,2)
```

yields an error. The problem is a bug in the current version of the GAP package HAP, version 1.8.5. The latest version 1.8.7 but there the bug still exists


```
gap> G := SymmetricGroup(4);
Sym( [ 1 .. 4 ] )
gap> GroupCohomology(G,1); ## an improvement over 1.8.5
[  ]
gap> GroupCohomology(G,1,2);
List Element: <position> must be a positive integer (not a integer) at
if IsInt( C!.fpIntHom[n] )  then
...
```



Issue created by migration from https://trac.sagemath.org/ticket/3719





---

archive/issue_comments_026329.json:
```json
{
    "body": "I posted a new gap_packages archive to\nhttp://sage.math.washington.edu/home/wdj/patches/gap_packages-4.4.10_6.spkg",
    "created_at": "2008-08-03T02:35:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3719#issuecomment-26329",
    "user": "https://github.com/wdjoyner"
}
```

I posted a new gap_packages archive to
http://sage.math.washington.edu/home/wdj/patches/gap_packages-4.4.10_6.spkg



---

archive/issue_comments_026330.json:
```json
{
    "body": "Sorry, meant to add that this passes sage -testall on amd64 hardy heron and includes hap1.8.8 which fixes the problem reported above.\n\n\n```\nsage: gap.eval('LoadPackage(\"hap\")')\n'true'\nsage: G = SymmetricGroup(4)\nsage: G.cohomology(1,2)\nMultiplicative Abelian Group isomorphic to C2\n```\n",
    "created_at": "2008-08-03T02:38:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3719#issuecomment-26330",
    "user": "https://github.com/wdjoyner"
}
```

Sorry, meant to add that this passes sage -testall on amd64 hardy heron and includes hap1.8.8 which fixes the problem reported above.


```
sage: gap.eval('LoadPackage("hap")')
'true'
sage: G = SymmetricGroup(4)
sage: G.cohomology(1,2)
Multiplicative Abelian Group isomorphic to C2
```




---

archive/issue_comments_026331.json:
```json
{
    "body": "David,\n\nplease also add an optional doctest that verifies that the issue has been fixed.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-03T08:13:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3719#issuecomment-26331",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

David,

please also add an optional doctest that verifies that the issue has been fixed.

Cheers,

Michael



---

archive/issue_comments_026332.json:
```json
{
    "body": "Michael:\nYou mean, supply a patch to permgroup.py with this addition to the docstring to the group_cohomology method for a new trac ticket?",
    "created_at": "2008-08-03T12:13:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3719#issuecomment-26332",
    "user": "https://github.com/wdjoyner"
}
```

Michael:
You mean, supply a patch to permgroup.py with this addition to the docstring to the group_cohomology method for a new trac ticket?



---

archive/issue_comments_026333.json:
```json
{
    "body": "Replying to [comment:5 wdj]:\n> Michael:\n> You mean, supply a patch to permgroup.py with this addition to the docstring to the group_cohomology method for a new trac ticket?\n\nYes, it should be an optional doctest. I am somewhat concerned that the author of the GAP package just rereleased the package with the bug fix instead of incrementing the release number. Since various packaging efforts are under way I could imagine something like this not getting fixed upstream in other distributions, so the doctest when run with optional flags would show that the problem remains unfixed. \n\nIt is still my plan to used optional testing in the future at least for the build on sage.math per default.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-03T13:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3719#issuecomment-26333",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:5 wdj]:
> Michael:
> You mean, supply a patch to permgroup.py with this addition to the docstring to the group_cohomology method for a new trac ticket?

Yes, it should be an optional doctest. I am somewhat concerned that the author of the GAP package just rereleased the package with the bug fix instead of incrementing the release number. Since various packaging efforts are under way I could imagine something like this not getting fixed upstream in other distributions, so the doctest when run with optional flags would show that the problem remains unfixed. 

It is still my plan to used optional testing in the future at least for the build on sage.math per default.

Cheers,

Michael



---

archive/issue_comments_026334.json:
```json
{
    "body": "docstring addition patch based on 3.1.alpha0",
    "created_at": "2008-08-03T14:48:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3719#issuecomment-26334",
    "user": "https://github.com/wdjoyner"
}
```

docstring addition patch based on 3.1.alpha0



---

archive/issue_comments_026335.json:
```json
{
    "body": "Attachment [10128.patch](tarball://root/attachments/some-uuid/ticket3719/10128.patch) by @wdjoyner created at 2008-08-03 14:54:28\n\nOkay, I just attached the patch you requested to this ticket. (I wasn't sure if it needed a new ticket or not.) It passes sage -t but it dawned on me afterwards that sage -t would not test for optional docstring additions. Anyway, hope this is what you were looking for.\n\nBTW, I am one of the webmasters for GAP (hence involved wityh package updates) and you can be sure that hap 1.8.8 will definitely get applied upstream, probably in the next week or so.",
    "created_at": "2008-08-03T14:54:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3719#issuecomment-26335",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [10128.patch](tarball://root/attachments/some-uuid/ticket3719/10128.patch) by @wdjoyner created at 2008-08-03 14:54:28

Okay, I just attached the patch you requested to this ticket. (I wasn't sure if it needed a new ticket or not.) It passes sage -t but it dawned on me afterwards that sage -t would not test for optional docstring additions. Anyway, hope this is what you were looking for.

BTW, I am one of the webmasters for GAP (hence involved wityh package updates) and you can be sure that hap 1.8.8 will definitely get applied upstream, probably in the next week or so.



---

archive/issue_comments_026336.json:
```json
{
    "body": "> Okay, I just attached the patch you requested to this ticket. (I wasn't sure\n>  if it needed a new ticket or not.) It passes sage -t but it dawned on \n> me afterwards that sage -t would not test for optional docstring additions. \n\nUse\n\n```\n\n  sage -t --optional \n\n```\n",
    "created_at": "2008-08-03T17:48:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3719#issuecomment-26336",
    "user": "https://github.com/williamstein"
}
```

> Okay, I just attached the patch you requested to this ticket. (I wasn't sure
>  if it needed a new ticket or not.) It passes sage -t but it dawned on 
> me afterwards that sage -t would not test for optional docstring additions. 

Use

```

  sage -t --optional 

```




---

archive/issue_comments_026337.json:
```json
{
    "body": "Attachment [10129.patch](tarball://root/attachments/some-uuid/ticket3719/10129.patch) by @wdjoyner created at 2008-08-04 04:02:48\n\nbased on 3.1.alpha0 and probably the previous patch",
    "created_at": "2008-08-04T04:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3719#issuecomment-26337",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [10129.patch](tarball://root/attachments/some-uuid/ticket3719/10129.patch) by @wdjoyner created at 2008-08-04 04:02:48

based on 3.1.alpha0 and probably the previous patch



---

archive/issue_comments_026338.json:
```json
{
    "body": "Okay, the attached passes sage -t --optional\nI had to make some changes to the code. For some reason, it seems gap packages were not loading for me properly (eg, gap.eval('LoadPackage(\"hap\")') gave a traceback the first time but loaded it the second time...). That was fixed with some try/except trickery which seems harmless even if packages do load as they should. Also, GAP's RequirePackage is actually being deprecated, so I replaced them with the preferred LoadPackage. Finally, Molien series do not require an optional package, so I removed some comments in the docstring for that method.\nHope this is okay now.",
    "created_at": "2008-08-04T04:08:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3719#issuecomment-26338",
    "user": "https://github.com/wdjoyner"
}
```

Okay, the attached passes sage -t --optional
I had to make some changes to the code. For some reason, it seems gap packages were not loading for me properly (eg, gap.eval('LoadPackage("hap")') gave a traceback the first time but loaded it the second time...). That was fixed with some try/except trickery which seems harmless even if packages do load as they should. Also, GAP's RequirePackage is actually being deprecated, so I replaced them with the preferred LoadPackage. Finally, Molien series do not require an optional package, so I removed some comments in the docstring for that method.
Hope this is okay now.



---

archive/issue_comments_026339.json:
```json
{
    "body": "Looks good.  The new spkg fixes the problem that was reported, and the few things that broke in the upgrade are fixed by the two patches.",
    "created_at": "2008-08-27T06:44:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3719#issuecomment-26339",
    "user": "https://github.com/aghitza"
}
```

Looks good.  The new spkg fixes the problem that was reported, and the few things that broke in the upgrade are fixed by the two patches.



---

archive/issue_comments_026340.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-27T08:08:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3719#issuecomment-26340",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026341.json:
```json
{
    "body": "Merged both patches in Sage 3.1.2.alpha1.\n\nDavid,\n\nI added an hg repo to the spkg (but kept the p6 patchlevel). Please base future spkgs on the spkg\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha1/gap_packages-4.4.10_6.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-08-27T08:08:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3719#issuecomment-26341",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.1.2.alpha1.

David,

I added an hg repo to the spkg (but kept the p6 patchlevel). Please base future spkgs on the spkg

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha1/gap_packages-4.4.10_6.spkg

Cheers,

Michael



---

archive/issue_events_003939.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-08-27T08:08:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3719",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3719#event-3939"
}
```
