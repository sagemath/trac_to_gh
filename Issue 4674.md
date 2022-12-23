# Issue 4674: use easy/load.js when loading jsmath

Issue created by migration from https://trac.sagemath.org/ticket/4674

Original creator: mabshoff

Original creation time: 2008-12-02 15:35:23

Assignee: boothby

From http://groups.google.com/group/sage-support/t/178d0bd277044918

```
Yes, that looks correct.  I'm not sure why people are getting the 
error -7 under these conditions.  It means that something has gone 
wrong when trying to load the fallback method, and that usually means 
it can't read the image font definition files.  There are a couple of 
other possibilities as well:  perhaps the noImageFonts plugin was not 
able to be read (permission issue?) or the unicode fallback file could 
not be read.  Given your use of noImageFonts, I suspect it may be the 
latter.  If the users who are getting error -7 are using Firefox3, 
that may well be it.  There were changes to the same-origin security 
policy in Firefox3 that prevent jsMath from loading local files from 
directories other than the one in which the HTML file is found.  I 
worked around this in jsMath v3.6 (released Sept. 2008), so those 
users should update to the latest version of jsMath to avoid that 
problem. 
> I'm pretty sure we don't use the easy/load.js (and I'm not sure why). 

Probably because it didn't exist when jsMath support was added to 
sage.  The easy/load.js file was a relatively late addition to jsMath, 
but certainly makes things easier for people.  You might consider 
whether you want to use that instead. 

Davide
```



---

Comment by jason created at 2008-12-02 16:06:11

jsMath is version 3.6a now: http://sourceforge.net/project/showfiles.php?group_id=172663


---

Comment by jason created at 2008-12-02 16:06:16

Changing status from new to assigned.


---

Comment by jason created at 2008-12-02 16:06:16

Changing assignee from boothby to jason.


---

Comment by jason created at 2008-12-02 16:07:13

#4267 is also related.


---

Comment by jason created at 2008-12-02 16:08:21

#4267 is related in that it already contains an spkg for the updated jsmath.


---

Comment by jason created at 2008-12-04 18:06:39

#3768 is the ticket for updating jsmath.


---

Comment by jason created at 2008-12-05 09:53:28

The jsmath spkgs are here: 

http://sage.math.washington.edu/home/jason/notebook/jsmath-3.6a.spkg

http://sage.math.washington.edu/home/jason/notebook/jsmath-image-fonts-1.3p0.spkg


---

Comment by jason created at 2008-12-05 09:54:49

The obsolete jsmath directory should be deleted out of the extcode repository as well.


---

Comment by jason created at 2008-12-05 10:08:53

I also cleaned up places where the JSMATH variable was set.  There is no purpose for the variable, since jsmath is a standard part of Sage (it is always installed).


---

Comment by jason created at 2008-12-05 10:11:12

See #4714 for the loading part of this ticket.


---

Comment by was created at 2008-12-06 22:52:49

> I also cleaned up places where the JSMATH variable was set. There 
> is no purpose for the variable, since jsmath is a standard part of 
> Sage (it is always installed). 

jsmath was standard ever since we used it with the notebook.  That wasn't the point of the variable.  The point is that it gives users a way to turn of use of jsmath entirely, which may be a very good idea in some settings (e.g., low bandwidth notebook servers).   Basically, for no good reason I think you've removed functionality.  Make a new patch that just has the first change in the first version of the patch you attached above.


---

Attachment


---

Comment by jason created at 2008-12-20 20:54:43

Okay, I updated the jsmath-spkg.patch to address the concerns above.

Note that functionality spoken of in the review has been broken for a while.  I think this is because run_notebook.py automatically sets the JSMATH variable to True, no matter what.  However, fixing this so that it works is a different issue than this ticket.


---

Comment by mabshoff created at 2008-12-24 17:17:04

Looks good to me. Some review changes were made at

 * http://sage.math.washington.edu/home/mabshoff/spkgs/jsmath-3.6a.p0.spkg
 * http://sage.math.washington.edu/home/mabshoff/spkgs/jsmath-image-fonts-1.3p1.spkg

Please rereview, the changes are fairly minor. I mostly fixed stylistic issues as well as made sure that old jsmath installs (including their fonts) are cleaned out to avoid problems due to left over cruft. This means that an upgrade to jsmath deletes also the image fonts, but that seems a worthwhile price to pay.

For the record: jsmath-3.6a.p0.spkg is going into standard Sage while jsmath-image-fonts-1.3p1.spkg should go into the optional repo.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-19 06:31:46

Positive review due to #4705.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-19 08:03:50

Resolution: fixed


---

Comment by mabshoff created at 2009-01-19 08:03:50

Merged jsmath-spkg.patch and jsmath-3.6a.p0.spkg in Sage 3.3.alpha0.

Merged jsmath-image-fonts-1.3p1.spkg into the optional spkg repo.

Cheers,

Michael
