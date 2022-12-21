# Issue 5697: Sage 3.4.1.rc1: Downgrade GAP to 4.4.10

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-04-06 18:48:49

Assignee: mabshoff

GAP 4.4.12 on Itanium is horribly broken again, i.e. loading packages seems to be completely broken. Downgrade it!

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-06 18:48:54

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-04-19 03:47:50

To review this there are three components: 

 * an updated GAP 4.4.10.spkg that reverts to 4.4.10.p10 and on top makes sure to nuke all gap-4.4.* installs, i.e. including 4.4.12.
 * a patch reverting functional changes, i.e. the parts of #3337 where random_seed was used due to uspstream changes and reverting #5455 to not skip loading the workspace on Itaniums
 * a patch fixing all the doctests due to the above patch. Since #3337 was pre-ReST it was a little messy and some of the changes moved to different files, etc.

Cheers,

Michael


---

Attachment

Apply this patch first


---

Comment by mabshoff created at 2009-04-19 03:51:33

The updated SPKG can be found at 

   http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.1/rc4/gap-4.4.10.p11.spkg

Cheers,

Michael


---

Comment by wdj created at 2009-04-19 13:49:19

I assume that to test this (on an amd64 ubuntu machine) I should

(1) create a clone of 3.4.1.rc3

(2) install http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.1/rc4/gap-4.4.10.p11.spkg

(3) apply the patches trac_5697-doctest.patch and then trac_5697-functional.patch 

Is this correct?


---

Comment by mabshoff created at 2009-04-19 15:06:43

Replying to [comment:4 wdj]:
> I assume that to test this (on an amd64 ubuntu machine) I should
> 
> (1) create a clone of 3.4.1.rc3
> 
> (2) install http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.1/rc4/gap-4.4.10.p11.spkg
> 
> (3) apply the patches trac_5697-doctest.patch and then trac_5697-functional.patch 

As mentioned above first functional, then doctests.

> Is this correct?

Yes, modulo the patch order.

Cheers,

Michael


---

Comment by was created at 2009-04-19 19:51:24

* 1 the spkg works and with the two patches applied, all tests pass.


* Question: why do trac_5697-functional.patch?   It seems like all of that functionality would make sense and be food for any gap version (at least everything but the very last chunk).  Wasn't it just implementing the randgen framework correctly for GAP?   -- I'm ok with this, but we want the functionality back at some point, I think.

* The other changes look fine, in the other patch. 

Install the spkg ends with

```
make[1]: Leaving directory `/scratch/wstein/build/sage-3.4.1.rc2/spkg/build/gap-4.4.10.p11/src/pkg/guava3.4/src/leon'
cp: omitting directory `../../bin'
cp: cannot stat `cp': No such file or directory

real    1m17.533s
user    0m58.840s
sys     0m9.180s
Successfully installed gap-4.4.10.p11
```


That `cp: cannot stat `cp': No such file or directory` worries me. 

Fix or explain that, and this gets a positive review.


---

Comment by mabshoff created at 2009-04-19 22:52:46

re failure for `cp: cannot stat `cp': No such file` - it was also in the old spkg and everything it where it needs to be, i.e. doctests pass. Since rlm is working on code to replace all of guava I am not too worried since it will be gone soon anyway.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-19 23:36:09

Replying to [comment:6 was]:

> * Question: why do trac_5697-functional.patch?   It seems like all of that functionality would make sense and be food for any gap version (at least everything but the very last chunk).  Wasn't it just implementing the randgen framework correctly for GAP?   -- I'm ok with this, but we want the functionality back at some point, I think.

If we don't need to set the random_seed we should not set the random seed. Once GAP 4.4.12+ works as expected it should be more or less trivial to take the two patches and revert them. 

Cheers,

Michael


---

Comment by was created at 2009-04-20 00:51:26

Given the cp issue was there before... positive review.


---

Comment by mabshoff created at 2009-04-20 03:30:48

Merged both patches as well as the gap.spkg in Sage 3.4.1.rc4.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-20 03:30:48

Resolution: fixed
