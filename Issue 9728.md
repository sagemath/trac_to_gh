# Issue 9728: Moving the Linear transformations interact from wiki into the library.

archive/issues_009728.json:
```json
{
    "body": "Assignee: itolkov, jason\n\nCC:  mhampton nishanth.amuluru@gmail.com\n\nThis code moves the interact example for linear transformations from the wiki to the library. \n\nIssue created by migration from https://trac.sagemath.org/ticket/9728\n\n",
    "created_at": "2010-08-11T21:33:05Z",
    "labels": [
        "component: interact",
        "minor"
    ],
    "title": "Moving the Linear transformations interact from wiki into the library.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9728",
    "user": "https://trac.sagemath.org/admin/accounts/users/punchagan"
}
```
Assignee: itolkov, jason

CC:  mhampton nishanth.amuluru@gmail.com

This code moves the interact example for linear transformations from the wiki to the library. 

Issue created by migration from https://trac.sagemath.org/ticket/9728





---

archive/issue_comments_094924.json:
```json
{
    "body": "Attachment [linear_transformation_interact.patch](tarball://root/attachments/some-uuid/ticket9728/linear_transformation_interact.patch) by punchagan created at 2010-08-11 21:34:21",
    "created_at": "2010-08-11T21:34:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9728#issuecomment-94924",
    "user": "https://trac.sagemath.org/admin/accounts/users/punchagan"
}
```

Attachment [linear_transformation_interact.patch](tarball://root/attachments/some-uuid/ticket9728/linear_transformation_interact.patch) by punchagan created at 2010-08-11 21:34:21



---

archive/issue_comments_094925.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-12T04:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9728#issuecomment-94925",
    "user": "https://trac.sagemath.org/admin/accounts/users/punchagan"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_094926.json:
```json
{
    "body": "Does this conflict with #9623?  It would be great to get that in first, then this and #9729.",
    "created_at": "2010-09-21T20:06:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9728#issuecomment-94926",
    "user": "https://github.com/kcrisman"
}
```

Does this conflict with #9623?  It would be great to get that in first, then this and #9729.



---

archive/issue_comments_094927.json:
```json
{
    "body": "So far as I can tell, this doesn't conflict with 9623. At very least, they don't attempt to implement overlapping interacts.",
    "created_at": "2010-11-07T07:16:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9728#issuecomment-94927",
    "user": "https://trac.sagemath.org/admin/accounts/users/samhop"
}
```

So far as I can tell, this doesn't conflict with 9623. At very least, they don't attempt to implement overlapping interacts.



---

archive/issue_comments_094928.json:
```json
{
    "body": "Attachment [trac_9728_add_user_definable_matrix.patch](tarball://root/attachments/some-uuid/ticket9728/trac_9728_add_user_definable_matrix.patch) by samhop created at 2010-11-07 07:17:05\n\nadds capability for user to set the matrix defining the transformation",
    "created_at": "2010-11-07T07:17:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9728#issuecomment-94928",
    "user": "https://trac.sagemath.org/admin/accounts/users/samhop"
}
```

Attachment [trac_9728_add_user_definable_matrix.patch](tarball://root/attachments/some-uuid/ticket9728/trac_9728_add_user_definable_matrix.patch) by samhop created at 2010-11-07 07:17:05

adds capability for user to set the matrix defining the transformation



---

archive/issue_comments_094929.json:
```json
{
    "body": "I want to propose some changes to this interact:\n\n* Adding a 2x3 transformation (affine, I guess) does not fit with plotting vectors, IMHO. I'd stick to linear transformations and possibly add a second interact for affine transformations.\n* Use input_grid instead of input_box for the matrix.\n* Why plot two concentric circles? It is useful to communicate that the aspect_ratio is 1, but if the axes are present, I don't think it's necessary.\n* Why not plot the unit sphere, and its image under A, instead? Using the same colors as with the vectors, this makes the idea more clear.\n\nSo how about using the following code instead:\n\n```\n@interact \ndef linear_transformation(\n    theta = slider(0, 2*pi, .1), \n    r     = slider(0.1,  2, .1, default=1),\n    A     = input_grid(2, 2, default = [[1,-1],[-1,1/2]],\n                             to_value=matrix)):\n    \"\"\"An interact which illustrates ...\n    \"\"\"\n    v=vector([r*cos(theta), r*sin(theta)]) \n    w = A*v\n\n    unit_sphere = circle((0,0), radius = 1, rgbcolor = (1,0,0))\n    var('t')\n    image_of_sphere = parametric_plot(A*vector([sin(t),cos(t)]), \n                         (t, 0, 2*pi), rgbcolor=(0,0,1))\n    \n    html(\"$v = %s,; %s w=%s$\"%(v.n(4),latex(A),w.n(4)))     \n    show(v.plot(rgbcolor=(1,0,0)) +\n         w.plot(rgbcolor=(0,0,1)) +\n         unit_sphere + image_of_sphere,\n         aspect_ratio=1)\n```\n",
    "created_at": "2010-11-18T09:46:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9728#issuecomment-94929",
    "user": "https://trac.sagemath.org/admin/accounts/users/pang"
}
```

I want to propose some changes to this interact:

* Adding a 2x3 transformation (affine, I guess) does not fit with plotting vectors, IMHO. I'd stick to linear transformations and possibly add a second interact for affine transformations.
* Use input_grid instead of input_box for the matrix.
* Why plot two concentric circles? It is useful to communicate that the aspect_ratio is 1, but if the axes are present, I don't think it's necessary.
* Why not plot the unit sphere, and its image under A, instead? Using the same colors as with the vectors, this makes the idea more clear.

So how about using the following code instead:

```
@interact 
def linear_transformation(
    theta = slider(0, 2*pi, .1), 
    r     = slider(0.1,  2, .1, default=1),
    A     = input_grid(2, 2, default = [[1,-1],[-1,1/2]],
                             to_value=matrix)):
    """An interact which illustrates ...
    """
    v=vector([r*cos(theta), r*sin(theta)]) 
    w = A*v

    unit_sphere = circle((0,0), radius = 1, rgbcolor = (1,0,0))
    var('t')
    image_of_sphere = parametric_plot(A*vector([sin(t),cos(t)]), 
                         (t, 0, 2*pi), rgbcolor=(0,0,1))
    
    html("$v = %s,; %s w=%s$"%(v.n(4),latex(A),w.n(4)))     
    show(v.plot(rgbcolor=(1,0,0)) +
         w.plot(rgbcolor=(0,0,1)) +
         unit_sphere + image_of_sphere,
         aspect_ratio=1)
```




---

archive/issue_comments_094930.json:
```json
{
    "body": "Attachment [linear_transformation.png](tarball://root/attachments/some-uuid/ticket9728/linear_transformation.png) by mhampton created at 2011-01-12 23:13:11",
    "created_at": "2011-01-12T23:13:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9728#issuecomment-94930",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [linear_transformation.png](tarball://root/attachments/some-uuid/ticket9728/linear_transformation.png) by mhampton created at 2011-01-12 23:13:11



---

archive/issue_comments_094931.json:
```json
{
    "body": "Based on pang's comments, apparently this is 'needs work'.",
    "created_at": "2011-06-13T18:13:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9728#issuecomment-94931",
    "user": "https://github.com/kcrisman"
}
```

Based on pang's comments, apparently this is 'needs work'.



---

archive/issue_comments_094932.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-06-13T18:13:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9728#issuecomment-94932",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.
