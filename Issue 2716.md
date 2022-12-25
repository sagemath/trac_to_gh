# Issue 2716: convex hulls and polyhedral functions

archive/issues_002716.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe patch adds functions to compute convex hulls and change back and forth from vertices to inequality descriptions of polytopes/polyhedra, using only cddlib and not polymake.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2716\n\n",
    "created_at": "2008-03-29T13:49:51Z",
    "labels": [
        "component: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "convex hulls and polyhedral functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2716",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: mabshoff

The patch adds functions to compute convex hulls and change back and forth from vertices to inequality descriptions of polytopes/polyhedra, using only cddlib and not polymake.

Issue created by migration from https://trac.sagemath.org/ticket/2716





---

archive/issue_comments_018676.json:
```json
{
    "body": "Changing component from Cygwin to linear algebra.",
    "created_at": "2008-03-29T13:57:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2716#issuecomment-18676",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from Cygwin to linear algebra.



---

archive/issue_comments_018677.json:
```json
{
    "body": "Changing assignee from mabshoff to @williamstein.",
    "created_at": "2008-03-29T13:57:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2716#issuecomment-18677",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from mabshoff to @williamstein.



---

archive/issue_events_006338.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-29T13:57:51Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2716",
    "milestone": "sage-2.11",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2716#event-6338"
}
```



---

archive/issue_comments_018678.json:
```json
{
    "body": "Changing component from linear algebra to geometry.",
    "created_at": "2008-03-29T13:58:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2716#issuecomment-18678",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from linear algebra to geometry.



---

archive/issue_comments_018679.json:
```json
{
    "body": "Changing assignee from @williamstein to mhampton.",
    "created_at": "2008-03-29T13:58:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2716#issuecomment-18679",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to mhampton.



---

archive/issue_comments_018680.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2008-03-29T14:30:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2716#issuecomment-18680",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing priority from major to minor.



---

archive/issue_comments_018681.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-03-29T14:30:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2716#issuecomment-18681",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing type from defect to enhancement.



---

archive/issue_events_006339.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mhampton",
    "created_at": "2008-03-30T04:32:27Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2716",
    "milestone": "sage-2.11",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2716#event-6339"
}
```



---

archive/issue_events_006340.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mhampton",
    "created_at": "2008-03-30T04:32:27Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2716",
    "milestone": "sage-3.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2716#event-6340"
}
```



---

archive/issue_comments_018682.json:
```json
{
    "body": "A much improved version is attached as a patch against sage-2.11.  I have moved some general functionality to a polyhedra.py module, which I hope will eventually provide most of what polytope.py does not, but without polymake (just cddlib).  These functions are also used for a 3D groebner fan function.",
    "created_at": "2008-04-05T16:56:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2716#issuecomment-18682",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

A much improved version is attached as a patch against sage-2.11.  I have moved some general functionality to a polyhedra.py module, which I hope will eventually provide most of what polytope.py does not, but without polymake (just cddlib).  These functions are also used for a 3D groebner fan function.



---

archive/issue_comments_018683.json:
```json
{
    "body": "Changing assignee from mhampton to somebody.",
    "created_at": "2008-04-05T16:56:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2716#issuecomment-18683",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing assignee from mhampton to somebody.



---

archive/issue_comments_018684.json:
```json
{
    "body": "**Review**\n* I cannot vouch for the math\n* `trac_2716_gfan_polyhedra.patch` applies cleanly against `3.0.alpha1`\n* all methods have doctests\n* I find the coding/interface style slightly strange and un-Sage-ish:\n\n```\nsage: po = extreme_verts([[1,2],[2,2],[2,1],[0,0]]) \nsage: po.ex_vertices \n[[1, 1, 2], [1, 2, 2], [1, 2, 1], [1, 0, 0]] \n```\n\n* But that shouldn't be a show-stopper, I'm giving it a preliminary positive review\n* PS: My first review with mercurial queues ;-)",
    "created_at": "2008-04-05T22:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2716#issuecomment-18684",
    "user": "https://github.com/malb"
}
```

**Review**
* I cannot vouch for the math
* `trac_2716_gfan_polyhedra.patch` applies cleanly against `3.0.alpha1`
* all methods have doctests
* I find the coding/interface style slightly strange and un-Sage-ish:

```
sage: po = extreme_verts([[1,2],[2,2],[2,1],[0,0]]) 
sage: po.ex_vertices 
[[1, 1, 2], [1, 2, 2], [1, 2, 1], [1, 0, 0]] 
```

* But that shouldn't be a show-stopper, I'm giving it a preliminary positive review
* PS: My first review with mercurial queues ;-)



---

archive/issue_comments_018685.json:
```json
{
    "body": "I do plan on cleaning this up more; I am still giving a lot of thought\nto what polytope classes there should be, and how they should behave,\netc.   When I rearrange things again I will try to give variable names\nmore suggestive names.    In the example below, \"po\" was my temporary\nshorthand for PolyhedralObject, which is a class that I know I will\nchange.\n\nThanks for the review.",
    "created_at": "2008-04-05T23:04:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2716#issuecomment-18685",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

I do plan on cleaning this up more; I am still giving a lot of thought
to what polytope classes there should be, and how they should behave,
etc.   When I rearrange things again I will try to give variable names
more suggestive names.    In the example below, "po" was my temporary
shorthand for PolyhedralObject, which is a class that I know I will
change.

Thanks for the review.



---

archive/issue_comments_018686.json:
```json
{
    "body": "Replying to [comment:7 mhampton]:\n> I do plan on cleaning this up more; I am still giving a lot of thought\n> to what polytope classes there should be, and how they should behave,\n> etc.   When I rearrange things again I will try to give variable names\n> more suggestive names.    In the example below, \"po\" was my temporary\n> shorthand for PolyhedralObject, which is a class that I know I will\n> change.\n\nSorry for not being more precise:\n* it might be fine for the particular situation but general, having functions rather than methods feels odd to me. However, in some cases it is just better.\n* It is quite seldom in the Sage library that attributes are actually accessed as attributes, like: `po.ex_vertices`, whereas in Sage it is more likely to meet `po.ex_vertices()`. However, Python encourages your coding style and I think Sage is off the path here.",
    "created_at": "2008-04-05T23:21:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2716#issuecomment-18686",
    "user": "https://github.com/malb"
}
```

Replying to [comment:7 mhampton]:
> I do plan on cleaning this up more; I am still giving a lot of thought
> to what polytope classes there should be, and how they should behave,
> etc.   When I rearrange things again I will try to give variable names
> more suggestive names.    In the example below, "po" was my temporary
> shorthand for PolyhedralObject, which is a class that I know I will
> change.

Sorry for not being more precise:
* it might be fine for the particular situation but general, having functions rather than methods feels odd to me. However, in some cases it is just better.
* It is quite seldom in the Sage library that attributes are actually accessed as attributes, like: `po.ex_vertices`, whereas in Sage it is more likely to meet `po.ex_vertices()`. However, Python encourages your coding style and I think Sage is off the path here.



---

archive/issue_comments_018687.json:
```json
{
    "body": "Marshall, trac_2716_gfan_polyhedra.patch fails quiet badly when I attempt to merge this into 3.0. Can you rebase this? I know you spend a lot of time in this area, so let's get this finally merged.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-26T04:17:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2716#issuecomment-18687",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Marshall, trac_2716_gfan_polyhedra.patch fails quiet badly when I attempt to merge this into 3.0. Can you rebase this? I know you spend a lot of time in this area, so let's get this finally merged.

Cheers,

Michael



---

archive/issue_comments_018688.json:
```json
{
    "body": "Attaching patch against 3.0; passes tests for me.  Several bugfixes from previous patch as well.",
    "created_at": "2008-04-27T15:35:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2716#issuecomment-18688",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attaching patch against 3.0; passes tests for me.  Several bugfixes from previous patch as well.



---

archive/issue_comments_018689.json:
```json
{
    "body": "Changing keywords from \"\" to \"polyhedra, convex hull, polytope, gfan\".",
    "created_at": "2008-04-27T15:35:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2716#issuecomment-18689",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing keywords from "" to "polyhedra, convex hull, polytope, gfan".



---

archive/issue_comments_018690.json:
```json
{
    "body": "Installs cleanly. sage -testall passed all tests (on an old rather cantankerous machine) but \n\n```\nThe following tests failed:\n\n\n        sage -t  devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py\n```\n\nHowever, when I reran sage -t devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py,\nI got all tests passed. I especially like the render_wireframe plotting function.\n\nLooks like a very interesting patch and I vote to apply it.",
    "created_at": "2008-04-27T20:08:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2716#issuecomment-18690",
    "user": "https://github.com/wdjoyner"
}
```

Installs cleanly. sage -testall passed all tests (on an old rather cantankerous machine) but 

```
The following tests failed:


        sage -t  devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py
```

However, when I reran sage -t devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py,
I got all tests passed. I especially like the render_wireframe plotting function.

Looks like a very interesting patch and I vote to apply it.



---

archive/issue_comments_018691.json:
```json
{
    "body": "We frown upon `from foo.bar import *`, so please fix those.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-28T00:14:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2716#issuecomment-18691",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

We frown upon `from foo.bar import *`, so please fix those.

Cheers,

Michael



---

archive/issue_comments_018692.json:
```json
{
    "body": "Attachment [trac_2716_improved.patch](tarball://root/attachments/some-uuid/ticket2716/trac_2716_improved.patch) by mhampton created at 2008-04-28 18:58:39\n\nimproved improved patch (cleaned up import * issues)",
    "created_at": "2008-04-28T18:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2716#issuecomment-18692",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [trac_2716_improved.patch](tarball://root/attachments/some-uuid/ticket2716/trac_2716_improved.patch) by mhampton created at 2008-04-28 18:58:39

improved improved patch (cleaned up import * issues)



---

archive/issue_comments_018693.json:
```json
{
    "body": "I believe I have made my imports explicit and minimal.",
    "created_at": "2008-04-28T18:59:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2716#issuecomment-18693",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

I believe I have made my imports explicit and minimal.



---

archive/issue_events_006341.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-29T00:18:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2716",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2716#event-6341"
}
```



---

archive/issue_comments_018694.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-29T00:18:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2716#issuecomment-18694",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018695.json:
```json
{
    "body": "Merged trac_2716_improved.patch in Sage 3.0.1.alpha1",
    "created_at": "2008-04-29T00:18:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2716#issuecomment-18695",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_2716_improved.patch in Sage 3.0.1.alpha1
