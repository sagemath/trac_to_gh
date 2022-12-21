# Issue 4267: Make javascript packages spkgs instead of part of the extcode repository

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-10-12 02:15:25

Assignee: boothby

Here are patches and spkgs to make most of the javascript applications we ship into spkgs instead of directories in the extcode repository.  This will facilitate updating these spkgs and makes things cleaner anyways.

I took the opportunity to upgrade each package to the lastest version while I was at it.  This affects the interact look and feel, since the new default theme for jqueryUI is different.  I chose a few colors and things, but of course, things are up for debate.  Let's not let bikeshedding get in the way of these patches, though; we can always make a follow-up patch that changes the theme very easily.


---

Comment by jason created at 2008-10-12 02:17:53

The spkgs are at:

http://sage.math.washington.edu/home/jason/notebook/jquery-1.2.6.spkg (standard spkgs)

http://sage.math.washington.edu/home/jason/notebook/jqueryui-1.6rc2.spkg (standard spkgs)

http://sage.math.washington.edu/home/jason/notebook/jsmath-3.6a.spkg (standard spkgs)

http://sage.math.washington.edu/home/jason/notebook/jsmath-image-fonts-1.3p0.spkg (optional spkgs)

http://sage.math.washington.edu/home/jason/notebook/tinyMCE-3.2.0.2.spkg (still under consideration)

The last package, tinyMCE, is still under consideration for inclusion.  The others have been accepted into either the standard or optional spkg groups.


---

Comment by mabshoff created at 2008-10-12 07:27:32

Jason,

the extcode patch is *huge* and should not be attached, but should be posted via some link.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-12 08:14:27

Jason,

the patch is now at

http://sage.math.washington.edu/home/mabshoff/extcode-remove-javascript-packages.patch

Either way, we should seriously consider resetting the extcode repo since the history is huge and there is relatively little benefit to keep it around considering the size.

Cheers,

Michael


---

Comment by jason created at 2008-10-18 04:06:19

Apply only edit-in-place-and-javascript-spkgs.patch.  Ignore the make-javascript-spkgs.patch file.

Note that the edit-in-place... patch also resolves #4255.

I also took the opportunity to clean up some of the javascript code in js.py to use jquery instead of custom code, and to note in comments several places where we could use jquery further to possibly simplify our code or make our code better.


---

Comment by jason created at 2008-10-18 04:10:29

This ticket also resolves #4184


---

Comment by jason created at 2008-10-18 04:15:25

This ticket also resolves #3767.


---

Comment by jason created at 2008-10-18 07:18:47

Updated the edit-in-place patch to fix two bugs.


---

Attachment

Apply only this patch from here and the extcode patch from the coments below.


---

Comment by jason created at 2008-10-18 07:56:34

Fixed two more bugs and made sure that applying the edit-in-place patch, the extcode patch from mabshoff's comment, and installing the spkgs above makes this all work on Sage 3.1.4.


---

Comment by jason created at 2008-10-19 02:30:58

I've updated the jqueryui spkg to the most recent svn version, which fixes some bugs in rc2.  The jqueryui spkg is here:

http://sage.math.washington.edu/home/jason/notebook/jqueryui-1.6r807svn.spkg


---

Comment by mhampton created at 2008-10-19 03:45:45

I'm having problems getting this to work, maybe because I'm still using the install that I tested #4255 on.  I applied the edit-in-place-and-javascript-spkgs.patch, which went OK, and the jqueryui-1.6r807svn.spkg, but I had only failures trying to install the extcode patch.  
After doing the above, I ran the notebook and couldn't even evaluate a cell.  I guess I will try again on a virgin 3.1.3 or 3.1.4.  A clarification of what order to do what spkgs and patches would be good though.


---

Comment by jason created at 2008-10-19 05:12:09

See #2113 if you're worried about how much stuff is sent to the browser.  That patch implements gzip compression for all javascript automatically (if the destination isn't a localhost).


---

Comment by mhampton created at 2008-10-19 13:19:16

I tried this again on a brand-new 3.1.4, and the extcode patch fails to apply, with man y statements like:

```
unable to find 'notebook/javascript/jqueryui/datepicker/i18n/ui.datepicker-hu.js' for patching
unable to find 'notebook/javascript/jsmath/extensions/bbox.js' for patching
```



---

Comment by mhampton created at 2008-10-19 13:27:45

OK, I applied using hg in extcode and it worked.  When I show() something, it tells me to download the jsmath fonts with a hyperlink, and when I click on the link I get:

```
Not Found

The requested URL /sage//jsmath was not found on this server. 
```


I did install the spkgs provided on this ticket.


---

Comment by mhampton created at 2008-10-19 13:33:26

The shift-click for making a new text cell does not appear to work, although I do get the tinymce editor when double-clicking existing cells.


---

Comment by jason created at 2008-10-20 19:31:55

I have a brand-new 3.1.4 install as well.  The extcode patch applies perfectly for me when I do the following, so something seems odd.  The patch just deletes a bunch of directories for cleanup purposes; applying the extcode patch should not change any functionality.


```
cd sage/data/extcode
wget http://sage.math.washington.edu/home/mabshoff/extcode-remove-javascript-packages.patch
hg qinit
hg qimport extcode-remove-javascript-packages.patch
hg qpush
```


I then also applied the edit-in-place-and-javascript-spkgs.patch patch from above to the main sage repository.

I then installed all the packages (except the jsmath-image-fonts one) from http://sage.math.washington.edu/home/jason/notebook/.  I used "sage -f <package>.spkg" to install these to make sure to overwrite the current package.

I then did sage -br

Then I started the notebook and everything seemed to work great (including the shift-click).  What browser are you using?  I'm using FF 3.0.1 on Ubuntu 8.04.


---

Comment by mhampton created at 2008-10-21 04:17:15

OK, that worked for me.  I was doing things in a different order, and somehow that caused some problems.

This seems to work well.  Something in the javascript changes seems to change the appearance of the `@`interact sliders, and I liked the old ones better, but I don't think thats important enough to object to this.  Other people might be more passionate about it.  I think this enhanced editing will be very useful for using the notebook in designing labs and for students writing up such labs.


---

Comment by jason created at 2008-10-21 14:08:58

The upgrade to the newest version of jqueryui changed the default theme.  It would be very easy to change back, or to design a new theme (with different colors, etc.).

If there is enough people wanting it, I will include the old theme as the default theme.  I don't really have a preference, though I think I do like the old sliders better.  It was easier to feel like you were moving them to a precise value since they weren't so big.

Would it be enough to just change the slider image back to the old image?


---

Comment by jason created at 2008-10-21 15:45:41

apply on top of the previous edit-...patch


---

Attachment

If its easy to do I think we should keep the old theme, for consistency.


---

Comment by boothby created at 2008-10-21 18:42:30

I'm gonna test the snot out of this later today.  I'll be happy to see my old ajax code go, but this needs to be heavily tested on every platform.


---

Comment by mhampton created at 2008-10-21 18:52:39

There seems to be a problem inserting new cells in Safari after focus has shifted to and from another application.  Reloading the page fixes this but its a bug.


---

Comment by jason created at 2008-10-21 20:26:24

Thanks for the extensive testing!


---

Attachment

The flora.patch should be applied on top of the previous patches and switches the default theme back to flora (the old theme).  I've also updated the http://sage.math.washington.edu/home/jason/notebook/jqueryui-1.6r807svn.spkg to contain this theme (and I ported the modifications that we made to it as well).


---

Comment by TimothyClemans created at 2008-10-31 03:38:02

On the Mac SHIFT-ENTER and other keys stop working.


---

Comment by ddrake created at 2008-11-03 08:29:48

I applied the extcode patch, edit-in-place-and-javascript-spkgs.patch, and flora.patch, and installed the jquery, jqueryui, jsmath, jsmath-image-fonts, and tinyMCE spkgs, all against 3.2.alpha2 on amd64 Ubuntu 8.10. I'm accessing the notebook using Firefox 3.0.3. First, the good news:

  * the tinyMCE stuff works well. I generally hate those sort of editing thingys, but shift-clicking for text entry and using tinyMCE works and is less annoying than I thought it would be.
  * ``@`interact` works well and seems a bit faster than before. I don't know if that's because of anything from this ticket, though.

Okay, now for bad news. :)

  * If I start typing "`plot(bess`" into a cell and hit tab to complete, I get "`plot%28bess`"
  * If I type "`plot(`" and hit tab, I get "`plot%3F`".
  * I also sometimes see the problems that [comment:21 mhampton reports] with inserting new cells.
  * I haven't figured out what does this, but frequently it gets stuck: there's the light green bar below a cell for something that's being evaluated, but there's no \/\/\/ blinky in the title. I can't do anything at that point other than quit -- interrupting, restarting, etc don't have any effect.

I tried with IE7 (in an XP virtual machine) and got the same tab-completion problems, but not the other problems.


---

Comment by jason created at 2008-11-03 12:32:08

Thanks.  The tab completion should be an easy fix (I think I already fixed it, but apparently somehow the update didn't make it to trac.)  As for the stuck problem, I have an idea, but not the time immediately to work on it.  I'll probably have more time later this week.

Thanks for testing!


---

Comment by boothby created at 2008-11-03 19:56:36

I like the idea of this patch.  However, it claims to "Make javascript packages spkgs" -- but in addition to that, it touches a huge amount of non-package javascript, adds a new editor, etc.  It introduces a number of bugs which have proven very difficult to even attempt to fix.  Please factor out the new code and move it to different tickets.


---

Comment by jason created at 2008-11-03 20:20:10

Good point. I originally had separate tickets, but the patches all got intertangled and mixed up.

I think it might be easier to fix the bugs in the current code than to separate it out into several tickets again.  If I need to separate it out again, it will probably be at least several weeks before I can get it done.  If fixing the bugs turns out to be the things I think are happening I can probably have it done a lot sooner.


---

Comment by was created at 2008-11-04 23:23:46

> I think it might be easier to fix the bugs in the current code than to separate it out > into several tickets again.

It might be easier for you to fix the known bugs, but it won't be easier for Tom to review the result, especially the lack of a good testing framework for the notebook.  Patch bombs are bad, especially wrt the notebook.   I thus hope you can separate things out some more.  Maybe just do one easy thing now?

William


---

Comment by jason created at 2008-11-05 00:33:49

Again, good point.  I'll work on teasing out things one at a time here as I have time.


---

Comment by jason created at 2008-12-02 16:06:57

#4674 is also relevant here.


---

Comment by jason created at 2008-12-04 18:05:21

As noted on #4674, this should be broken into four tickets:

   1. Make all the existing javascript code spkgs
   2. Various jquery-related cleanups of the javascript code
   3. Add TinyMCE as an (optional?) spkg
   4. Make the shift-click work (in-place wysiwyg editing).


---

Comment by jason created at 2008-12-04 18:05:21

Changing assignee from boothby to jason.


---

Comment by jason created at 2008-12-04 18:05:21

Changing status from new to assigned.


---

Comment by jason created at 2008-12-05 01:23:15

This was split up into #4700, #4705, and #4705, so it is invalid as-is.


---

Comment by jason created at 2008-12-05 01:23:15

Resolution: invalid


---

Comment by mabshoff created at 2009-01-19 08:16:05

Changing status from closed to reopened.


---

Comment by mabshoff created at 2009-01-19 08:16:05

Ok, the patch 

trac_4267_extcode-remove-javascript-packages.patch

is still relevant and I am giving it a positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-19 08:16:05

Resolution changed from invalid to 


---

Comment by mabshoff created at 2009-01-19 08:16:27

Merged trac_4267_extcode-remove-javascript-packages.patch in Sage 3.3.alpha0


---

Comment by mabshoff created at 2009-01-19 08:16:27

Resolution: fixed
