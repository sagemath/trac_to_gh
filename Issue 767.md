# Issue 767: animate has cryptic error message when imagemagick is not installed

Issue created by migration from https://trac.sagemath.org/ticket/767

Original creator: moretti

Original creation time: 2007-09-30 22:11:24

Assignee: boothby

when creating an animated gif on a system without imagemagick installed, the animate() command  just outputs

"sh: convert: not found"

instead of a more helpful error message (such as, "please install imagemagick")


---

Attachment


---

Comment by jhpalmieri created at 2008-09-30 17:03:55

Changing keywords from "" to "animate, ImageMagick".


---

Comment by jhpalmieri created at 2008-09-30 17:03:55

I'm attaching a patch; it depends on #4216.

With this patch, if 'convert' is not found, I get an error message like this:

```
/usr/local/share/sage/local/bin/sage-native-execute: 8: convert: not
found

Error: ImageMagick does not appear to be installed. Saving an
animation to a GIF file or displaying an animation requires
ImageMagick, so please install it and try again.

See www.imagemagick.org, for example.
```

So the first line is cryptic (but could be useful in debugging, if the problem is something other than a missing 'convert'), while the rest of the message is friendlier.


---

Comment by mabshoff created at 2008-09-30 17:23:25

Positive review on the patch. One small issue is that the animate.py doctest fails if convert is not installed:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2$ ./sage -t devel//sage/sage/plot/animate.py 
sage -t  devel/sage/sage/plot/animate.py                    
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/animate.py", line 59:
    sage: a.show()
Expected nothing
Got:
    <BLANKLINE>
    Error: ImageMagick does not appear to be installed. Saving an
    animation to a GIF file or displaying an animation requires
    ImageMagick, so please install it and try again.
    <BLANKLINE>
    See www.imagemagick.org, for example.
**********************************************************************
```


One way around this would be to make the doctest optional. 

Thoughts?

Cheers,

Michael


---

Comment by jhpalmieri created at 2008-09-30 17:34:22

> One way around this would be to make the doctest optional. 

This seems okay to me, but I also don't know enough about doctesting to know if there is any other choice.


---

Comment by mabshoff created at 2008-09-30 17:34:46

Ironically I just checked the animate.py file and all but one of the convert commands are already optional. So I am posting a trivial reviewer patch on top of John's patch and will merge both of them.

Cheers,

Michael


---

Comment by jhpalmieri created at 2008-09-30 17:57:31

Sorry, I should have checked the doctesting myself. Also, I noticed that several functions (including the one that I patched, `gif`) don't have doctests.  When I get around to it, I will open up another ticket and fix this.

Also, in my experience, running `animate(...)` doesn't require convert, _showing_ the animation does. So we can remove some of the `optional` flags, so that more things are doctested. I may try to do that in the same (soon to be forthcoming?) ticket.


---

Attachment


---

Comment by mabshoff created at 2008-09-30 18:16:58

Merged in Sage 3.1.3.alpha2


---

Comment by mabshoff created at 2008-09-30 18:16:58

Resolution: fixed
