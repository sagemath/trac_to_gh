# Issue 1483: animate -- polish the animate command

archive/issues_001483.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\n\n\nOn Dec 12, 2007 12:22 PM, kcrisman <> wrote:\n> \n> \n> \n> \n> >\n> > > The question:\n> > > Is there any way to get SAGE to update a graphic without actually\n> > > creating a new graphic, either in command-line mode or in notebook?\n> >\n> > Would creating an animation be a reasonable substitute?\n> > E.g.,\n> >\n> > {{{id=119|\n> > a = random_matrix(GF(37),10)*10\n> > b = [a^i for i in [1..37]]\n> >\n> > }}}\n> >\n> > {{{id=122|\n> > A = animate(matrix_plot(x) for x in b)\n> >\n> > }}}\n> >\n> > {{{id=120|\n> > show(A)\n> >\n> > }}}\n> \n> Oh, yes, this is exactly it - I feel a little silly for not thinking\n> of searching for \"animate\".\n> \n> Though it is still not at all easy to figure out how to do it.  You\n> have to think of animate; then you have to figure out that the mystery\n> error message about 'convert' means you should find Imagemagick; then\n> you have to figure out how to get it and unpack it (luckily I have\n> Fink), etc.  So another example of a steepish learning curve.  Still,\n> good to know how to do it.  Actually, animate has some very\n> interesting methods - I am really looking forward to trying the\n> addition of animations!\n\nI totally agree.  It would be great if somebody new of a simple\nlightweight tool or way to assemble a bunch of png's together\ninto an animated gif -- I used convert (via imagemagick) since\nit was the only thing I could find that works.  Regarding\nthe lack of a good error message that explains what convert\nis, how to install it, etc., that is mainly because I wrote the animate\ncommand pretty recently specifically for a high-school workshop I was\nrunning, and didn't have to worry about convert not being\navailable.   animate hasn't got the additional polish it deserves. \n\n> On a different note (and I don't know what people think of this, as\n> it's not really SAGE) I noticed two problems, perhaps unique to Mac,\n> after the SAGE stuff is resolved.  First, if you do it command-line,\n\nThat's a good point -- that should be changed.  \n\n> Preview opens the animated .gif up automatically and won't play it (it\n> lists all the individual frames), and I couldn't even save it there,\n> nor drag it into a browser to play it (had to dig into the .sage\n> directory in Terminal to do this).  Second, when I do it in the\n> browser, it just plays forever like any other dorky animated .gif on a\n> 1995-vintage website.  Is this a bug or a feature?\n\nAnimate *is* outputting a dorky animated .gif 1995-vintage style.\nThe con is that it looks dorky.  The pro is that you can save that give\nand trivially put it on any web page, etc.\n\n -- William\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1483\n\n",
    "created_at": "2007-12-12T20:39:28Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "animate -- polish the animate command",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1483",
    "user": "@williamstein"
}
```
Assignee: @williamstein


```


On Dec 12, 2007 12:22 PM, kcrisman <> wrote:
> 
> 
> 
> 
> >
> > > The question:
> > > Is there any way to get SAGE to update a graphic without actually
> > > creating a new graphic, either in command-line mode or in notebook?
> >
> > Would creating an animation be a reasonable substitute?
> > E.g.,
> >
> > {{{id=119|
> > a = random_matrix(GF(37),10)*10
> > b = [a^i for i in [1..37]]
> >
> > }}}
> >
> > {{{id=122|
> > A = animate(matrix_plot(x) for x in b)
> >
> > }}}
> >
> > {{{id=120|
> > show(A)
> >
> > }}}
> 
> Oh, yes, this is exactly it - I feel a little silly for not thinking
> of searching for "animate".
> 
> Though it is still not at all easy to figure out how to do it.  You
> have to think of animate; then you have to figure out that the mystery
> error message about 'convert' means you should find Imagemagick; then
> you have to figure out how to get it and unpack it (luckily I have
> Fink), etc.  So another example of a steepish learning curve.  Still,
> good to know how to do it.  Actually, animate has some very
> interesting methods - I am really looking forward to trying the
> addition of animations!

I totally agree.  It would be great if somebody new of a simple
lightweight tool or way to assemble a bunch of png's together
into an animated gif -- I used convert (via imagemagick) since
it was the only thing I could find that works.  Regarding
the lack of a good error message that explains what convert
is, how to install it, etc., that is mainly because I wrote the animate
command pretty recently specifically for a high-school workshop I was
running, and didn't have to worry about convert not being
available.   animate hasn't got the additional polish it deserves. 

> On a different note (and I don't know what people think of this, as
> it's not really SAGE) I noticed two problems, perhaps unique to Mac,
> after the SAGE stuff is resolved.  First, if you do it command-line,

That's a good point -- that should be changed.  

> Preview opens the animated .gif up automatically and won't play it (it
> lists all the individual frames), and I couldn't even save it there,
> nor drag it into a browser to play it (had to dig into the .sage
> directory in Terminal to do this).  Second, when I do it in the
> browser, it just plays forever like any other dorky animated .gif on a
> 1995-vintage website.  Is this a bug or a feature?

Animate *is* outputting a dorky animated .gif 1995-vintage style.
The con is that it looks dorky.  The pro is that you can save that give
and trivially put it on any web page, etc.

 -- William
```


Issue created by migration from https://trac.sagemath.org/ticket/1483





---

archive/issue_comments_009545.json:
```json
{
    "body": "Duh -- now I remember what I was going to do with animate\nwhen I had more time.  Just use javascript!  Javascript\nis great at animating a sequence of images, scratching through,\nchanging the speed, etc.  So, who can find a good free \njavascript script to do this somewhere online, which we can\ntouch up for inclusion in sage?",
    "created_at": "2007-12-12T21:23:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1483#issuecomment-9545",
    "user": "@williamstein"
}
```

Duh -- now I remember what I was going to do with animate
when I had more time.  Just use javascript!  Javascript
is great at animating a sequence of images, scratching through,
changing the speed, etc.  So, who can find a good free 
javascript script to do this somewhere online, which we can
touch up for inclusion in sage?



---

archive/issue_comments_009546.json:
```json
{
    "body": "Changing assignee from @williamstein to mhampton.",
    "created_at": "2009-01-16T14:06:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1483#issuecomment-9546",
    "user": "mhampton"
}
```

Changing assignee from @williamstein to mhampton.



---

archive/issue_comments_009547.json:
```json
{
    "body": "It would also be good to have an option that used ffmpeg, which I can do.  Any comments on how to do this in javascript are appreciated.",
    "created_at": "2009-01-16T14:06:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1483#issuecomment-9547",
    "user": "mhampton"
}
```

It would also be good to have an option that used ffmpeg, which I can do.  Any comments on how to do this in javascript are appreciated.



---

archive/issue_comments_009548.json:
```json
{
    "body": "> It would also be good to have an option that used ffmpeg, which I can do. Any comments > on how to do this in javascript are appreciated. \n\nWhat does \"do this in javascript\" mean?  Do you mean have a sequence of frames displayed using javascript (or something else) instead of an animated gif?   I just want to make sure.  I don't know how to do this, but suspect something like this is possible.  It's the sort of thing I would google for, e.g, \"javascript\" \"animation\".   I think flash would also be something to try, though of course it is has openness issues, etc., but the result would be excellent, and it is pretty much the standard on the web for animations, I think.",
    "created_at": "2009-01-17T18:44:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1483#issuecomment-9548",
    "user": "@williamstein"
}
```

> It would also be good to have an option that used ffmpeg, which I can do. Any comments > on how to do this in javascript are appreciated. 

What does "do this in javascript" mean?  Do you mean have a sequence of frames displayed using javascript (or something else) instead of an animated gif?   I just want to make sure.  I don't know how to do this, but suspect something like this is possible.  It's the sort of thing I would google for, e.g, "javascript" "animation".   I think flash would also be something to try, though of course it is has openness issues, etc., but the result would be excellent, and it is pretty much the standard on the web for animations, I think.



---

archive/issue_comments_009549.json:
```json
{
    "body": "Yes, I meant display a sequence of frames using javascript - I meant to refer to your initial comment on this ticket.  That should work on any browser.  It doesn't look hard, using setTimeout and setInterval, although it might take some work to look good.",
    "created_at": "2009-01-17T18:55:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1483#issuecomment-9549",
    "user": "mhampton"
}
```

Yes, I meant display a sequence of frames using javascript - I meant to refer to your initial comment on this ticket.  That should work on any browser.  It doesn't look hard, using setTimeout and setInterval, although it might take some work to look good.



---

archive/issue_comments_009550.json:
```json
{
    "body": "Here's a stab at using javascript to do animations. This doesn't work, but I don't understand enough about the notebook and/or javascript to know why; maybe someone else can do something with it.  To try it:\n\n```\na = animate([sin(x + float(k)) for k in srange(0,2*pi,0.3)], xmin=0, xmax=2*pi, figsize=[2,1])\na.js()\n```\n\nThis ought to show the animation, but it doesn't.  As a compromise, it creates a link \"animate.html\" which shows the animation in a separate browser window.\n\n(Since this doesn't work, it doesn't have much of a docstring, and there are no doctests.)",
    "created_at": "2009-06-29T23:55:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1483#issuecomment-9550",
    "user": "@jhpalmieri"
}
```

Here's a stab at using javascript to do animations. This doesn't work, but I don't understand enough about the notebook and/or javascript to know why; maybe someone else can do something with it.  To try it:

```
a = animate([sin(x + float(k)) for k in srange(0,2*pi,0.3)], xmin=0, xmax=2*pi, figsize=[2,1])
a.js()
```

This ought to show the animation, but it doesn't.  As a compromise, it creates a link "animate.html" which shows the animation in a separate browser window.

(Since this doesn't work, it doesn't have much of a docstring, and there are no doctests.)



---

archive/issue_comments_009551.json:
```json
{
    "body": "(This is the same as \"trac_1483_animate.py\", but it has the right name :p)",
    "created_at": "2009-06-29T23:56:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1483#issuecomment-9551",
    "user": "@jhpalmieri"
}
```

(This is the same as "trac_1483_animate.py", but it has the right name :p)



---

archive/issue_comments_009552.json:
```json
{
    "body": "Attachment [trac_1483_animate.patch](tarball://root/attachments/some-uuid/ticket1483/trac_1483_animate.patch) by @williamstein created at 2009-06-30 14:35:29\n\nmodified the previous posted code so it actually works in the notebook and fixed some bugs",
    "created_at": "2009-06-30T14:35:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1483#issuecomment-9552",
    "user": "@williamstein"
}
```

Attachment [trac_1483_animate.patch](tarball://root/attachments/some-uuid/ticket1483/trac_1483_animate.patch) by @williamstein created at 2009-06-30 14:35:29

modified the previous posted code so it actually works in the notebook and fixed some bugs



---

archive/issue_comments_009553.json:
```json
{
    "body": "Attachment [trac_1483-part2.patch](tarball://root/attachments/some-uuid/ticket1483/trac_1483-part2.patch) by @williamstein created at 2009-06-30 14:36:14",
    "created_at": "2009-06-30T14:36:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1483#issuecomment-9553",
    "user": "@williamstein"
}
```

Attachment [trac_1483-part2.patch](tarball://root/attachments/some-uuid/ticket1483/trac_1483-part2.patch) by @williamstein created at 2009-06-30 14:36:14



---

archive/issue_comments_009554.json:
```json
{
    "body": "This doesn't seem to work for me.  After executing a.js(), I get a pop-up message \"Syntax error: illegal character\", and then the output in the cell is:\n'\\n        \\n        \\n        '\n\n-Marshall",
    "created_at": "2009-07-17T12:44:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1483#issuecomment-9554",
    "user": "mhampton"
}
```

This doesn't seem to work for me.  After executing a.js(), I get a pop-up message "Syntax error: illegal character", and then the output in the cell is:
'\n        \n        \n        '

-Marshall



---

archive/issue_comments_009555.json:
```json
{
    "body": "Replying to [comment:7 mhampton]:\n> This doesn't seem to work for me.  After executing a.js(), I get a pop-up message \"Syntax error: illegal character\", and then the output in the cell is:\n> '\\n        \\n        \\n        '\n\nI don't know what's causing this (or I do, but I don't know why: it's the line `s = '<html>%s</html>'%s`).  Anyway, in the notebook, don't execute `a.js()`.  Instead, execute `print a.js()`.",
    "created_at": "2009-07-21T19:06:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1483#issuecomment-9555",
    "user": "@jhpalmieri"
}
```

Replying to [comment:7 mhampton]:
> This doesn't seem to work for me.  After executing a.js(), I get a pop-up message "Syntax error: illegal character", and then the output in the cell is:
> '\n        \n        \n        '

I don't know what's causing this (or I do, but I don't know why: it's the line `s = '<html>%s</html>'%s`).  Anyway, in the notebook, don't execute `a.js()`.  Instead, execute `print a.js()`.



---

archive/issue_comments_009556.json:
```json
{
    "body": "See #11170 for an approach using ffmpeg.  If #11170 works, should we close this ticket?",
    "created_at": "2011-04-26T18:50:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1483#issuecomment-9556",
    "user": "@jhpalmieri"
}
```

See #11170 for an approach using ffmpeg.  If #11170 works, should we close this ticket?



---

archive/issue_comments_009557.json:
```json
{
    "body": "I'd say that the following would be needed to close this ticket.\n* Add documentation showing actual use of ffmpeg to `animate?` (currently one needs\n\n```\nsage.plot.animate.Animation.ffmpeg?\n```\n\n  which seems hard to find unless one knows where to look.  Naturally, the doctests would have to be optional.\n* Find out whether the annoying issue of Preview automatically opening these in a way that can't be used in Mac can be resolved.",
    "created_at": "2012-06-01T19:20:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1483#issuecomment-9557",
    "user": "@kcrisman"
}
```

I'd say that the following would be needed to close this ticket.
* Add documentation showing actual use of ffmpeg to `animate?` (currently one needs

```
sage.plot.animate.Animation.ffmpeg?
```

  which seems hard to find unless one knows where to look.  Naturally, the doctests would have to be optional.
* Find out whether the annoying issue of Preview automatically opening these in a way that can't be used in Mac can be resolved.
