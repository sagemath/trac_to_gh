# Issue 1509: plotting -- improve text support

archive/issues_001509.json:
```json
{
    "body": "Assignee: was\n\n\n```\n\nSince axes_label is broken in plot(), one must resort to adding your\nown custom labels to a plot().\n\nIt would be nice in this application, and others, if one could rotate\ntext objects.  For example, it\nwould be nice to be able to make a custom y-axis label that was\nparallel to the y-axis.  I guess,\nin general, the ability to rotate text would be a useful feature.\n\n```\n\n\nFor Sage, make sure to look up how Mathematica does text rotation, etc.,\nand use that interface instead of making something up at random. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1509\n\n",
    "created_at": "2007-12-14T18:05:28Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "plotting -- improve text support",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1509",
    "user": "was"
}
```
Assignee: was


```

Since axes_label is broken in plot(), one must resort to adding your
own custom labels to a plot().

It would be nice in this application, and others, if one could rotate
text objects.  For example, it
would be nice to be able to make a custom y-axis label that was
parallel to the y-axis.  I guess,
in general, the ability to rotate text would be a useful feature.

```


For Sage, make sure to look up how Mathematica does text rotation, etc.,
and use that interface instead of making something up at random. 

Issue created by migration from https://trac.sagemath.org/ticket/1509





---

archive/issue_comments_009661.json:
```json
{
    "body": "Regarding text rotation, can we just pass through the rotation option?  This option is already available on the underlying matplotlib text objects, so it seems like a layup.  I've attached a patch which accomplishes just that (it is a very minor change).  This seems to work quite well here.\n\nAs for how Mathematica accomplishes it, take a look at their page:  http://demonstrations.wolfram.com/HowTextRotationWorksInMathematica/\n\nI think a solution like that would be pretty easy in sage.  For example, this might work: a function which takes a text graphics primative and an angle and properly applies the rotation to the underlying matplotlib text object.",
    "created_at": "2009-08-17T17:51:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1509#issuecomment-9661",
    "user": "mrtrumbe"
}
```

Regarding text rotation, can we just pass through the rotation option?  This option is already available on the underlying matplotlib text objects, so it seems like a layup.  I've attached a patch which accomplishes just that (it is a very minor change).  This seems to work quite well here.

As for how Mathematica accomplishes it, take a look at their page:  http://demonstrations.wolfram.com/HowTextRotationWorksInMathematica/

I think a solution like that would be pretty easy in sage.  For example, this might work: a function which takes a text graphics primative and an angle and properly applies the rotation to the underlying matplotlib text object.



---

archive/issue_comments_009662.json:
```json
{
    "body": "Attachment [text.py.patch](tarball://root/attachments/some-uuid/ticket1509/text.py.patch) by wdj created at 2009-08-17 19:36:50\n\nReplying to [comment:1 mrtrumbe]:\n> Regarding text rotation, can we just pass through the rotation option?  \n> This option is already available on the underlying matplotlib text objects, \n> so it seems like a layup.  I've attached a patch which accomplishes just that \n> (it is a very minor change).  This seems to work quite well here.\n\n\nI tried to download it and got a strange method. I guess it is not an hg patch but a diff?\n\nAlso, did you include an example in the docstring to illustrate your new feature?",
    "created_at": "2009-08-17T19:36:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1509#issuecomment-9662",
    "user": "wdj"
}
```

Attachment [text.py.patch](tarball://root/attachments/some-uuid/ticket1509/text.py.patch) by wdj created at 2009-08-17 19:36:50

Replying to [comment:1 mrtrumbe]:
> Regarding text rotation, can we just pass through the rotation option?  
> This option is already available on the underlying matplotlib text objects, 
> so it seems like a layup.  I've attached a patch which accomplishes just that 
> (it is a very minor change).  This seems to work quite well here.


I tried to download it and got a strange method. I guess it is not an hg patch but a diff?

Also, did you include an example in the docstring to illustrate your new feature?



---

archive/issue_comments_009663.json:
```json
{
    "body": "Replying to [comment:2 wdj]:\n> I tried to download it and got a strange method. I guess it is not an hg patch but a diff?\n> \n> Also, did you include an example in the docstring to illustrate your new feature?\n> \n\nSorry, I'm new to sage dev practices...is there documentation on generating a standard patch?  I used diff to generate the attached patch.\n\nI didn't include an example usage in the docstrings, but did include explanation of the feature.  I'll update the docstring accordingly and update the patch.",
    "created_at": "2009-08-18T21:08:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1509#issuecomment-9663",
    "user": "mrtrumbe"
}
```

Replying to [comment:2 wdj]:
> I tried to download it and got a strange method. I guess it is not an hg patch but a diff?
> 
> Also, did you include an example in the docstring to illustrate your new feature?
> 

Sorry, I'm new to sage dev practices...is there documentation on generating a standard patch?  I used diff to generate the attached patch.

I didn't include an example usage in the docstrings, but did include explanation of the feature.  I'll update the docstring accordingly and update the patch.



---

archive/issue_comments_009664.json:
```json
{
    "body": "Replying to [comment:3 mrtrumbe]:\n> Replying to [comment:2 wdj]:\n> > I tried to download it and got a strange method. I guess it is not an hg patch but a diff?\n> > \n> > Also, did you include an example in the docstring to illustrate your new feature?\n> > \n> \n> Sorry, I'm new to sage dev practices...is there documentation on generating a standard patch?  I used diff to generate the attached patch.\n\nhttp://www.sagemath.org/doc/developer/conventions.html\nand\nhttp://www.sagemath.org/doc/developer/producing_patches.html\n\n> \n> I didn't include an example usage in the docstrings, but did include explanation of the feature.  I'll update the docstring accordingly and update the patch.\n\nThanks.",
    "created_at": "2009-08-18T21:13:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1509#issuecomment-9664",
    "user": "wdj"
}
```

Replying to [comment:3 mrtrumbe]:
> Replying to [comment:2 wdj]:
> > I tried to download it and got a strange method. I guess it is not an hg patch but a diff?
> > 
> > Also, did you include an example in the docstring to illustrate your new feature?
> > 
> 
> Sorry, I'm new to sage dev practices...is there documentation on generating a standard patch?  I used diff to generate the attached patch.

http://www.sagemath.org/doc/developer/conventions.html
and
http://www.sagemath.org/doc/developer/producing_patches.html

> 
> I didn't include an example usage in the docstrings, but did include explanation of the feature.  I'll update the docstring accordingly and update the patch.

Thanks.



---

archive/issue_comments_009665.json:
```json
{
    "body": "Patch was premature.  Accidental revert of other changes.  Will fix shortly.",
    "created_at": "2009-08-19T18:52:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1509#issuecomment-9665",
    "user": "mrtrumbe"
}
```

Patch was premature.  Accidental revert of other changes.  Will fix shortly.



---

archive/issue_comments_009666.json:
```json
{
    "body": "Attachment [12846.2.patch](tarball://root/attachments/some-uuid/ticket1509/12846.2.patch) by mrtrumbe created at 2009-08-19 18:53:08\n\nUgh.  Can't seem to delete patch files.  Sorry for the clutter.",
    "created_at": "2009-08-19T18:53:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1509#issuecomment-9666",
    "user": "mrtrumbe"
}
```

Attachment [12846.2.patch](tarball://root/attachments/some-uuid/ticket1509/12846.2.patch) by mrtrumbe created at 2009-08-19 18:53:08

Ugh.  Can't seem to delete patch files.  Sorry for the clutter.



---

archive/issue_comments_009667.json:
```json
{
    "body": "This is a proper hg patch.  Code is docstring tested.",
    "created_at": "2009-08-19T20:43:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1509#issuecomment-9667",
    "user": "mrtrumbe"
}
```

This is a proper hg patch.  Code is docstring tested.



---

archive/issue_comments_009668.json:
```json
{
    "body": "Attachment [12846.patch](tarball://root/attachments/some-uuid/ticket1509/12846.patch) by kcrisman created at 2009-10-05 18:24:07\n\nThis is really neat, as the graphic says! It makes good sense to get more of the mpl functionality exposed, even if axes_labels now works again.  Positive review.  Apply only most recent patch.",
    "created_at": "2009-10-05T18:24:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1509#issuecomment-9668",
    "user": "kcrisman"
}
```

Attachment [12846.patch](tarball://root/attachments/some-uuid/ticket1509/12846.patch) by kcrisman created at 2009-10-05 18:24:07

This is really neat, as the graphic says! It makes good sense to get more of the mpl functionality exposed, even if axes_labels now works again.  Positive review.  Apply only most recent patch.



---

archive/issue_comments_009669.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T05:22:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1509#issuecomment-9669",
    "user": "mhansen"
}
```

Resolution: fixed
