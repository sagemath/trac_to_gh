# Issue 5217: update libpng to 1.2.34

Issue created by migration from https://trac.sagemath.org/ticket/5217

Original creator: mabshoff

Original creation time: 2009-02-09 12:25:13

Assignee: mabshoff

This is also a security issue and we are shipping quite an outdated libpng. So update it.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-09 12:25:18

Changing status from new to assigned.


---

Comment by wdj created at 2009-02-11 20:58:18

If you interested in help from me on this, I am willing to try. (After the problems with GAP, I'll understand if you want to pass on the offer:-)


There re two tarballs in the source section of http://www.libpng.org/pub/png/libpng.html
(with config and without). Which one did you get last time?


Also, the wiki page of lists of packages has libpng listed under png. Is this confusing?


---

Comment by mabshoff created at 2009-02-11 21:05:07

Replying to [comment:2 wdj]:

Hi David,

> If you interested in help from me on this, I am willing to try. (After the problems with GAP, I'll understand if you want to pass on the offer:-)

I have things more or less ready to go for libpng, bzip2 and the Python upgrade, but thanks for the offer.

The GAP.spkg is a lot more complex than any of the above and hopefully it will be a lot smoother in the future. After the initial learning curve had been climbed the quality of your GAP.spkg did improve enough so I did not need to change anything, but any ticket with 50 comments didn't go well :). I have been rather busy and under pressure to get 3.3 out the last 10 days or so, so my comments might not have always been as appropriate as they should have been, so sorry if I did flame you.

I still want to get the GAP.spkg into 3.3, so I will work on the warning issues later. 
 
> There re two tarballs in the source section of http://www.libpng.org/pub/png/libpng.html
> (with config and without). Which one did you get last time?
 
I need to look it up.
 
> Also, the wiki page of lists of packages has libpng listed under png. Is this confusing?

Well, what we currently do is certainly inconsistent, but given that the name is libpng.spkg it should be changed.

Cheers,

Michael


---

Comment by wdj created at 2009-02-11 22:40:22

> my comments might not have always been as appropriate 
> as they should have been, so sorry if I did flame you. 

Don't worry - I always wear frame-retardent material while at the keyboard:-) It was probably deserved anyway - garbage at work kept me from focusing.

>>   There re two tarballs in the source section of 
>> http://www.libpng.org/pub/png/libpng.html  (with 
>> config and without). Which one did you get last time?

> I need to look it up. 


For the future, if you be more specific in SPKG.txt about which tarball gets downloaded and how it is pre-processed before creating the spkg, I (or someone else) could help out in the future. 


Generally, I'm happy to help with group theory (eg, GAP), coding theory (though actually I want to *remove* guava), and image-processing (such as libpng and PIL), if you can use a hand.


---

Comment by mabshoff created at 2009-02-11 23:15:46

Replying to [comment:4 wdj]:

Hi David,

> Don't worry - I always wear frame-retardent material while at the keyboard:-) It was probably deserved anyway - garbage at work kept me from focusing.

Well, I certainly won't claim you deserved it. But then an occasional rude email can make people pay attention to the problem :)
 

 > For the future, if you be more specific in SPKG.txt about which tarball gets downloaded and how it is pre-processed before creating the spkg, I (or someone else) could help out in the future. 

Absolutely. I never upgraded the libpng.spkg and it shows, i.e. I tend to write a cleaned up and complete SPKG.txt so that it is easier for other people to upgrade. It also works as a great reminder for myself when I have to revisits spkgs. I have only changed small things like C flags in spkg-install, but never took the time required to truly clean up SPKG.txt in libpng.spkg. That is why I also insisted so much on the SPKG.txt for GAP having all the details you mentioned on the ticket. 

And the cleaned up SPKG.txt have all ended in the wiki where sooner or later the plan is to automatically extract the info before each release and make it part of the Spkg chapter/appendix in the developer's manual. But that will be post-ReST like so many things.

> Generally, I'm happy to help with group theory (eg, GAP), coding theory (though actually I want to *remove* guava), and image-processing (such as libpng and PIL), if you can use a hand.

I think we will include PIL sooner or later.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-16 04:55:25

The spkg at

 http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc1/libpng-1.2.34.spkg

does the update. Note that you need various other spkgs to keep a working tree:

 * #4774 (in 3.3.rc1)
 * #5265 (in 3.3.rc1)
 * #5277 (needs review)


---

Comment by mhampton created at 2009-02-16 11:09:08

This works for me on an intel mac running 10.5.6.  I plotted and saved various 2d graphics objects.  Also tested tachyon with the new spkg, no problems seen.


---

Comment by mabshoff created at 2009-02-16 11:22:25

Resolution: fixed


---

Comment by mabshoff created at 2009-02-16 11:22:25

Merged in Sage 3.3.rc1.

Cheers,

Michael
