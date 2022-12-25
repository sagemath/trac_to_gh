# Issue 7872: Adding coordinate transformations to plot3d

archive/issues_007872.json:
```json
{
    "body": "Assignee: olazo\n\nCC:  wcauchois @jasongrout mhampton olazo @kcrisman\n\nWhile developing a command called transform_plot3d, that generalized ploting in diferent coordinate systems, Jason Grout suggested to me that such a command would be better implemented within plot3d.\n\nI agreed to that, so I propose an adition to plot3d's syntax: \"plot3d(function,var1range,var2range,transformation=None,**kwds)\" where transformation is a 4-tuple containing 3 functions of arity 3, and a variable which is to be interpreted as the function to be ploted. Like this (r*cos(fi),r*sin(fi),z,r), so the function will be ploted as r.\n\nIt's inclution within plot3d would be something on the likes of\n\n\n```\ndef plot3d_new(f,v1ran,v2ran,transformation=None,**kwds):\n    if transformation==None:\n        return plot3d(f,v1ran,v2ran,**kwds)\n    else:\n        v1=v1ran[0]\n        v2=v2ran[0]\n\n        if transformation=='spherical':\n            r=var('r')\n            transformation=(r*cos(v1)*sin(v2),r*sin(v1)*sin(v2),r*cos(v2),r)\n        elif transformation=='cylindrical':\n            r=var('r')\n            transformation=(r*cos(v1),r*sin(v1),v2,r)\n        elif str(type(transformation))==\"<type 'str'>\":\n            print 'Warning: the transformation given is not amongst the options, it will be ignored'\n            return plot3d(f,v1ran,v2ran,**kwds)\n\n        fvar=transformation[3]\n        transformation=(transformation[0],transformation[1],transformation[2])\n\n        try:\n            R=[t.subs({fvar:f}) for t in transformation]\n        except:\n            def subs_func(t):\n                return lambda x,y: t.subs({fvar:f(x,y), v1:x, v2:y})\n            R=map(subs_func,transformation)\n        return parametric_plot(R,v1ran,v2ran,**kwds)\n```\n\n\nExamples can be found in [http://www.sagenb.org/home/omologos/9/](http://www.sagenb.org/home/omologos/9/).\n\nSpherical and cylindrical plots are now meant to be purely derived from plot3d. So tickets [http://trac.sagemath.org/sage_trac/ticket/7850](http://trac.sagemath.org/sage_trac/ticket/7850) and [http://trac.sagemath.org/sage_trac/ticket/7869](http://trac.sagemath.org/sage_trac/ticket/7869) should be updated\n\nIssue created by migration from https://trac.sagemath.org/ticket/7872\n\n",
    "created_at": "2010-01-08T17:44:47Z",
    "labels": [
        "component: graphics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Adding coordinate transformations to plot3d",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7872",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```
Assignee: olazo

CC:  wcauchois @jasongrout mhampton olazo @kcrisman

While developing a command called transform_plot3d, that generalized ploting in diferent coordinate systems, Jason Grout suggested to me that such a command would be better implemented within plot3d.

I agreed to that, so I propose an adition to plot3d's syntax: "plot3d(function,var1range,var2range,transformation=None,**kwds)" where transformation is a 4-tuple containing 3 functions of arity 3, and a variable which is to be interpreted as the function to be ploted. Like this (r*cos(fi),r*sin(fi),z,r), so the function will be ploted as r.

It's inclution within plot3d would be something on the likes of


```
def plot3d_new(f,v1ran,v2ran,transformation=None,**kwds):
    if transformation==None:
        return plot3d(f,v1ran,v2ran,**kwds)
    else:
        v1=v1ran[0]
        v2=v2ran[0]

        if transformation=='spherical':
            r=var('r')
            transformation=(r*cos(v1)*sin(v2),r*sin(v1)*sin(v2),r*cos(v2),r)
        elif transformation=='cylindrical':
            r=var('r')
            transformation=(r*cos(v1),r*sin(v1),v2,r)
        elif str(type(transformation))=="<type 'str'>":
            print 'Warning: the transformation given is not amongst the options, it will be ignored'
            return plot3d(f,v1ran,v2ran,**kwds)

        fvar=transformation[3]
        transformation=(transformation[0],transformation[1],transformation[2])

        try:
            R=[t.subs({fvar:f}) for t in transformation]
        except:
            def subs_func(t):
                return lambda x,y: t.subs({fvar:f(x,y), v1:x, v2:y})
            R=map(subs_func,transformation)
        return parametric_plot(R,v1ran,v2ran,**kwds)
```


Examples can be found in [http://www.sagenb.org/home/omologos/9/](http://www.sagenb.org/home/omologos/9/).

Spherical and cylindrical plots are now meant to be purely derived from plot3d. So tickets [http://trac.sagemath.org/sage_trac/ticket/7850](http://trac.sagemath.org/sage_trac/ticket/7850) and [http://trac.sagemath.org/sage_trac/ticket/7869](http://trac.sagemath.org/sage_trac/ticket/7869) should be updated

Issue created by migration from https://trac.sagemath.org/ticket/7872





---

archive/issue_comments_068221.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-01-08T17:53:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68221",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_068222.json:
```json
{
    "body": "Hi! William directed me to your thread on sage-devel. Since I have experience working on 3D plotting, I think I could help integrate this code into Sage.",
    "created_at": "2010-01-11T07:21:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68222",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Hi! William directed me to your thread on sage-devel. Since I have experience working on 3D plotting, I think I could help integrate this code into Sage.



---

archive/issue_comments_068223.json:
```json
{
    "body": "based on sage 4.3.1.alpha1",
    "created_at": "2010-01-12T05:29:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68223",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

based on sage 4.3.1.alpha1



---

archive/issue_comments_068224.json:
```json
{
    "body": "Attachment [trac_7872.patch](tarball://root/attachments/some-uuid/ticket7872/trac_7872.patch) by wcauchois created at 2010-01-12 05:46:29\n\nThe patch I just attached represents my initial work on this issue. I added Oscar's code to plot3d() to implement the transformation keyword parameter, and I added the two new plotting functions spherical_plot3d and cylindrical_plot3d.\n\nI made some minor changes to the original code. I moved the formulae for the transformations for spherical and cylindrical coordinates out of the body of plot3d, and into the bodies of spherical_plot3d and cylindrical_plot3d, since I thought that was a better place for them. I also added some error handling; the urange and vrange given to plot3d may be 2-tuples, in which case the variables are implicit -- but we expect urange[0] and vrange[0] to be the plot variables.\n\nWe need to add some documentation for the new features. I think I can draw upon the examples Oscar provided in his published worksheets to create doctests for the new functions. Oscar, could you help me come up with descriptions of cylindrical_plot3d and spherical_plot3d for use in their docstrings? And more examples are always helpful.",
    "created_at": "2010-01-12T05:46:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68224",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Attachment [trac_7872.patch](tarball://root/attachments/some-uuid/ticket7872/trac_7872.patch) by wcauchois created at 2010-01-12 05:46:29

The patch I just attached represents my initial work on this issue. I added Oscar's code to plot3d() to implement the transformation keyword parameter, and I added the two new plotting functions spherical_plot3d and cylindrical_plot3d.

I made some minor changes to the original code. I moved the formulae for the transformations for spherical and cylindrical coordinates out of the body of plot3d, and into the bodies of spherical_plot3d and cylindrical_plot3d, since I thought that was a better place for them. I also added some error handling; the urange and vrange given to plot3d may be 2-tuples, in which case the variables are implicit -- but we expect urange[0] and vrange[0] to be the plot variables.

We need to add some documentation for the new features. I think I can draw upon the examples Oscar provided in his published worksheets to create doctests for the new functions. Oscar, could you help me come up with descriptions of cylindrical_plot3d and spherical_plot3d for use in their docstrings? And more examples are always helpful.



---

archive/issue_comments_068225.json:
```json
{
    "body": "More examples now available at the bottom of: [http://sagenb.org/home/pub/1328/](http://sagenb.org/home/pub/1328/). I'll do the descriptions later.",
    "created_at": "2010-01-12T16:16:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68225",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```

More examples now available at the bottom of: [http://sagenb.org/home/pub/1328/](http://sagenb.org/home/pub/1328/). I'll do the descriptions later.



---

archive/issue_comments_068226.json:
```json
{
    "body": "I have attatced a proposal for a docstring in spherical_plot #7850 . Also, I checked your code. Do you think it is best to use \"spherical_plot3d\" instead of \"spherical_plot\"? I find the 3d redundant, and I like to type less. Also, I noticed that your implementation will not allow adaptative refinement to be used together with \"transformation\". I have never used that option and I don't know whether it is important. When my plots are not sufficiently rounded I use plot_points, and that usually does the trick.",
    "created_at": "2010-01-13T01:15:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68226",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```

I have attatced a proposal for a docstring in spherical_plot #7850 . Also, I checked your code. Do you think it is best to use "spherical_plot3d" instead of "spherical_plot"? I find the 3d redundant, and I like to type less. Also, I noticed that your implementation will not allow adaptative refinement to be used together with "transformation". I have never used that option and I don't know whether it is important. When my plots are not sufficiently rounded I use plot_points, and that usually does the trick.



---

archive/issue_comments_068227.json:
```json
{
    "body": "Attachment [13535.patch](tarball://root/attachments/some-uuid/ticket7872/13535.patch) by olazo created at 2010-01-24 19:39:48",
    "created_at": "2010-01-24T19:39:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68227",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```

Attachment [13535.patch](tarball://root/attachments/some-uuid/ticket7872/13535.patch) by olazo created at 2010-01-24 19:39:48



---

archive/issue_comments_068228.json:
```json
{
    "body": "I've just added a patch with some improvements as well as the docstrings. However, the docstrings of spherical_plot3d and cylindrical_plot3d are impropperly formated. I could not manage format them right. Please review!",
    "created_at": "2010-01-24T19:42:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68228",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```

I've just added a patch with some improvements as well as the docstrings. However, the docstrings of spherical_plot3d and cylindrical_plot3d are impropperly formated. I could not manage format them right. Please review!



---

archive/issue_comments_068229.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-24T19:42:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68229",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068230.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-25T02:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68230",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_068231.json:
```json
{
    "body": "I will be uploading a patch very soon with some improvements to Oscar's code.",
    "created_at": "2010-01-25T02:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68231",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

I will be uploading a patch very soon with some improvements to Oscar's code.



---

archive/issue_comments_068232.json:
```json
{
    "body": "Attachment [trac_7872_new.patch](tarball://root/attachments/some-uuid/ticket7872/trac_7872_new.patch) by wcauchois created at 2010-01-26 07:52:23\n\nbased on sage 4.3.1.rc0",
    "created_at": "2010-01-26T07:52:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68232",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Attachment [trac_7872_new.patch](tarball://root/attachments/some-uuid/ticket7872/trac_7872_new.patch) by wcauchois created at 2010-01-26 07:52:23

based on sage 4.3.1.rc0



---

archive/issue_comments_068233.json:
```json
{
    "body": "So here is what I've been working on: a very unambiguous system for specifying predefined transformations, that will work with symbolic expressions and Python callables alike.\n\nIt has turned out to be a lot of work.\n\nJason, could you take a look and tell me what you think of the code and the documentation I've added?",
    "created_at": "2010-01-26T07:54:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68233",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

So here is what I've been working on: a very unambiguous system for specifying predefined transformations, that will work with symbolic expressions and Python callables alike.

It has turned out to be a lot of work.

Jason, could you take a look and tell me what you think of the code and the documentation I've added?



---

archive/issue_comments_068234.json:
```json
{
    "body": "I like how you incorporated olazo's work and your work.  Hooray for collaborative development.\n\nIn the first reading through, it looks great to me.  olazo: what do you think?",
    "created_at": "2010-01-26T08:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68234",
    "user": "https://github.com/jasongrout"
}
```

I like how you incorporated olazo's work and your work.  Hooray for collaborative development.

In the first reading through, it looks great to me.  olazo: what do you think?



---

archive/issue_comments_068235.json:
```json
{
    "body": "It seems fantastic to me! Many thanks to both of you!",
    "created_at": "2010-01-28T05:43:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68235",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```

It seems fantastic to me! Many thanks to both of you!



---

archive/issue_comments_068236.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-01T02:28:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68236",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068237.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-05T19:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68237",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_068238.json:
```json
{
    "body": "I haven't been able to do a thorough review yet, but in general I agree that this looks very nice!  Everything below should be interpreted as nitpicking; however, because of the last item (doctests) I must put this as 'needs work'.\n\nIn spherical_plot3d, it is a 'drop' of water, not a 'drom'.\n\nIn plot3d where the transformations are added, should it be\n\n```\nelif adaptive:\n```\n\nor \n\n```\nif adaptive:\n```\n\nThat is, does transformation exclude adaptive?  If so, this should be documented.  Also, shouldn't\n\n```\n+    from sage.symbolic.callable import is_CallableSymbolicExpression\n```\n\nbe done only if transformation is not None?\n\nThe `@`interact doctests don't really make sense in the command-line format.  I tried them nonetheless, and it popped up a bunch of jmol windows - looked nice!  But there must be a better way to doctest this; perhaps just A;B;C;D;E or something.\n\nAlso, why are Cylindrical and Spherical imported in plot3d/all.py?    It's not clear to me why someone would want that available but not just use e.g. spherical_plot3d or just import Spherical if they really needed it? \n\nAlso, doctests are needed for the abstract classes, and (for readability) a blank line between methods wouldn't hurt.",
    "created_at": "2010-02-05T19:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68238",
    "user": "https://github.com/kcrisman"
}
```

I haven't been able to do a thorough review yet, but in general I agree that this looks very nice!  Everything below should be interpreted as nitpicking; however, because of the last item (doctests) I must put this as 'needs work'.

In spherical_plot3d, it is a 'drop' of water, not a 'drom'.

In plot3d where the transformations are added, should it be

```
elif adaptive:
```

or 

```
if adaptive:
```

That is, does transformation exclude adaptive?  If so, this should be documented.  Also, shouldn't

```
+    from sage.symbolic.callable import is_CallableSymbolicExpression
```

be done only if transformation is not None?

The `@`interact doctests don't really make sense in the command-line format.  I tried them nonetheless, and it popped up a bunch of jmol windows - looked nice!  But there must be a better way to doctest this; perhaps just A;B;C;D;E or something.

Also, why are Cylindrical and Spherical imported in plot3d/all.py?    It's not clear to me why someone would want that available but not just use e.g. spherical_plot3d or just import Spherical if they really needed it? 

Also, doctests are needed for the abstract classes, and (for readability) a blank line between methods wouldn't hurt.



---

archive/issue_comments_068239.json:
```json
{
    "body": "Replying to [comment:17 kcrisman]:\n\nFirst of all, thanks for taking a look at this. Your comments are very thorough and I will respond to each of them in turn.\n\n> I haven't been able to do a thorough review yet, but in general I agree that this looks very nice!  Everything below should be interpreted as nitpicking; however, because of the last item (doctests) I must put this as 'needs work'.\n> \n> In spherical_plot3d, it is a 'drop' of water, not a 'drom'.\n\nYes, I think that's correct.\n\n> In plot3d where the transformations are added, should it be\n> {{{\n> elif adaptive:\n> }}}\n> or \n> {{{\n> if adaptive:\n> }}}\n> That is, does transformation exclude adaptive?  If so, this should be documented.  Also, shouldn't\n\nI think transformation excludes adaptive since parametric_plot3d doesn't support adaptive plots. I'll make sure to document this.\n\n> {{{\n> +    from sage.symbolic.callable import is_CallableSymbolicExpression\n> }}}\n> be done only if transformation is not None?\n\nSure. I don't see how that really matters though, since its just an import statement.\n\n> The `@`interact doctests don't really make sense in the command-line format.  I tried them nonetheless, and it popped up a bunch of jmol windows - looked nice!  But there must be a better way to doctest this; perhaps just A;B;C;D;E or something.\n\nHow about `show(A + B + C + D + E)` in the TESTS section below?\n\n> Also, why are Cylindrical and Spherical imported in plot3d/all.py?    It's not clear to me why someone would want that available but not just use e.g. spherical_plot3d or just import Spherical if they really needed it?\n\nThis is one of the major features of the transformation system. You can use spherical_plot3d, which will graph a function r in terms of phi and theta, or you can specify transformation=Spherical() which lets you choose the dependent and independent variables.\n\nFor example,\n\n```\nplot3d(..., transformation=Spherical('phi', ['r', 'theta']))\n```\n\nwill graph a function phi in terms of r and theta. So basically you get more flexibility by using Spherical(). Is there a way I could make that clearer in the documentation?\n\n> Also, doctests are needed for the abstract classes, and (for readability) a blank line between methods wouldn't hurt.\n\nOkay.",
    "created_at": "2010-02-08T01:53:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68239",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Replying to [comment:17 kcrisman]:

First of all, thanks for taking a look at this. Your comments are very thorough and I will respond to each of them in turn.

> I haven't been able to do a thorough review yet, but in general I agree that this looks very nice!  Everything below should be interpreted as nitpicking; however, because of the last item (doctests) I must put this as 'needs work'.
> 
> In spherical_plot3d, it is a 'drop' of water, not a 'drom'.

Yes, I think that's correct.

> In plot3d where the transformations are added, should it be
> {{{
> elif adaptive:
> }}}
> or 
> {{{
> if adaptive:
> }}}
> That is, does transformation exclude adaptive?  If so, this should be documented.  Also, shouldn't

I think transformation excludes adaptive since parametric_plot3d doesn't support adaptive plots. I'll make sure to document this.

> {{{
> +    from sage.symbolic.callable import is_CallableSymbolicExpression
> }}}
> be done only if transformation is not None?

Sure. I don't see how that really matters though, since its just an import statement.

> The `@`interact doctests don't really make sense in the command-line format.  I tried them nonetheless, and it popped up a bunch of jmol windows - looked nice!  But there must be a better way to doctest this; perhaps just A;B;C;D;E or something.

How about `show(A + B + C + D + E)` in the TESTS section below?

> Also, why are Cylindrical and Spherical imported in plot3d/all.py?    It's not clear to me why someone would want that available but not just use e.g. spherical_plot3d or just import Spherical if they really needed it?

This is one of the major features of the transformation system. You can use spherical_plot3d, which will graph a function r in terms of phi and theta, or you can specify transformation=Spherical() which lets you choose the dependent and independent variables.

For example,

```
plot3d(..., transformation=Spherical('phi', ['r', 'theta']))
```

will graph a function phi in terms of r and theta. So basically you get more flexibility by using Spherical(). Is there a way I could make that clearer in the documentation?

> Also, doctests are needed for the abstract classes, and (for readability) a blank line between methods wouldn't hurt.

Okay.



---

archive/issue_comments_068240.json:
```json
{
    "body": "based on sage 4.3.1.rc0",
    "created_at": "2010-02-08T04:06:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68240",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

based on sage 4.3.1.rc0



---

archive/issue_comments_068241.json:
```json
{
    "body": "Attachment [trac_7872_new-all.patch](tarball://root/attachments/some-uuid/ticket7872/trac_7872_new-all.patch) by wcauchois created at 2010-02-08 04:08:15\n\nbased on sage 4.3.1",
    "created_at": "2010-02-08T04:08:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68241",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Attachment [trac_7872_new-all.patch](tarball://root/attachments/some-uuid/ticket7872/trac_7872_new-all.patch) by wcauchois created at 2010-02-08 04:08:15

based on sage 4.3.1



---

archive/issue_comments_068242.json:
```json
{
    "body": "Please take a look at the changes in trac_7872_new-referee.patch. You can apply trac_7872_new-all.patch to a new sage branch to get all of the changes.",
    "created_at": "2010-02-08T04:09:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68242",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Please take a look at the changes in trac_7872_new-referee.patch. You can apply trac_7872_new-all.patch to a new sage branch to get all of the changes.



---

archive/issue_comments_068243.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-08T04:09:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68243",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068244.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-12T19:55:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68244",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_068245.json:
```json
{
    "body": "> > Also, why are Cylindrical and Spherical imported in plot3d/all.py?    It's not clear to me why someone would want that available but not just use e.g. spherical_plot3d or just import Spherical if they really needed it?\n> \n> This is one of the major features of the transformation system. You can use spherical_plot3d, which will graph a function r in terms of phi and theta, or you can specify transformation=Spherical() which lets you choose the dependent and independent variables.\n> \n> For example,\n> {{{\n> plot3d(..., transformation=Spherical('phi', ['r', 'theta']))\n> }}}\n> will graph a function phi in terms of r and theta. So basically you get more flexibility by using Spherical(). Is there a way I could make that clearer in the documentation?\n> \n\nMost of the changes seem fine.  I am still confused about this, though.  Isn't\n\n```\nsage: spherical_plot3d(e^-y,(x,0,2*pi),(y,0,pi))\n```\n\nalready allowing one to use a different name for the variables?  \n\nAh, I think I see.  There are six different possibilities for order of independent variables and the dependent variable, and you want to allow all of these - it that it?  Maybe you should make it clearer that this is what is going on by saying that it's not the names, but rather which one is the dependent variable, you are changing - in fact, that the names look the same only to preserve the usual terminology - and then adding to\n\n```\n      sage: Spherical('theta', ['r', 'phi']) \n      Spherical coordinate system (theta in terms of r, phi) \n```\n\nby actually plotting something with this.  \n\nAlso, in line 623, I think it should be\n\n```\n   sage: var('r,u,v')\n```\n \ninstead of r, u, u; I am surprised this doesn't give a doctest failure (I didn't get a chance to run that right now).\n\nIs it ok if I make it still 'needs work' to just clarify these?  For most users it will all be irrelevant, of course, but if we are really going to import Spherical() at the top level, then it should be very clear what the point is.",
    "created_at": "2010-02-12T19:55:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68245",
    "user": "https://github.com/kcrisman"
}
```

> > Also, why are Cylindrical and Spherical imported in plot3d/all.py?    It's not clear to me why someone would want that available but not just use e.g. spherical_plot3d or just import Spherical if they really needed it?
> 
> This is one of the major features of the transformation system. You can use spherical_plot3d, which will graph a function r in terms of phi and theta, or you can specify transformation=Spherical() which lets you choose the dependent and independent variables.
> 
> For example,
> {{{
> plot3d(..., transformation=Spherical('phi', ['r', 'theta']))
> }}}
> will graph a function phi in terms of r and theta. So basically you get more flexibility by using Spherical(). Is there a way I could make that clearer in the documentation?
> 

Most of the changes seem fine.  I am still confused about this, though.  Isn't

```
sage: spherical_plot3d(e^-y,(x,0,2*pi),(y,0,pi))
```

already allowing one to use a different name for the variables?  

Ah, I think I see.  There are six different possibilities for order of independent variables and the dependent variable, and you want to allow all of these - it that it?  Maybe you should make it clearer that this is what is going on by saying that it's not the names, but rather which one is the dependent variable, you are changing - in fact, that the names look the same only to preserve the usual terminology - and then adding to

```
      sage: Spherical('theta', ['r', 'phi']) 
      Spherical coordinate system (theta in terms of r, phi) 
```

by actually plotting something with this.  

Also, in line 623, I think it should be

```
   sage: var('r,u,v')
```
 
instead of r, u, u; I am surprised this doesn't give a doctest failure (I didn't get a chance to run that right now).

Is it ok if I make it still 'needs work' to just clarify these?  For most users it will all be irrelevant, of course, but if we are really going to import Spherical() at the top level, then it should be very clear what the point is.



---

archive/issue_comments_068246.json:
```json
{
    "body": "Replying to [comment:20 kcrisman]:\n> Ah, I think I see.  There are six different possibilities for order of independent variables and the dependent variable, and you want to allow all of these - it that it?  Maybe you should make it clearer that this is what is going on by saying that it's not the names, but rather which one is the dependent variable, you are changing - in fact, that the names look the same only to preserve the usual terminology - and then adding to\n> {{{\n>       sage: Spherical('theta', ['r', 'phi']) \n>       Spherical coordinate system (theta in terms of r, phi) \n> }}}\n> by actually plotting something with this.  \n\nIn the docstring on line 254, I do just that.\n\n> Also, in line 623, I think it should be\n> {{{\n>    sage: var('r,u,v')\n> }}} \n> instead of r, u, u; I am surprised this doesn't give a doctest failure (I didn't get a chance to run that right now).\n\nGood catch!\n\n> Is it ok if I make it still 'needs work' to just clarify these?  For most users it will all be irrelevant, of course, but if we are really going to import Spherical() at the top level, then it should be very clear what the point is.\n\nI've done my best on the documentation, but it still might not be entirely clear on how to use Spherical and Cylindrical. Most users, of course, can simply use spherical_plot3d and cylindrical_plot3d. Can you make any concrete suggestions on how to improve the documentation? Does anyone have any ideas for sentences to add?",
    "created_at": "2010-02-13T00:21:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68246",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Replying to [comment:20 kcrisman]:
> Ah, I think I see.  There are six different possibilities for order of independent variables and the dependent variable, and you want to allow all of these - it that it?  Maybe you should make it clearer that this is what is going on by saying that it's not the names, but rather which one is the dependent variable, you are changing - in fact, that the names look the same only to preserve the usual terminology - and then adding to
> {{{
>       sage: Spherical('theta', ['r', 'phi']) 
>       Spherical coordinate system (theta in terms of r, phi) 
> }}}
> by actually plotting something with this.  

In the docstring on line 254, I do just that.

> Also, in line 623, I think it should be
> {{{
>    sage: var('r,u,v')
> }}} 
> instead of r, u, u; I am surprised this doesn't give a doctest failure (I didn't get a chance to run that right now).

Good catch!

> Is it ok if I make it still 'needs work' to just clarify these?  For most users it will all be irrelevant, of course, but if we are really going to import Spherical() at the top level, then it should be very clear what the point is.

I've done my best on the documentation, but it still might not be entirely clear on how to use Spherical and Cylindrical. Most users, of course, can simply use spherical_plot3d and cylindrical_plot3d. Can you make any concrete suggestions on how to improve the documentation? Does anyone have any ideas for sentences to add?



---

archive/issue_comments_068247.json:
```json
{
    "body": "In your definition of spherical coordinates, is your second angle the *elevation*, or the *inclination*.  I think it might be the inclination, rather than what is stated in the docstring (\"elevation\").  Inclination is measured with 0 corresponding to the positive z-axis, and has a range of [0,pi].  Elevation is measured from the xy-plane, and has a range of [-pi/2,pi/2], if I understand things correctly.",
    "created_at": "2010-02-24T07:38:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68247",
    "user": "https://github.com/jasongrout"
}
```

In your definition of spherical coordinates, is your second angle the *elevation*, or the *inclination*.  I think it might be the inclination, rather than what is stated in the docstring ("elevation").  Inclination is measured with 0 corresponding to the positive z-axis, and has a range of [0,pi].  Elevation is measured from the xy-plane, and has a range of [-pi/2,pi/2], if I understand things correctly.



---

archive/issue_comments_068248.json:
```json
{
    "body": "Also, given the confusion surrounding different conventions and variable names for spherical coordinates, I think it would be better to use \"radius\", \"azimuth\", and \"inclination\" (or \"elevation\"), instead of \"r\", \"phi\", and \"theta\".  Then it's unambiguous what \n\n\n```\nSpherical('radius', ['azimuth', 'inclination'])\n```\n\n\nrepresents.",
    "created_at": "2010-02-24T07:45:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68248",
    "user": "https://github.com/jasongrout"
}
```

Also, given the confusion surrounding different conventions and variable names for spherical coordinates, I think it would be better to use "radius", "azimuth", and "inclination" (or "elevation"), instead of "r", "phi", and "theta".  Then it's unambiguous what 


```
Spherical('radius', ['azimuth', 'inclination'])
```


represents.



---

archive/issue_comments_068249.json:
```json
{
    "body": "Similarly, I think cylindrical coordinate components should be spelled out:\n\n\n```\nclass Cylindrical(sage.plot.plot3d.plot3d._CoordTrans):\n    all_vars = ['radius', 'azimuth', 'height']\n\n    _name = 'Cylindrical (radius, azimuth, height) coordinate system'\n\n    def gen_transform(self, radius=None, azimuth=None, height=None):\n        return (radius * cos(azimuth),\n                radius * sin(azimuth),\n                height)\n```\n",
    "created_at": "2010-02-24T07:54:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68249",
    "user": "https://github.com/jasongrout"
}
```

Similarly, I think cylindrical coordinate components should be spelled out:


```
class Cylindrical(sage.plot.plot3d.plot3d._CoordTrans):
    all_vars = ['radius', 'azimuth', 'height']

    _name = 'Cylindrical (radius, azimuth, height) coordinate system'

    def gen_transform(self, radius=None, azimuth=None, height=None):
        return (radius * cos(azimuth),
                radius * sin(azimuth),
                height)
```




---

archive/issue_comments_068250.json:
```json
{
    "body": "One more point that I thought of when trying to use this feature.  Why should I have to specify the names of variables more than once?  Introspection should be able to get these from my gen_transform function.  It seems like I should be able to do this:\n\n\n```\nclass Cylindrical(sage.plot.plot3d.plot3d._CoordTrans):\n    \"\"\"\n    Some docs for the mathematical definitions of the variables\n    \"\"\"\n    def gen_transform(self, radius=None, azimuth=None, height=None):\n        return (radius * cos(azimuth),\n                radius * sin(azimuth),\n                height)\n```\n\n\nand things should just work.  all_vars can be inferred from the keyword arguments to gen_transform.  It's pretty easy to come up with a good default _name (i.e., 'name of class (variables) coordinate system').",
    "created_at": "2010-02-24T08:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68250",
    "user": "https://github.com/jasongrout"
}
```

One more point that I thought of when trying to use this feature.  Why should I have to specify the names of variables more than once?  Introspection should be able to get these from my gen_transform function.  It seems like I should be able to do this:


```
class Cylindrical(sage.plot.plot3d.plot3d._CoordTrans):
    """
    Some docs for the mathematical definitions of the variables
    """
    def gen_transform(self, radius=None, azimuth=None, height=None):
        return (radius * cos(azimuth),
                radius * sin(azimuth),
                height)
```


and things should just work.  all_vars can be inferred from the keyword arguments to gen_transform.  It's pretty easy to come up with a good default _name (i.e., 'name of class (variables) coordinate system').



---

archive/issue_comments_068251.json:
```json
{
    "body": "Changing assignee from olazo to @jasongrout.",
    "created_at": "2010-02-24T08:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68251",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from olazo to @jasongrout.



---

archive/issue_comments_068252.json:
```json
{
    "body": "Another polishing point: when given this syntax\n\n\n```\nspherical=(w*cos(u)*sin(v),w*sin(u)*sin(v),w*cos(v),w) \nplot3d(2,(u,-pi,pi),(v,0,pi),transformation=spherical,plot_points=[100,100])\n```\n\n\nwhy do I have to specify the fourth argument in spherical (i.e., \"w\")?  In the plot, you know that I'm specifying u and v to be numeric ranges, so it should be easy for Sage to realize that the function variable is w and the independent variables are u and v.",
    "created_at": "2010-02-24T08:27:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68252",
    "user": "https://github.com/jasongrout"
}
```

Another polishing point: when given this syntax


```
spherical=(w*cos(u)*sin(v),w*sin(u)*sin(v),w*cos(v),w) 
plot3d(2,(u,-pi,pi),(v,0,pi),transformation=spherical,plot_points=[100,100])
```


why do I have to specify the fourth argument in spherical (i.e., "w")?  In the plot, you know that I'm specifying u and v to be numeric ranges, so it should be easy for Sage to realize that the function variable is w and the independent variables are u and v.



---

archive/issue_comments_068253.json:
```json
{
    "body": "The current code might have a problem if I do:\n\n\n```\nspherical=(w*cos(u)*sin(v),w*sin(u)*sin(v),w*cos(v),w) \nplot3d(lambda x,y: 2,(-pi,pi),(0,pi),transformation=spherical,plot_points=[100,100])\n\n```\n\n\nbecause the current strategy does not specify if u or v is the first coordinate range.",
    "created_at": "2010-02-24T08:44:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68253",
    "user": "https://github.com/jasongrout"
}
```

The current code might have a problem if I do:


```
spherical=(w*cos(u)*sin(v),w*sin(u)*sin(v),w*cos(v),w) 
plot3d(lambda x,y: 2,(-pi,pi),(0,pi),transformation=spherical,plot_points=[100,100])

```


because the current strategy does not specify if u or v is the first coordinate range.



---

archive/issue_comments_068254.json:
```json
{
    "body": "Indeed, with the patch:\n\n\n```\nsage: var('u,v,w')\nsage: spherical=(w*cos(u)*sin(v),w*sin(u)*sin(v),w*cos(v),w) \nsage: plot3d(lambda x,y: 2,(-pi,pi),(0,pi),transformation=spherical,plot_points=[100,100])\nTraceback (most recent call last):\n...\nValueError: expected 3-tuple for urange and vrange\n```\n",
    "created_at": "2010-02-25T04:09:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68254",
    "user": "https://github.com/jasongrout"
}
```

Indeed, with the patch:


```
sage: var('u,v,w')
sage: spherical=(w*cos(u)*sin(v),w*sin(u)*sin(v),w*cos(v),w) 
sage: plot3d(lambda x,y: 2,(-pi,pi),(0,pi),transformation=spherical,plot_points=[100,100])
Traceback (most recent call last):
...
ValueError: expected 3-tuple for urange and vrange
```




---

archive/issue_comments_068255.json:
```json
{
    "body": "Attachment [trac-7872-polish.patch](tarball://root/attachments/some-uuid/ticket7872/trac-7872-polish.patch) by @jasongrout created at 2010-02-27 10:11:53\n\napply on top of trac_7872_new-all.patch; based on 4.3.2.",
    "created_at": "2010-02-27T10:11:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68255",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-7872-polish.patch](tarball://root/attachments/some-uuid/ticket7872/trac-7872-polish.patch) by @jasongrout created at 2010-02-27 10:11:53

apply on top of trac_7872_new-all.patch; based on 4.3.2.



---

archive/issue_comments_068256.json:
```json
{
    "body": "I've addressed every single one of my comments in the trac-7872-polish.patch.  I think this is great functionality, and definitely ready for review!",
    "created_at": "2010-02-27T10:13:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68256",
    "user": "https://github.com/jasongrout"
}
```

I've addressed every single one of my comments in the trac-7872-polish.patch.  I think this is great functionality, and definitely ready for review!



---

archive/issue_comments_068257.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-27T10:13:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68257",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068258.json:
```json
{
    "body": "Remove assignee @jasongrout.",
    "created_at": "2010-02-27T10:18:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68258",
    "user": "https://github.com/jasongrout"
}
```

Remove assignee @jasongrout.



---

archive/issue_comments_068259.json:
```json
{
    "body": "Wow, great work Jason. Thank you so much. I've had a really tough quarter in school and I really didn't have time to work on this. I'm also excited to see this feature in Sage. Thanks to everyone who helped make this happen.",
    "created_at": "2010-02-27T10:21:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68259",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Wow, great work Jason. Thank you so much. I've had a really tough quarter in school and I really didn't have time to work on this. I'm also excited to see this feature in Sage. Thanks to everyone who helped make this happen.



---

archive/issue_comments_068260.json:
```json
{
    "body": "Replying to [comment:33 wcauchois]:\n> Wow, great work Jason. Thank you so much. I've had a really tough quarter in school and I really didn't have time to work on this. I'm also excited to see this feature in Sage. Thanks to everyone who helped make this happen.\n\nI totally understand.  Now I am talking about transformations in my calc 3 class, so I could take some time to finish this up.  I'm hoping it gets in fairly quickly, though I'll probably apply the patch to our class server anyway.\n\nI positive review your code (well, except for the changes I made :).  Can you review my code?",
    "created_at": "2010-02-27T16:41:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68260",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:33 wcauchois]:
> Wow, great work Jason. Thank you so much. I've had a really tough quarter in school and I really didn't have time to work on this. I'm also excited to see this feature in Sage. Thanks to everyone who helped make this happen.

I totally understand.  Now I am talking about transformations in my calc 3 class, so I could take some time to finish this up.  I'm hoping it gets in fairly quickly, though I'll probably apply the patch to our class server anyway.

I positive review your code (well, except for the changes I made :).  Can you review my code?



---

archive/issue_comments_068261.json:
```json
{
    "body": "Jason,\nI've taken a look at your code and you've done a great job of cleaning this up! I can't find any fault with it. Apply the following patches to Sage 4.3.3: trac-7872-polish.patch, trac_7872_new-all.patch. Applies fine and passes all doctests.\n\nNow which one of us should mark this as a positive review, or should we bring in a 3rd party?",
    "created_at": "2010-02-28T20:20:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68261",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Jason,
I've taken a look at your code and you've done a great job of cleaning this up! I can't find any fault with it. Apply the following patches to Sage 4.3.3: trac-7872-polish.patch, trac_7872_new-all.patch. Applies fine and passes all doctests.

Now which one of us should mark this as a positive review, or should we bring in a 3rd party?



---

archive/issue_comments_068262.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-01T12:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68262",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068263.json:
```json
{
    "body": "Replying to [comment:35 wcauchois]:\n> Jason,\n> I've taken a look at your code and you've done a great job of cleaning this up! I can't find any fault with it. Apply the following patches to Sage 4.3.3: trac-7872-polish.patch, trac_7872_new-all.patch. Applies fine and passes all doctests.\n> \n\nApply the patches in this order, though: trac_7872_new-all.patch, trac-7872-polish.patch.\n\nThere is precedent for two people collaboratively writing and reviewing each other's code as being okay.  Since you've passed off on my code, and I've passed off on your code, I'll mark this as positive review.  olazo: can you look at this as well, and if you find a problem, change it back to needs work?",
    "created_at": "2010-03-01T12:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68263",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:35 wcauchois]:
> Jason,
> I've taken a look at your code and you've done a great job of cleaning this up! I can't find any fault with it. Apply the following patches to Sage 4.3.3: trac-7872-polish.patch, trac_7872_new-all.patch. Applies fine and passes all doctests.
> 

Apply the patches in this order, though: trac_7872_new-all.patch, trac-7872-polish.patch.

There is precedent for two people collaboratively writing and reviewing each other's code as being okay.  Since you've passed off on my code, and I've passed off on your code, I'll mark this as positive review.  olazo: can you look at this as well, and if you find a problem, change it back to needs work?



---

archive/issue_comments_068264.json:
```json
{
    "body": "(actually, in this case, it was three people because olazo wrote the initial implementation!)",
    "created_at": "2010-03-01T12:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68264",
    "user": "https://github.com/jasongrout"
}
```

(actually, in this case, it was three people because olazo wrote the initial implementation!)



---

archive/issue_comments_068265.json:
```json
{
    "body": "Replying to [comment:36 jason]:\n> There is precedent for two people collaboratively writing and reviewing each other's code as being okay.  Since you've passed off on my code, and I've passed off on your code, I'll mark this as positive review.  olazo: can you look at this as well, and if you find a problem, change it back to needs work?\n\nI can't find anything wrong with the code, it seems quite powerful already :) ! Thanks to you two for taking interest in this. I couldn't do any more recently because of school... It's been great so far though!",
    "created_at": "2010-03-03T03:12:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68265",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```

Replying to [comment:36 jason]:
> There is precedent for two people collaboratively writing and reviewing each other's code as being okay.  Since you've passed off on my code, and I've passed off on your code, I'll mark this as positive review.  olazo: can you look at this as well, and if you find a problem, change it back to needs work?

I can't find anything wrong with the code, it seems quite powerful already :) ! Thanks to you two for taking interest in this. I couldn't do any more recently because of school... It's been great so far though!



---

archive/issue_comments_068266.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-03T14:09:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68266",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_008087.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-03-03T14:09:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7872#event-8087"
}
```



---

archive/issue_comments_068267.json:
```json
{
    "body": "Merged in this order:\n\n1. [trac_7872_new-all.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7872/trac_7872_new-all.patch)\n2. [trac-7872-polish.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7872/trac-7872-polish.patch)",
    "created_at": "2010-03-03T14:09:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7872#issuecomment-68267",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged in this order:

1. [trac_7872_new-all.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7872/trac_7872_new-all.patch)
2. [trac-7872-polish.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7872/trac-7872-polish.patch)
