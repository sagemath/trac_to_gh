# Issue 1483: animate -- polish the animate command

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-12 20:39:28

Assignee: was


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



---

Comment by was created at 2007-12-12 21:23:14

Duh -- now I remember what I was going to do with animate
when I had more time.  Just use javascript!  Javascript
is great at animating a sequence of images, scratching through,
changing the speed, etc.  So, who can find a good free 
javascript script to do this somewhere online, which we can
touch up for inclusion in sage?


---

Comment by mhampton created at 2009-01-16 14:06:30

Changing assignee from was to mhampton.


---

Comment by mhampton created at 2009-01-16 14:06:30

It would also be good to have an option that used ffmpeg, which I can do.  Any comments on how to do this in javascript are appreciated.


---

Comment by was created at 2009-01-17 18:44:01

> It would also be good to have an option that used ffmpeg, which I can do. Any comments > on how to do this in javascript are appreciated. 

What does "do this in javascript" mean?  Do you mean have a sequence of frames displayed using javascript (or something else) instead of an animated gif?   I just want to make sure.  I don't know how to do this, but suspect something like this is possible.  It's the sort of thing I would google for, e.g, "javascript" "animation".   I think flash would also be something to try, though of course it is has openness issues, etc., but the result would be excellent, and it is pretty much the standard on the web for animations, I think.


---

Comment by mhampton created at 2009-01-17 18:55:22

Yes, I meant display a sequence of frames using javascript - I meant to refer to your initial comment on this ticket.  That should work on any browser.  It doesn't look hard, using setTimeout and setInterval, although it might take some work to look good.


---

Comment by jhpalmieri created at 2009-06-29 23:55:03

Here's a stab at using javascript to do animations. This doesn't work, but I don't understand enough about the notebook and/or javascript to know why; maybe someone else can do something with it.  To try it:

```
a = animate([sin(x + float(k)) for k in srange(0,2*pi,0.3)], xmin=0, xmax=2*pi, figsize=[2,1])
a.js()
```

This ought to show the animation, but it doesn't.  As a compromise, it creates a link "animate.html" which shows the animation in a separate browser window.

(Since this doesn't work, it doesn't have much of a docstring, and there are no doctests.)


---

Comment by jhpalmieri created at 2009-06-29 23:56:32

(This is the same as "trac_1483_animate.py", but it has the right name :p)


---

Attachment

modified the previous posted code so it actually works in the notebook and fixed some bugs


---

Attachment


---

Comment by mhampton created at 2009-07-17 12:44:40

This doesn't seem to work for me.  After executing a.js(), I get a pop-up message "Syntax error: illegal character", and then the output in the cell is:
'\n        \n        \n        '

-Marshall


---

Comment by jhpalmieri created at 2009-07-21 19:06:39

Replying to [comment:7 mhampton]:
> This doesn't seem to work for me.  After executing a.js(), I get a pop-up message "Syntax error: illegal character", and then the output in the cell is:
> '\n        \n        \n        '

I don't know what's causing this (or I do, but I don't know why: it's the line `s = '<html>%s</html>'%s`).  Anyway, in the notebook, don't execute `a.js()`.  Instead, execute `print a.js()`.


---

Comment by jhpalmieri created at 2011-04-26 18:50:56

See #11170 for an approach using ffmpeg.  If #11170 works, should we close this ticket?


---

Comment by kcrisman created at 2012-06-01 19:20:25

I'd say that the following would be needed to close this ticket.
* Add documentation showing actual use of ffmpeg to `animate?` (currently one needs

```
sage.plot.animate.Animation.ffmpeg?
```

  which seems hard to find unless one knows where to look.  Naturally, the doctests would have to be optional.
* Find out whether the annoying issue of Preview automatically opening these in a way that can't be used in Mac can be resolved.
