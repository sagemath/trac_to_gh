# Issue 2483: [with updated spkg] Currently R help does not work

Issue created by migration from Trac.

Original creator: jkantor

Original creation time: 2008-03-12 08:05:26

Assignee: jkantor

Keywords: R

I was looking into the R pexpect interface and noticed that the R help system is totally broken for us. 

However, adding 

make vignettes 

to the R spkg-install fixed this. According to the R website this is for some reason necessary for 
builds based on the subversion source. 

http://sage.math.washington.edu/home/jkantor/spkgs/r-2.6.1.p15.spkg

With the old package in R, ?mean returned garbage. Now it returns the documentation.



---

Comment by mabshoff created at 2008-03-14 14:48:49

Positive review, i.e. the help system now works. But I had to do a couple things:

 * add and SPKG.txt entry for the new version
 * commit outstanding changes in the main hg repo

The new spkg can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.4/alpha0/r-2.6.1.p15.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-14 14:52:52

Merged in Sage 2.10.4.alpha0


---

Comment by mabshoff created at 2008-03-14 14:52:52

Resolution: fixed
