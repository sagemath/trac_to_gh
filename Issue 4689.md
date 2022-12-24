# Issue 4689: Documentation documenting the wrong thing

archive/issues_004689.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  mhansen\n\nThe examples in the documentation for the save method seems to be broken. If I try\n\n\n```\nsage: E=EllipticCurve([1,0])\nsage: Eplot=E.plot()\nsage: Eplot.save?\n```\n\n\nthen I get\n\n\n``` \nEXAMPLES:\n                sage: c = circle((1,1),1,rgbcolor=(1,0,0))\n                sage: c.show(xmin=-1,xmax=3,ymin=-1,ymax=3)\n\n                To correct the apect ratio of certain graphics, it is necessary\n                to show with a 'figsize' of square dimensions.\n\n                sage: c.show(figsize=[5,5],xmin=-1,xmax=3,ymin=-1,ymax=3)\n\n                sage: point((-1,1),pointsize=30, rgbcolor=(1,0,0))\n```\n\n\nwhich never mentions \"save\" at all. Presumably there should be an extra line, something like\n\n\n```\nsage: c.save(\"example.png\")\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4689\n\n",
    "created_at": "2008-12-03T22:37:41Z",
    "labels": [
        "algebra",
        "minor",
        "bug"
    ],
    "title": "Documentation documenting the wrong thing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4689",
    "user": "ljpk"
}
```
Assignee: tbd

CC:  mhansen

The examples in the documentation for the save method seems to be broken. If I try


```
sage: E=EllipticCurve([1,0])
sage: Eplot=E.plot()
sage: Eplot.save?
```


then I get


``` 
EXAMPLES:
                sage: c = circle((1,1),1,rgbcolor=(1,0,0))
                sage: c.show(xmin=-1,xmax=3,ymin=-1,ymax=3)

                To correct the apect ratio of certain graphics, it is necessary
                to show with a 'figsize' of square dimensions.

                sage: c.show(figsize=[5,5],xmin=-1,xmax=3,ymin=-1,ymax=3)

                sage: point((-1,1),pointsize=30, rgbcolor=(1,0,0))
```


which never mentions "save" at all. Presumably there should be an extra line, something like


```
sage: c.save("example.png")
```


Issue created by migration from https://trac.sagemath.org/ticket/4689





---

archive/issue_comments_035342.json:
```json
{
    "body": "Hi,\n\nwhich Sage release is that? If it is 3.2.1 this might be #4672. There is a patch over there that needs one doctest fix to be merged into 3.2.2.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-03T22:44:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4689#issuecomment-35342",
    "user": "mabshoff"
}
```

Hi,

which Sage release is that? If it is 3.2.1 this might be #4672. There is a patch over there that needs one doctest fix to be merged into 3.2.2.

Cheers,

Michael



---

archive/issue_comments_035343.json:
```json
{
    "body": "Changing assignee from tbd to tba.",
    "created_at": "2008-12-03T22:44:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4689#issuecomment-35343",
    "user": "mabshoff"
}
```

Changing assignee from tbd to tba.



---

archive/issue_comments_035344.json:
```json
{
    "body": "Changing component from algebra to documentation.",
    "created_at": "2008-12-03T22:44:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4689#issuecomment-35344",
    "user": "mabshoff"
}
```

Changing component from algebra to documentation.



---

archive/issue_comments_035345.json:
```json
{
    "body": "It's in both 3.1.4 and 3.2.1, but that bug report does look relevant; hopefully fixing that will sort this out too.",
    "created_at": "2008-12-03T22:48:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4689#issuecomment-35345",
    "user": "ljpk"
}
```

It's in both 3.1.4 and 3.2.1, but that bug report does look relevant; hopefully fixing that will sort this out too.



---

archive/issue_comments_035346.json:
```json
{
    "body": "With #4672 appplied:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: E=EllipticCurve([1,0])\nsage: Eplot=E.plot()\nsage: Eplot.save?\n```\n\nresults in\n\n```\nType:           instancemethod\nBase Class:     <type 'instancemethod'>\nString Form:    <bound method Graphics.save of >\nNamespace:      Interactive\nFile:           /scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/plot/plot.py\nDefinition:     Eplot.save(self, filename=None, xmin=None, xmax=None, ymin=None, ymax=None, figsize=(6, 3.7082039324993699), figure=None, sub=None, savenow=True, dpi=100, axes=None, axes_labels=None, fontsize=None, frame=False, verify=True, aspect_ratio=None, gridlines=None, gridlinesstyle=None, vgridlinesstyle=None, hgridlinesstyle=None)\nDocstring:\n    \n            Save the graphics to an image file of type: PNG, PS, EPS, SVG, SOBJ,\n            depending on the file extension you give the filename.\n                Extension types can be: file{.png}, file{.ps}, file{.eps}, file{.svg},\n                and file{.sobj} (for a SAGE object you can load later). \n    \n            EXAMPLES:\n                sage: c = circle((1,1),1,rgbcolor=(1,0,0))\n                sage: c.show(xmin=-1,xmax=3,ymin=-1,ymax=3)\n    \n                To correct the apect ratio of certain graphics, it is necessary\n                to show with a 'figsize' of square dimensions.\n    \n                sage: c.show(figsize=[5,5],xmin=-1,xmax=3,ymin=-1,ymax=3)\n                \n                sage: point((-1,1),pointsize=30, rgbcolor=(1,0,0))\n```\n\nRereading the original ticket I now get your main point: the docstring does not contain \"save\", but \"show\" does save the png and then pops up a viewer. We could resolve this by adding a example that uses the save method as you suggested, but my guess would be that such example (in case it did exist) was either changed or removed since \"save('foo.png')\" saves in the current working directory which is bad for doctesting as a non-owner. \n| Sage Version 3.2.1, Release Date: 2008-12-01                       |\n| Type notebook() for the GUI, and license() for information.        |\nSo, what do you want to do? Close this ticket as \"wontfix\" or we add a doctest that saves an image in SAGE_TMP - which is the clean way to deal with temporary files.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-04T17:35:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4689#issuecomment-35346",
    "user": "mabshoff"
}
```

With #4672 appplied:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: E=EllipticCurve([1,0])
sage: Eplot=E.plot()
sage: Eplot.save?
```

results in

```
Type:           instancemethod
Base Class:     <type 'instancemethod'>
String Form:    <bound method Graphics.save of >
Namespace:      Interactive
File:           /scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/plot/plot.py
Definition:     Eplot.save(self, filename=None, xmin=None, xmax=None, ymin=None, ymax=None, figsize=(6, 3.7082039324993699), figure=None, sub=None, savenow=True, dpi=100, axes=None, axes_labels=None, fontsize=None, frame=False, verify=True, aspect_ratio=None, gridlines=None, gridlinesstyle=None, vgridlinesstyle=None, hgridlinesstyle=None)
Docstring:
    
            Save the graphics to an image file of type: PNG, PS, EPS, SVG, SOBJ,
            depending on the file extension you give the filename.
                Extension types can be: file{.png}, file{.ps}, file{.eps}, file{.svg},
                and file{.sobj} (for a SAGE object you can load later). 
    
            EXAMPLES:
                sage: c = circle((1,1),1,rgbcolor=(1,0,0))
                sage: c.show(xmin=-1,xmax=3,ymin=-1,ymax=3)
    
                To correct the apect ratio of certain graphics, it is necessary
                to show with a 'figsize' of square dimensions.
    
                sage: c.show(figsize=[5,5],xmin=-1,xmax=3,ymin=-1,ymax=3)
                
                sage: point((-1,1),pointsize=30, rgbcolor=(1,0,0))
```

Rereading the original ticket I now get your main point: the docstring does not contain "save", but "show" does save the png and then pops up a viewer. We could resolve this by adding a example that uses the save method as you suggested, but my guess would be that such example (in case it did exist) was either changed or removed since "save('foo.png')" saves in the current working directory which is bad for doctesting as a non-owner. 
| Sage Version 3.2.1, Release Date: 2008-12-01                       |
| Type notebook() for the GUI, and license() for information.        |
So, what do you want to do? Close this ticket as "wontfix" or we add a doctest that saves an image in SAGE_TMP - which is the clean way to deal with temporary files.

Cheers,

Michael



---

archive/issue_comments_035347.json:
```json
{
    "body": "I think your idea of having a doctest which saves an image somewhere temporary would be the best idea as it would give the reader the idea of how to use the method and reassure them that it is the correct help function.",
    "created_at": "2008-12-04T21:38:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4689#issuecomment-35347",
    "user": "ljpk"
}
```

I think your idea of having a doctest which saves an image somewhere temporary would be the best idea as it would give the reader the idea of how to use the method and reassure them that it is the correct help function.



---

archive/issue_comments_035348.json:
```json
{
    "body": "Attachment [trac-4689-save-docstring.patch](tarball://root/attachments/some-uuid/ticket4689/trac-4689-save-docstring.patch) by jason created at 2010-01-20 06:56:08",
    "created_at": "2010-01-20T06:56:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4689#issuecomment-35348",
    "user": "jason"
}
```

Attachment [trac-4689-save-docstring.patch](tarball://root/attachments/some-uuid/ticket4689/trac-4689-save-docstring.patch) by jason created at 2010-01-20 06:56:08



---

archive/issue_comments_035349.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-20T06:56:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4689#issuecomment-35349",
    "user": "jason"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_035350.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T07:28:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4689#issuecomment-35350",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_035351.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-01-20T07:28:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4689#issuecomment-35351",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_035352.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-23T15:25:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4689#issuecomment-35352",
    "user": "mvngu"
}
```

Resolution: fixed
