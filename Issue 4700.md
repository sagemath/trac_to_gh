# Issue 4700: Move existing javascript packages in extcode to their own spkg packages

Issue created by migration from https://trac.sagemath.org/ticket/4700

Original creator: jason

Original creation time: 2008-12-05 00:23:39

Assignee: boothby

This ticket moves the jsmath, jquery, jqueryui, and jsmath-image-fonts packages to their own spkgs that install in local/notebook/javascript.

Sorry, mabshoff; it was much easier to group these very related and similar tasks together.

The spkgs are at:



http://sage.math.washington.edu/home/jason/notebook/jquery-1.2.6.spkg

http://sage.math.washington.edu/home/jason/notebook/jqueryui-1.6r807svn.spkg

http://sage.math.washington.edu/home/jason/notebook/jsmath-3.6a.spkg

http://sage.math.washington.edu/home/jason/notebook/jsmath-image-fonts-1.3p0.spkg

The (huge) patch that deletes things from the extcode repository is at

http://sage.math.washington.edu/home/mabshoff/extcode-remove-javascript-packages.patch (apply to the extcode repository; we might reset the extcode history, as mabshoff suggested on #4267).




---

Comment by jason created at 2008-12-05 00:26:23

This ticket also takes the opportunity to update each of the javascript packages to the latest version (as of late October, 2008).  Some of the changes in the patch reflect the updating (primarily, the updating of jqueryui).


---

Comment by mabshoff created at 2008-12-05 00:34:54

Resolution: invalid


---

Comment by mabshoff created at 2008-12-05 00:34:54

No, 

the whole point was that

 1. these tasks are independent
 1. this is again a composite ticket just like #4267

So: invalid.

Cheers,

Michael


---

Comment by was created at 2008-12-05 00:53:35

OK, guys calm down.    It will be _massively_ easier referee wise if you can break this up into independent tasks, especially because there's still a lot of work to integrate this into sage, even after handing it off.    Please please please Jason can you split this into smaller well-defined tasks?  Thanks!!


---

Attachment


---

Comment by mabshoff created at 2008-12-05 00:56:31

To elaborate some more why these tickets need to be split up:

 * verifying that the updated jsmath.spkg works is trivial
 * anything touching jquery needs to be reviewed in much more detail, i.e. somebody needs to check that DSage still works, i.e. its GUI
 * jsmath-image-fonts-1.3p0.spkg is an optional spkg, so it should be trivial to review

Mixing and matching seemingly related tickets and then ending up piling fixes on top has proven a disaster time after time, so let's please be nice about this and get this resolved.

Cheers,

Michael

PS: Sorry if my tone was out of line, I had just woken up :)


---

Comment by jason created at 2008-12-05 01:17:22

Okay; I saw all of these tasks as very similar, hence the same ticket.  It'll be a lot more work to split it up further than this, but I'll get to it eventually.
