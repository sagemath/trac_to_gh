# Issue 2741: Implement mesh lines in 3d plots

archive/issues_002741.json:
```json
{
    "body": "Assignee: was\n\nCC:  timothyclemans\n\n> >  Is there an easy way to get mesh lines in a plot3d surface?\n\nThis is not implemented.  I wish you would implement it  :-) \n\nRobert Bradshaw might have some useful advise.\n\n> > Sometimes\n> >  it is hard to visualize the plot (especially when it is printed) without\n> >  the mesh lines.\n> >\n> >  If that is easy, what about the possibility of doing some of things that\n> >  Mma does with different types of meshes?  For reference, see:\n> >\n> >  http://reference.wolfram.com/mathematica/ref/Mesh.html\n> >\n> >  http://reference.wolfram.com/mathematica/ref/MeshFunctions.html\n> >\n> >  http://reference.wolfram.com/mathematica/ref/MeshShading.html\n> >\n> >  http://reference.wolfram.com/mathematica/ref/MeshStyle.html\n> >\n\nIssue created by migration from https://trac.sagemath.org/ticket/2741\n\n",
    "created_at": "2008-03-31T18:19:49Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "title": "Implement mesh lines in 3d plots",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2741",
    "user": "jason"
}
```
Assignee: was

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

archive/issue_comments_018845.json:
```json
{
    "body": "Well, he already answered my question in the source.\n\nIn sage/sage/plot/plot3d/index_set.pyx, starting at line 658 (in 2.10.4):\n\n```\n        # If we wanted to turn on display of the mesh lines or dots\n        # we would uncomment thse.  This should be determined by\n        # render_params, probably. \n        #s += '\\npmesh %s mesh\\n'%name\n        #s += '\\npmesh %s dots\\n'%name\n```\n\n\nUncommenting the appropriate line does indeed give a mesh in JMOL.  So now the question is how to expose this to the user.  And how to extend it to do nontrivial mesh functions.",
    "created_at": "2008-03-31T18:34:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2741#issuecomment-18845",
    "user": "jason"
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

archive/issue_comments_018846.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-30T04:24:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2741#issuecomment-18846",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_018847.json:
```json
{
    "body": "fixes doctest failures",
    "created_at": "2008-04-30T05:39:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2741#issuecomment-18847",
    "user": "TimothyClemans"
}
```

fixes doctest failures



---

archive/issue_comments_018848.json:
```json
{
    "body": "Attachment\n\nImpressive plots with mesh lines! There were two doctest failures I fixed them and uploaded a patch.",
    "created_at": "2008-04-30T05:41:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2741#issuecomment-18848",
    "user": "TimothyClemans"
}
```

Attachment

Impressive plots with mesh lines! There were two doctest failures I fixed them and uploaded a patch.



---

archive/issue_comments_018849.json:
```json
{
    "body": "Timothy's patch looks good to me. Somebody didn't doctest his own patch ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-04-30T05:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2741#issuecomment-18849",
    "user": "mabshoff"
}
```

Timothy's patch looks good to me. Somebody didn't doctest his own patch ;)

Cheers,

Michael



---

archive/issue_comments_018850.json:
```json
{
    "body": "Merger in Sage 3.0.1.alpha1",
    "created_at": "2008-04-30T05:47:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2741#issuecomment-18850",
    "user": "mabshoff"
}
```

Merger in Sage 3.0.1.alpha1



---

archive/issue_comments_018851.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-30T05:47:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2741#issuecomment-18851",
    "user": "mabshoff"
}
```

Resolution: fixed
