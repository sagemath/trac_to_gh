# Issue 1480: [with patch] implement P.show() for mathematica elements -- nice mathematica graphics in the sage notebook!

archive/issues_001480.json:
```json
{
    "body": "Assignee: @williamstein\n\nAs the summary says.  Inspired by this email\n\n```\n\n\nOn Dec 12, 2007 10:07 AM, carlosap <carlosap78@gmail.com> wrote:\n> \n> I typed mathematica.NIntegrate[x^2,{x,1,0}]\n> \n> And I get\n> \n> Syntax Error:\n>     mathematica.NIntegrate[x^2,{x,1,0}]\n> \n> I know that I can switch to mathematica in the browser and works ok,\n> but if I want some result from mathematica and then use Sage, is that\n> possible?\n\nTry this:\n\nsage: z = mathematica('NIntegrate[x^2,{x,1,0}]'); z\n-0.3333333333333338\nsage: z + 3.5\n3.166666666666666\nsage: sin(float(z))\n-0.32719438181048527\n \n> I didnt find any docs on how to use mathematica in sage. \n\n\nThey are here:\n   http://sage.math.washington.edu/sage/doc/html/ref/module-sage.interfaces.mathematica.html\n\n> I find really\n> cool to use mathematica with the browser so I dont have to buy\n> webmathematica.  Is it possible to plot something in mathematica with\n> sage browser ?\n\nI've never done this before or seen anybody do it.  I just figured out how.\nAs an example, paste the following two lines into an input cell and press shift-enter:\n\nmathematica('SetDirectory[\"%s\"]'%os.path.abspath(\".\"))\n_ = mathematica('Export[\"a.png\", Plot[Sin[x],{x,-2Pi,4Pi}], ImageSize->600]')\n\nThe first complicated line above -- i.e., to set the directory, will not be needed \nin sage >= 2.9 -- I just made it automatic for future versions of sage. \n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1480\n\n",
    "created_at": "2007-12-12T18:35:05Z",
    "labels": [
        "interfaces",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "[with patch] implement P.show() for mathematica elements -- nice mathematica graphics in the sage notebook!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1480",
    "user": "@williamstein"
}
```
Assignee: @williamstein

As the summary says.  Inspired by this email

```


On Dec 12, 2007 10:07 AM, carlosap <carlosap78@gmail.com> wrote:
> 
> I typed mathematica.NIntegrate[x^2,{x,1,0}]
> 
> And I get
> 
> Syntax Error:
>     mathematica.NIntegrate[x^2,{x,1,0}]
> 
> I know that I can switch to mathematica in the browser and works ok,
> but if I want some result from mathematica and then use Sage, is that
> possible?

Try this:

sage: z = mathematica('NIntegrate[x^2,{x,1,0}]'); z
-0.3333333333333338
sage: z + 3.5
3.166666666666666
sage: sin(float(z))
-0.32719438181048527
 
> I didnt find any docs on how to use mathematica in sage. 


They are here:
   http://sage.math.washington.edu/sage/doc/html/ref/module-sage.interfaces.mathematica.html

> I find really
> cool to use mathematica with the browser so I dont have to buy
> webmathematica.  Is it possible to plot something in mathematica with
> sage browser ?

I've never done this before or seen anybody do it.  I just figured out how.
As an example, paste the following two lines into an input cell and press shift-enter:

mathematica('SetDirectory["%s"]'%os.path.abspath("."))
_ = mathematica('Export["a.png", Plot[Sin[x],{x,-2Pi,4Pi}], ImageSize->600]')

The first complicated line above -- i.e., to set the directory, will not be needed 
in sage >= 2.9 -- I just made it automatic for future versions of sage. 

```


Issue created by migration from https://trac.sagemath.org/ticket/1480





---

archive/issue_comments_009516.json:
```json
{
    "body": "Attachment [trac-1480.patch](tarball://root/attachments/some-uuid/ticket1480/trac-1480.patch) by @williamstein created at 2007-12-13 18:00:37\n\nTimothy Clemans points out that to get graphics to work remotely do:\n\n\n```\nXvfb 19\nexport DISPLAY=localhost:19\n```\n\nthen start the sage notebook server. \n\nThis is discussed at \n\n http://witm.sourceforge.net/installation.php\n\nThis should definitely somehow be in sage before this ticket is closed!\n\nE.g., on failure a message could be printed out telling the user to do the\nabove... and something like this could be in the docstring for the new show command.",
    "created_at": "2007-12-13T18:00:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1480#issuecomment-9516",
    "user": "@williamstein"
}
```

Attachment [trac-1480.patch](tarball://root/attachments/some-uuid/ticket1480/trac-1480.patch) by @williamstein created at 2007-12-13 18:00:37

Timothy Clemans points out that to get graphics to work remotely do:


```
Xvfb 19
export DISPLAY=localhost:19
```

then start the sage notebook server. 

This is discussed at 

 http://witm.sourceforge.net/installation.php

This should definitely somehow be in sage before this ticket is closed!

E.g., on failure a message could be printed out telling the user to do the
above... and something like this could be in the docstring for the new show command.



---

archive/issue_comments_009517.json:
```json
{
    "body": "Attachment [trac-148-part2.patch](tarball://root/attachments/some-uuid/ticket1480/trac-148-part2.patch) by @williamstein created at 2007-12-15 13:54:38",
    "created_at": "2007-12-15T13:54:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1480#issuecomment-9517",
    "user": "@williamstein"
}
```

Attachment [trac-148-part2.patch](tarball://root/attachments/some-uuid/ticket1480/trac-148-part2.patch) by @williamstein created at 2007-12-15 13:54:38



---

archive/issue_comments_009518.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T14:07:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1480#issuecomment-9518",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009519.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T14:07:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1480#issuecomment-9519",
    "user": "mabshoff"
}
```

Merged in 2.9.rc0.
