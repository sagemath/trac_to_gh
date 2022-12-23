# Issue 3239: [with patch; needs review] cygwin polybori -- add Cygwin build support for polybori

Issue created by migration from https://trac.sagemath.org/ticket/3239

Original creator: was

Original creation time: 2008-05-17 17:03:47

Assignee: mabshoff

CC:  polybori

See also #3195: add 64 bit OSX build support for polybori

New spkg here:

http://sage.math.washington.edu/home/was/cygwin/polybori-0.3.1.p3.spkg


---

Attachment

Cygwin build fix


---

Comment by mabshoff created at 2008-05-18 13:47:02

Cygwin python.exe fix


---

Attachment

Spkg looks good to me. I checked in some diffs of all the patched files we use on Cygwin. I also attached those files to the ticket and added PolyBoRi to the CC field on this ticket so the changes can get cleaned up and integrated upstream [at least the SConstuct fix must be cleaned up].

In total: Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-18 13:49:59

Resolution: fixed


---

Comment by mabshoff created at 2008-05-18 13:49:59

Merged in Sage 3.0.2.alpha1


---

Comment by PolyBoRi created at 2008-05-18 22:56:00

Hi Michael,
could you check, whether SConstruct.generic.patch does the Job on cygwin? Also, the first part of the cpu_stats.c.patch could be avoided by setting the predefines more sensitive in the construct file. I'll have a look at that issue in the next days.
Best regards,
  Alexander


---

Comment by mabshoff created at 2008-05-18 23:17:08

Replying to [comment:3 PolyBoRi]:
> Hi Michael,
> could you check, whether SConstruct.generic.patch does the Job on cygwin? Also, the first part of the cpu_stats.c.patch could be avoided by setting the predefines more sensitive in the construct file. I'll have a look at that issue in the next days.
> Best regards,
>   Alexander

Hi Alexander,

that looks like a likely fix. Right now I don't have a Cygwin env setup up to test, but it won't take long. 

Re cpu_stats.c: it looks like the sledge hammer approach and we conditionally copy it into the PolyBoRi tree on Cygwin only. Any cleaner solution is appreciated and I plan to write some Win2K+ specific patches that uses the native Windows infrastructure for accounting and memory consumption. I already did so for CoCoALib, so it should be an easy fix.

Cheers,

Michael


---

Comment by PolyBoRi created at 2008-05-18 23:21:46

More generic patch, which obsoletes both patches above


---

Attachment

Hi Michael,
> that looks like a likely fix. Right now I don't have a Cygwin env setup up to test, but it won't take long. 
> 
> Re cpu_stats.c: it looks like the sledge hammer approach and we conditionally copy it into the PolyBoRi tree on Cygwin only. Any cleaner solution is appreciated and I plan to write some Win2K+ specific patches that uses the native Windows infrastructure for accounting and memory consumption. I already did so for CoCoALib, so it should be an easy fix.
I've uploaded an extended version of the patch, which should fix both problems from SConstruct, so the cpu_stats.c patch will be obsolete.

Best regards,
  Alexander
