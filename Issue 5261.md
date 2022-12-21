# Issue 5261: Straigten out some annoyances with the OSX Sage.app bundle

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-02-14 00:09:23

Assignee: mabshoff

CC:  kcrisman

This is somewhat of a multi issue ticket, but I don't think that doing all four of them individually will give us much of a benefit.

  * default the name to Sage-x.y.z.app - that way you can have many Sage releases in parallel :) 
  * fix a bug that causes the app to fail to start if the name of the app contains spaces 
  * remove the extra copyright work in credits as well as give credit to "William Stein and the Sage Development Team" 
  * do not put the app skeleton in a tar.gz in the ext repo since it makes applying patches very expensive and opaque 


Cheers,

Michael


---

Comment by mabshoff created at 2009-02-14 13:44:44

Changing status from new to assigned.


---

Comment by GeorgSWeber created at 2009-02-17 22:21:03

One more point from #5254, not to be forgotten (no discussion on sage-devel yet):

What do you think of putting in the name also the dependency "Intel vs. PPC" resp. "32Bit vs. 64Bit"?


---

Comment by mabshoff created at 2009-02-17 22:24:20

Replying to [comment:3 GeorgSWeber]:
> One more point from #5254, not to be forgotten (no discussion on sage-devel yet):
> 
> What do you think of putting in the name also the dependency "Intel vs. PPC" resp. "32Bit vs. 64Bit"?

It might happen, but it is something bigger, i.e. we should add a check in the startup script that this is the right arch to begin with, i.e. it should be another ticket altogether.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-01 02:26:38

Better luck in 3.4.1.

Cheers,

Michael


---

Attachment


---

Comment by iandrus created at 2009-11-28 09:12:55

Changing status from new to needs_review.


---

Comment by iandrus created at 2009-11-28 09:12:55

The patch (spaces-5261.patch) requires that the patch at #7546 be applied first.  

This patch is a hack to ensure there are no spaces in the path.  It would be much better to fix the components that don't support it, but there are too many of them for me to be confident that I found them all.

It also does the location checking from #5254, but I don't actually think it's necessary with the hack above.

The naming Sage-x.y.z and changing from tar.gz were taken care of in #7546.

Someone with a better understanding of the copyright situation should change data/extcode/sage/ext/mac-app/Sage.app/Contents/Info.plist (it's an xml file) in two places.


---

Comment by kcrisman created at 2009-12-08 16:17:40

The naming in #7546 works fine.

Location changes seem to work okay, I'll put in final positive review once I've checked a few more things.

Copyright is now #7622, naming for PPC/Intel is #7623.


---

Comment by kcrisman created at 2009-12-08 16:44:42

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2009-12-08 16:44:42

Unfortunately, if I rename the app bundle to have a space, things don't work.  I misread the stuff above - now I understand what the problem was. 

I am renaming the ticket, and hopefully this will be possible to fix still.


---

Comment by kcrisman created at 2009-12-08 16:51:37

Sorry, I must have made a mistake in which app bundle to use - it works!  On both PPC and Macintel, though occasionally I get weird cookie issues, presumably not directly related, which a reload fixes.


---

Comment by kcrisman created at 2009-12-08 16:51:37

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2009-12-08 16:51:47

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-09 02:44:34

Resolution: fixed


---

Comment by kcrisman created at 2009-12-17 17:01:29

Just to check, I did end up trying an Intel build on a PPC finally. It runs sage-location and then gives messages like

```
/tmp/sage-map-app/local/bin/python: /tmp/sage-map-app/local/bin/python: cannot execute binary file
```

So presumably this is what we want?  Or should there be a better error message?
