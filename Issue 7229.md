# Issue 7229: jsmath-image-fonts spkg installs to wrong directory

Issue created by migration from https://trac.sagemath.org/ticket/7229

Original creator: jason

Original creation time: 2009-10-15 15:54:26

Assignee: boothby

With the update to the new sage notebook, the jsmath-image-fonts spkg now installs to the wrong directory.


```
> >  * Install *all* jsMath image fonts on sagenb.org
> >  * Silently fall back to using image fonts if TeX fonts are not available


This is what was done in the sage notebook a few days ago.  William had 
installed the optional jsmath-image-fonts spkg a long time ago.  What 
probably happened is that no one rebased the jsmath-image-fonts to copy 
to the right javascript directory, and since these all moved around with 
the new notebook code, everything is broken with respect to this spkg now.

A solution is to modify the spkg to install to the right location, and 
install it again on sagenb.org.
```


Robert replies:

Installed 4.1.2. and the old spkg file with image fonts.
I got this error
I copied the image fonts from /opt/sage/local/notebook/javascript/
jsmath to /opt/sage/local/lib/python2.6/site-packages/sagenb/data/
javascript/jsmath and everything works fine.



---

Comment by robert.marik created at 2009-10-15 21:25:50

Changing status from new to needs_review.


---

Comment by robert.marik created at 2009-10-15 21:25:50

The fixed spkg file is at http://user.mendelu.cz/marik/temp/jsmath-image-fonts-1.4.spkg
(cannot upload to trac server due to the filesize limit)

The description of the change is at 
http://groups.google.cz/group/sage-devel/browse_thread/thread/3bce4bbe7ace0dc0


---

Comment by was created at 2009-10-15 21:34:55

The spkg didn't have the changed checked in. Also, it had some old bash-isms that would make it not work with some /bin/sh's.  Also, it would fail on any sage before 4.1.2, so I decided to fix it by (1) making it work on older sage's still, and (2) checkin the repo. I also updated the spkg name to .p1.   The new spkg is here:

http://sage.math.washington.edu/home/wstein/patches/jsmath-image-fonts-1.4.p1.spkg

So instead of me giving this a positive review, somebody else should look at it.


---

Comment by mpatel created at 2009-10-15 21:50:52

How should we deal with #7196?  A special `JSMATH_HOME` variable?

Also: Should we add the [extra fonts](http://www.math.union.edu/~dpvc/jsMath/download/extra-fonts/welcome.html)?


---

Comment by mpatel created at 2009-10-15 22:52:56

Replying to [comment:3 mpatel]:
> How should we deal with #7196?
I updated `spkg-install` to handle post-#7196 new notebooks.  For another reviewer:

http://sage.math.washington.edu/home/mpatel/trac/7229/jsmath-image-fonts-1.4.p2.spkg


---

Comment by robert.marik created at 2009-10-16 07:42:42

Replying to [comment:4 mpatel]:
> I updated `spkg-install` to handle post-#7196 new notebooks.  For another reviewer:
> 
> http://sage.math.washington.edu/home/mpatel/trac/7229/jsmath-image-fonts-1.4.p2.spkg

Works fine on fresh install of Sage 4.1.2. 
However (as new) I give up the closing of this ticket to some more skilled Sage user/developer.
Thank you for the fix.
Robert


---

Comment by was created at 2009-10-18 01:14:05

Positive review -- looks good to me.  I've posted the spkg here and closed the ticket.
http://sagemath.org/packages/optional/


---

Comment by was created at 2009-10-18 01:14:05

Resolution: fixed
