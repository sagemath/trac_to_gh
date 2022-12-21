# Issue 3768: move jsmath into its own spkg

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-08-03 19:29:09

Assignee: mabshoff

We should move jsmath into its own spkg.  Like jquery, there seem to be two copies of it, and it'd be good to get rid of this duplication and track its versioning explicitly.


---

Comment by jason created at 2008-10-10 23:33:59

I'm working on this.


---

Comment by mabshoff created at 2008-12-04 17:42:23

Jason,

can you post the spkg here? This should be fairly orthogonal to all the other javascript work you are doing. Since the other patches need to be rebased anyway this would likey make it easier.


---

Comment by jason created at 2008-12-04 17:54:01

This is posted at #4267 :

http://sage.math.washington.edu/home/jason/notebook/jsmath-3.6a.spkg


---

Comment by jason created at 2008-12-04 17:54:49

I think it relies on changes in #4267, though, since it changes the paths that the notebook uses to include jsmath.  All of these changes are intertangled at #4267.


---

Comment by mabshoff created at 2008-12-04 17:58:20

Replying to [comment:4 jason]:
> I think it relies on changes in #4267, though, since it changes the paths that the notebook uses to include jsmath.  All of these changes are intertangled at #4267.

Mmh, the jsmath changes should be pretty harmless and as is #4267 is a mess. So taking care of jsmath independently and then redoing #4267 might be an option, but unless somebody else is doing the work I guess it is your call :)

Cheers,

Michael


---

Comment by jason created at 2008-12-04 18:01:45

I'd rather try doing it all at once, since once I'm sifting through the changes in #4267, it'll be easiest just to break it up all at once.  I'll try to get this done before the Joint Meetings (hopefully way before).


---

Comment by jason created at 2008-12-04 18:04:28

(when I say "all at once", I mean "breaking up #4267 into functional tickets" instead of trying to just pull out one change and then redo #4267).

Likely, #4267 will end up as several tickets:

 1. Make all the existing javascript code spkgs
 1. Various jquery-related cleanups of the javascript code
 1. Add TinyMCE as an (optional?) spkg
 1. Make the shift-click work (in-place wysiwyg editing).


---

Comment by jason created at 2008-12-04 18:07:08

#4674 is also a ticket about updating jsmath (but also includes one other thing).


---

Comment by mabshoff created at 2008-12-04 18:09:23

Replying to [comment:8 jason]:
> #4674 is also a ticket about updating jsmath (but also includes one other thing).

I agree, so I am closing this as a dupe of #4674.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-04 18:09:39

Resolution: duplicate


---

Comment by mabshoff created at 2008-12-04 18:16:00

Replying to [comment:7 jason]:
> (when I say "all at once", I mean "breaking up #4267 into functional tickets" instead of trying to just pull out one change and then redo #4267).
> 
> Likely, #4267 will end up as several tickets:
> 
>  1. Make all the existing javascript code spkgs
>  1. Various jquery-related cleanups of the javascript code
>  1. Add TinyMCE as an (optional?) spkg
>  1. Make the shift-click work (in-place wysiwyg editing).
> 

I would much rather have individual tickers:

 * move jsmath to its own spkg (#4674)
 * move jquery to its own spkg and remove both in tree copies (#3767)
 * cleanups of jquery code
 * TinyMCE
 * in place wysiwyg editing 

in exactly that order. Feel free to open three tickets (since we already have the jsmath and the jquery one) and then nuke #4267 and #4184 since both of them are a mess.

Doing multiple related, but independent tasks always leads to giant screw ups like #4276 where one small issue with one aspect of the ticket leads to the whole ticket going stale. 

Cheers,

Michael
