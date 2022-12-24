# Issue 2755: [with patch, needs review] lattice_polytope.py update

archive/issues_002755.json:
```json
{
    "body": "Assignee: mhampton\n\nFinally, the patch with the second version of the module... Does what was proposed on Sage Days 7 and has doctests for all functions (tests for such things as setstate  do not have explicit calls but certainly use the required functions).\n\nADDITIONS:\n\nconvex_hull(), minkowski_sum(), NEFPartition.dual()\n\nReflexivePolytope(), ReflexivePolytopes()\n\nLatticePolytopeClass.plot3d(), LatticePolytopeClass.skeleton* (points, graph, plot)\n\nVertices of polytopes are now computed by default.\n\nLittle shortcuts like edges() or point().\n\nExamples/tests for each function.\n\nATTACHED FILES:\n\nSaved Sage objects for sequences of all reflexive polytopes in 2 and 3 dimensions with some precomputed data and dictionaries to these sequences allowing fast identification of the isomorphism class under GL(Z) action.\n\nThe module assumes they are located in DB_HOME/reflexive_polytopes/\n\nIssue created by migration from https://trac.sagemath.org/ticket/2755\n\n",
    "created_at": "2008-04-01T17:19:58Z",
    "labels": [
        "geometry",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "[with patch, needs review] lattice_polytope.py update",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2755",
    "user": "@novoselt"
}
```
Assignee: mhampton

Finally, the patch with the second version of the module... Does what was proposed on Sage Days 7 and has doctests for all functions (tests for such things as setstate  do not have explicit calls but certainly use the required functions).

ADDITIONS:

convex_hull(), minkowski_sum(), NEFPartition.dual()

ReflexivePolytope(), ReflexivePolytopes()

LatticePolytopeClass.plot3d(), LatticePolytopeClass.skeleton* (points, graph, plot)

Vertices of polytopes are now computed by default.

Little shortcuts like edges() or point().

Examples/tests for each function.

ATTACHED FILES:

Saved Sage objects for sequences of all reflexive polytopes in 2 and 3 dimensions with some precomputed data and dictionaries to these sequences allowing fast identification of the isomorphism class under GL(Z) action.

The module assumes they are located in DB_HOME/reflexive_polytopes/

Issue created by migration from https://trac.sagemath.org/ticket/2755





---

archive/issue_comments_018926.json:
```json
{
    "body": "Attachment [lattice_polytope2.patch](tarball://root/attachments/some-uuid/ticket2755/lattice_polytope2.patch) by @novoselt created at 2008-04-01 17:21:02",
    "created_at": "2008-04-01T17:21:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2755#issuecomment-18926",
    "user": "@novoselt"
}
```

Attachment [lattice_polytope2.patch](tarball://root/attachments/some-uuid/ticket2755/lattice_polytope2.patch) by @novoselt created at 2008-04-01 17:21:02



---

archive/issue_comments_018927.json:
```json
{
    "body": "Attachment [reflexive_polytopes_2d.sobj](tarball://root/attachments/some-uuid/ticket2755/reflexive_polytopes_2d.sobj) by @novoselt created at 2008-04-01 17:21:25",
    "created_at": "2008-04-01T17:21:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2755#issuecomment-18927",
    "user": "@novoselt"
}
```

Attachment [reflexive_polytopes_2d.sobj](tarball://root/attachments/some-uuid/ticket2755/reflexive_polytopes_2d.sobj) by @novoselt created at 2008-04-01 17:21:25



---

archive/issue_comments_018928.json:
```json
{
    "body": "Attachment [reflexive_polytopes_2d_dict.sobj](tarball://root/attachments/some-uuid/ticket2755/reflexive_polytopes_2d_dict.sobj) by @novoselt created at 2008-04-01 17:22:21",
    "created_at": "2008-04-01T17:22:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2755#issuecomment-18928",
    "user": "@novoselt"
}
```

Attachment [reflexive_polytopes_2d_dict.sobj](tarball://root/attachments/some-uuid/ticket2755/reflexive_polytopes_2d_dict.sobj) by @novoselt created at 2008-04-01 17:22:21



---

archive/issue_comments_018929.json:
```json
{
    "body": "Attachment [reflexive_polytopes_3d_dict.sobj](tarball://root/attachments/some-uuid/ticket2755/reflexive_polytopes_3d_dict.sobj) by @novoselt created at 2008-04-01 17:24:36\n\nThere is one more file which is too big for attaching it to the ticket. All four are available at\nhttp://sage.math.washington.edu/home/novoselt/patch%202008-04-01/",
    "created_at": "2008-04-01T17:24:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2755#issuecomment-18929",
    "user": "@novoselt"
}
```

Attachment [reflexive_polytopes_3d_dict.sobj](tarball://root/attachments/some-uuid/ticket2755/reflexive_polytopes_3d_dict.sobj) by @novoselt created at 2008-04-01 17:24:36

There is one more file which is too big for attaching it to the ticket. All four are available at
http://sage.math.washington.edu/home/novoselt/patch%202008-04-01/



---

archive/issue_comments_018930.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-02T01:20:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2755#issuecomment-18930",
    "user": "mhampton"
}
```

Changing status from new to assigned.



---

archive/issue_comments_018931.json:
```json
{
    "body": "Changing assignee from mhampton to mabshoff.",
    "created_at": "2008-04-02T18:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2755#issuecomment-18931",
    "user": "mhampton"
}
```

Changing assignee from mhampton to mabshoff.



---

archive/issue_comments_018932.json:
```json
{
    "body": "Nice job!  This is a positive review, pending the very minor changes I am attaching as a patch.  100% coverage, passes all tests on my mac intel 10.4.11 machine.  \n\nIn the future, it might be worth replacing the convex_hull function by my cddlib interface, since it seems that PALP is not configured to handle large polytopes in higher dimensions (for example, it seems extremely fragile starting in dimension 5).\n\nThe patch makes convex_hull a little more robust by explicitly casting the input to ZZ; previously it would crash on python int lists.",
    "created_at": "2008-04-02T18:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2755#issuecomment-18932",
    "user": "mhampton"
}
```

Nice job!  This is a positive review, pending the very minor changes I am attaching as a patch.  100% coverage, passes all tests on my mac intel 10.4.11 machine.  

In the future, it might be worth replacing the convex_hull function by my cddlib interface, since it seems that PALP is not configured to handle large polytopes in higher dimensions (for example, it seems extremely fragile starting in dimension 5).

The patch makes convex_hull a little more robust by explicitly casting the input to ZZ; previously it would crash on python int lists.



---

archive/issue_comments_018933.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2008-04-02T18:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2755#issuecomment-18933",
    "user": "mhampton"
}
```

Changing status from assigned to new.



---

archive/issue_comments_018934.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2008-04-02T18:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2755#issuecomment-18934",
    "user": "mhampton"
}
```

Changing priority from major to minor.



---

archive/issue_comments_018935.json:
```json
{
    "body": "Attachment [trac_2755_review1.patch](tarball://root/attachments/some-uuid/ticket2755/trac_2755_review1.patch) by mhampton created at 2008-04-02 18:28:01\n\nminor changes; apply after previous patch",
    "created_at": "2008-04-02T18:28:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2755#issuecomment-18935",
    "user": "mhampton"
}
```

Attachment [trac_2755_review1.patch](tarball://root/attachments/some-uuid/ticket2755/trac_2755_review1.patch) by mhampton created at 2008-04-02 18:28:01

minor changes; apply after previous patch



---

archive/issue_comments_018936.json:
```json
{
    "body": "Sorry for crashes on large dimension - it is my fault, not PALP. I have encountered this issue before but forgot about it since usually polytopes I work with are small enough.\n\nThe problem is in piping to poly.x - if the output is too big to fit into the buffer, the output is never read. A fast workaround is to use temp files as it is done in lattice_polytope._palp function, but it maybe slower. On the other hand, I didn't actually benchmark it and interface to a C-library definitely should be better.",
    "created_at": "2008-04-02T18:46:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2755#issuecomment-18936",
    "user": "@novoselt"
}
```

Sorry for crashes on large dimension - it is my fault, not PALP. I have encountered this issue before but forgot about it since usually polytopes I work with are small enough.

The problem is in piping to poly.x - if the output is too big to fit into the buffer, the output is never read. A fast workaround is to use temp files as it is done in lattice_polytope._palp function, but it maybe slower. On the other hand, I didn't actually benchmark it and interface to a C-library definitely should be better.



---

archive/issue_comments_018937.json:
```json
{
    "body": "Let's make a push to get this merged. What is the status on the requested changes? Or should we merge this as is and then hope that people will finish to polish this code?\n\nCheers,\n\nMichael",
    "created_at": "2008-04-26T04:20:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2755#issuecomment-18937",
    "user": "mabshoff"
}
```

Let's make a push to get this merged. What is the status on the requested changes? Or should we merge this as is and then hope that people will finish to polish this code?

Cheers,

Michael



---

archive/issue_comments_018938.json:
```json
{
    "body": "I think we should merge this as is.  Andrey wrote to me just now and wrote: \"I had the impression that the \"minor change\" was the extra patch with ZZ-conversion and otherwise the current version is adequate.\"",
    "created_at": "2008-04-26T19:59:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2755#issuecomment-18938",
    "user": "@williamstein"
}
```

I think we should merge this as is.  Andrey wrote to me just now and wrote: "I had the impression that the "minor change" was the extra patch with ZZ-conversion and otherwise the current version is adequate."



---

archive/issue_comments_018939.json:
```json
{
    "body": "Ok, where do we stick the sobj files? I think they should end up in \"data_location = DB_HOME + '/reflexive_polytopes/'\". This is $SAGE_ROOT/data/reflexive_polytopes/ - so I would need to create that directory. I will play around with this and see what happens.\n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2008-04-30T02:24:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2755#issuecomment-18939",
    "user": "mabshoff"
}
```

Ok, where do we stick the sobj files? I think they should end up in "data_location = DB_HOME + '/reflexive_polytopes/'". This is $SAGE_ROOT/data/reflexive_polytopes/ - so I would need to create that directory. I will play around with this and see what happens.

Thoughts?

Cheers,

Michael



---

archive/issue_comments_018940.json:
```json
{
    "body": "Looking at the problem some more it seems that we need an lattice_polytope-db.spkg. That is the way we deal with all the other databases in the SAGE_DATA directory. This should be fairly trivial to do and not require formal voting due to its minuscule size.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-30T02:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2755#issuecomment-18940",
    "user": "mabshoff"
}
```

Looking at the problem some more it seems that we need an lattice_polytope-db.spkg. That is the way we deal with all the other databases in the SAGE_DATA directory. This should be fairly trivial to do and not require formal voting due to its minuscule size.

Cheers,

Michael



---

archive/issue_comments_018941.json:
```json
{
    "body": "What exactly this package should do? Should it be an optional package? (In this case some functions should probably be rewritten to react in a nice way to the absence of data files.)",
    "created_at": "2008-04-30T05:57:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2755#issuecomment-18941",
    "user": "@novoselt"
}
```

What exactly this package should do? Should it be an optional package? (In this case some functions should probably be rewritten to react in a nice way to the absence of data files.)



---

archive/issue_comments_018942.json:
```json
{
    "body": "Nah, it will be standard and I will take care of it shortly. You can take over from there and maybe add larger optional databases for polytopes of higher dimension if that makes sense.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-30T06:10:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2755#issuecomment-18942",
    "user": "mabshoff"
}
```

Nah, it will be standard and I will take care of it shortly. You can take over from there and maybe add larger optional databases for polytopes of higher dimension if that makes sense.

Cheers,

Michael



---

archive/issue_comments_018943.json:
```json
{
    "body": "Ok, good news and bad news:\n\nBad news first: tice_polytope2.patch needs a rebase against Sage 3.0.1.alpha1 - out in 10 minutes.\n\n```\nsage-3.0.1.alpha1/devel/sage$ patch -p1 --dry-run < lattice_polytope2.patch\npatching file sage/geometry/all.py\nHunk #1 succeeded at 3 with fuzz 1 (offset 2 lines).\npatching file sage/geometry/lattice_polytope.py\nHunk #2 FAILED at 57.\n1 out of 50 hunks FAILED -- saving rejects to file sage/geometry/lattice_polytope.py.rej\n```\n\nBut I create a spkg with the polytope db data with all four files, which has been merged in Sage 3.0.1.alpha1.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-01T06:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2755#issuecomment-18943",
    "user": "mabshoff"
}
```

Ok, good news and bad news:

Bad news first: tice_polytope2.patch needs a rebase against Sage 3.0.1.alpha1 - out in 10 minutes.

```
sage-3.0.1.alpha1/devel/sage$ patch -p1 --dry-run < lattice_polytope2.patch
patching file sage/geometry/all.py
Hunk #1 succeeded at 3 with fuzz 1 (offset 2 lines).
patching file sage/geometry/lattice_polytope.py
Hunk #2 FAILED at 57.
1 out of 50 hunks FAILED -- saving rejects to file sage/geometry/lattice_polytope.py.rej
```

But I create a spkg with the polytope db data with all four files, which has been merged in Sage 3.0.1.alpha1.

Cheers,

Michael



---

archive/issue_comments_018944.json:
```json
{
    "body": "Sorry for a probably dumb question, but what is a \"rebase?\"",
    "created_at": "2008-05-01T06:59:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2755#issuecomment-18944",
    "user": "@novoselt"
}
```

Sorry for a probably dumb question, but what is a "rebase?"



---

archive/issue_comments_018945.json:
```json
{
    "body": "Replying to [comment:12 novoselt]:\n> Sorry for a probably dumb question, but what is a \"rebase?\"\n\nHi,\n\nno dumb questions here, just dumb answers. \"rebase\" in this context means that you should fix the patch so it does apply cleanly against the latest release. 3.0.1.alpha1 just came out and there is a binary for sage.math in case you don't want to build from scratch yourself. The problem in the patch was in the second hunk and since that was a rather large one I didn't want to fiddle in it and potentially break things. \n\nLet me know if you have any more questions.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-01T07:10:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2755#issuecomment-18945",
    "user": "mabshoff"
}
```

Replying to [comment:12 novoselt]:
> Sorry for a probably dumb question, but what is a "rebase?"

Hi,

no dumb questions here, just dumb answers. "rebase" in this context means that you should fix the patch so it does apply cleanly against the latest release. 3.0.1.alpha1 just came out and there is a binary for sage.math in case you don't want to build from scratch yourself. The problem in the patch was in the second hunk and since that was a rather large one I didn't want to fiddle in it and potentially break things. 

Let me know if you have any more questions.

Cheers,

Michael



---

archive/issue_comments_018946.json:
```json
{
    "body": "Attachment [lp_patch_for_3.0.1.alpha1.patch](tarball://root/attachments/some-uuid/ticket2755/lp_patch_for_3.0.1.alpha1.patch) by @novoselt created at 2008-05-01 23:49:45\n\nUpdated patch",
    "created_at": "2008-05-01T23:49:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2755#issuecomment-18946",
    "user": "@novoselt"
}
```

Attachment [lp_patch_for_3.0.1.alpha1.patch](tarball://root/attachments/some-uuid/ticket2755/lp_patch_for_3.0.1.alpha1.patch) by @novoselt created at 2008-05-01 23:49:45

Updated patch



---

archive/issue_comments_018947.json:
```json
{
    "body": "ZZ conversion patch still should be applied, I forgot about that one.",
    "created_at": "2008-05-02T00:00:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2755#issuecomment-18947",
    "user": "@novoselt"
}
```

ZZ conversion patch still should be applied, I forgot about that one.



---

archive/issue_comments_018948.json:
```json
{
    "body": "The two new patches apply, but now I get the following, probably harmless, doctest failure:\n\n```\nsage -t  devel/sage/sage/rings/number_field/totallyreal_rel.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.1.rc0/tmp/totallyreal_rel.py\", line 98:\n    sage: sage.rings.number_field.totallyreal_rel.integral_elements_in_box(K, [[0,5],[0,5]])\nExpected:\n    [0, 5, 3, -alpha + 2, -alpha + 3, 1, 2, 4, alpha + 2, alpha + 3]\nGot:\n    [0, 5, -alpha + 2, -alpha + 3, 1, 2, 3, 4, alpha + 2, alpha + 3]\n**********************************************************************\n```\n\nI will contact Craig Citro and John Voight to see what their take on this is. Once this is resolved I will merge both patches.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-02T10:20:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2755#issuecomment-18948",
    "user": "mabshoff"
}
```

The two new patches apply, but now I get the following, probably harmless, doctest failure:

```
sage -t  devel/sage/sage/rings/number_field/totallyreal_rel.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.1.rc0/tmp/totallyreal_rel.py", line 98:
    sage: sage.rings.number_field.totallyreal_rel.integral_elements_in_box(K, [[0,5],[0,5]])
Expected:
    [0, 5, 3, -alpha + 2, -alpha + 3, 1, 2, 4, alpha + 2, alpha + 3]
Got:
    [0, 5, -alpha + 2, -alpha + 3, 1, 2, 3, 4, alpha + 2, alpha + 3]
**********************************************************************
```

I will contact Craig Citro and John Voight to see what their take on this is. Once this is resolved I will merge both patches.

Cheers,

Michael



---

archive/issue_comments_018949.json:
```json
{
    "body": "John says:\n\n```\nYes, the ordering of the elements does not at all affect the\ncorrectness of the output--the most mathematically correct thing would\nbe to output a set.   This change can be due to any number of things,\nbut it's probably not worth ascertaining the exact cause.\n\nJV \n```\n\nErgo: positive review since I will fix the doctest issue. Let's hope this is not CPU or endianess dependent.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-02T17:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2755#issuecomment-18949",
    "user": "mabshoff"
}
```

John says:

```
Yes, the ordering of the elements does not at all affect the
correctness of the output--the most mathematically correct thing would
be to output a set.   This change can be due to any number of things,
but it's probably not worth ascertaining the exact cause.

JV 
```

Ergo: positive review since I will fix the doctest issue. Let's hope this is not CPU or endianess dependent.

Cheers,

Michael



---

archive/issue_comments_018950.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-02T17:38:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2755#issuecomment-18950",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018951.json:
```json
{
    "body": "Merged in Sage 3.0.1.rc0",
    "created_at": "2008-05-02T17:38:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2755#issuecomment-18951",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.1.rc0
