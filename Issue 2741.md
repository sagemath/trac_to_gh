# Issue 2741: Implement mesh lines in 3d plots

archive/issues_002741.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  timothyclemans\n\n> >  Is there an easy way to get mesh lines in a plot3d surface?\n\n\nThis is not implemented.  I wish you would implement it  :-) \n\nRobert Bradshaw might have some useful advise.\n\n> > Sometimes\n> >  it is hard to visualize the plot (especially when it is printed) without\n> >  the mesh lines.\n\n> >\n> >  If that is easy, what about the possibility of doing some of things that\n> >  Mma does with different types of meshes?  For reference, see:\n\n> >\n> >  http://reference.wolfram.com/mathematica/ref/Mesh.html\n\n> >\n> >  http://reference.wolfram.com/mathematica/ref/MeshFunctions.html\n\n> >\n> >  http://reference.wolfram.com/mathematica/ref/MeshShading.html\n\n> >\n> >  http://reference.wolfram.com/mathematica/ref/MeshStyle.html\n\n> >\n\nIssue created by migration from https://trac.sagemath.org/ticket/2741\n\n",
    "created_at": "2008-03-31T18:19:49Z",
    "labels": [
        "component: graphics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "Implement mesh lines in 3d plots",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2741",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

CC:  timothyclemans

> >  Is there an easy way to get mesh lines in a plot3d surface?


This is not implemented.  I wish you would implement it  :-) 

Robert Bradshaw might have some useful advise.

> > Sometimes
> >  it is hard to visualize the plot (especially when it is printed) without
> >  the mesh lines.

> >
> >  If that is easy, what about the possibility of doing some of things that
> >  Mma does with different types of meshes?  For reference, see:

> >
> >  http://reference.wolfram.com/mathematica/ref/Mesh.html

> >
> >  http://reference.wolfram.com/mathematica/ref/MeshFunctions.html

> >
> >  http://reference.wolfram.com/mathematica/ref/MeshShading.html

> >
> >  http://reference.wolfram.com/mathematica/ref/MeshStyle.html

> >

Issue created by migration from https://trac.sagemath.org/ticket/2741





---

archive/issue_comments_018806.json:
```json
{
    "body": "Well, he already answered my question in the source.\n\nIn sage/sage/plot/plot3d/index_set.pyx, starting at line 658 (in 2.10.4):\n\n```\n        # If we wanted to turn on display of the mesh lines or dots\n        # we would uncomment thse.  This should be determined by\n        # render_params, probably. \n        #s += '\\npmesh %s mesh\\n'%name\n        #s += '\\npmesh %s dots\\n'%name\n```\n\nUncommenting the appropriate line does indeed give a mesh in JMOL.  So now the question is how to expose this to the user.  And how to extend it to do nontrivial mesh functions.",
    "created_at": "2008-03-31T18:34:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2741#issuecomment-18806",
    "user": "https://github.com/jasongrout"
}
```

Well, he already answered my question in the source.

In sage/sage/plot/plot3d/index_set.pyx, starting at line 658 (in 2.10.4):

```
        # If we wanted to turn on display of the mesh lines or dots
        # we would uncomment thse.  This should be determined by
        # render_params, probably. 
        #s += '\npmesh %s mesh\n'%name
        #s += '\npmesh %s dots\n'%name
```

Uncommenting the appropriate line does indeed give a mesh in JMOL.  So now the question is how to expose this to the user.  And how to extend it to do nontrivial mesh functions.



---

archive/issue_comments_018807.json:
```json
{
    "body": "Attachment [sage-2741.patch](tarball://root/attachments/some-uuid/ticket2741/sage-2741.patch) by @williamstein created at 2008-04-30 04:24:33",
    "created_at": "2008-04-30T04:24:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2741#issuecomment-18807",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-2741.patch](tarball://root/attachments/some-uuid/ticket2741/sage-2741.patch) by @williamstein created at 2008-04-30 04:24:33



---

archive/issue_comments_018808.json:
```json
{
    "body": "fixes doctest failures",
    "created_at": "2008-04-30T05:39:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2741#issuecomment-18808",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

fixes doctest failures



---

archive/issue_comments_018809.json:
```json
{
    "body": "Attachment [2741-doctest.patch](tarball://root/attachments/some-uuid/ticket2741/2741-doctest.patch) by TimothyClemans created at 2008-04-30 05:41:09\n\nImpressive plots with mesh lines! There were two doctest failures I fixed them and uploaded a patch.",
    "created_at": "2008-04-30T05:41:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2741#issuecomment-18809",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [2741-doctest.patch](tarball://root/attachments/some-uuid/ticket2741/2741-doctest.patch) by TimothyClemans created at 2008-04-30 05:41:09

Impressive plots with mesh lines! There were two doctest failures I fixed them and uploaded a patch.



---

archive/issue_comments_018810.json:
```json
{
    "body": "Timothy's patch looks good to me. Somebody didn't doctest his own patch ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-04-30T05:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2741#issuecomment-18810",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Timothy's patch looks good to me. Somebody didn't doctest his own patch ;)

Cheers,

Michael



---

archive/issue_comments_018811.json:
```json
{
    "body": "Merger in Sage 3.0.1.alpha1",
    "created_at": "2008-04-30T05:47:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2741#issuecomment-18811",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merger in Sage 3.0.1.alpha1



---

archive/issue_events_006371.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-30T05:47:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2741",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2741#event-6371"
}
```



---

archive/issue_comments_018812.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-30T05:47:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2741#issuecomment-18812",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
