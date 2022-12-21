# Issue 6938: sage-README-osx.txt is non-sensical for a source distribution.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-09-15 21:44:18

Assignee: tba

CC:  drkirkby

The file sage-README-osx.txt is very confusing. If someone downloads the source, the readme file indicates they have downloaded binaries. 

There should perhaps be two README files - one for source, and one for binaries. 


---

Comment by jhpalmieri created at 2010-03-31 16:58:48

See also #5296.

By the way, I see two copies of the file "sage-README-osx.txt": 

 - in the top-level directory: this one should be present in a binary distribution on OS X, not otherwise.
 - in SAGE_ROOT/local/bin.  This one should be deleted.  It doesn't seem to be tracked by Mercurial, so it needs to be removed by hand.


---

Comment by kcrisman created at 2010-04-22 01:55:50

Replying to [comment:2 jhpalmieri]:
> See also #5296.
> 
> By the way, I see two copies of the file "sage-README-osx.txt": 
> 
>  - in the top-level directory: this one should be present in a binary distribution on OS X, not otherwise.
>  - in SAGE_ROOT/local/bin.  This one should be deleted.  It doesn't seem to be tracked by Mercurial, so it needs to be removed by hand.
> 

Hmm.  But if both of these are not present in a source distribution, then where will it come from when sage -bdist is run?  It has to be somewhere, right?


---

Comment by kcrisman created at 2010-04-22 02:31:06

Replying to [comment:2 jhpalmieri]:
> See also #5296.
> 
> By the way, I see two copies of the file "sage-README-osx.txt": 
> 
>  - in the top-level directory: this one should be present in a binary distribution on OS X, not otherwise.
>  - in SAGE_ROOT/local/bin.  This one should be deleted.  It doesn't seem to be tracked by Mercurial, so it needs to be removed by hand.
> 

Oh yeah, this one is needed for sage-bdist - see line 92:

```
    cp sage/local/bin/sage-README-osx.txt README.txt
```

But the one on the top level should be able to be safely removed, given that line in sage-bdist, methinks.  Whether the one in /local/bin should overwrite the usual README.txt is another question.  

Incidentally, the usual README.txt maybe should be updated - for instance, Mac OS X is essentially fully supported now, correct?  And Fortran is now only included for OS X, not Linux, I believe. 

Anyway, the correct course of action for this ticket is to remove the (untracked?) top-level OSX README file, as far as I can tell.  How does one review this?


---

Comment by kcrisman created at 2010-04-22 02:31:06

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-04-22 11:00:27

One option might be to have a file ".README-OSX-binary.txt" for information about binaries, and README-OSX.txt for information about source. Then if one runs sage -bdist, it replace README-OSX.txt with .README-OSX-binary.txt

The fact the file starts with a dot, would tend to make it less obvious. Or perhaps have one file, but make it a bit clearer what is relevant to those using a binary distribution, and what is relevant to those using a source distribution. 

Dave


---

Comment by kcrisman created at 2010-04-22 13:04:42

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2010-04-22 13:04:42

Replying to [comment:5 drkirkby]:
> One option might be to have a file ".README-OSX-binary.txt" for information about binaries, and README-OSX.txt for information about source. Then if one runs sage -bdist, it replace README-OSX.txt with .README-OSX-binary.txt
> 

Except for the dot, that is a good idea, and maybe a not hard way to fix this.  Unfortunately, Macs automatically hide dot files in the Finder, and so most people would then have no README to see (unless they though to use ls -a in command line, which is not automatic for many). 

> The fact the file starts with a dot, would tend to make it less obvious. Or perhaps have one file, but make it a bit clearer what is relevant to those using a binary distribution, and what is relevant to those using a source distribution. 
> 

That is also a good solution.  I'll try to work on this over the next week - isn't hard, just have to find time to do it.


---

Comment by drkirkby created at 2010-04-22 15:42:12

Replying to [comment:6 kcrisman]:
> Replying to [comment:5 drkirkby]:
> > One option might be to have a file ".README-OSX-binary.txt" for information about binaries, and README-OSX.txt for information about source. Then if one runs sage -bdist, it replace README-OSX.txt with .README-OSX-binary.txt
> > 
> 
> Except for the dot, that is a good idea, and maybe a not hard way to fix this.  Unfortunately, Macs automatically hide dot files in the Finder, and so most people would then have no README to see (unless they though to use ls -a in command line, which is not automatic for many). 

That was my whole point about using a dot - it would not be found easily. 

If the information only relevant to those using a binary distribution was in a file starting with dot in the sources, then it would not be too obvious to those looking at the sources. 

It would only become apparent on a binary distribution, because the act of running 'sage -bdist' would have removed the dot. 

Dave


---

Comment by kcrisman created at 2010-04-22 17:54:13

Replying to [comment:7 drkirkby]:
> Replying to [comment:6 kcrisman]:
> > Replying to [comment:5 drkirkby]:
> > > One option might be to have a file ".README-OSX-binary.txt" for information about binaries, and README-OSX.txt for information about source. Then if one runs sage -bdist, it replace README-OSX.txt with .README-OSX-binary.txt
> > > 
> > 
> > Except for the dot, that is a good idea, and maybe a not hard way to fix this.  Unfortunately, Macs automatically hide dot files in the Finder, and so most people would then have no README to see (unless they though to use ls -a in command line, which is not automatic for many). 
> 
> That was my whole point about using a dot - it would not be found easily. 
> 
> If the information only relevant to those using a binary distribution was in a file starting with dot in the sources, then it would not be too obvious to those looking at the sources. 
> 
> It would only become apparent on a binary distribution, because the act of running 'sage -bdist' would have removed the dot. 

I understand now - I got confused by all the files and dots, sort of Dr. Seuss-esque.  I'll definitely look into this soon.


---

Comment by drkirkby created at 2010-04-22 18:44:58

Replying to [comment:8 kcrisman]:
> Replying to [comment:7 drkirkby]:
> > That was my whole point about using a dot - it would not be found easily. 
> > 
> > If the information only relevant to those using a binary distribution was in a file starting with dot in the sources, then it would not be too obvious to those looking at the sources. 
> > 
> > It would only become apparent on a binary distribution, because the act of running 'sage -bdist' would have removed the dot. 
> 
> I understand now - I got confused by all the files and dots, sort of Dr. Seuss-esque.  I'll definitely look into this soon.

It's one option, but I suspect a simpler one is to just have the one file be a bit more explicit about what is relevant to a source distribution, and what is relevant to a binary distribution. 

I'm not overly concerned whether it is done in one file, two files, or whether any files are semi-hidden by the use of a dot in front of their name. But the current version is rather confusing.


---

Comment by kcrisman created at 2010-04-28 18:51:51

Okay, this is mostly fixed by simply removing the README-osx file from the top directory.  There is no HG for this, so it has to be removed by hand.

The place the one in /local/bin is copied to is in fact the top directory in a dmg/tgz only when bdisted, which is definitely very appropriate for this file!    

So I don't think there is a need for any other changes, since any binary would be distributed with the OS X readme, but renamed to README.txt, in that very top directory, where anyone could read it.  They would only have to read the usual README.txt in the sage/ directory if they wanted that sort of information, in which case the information in the OS X README is superfluous (i.e., they know how to use Terminal already).  

Does that make any sense?  My point is we don't need a separate README for any other purpose.  I'm marking this needs review.  I'm putting myself as an "author", but since I didn't actually write anything, if the reviewer disagrees then they can just make me a reviewer.

To release manager: Upon positive review, remove the sage-README-osx.txt in the top directory, leave the one in local/bin/ alone!


---

Comment by kcrisman created at 2010-04-28 18:51:51

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-08-11 13:12:54

If #9433 is merged, this should probably get positive review and marked as merged.  Of course, one could just merge this first anyway, before revision control is implemented :)


---

Comment by jhpalmieri created at 2010-08-11 20:48:48

I'll give this a positive review.  To the release manager: delete the file sage-README-osx.txt in the top directory.

I think doing this won't have any effect on #9433.  If #9433 gets merged first, on the other hand, then this should automatically be taken care of.


---

Comment by jhpalmieri created at 2010-08-11 20:48:48

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-15 11:38:13

Resolution: fixed
