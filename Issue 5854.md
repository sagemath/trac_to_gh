# Issue 5854: [with patch, with spkg, needs review] Include Michael Stoll's ratpoints in Sage

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2009-04-22 15:17:52

Assignee: was

CC:  cremona

The spkg is located here:

http://sage.math.washington.edu/home/rlmill/ratpoints-2.1.1.spkg

(The final version for review was created 22 April 2009-- there were previous versions by the same file name, but this one can be identified as the one possessing an SPKG.txt file.)


---

Attachment


---

Comment by mabshoff created at 2009-04-22 18:49:27

This spkg needs a formal vote and some more widespread testing. I am also curious about the MSVC build, but we can try that in person.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-22 18:52:29

Another thing: Why is the dependency on the header commented out?:

```
 	386	    Extension('sage.libs.ratpoints', 
 	387	              sources = ["sage/libs/ratpoints.pyx"], 
 	388	              #depends = [SAGE_ROOT + 'local/include/ratpoints.h'], 
 	389	              libraries = ["ratpoints", "gmp"]),
```

And another question: What is the long term plan here with eclib? Will it use ratpoints in the future?

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-22 19:16:50

And while I am at it:

 * SPKG.txt is missing the license section. Since the code is GPL V2+ again now it would be nice to mention
 * src is under version control - any reason to do that in the spkg since this should be clean upstream? Given the size I don't mind too much, but it is unusual.  
 * there is one PDF in src that isn't in the repo - in case we want src under hg you should put that PDF in .hgignore.

Cheers,

Michael


---

Comment by rlm created at 2009-04-22 20:46:34

* SPKG.txt was based directly on the one for eclib, so anything wrong with this one will be wrong with that one too.
 * `src` was under version control originally because I found a bug and fixed it, but Michael Stoll has merged that fix upstream. I suppose there's no reason now.
 * The depends line is commented out to demonstrate that it is automatically picked up somewhere, and thus not needed...


---

Comment by mabshoff created at 2009-04-22 21:47:50

Replying to [comment:4 rlm]:
>  * SPKG.txt was based directly on the one for eclib, so anything wrong with this one will be wrong with that one too.

Yes, that needs to be fixed, too.

>  * `src` was under version control originally because I found a bug and fixed it, but Michael Stoll has merged that fix upstream. I suppose there's no reason now.

Good. Can you post an SPKG that has a clean .hg and .hgignore, i.e. just get rid of the old .hg and check the relevant bits back in again.

>  * The depends line is commented out to demonstrate that it is automatically picked up somewhere, and thus not needed...

Hmmm, does rebuilding the spkg lead to "sage -b" rebuilding the extension? That does surprise me and I would be curious what this triggers.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-22 21:50:38

Since this ticket is relevant to eclib (I believe in sage-nt John mentioned that he had looked into using ratpoints from eclib again and that the current library interface worked, but my collection is a little hazy here) I am CCing him to keep him uptodate on this development. Once ratpoints is in Sage I consider it desirable to use the library from eclib unless there is some unforeseen technical reason not to do it.

Cheers,

Michael


---

Comment by cremona created at 2009-04-23 08:27:55

Replying to [comment:6 mabshoff]:
> Since this ticket is relevant to eclib (I believe in sage-nt John mentioned that he had looked into using ratpoints from eclib again and that the current library interface worked, but my collection is a little hazy here) I am CCing him to keep him uptodate on this development. Once ratpoints is in Sage I consider it desirable to use the library from eclib unless there is some unforeseen technical reason not to do it.
> 
> Cheers,
> 
> Michael

Thanks.  It is not quite as easy as that, and one part of eclib will need to be rewritten to use this library, but it has all the ingredients which I needs so that is possible and would only take a day or too.  That would also mean that *either* I put in a compiler switch to eclib Makefiles to tell it to use ratpoints instead of its own code, *or* I rely on ratpoints for ever, which gives people who download mwrank by itself will have something else they need to install first (as well as NTL and pari).


---

Comment by cremona created at 2009-04-29 11:46:23

What is the correct procedure for testing this.  Is it: (1) install the spkg using "sage -f" (2) apply the patch to a clone and do "sage -b" (3) do a "sage -t" on sage/libs/ratpoints.pyx (and try the functions in there at will) ?


---

Comment by rlm created at 2009-04-29 14:53:02

Replying to [comment:8 cremona]:

Mostly:

> (and try the functions in there at will) ?

Someone should run a valgrind session to check my code and Michael Stoll's code both for leaks. I'll try to get to this today or tomorrow.


---

Comment by cremona created at 2009-04-29 15:54:34

Partial review:  I ran valgrind on ratpoints's own test function and it does reasonably well:

```
masgaj`@`host-56-150%valgrind ./rptest > rptest.out
==4873== Memcheck, a memory error detector.
==4873== Copyright (C) 2002-2007, and GNU GPL'd, by Julian Seward et al.
==4873== Using LibVEX rev 1804, a library for dynamic binary translation.
==4873== Copyright (C) 2004-2007, and GNU GPL'd, by OpenWorks LLP.
==4873== Using valgrind-3.3.0, a dynamic binary instrumentation framework.
==4873== Copyright (C) 2000-2007, and GNU GPL'd, by Julian Seward et al.
==4873== For more details, rerun with: -v
==4873==
==4873==
==4873== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 5 from 1)
==4873== malloc/free: in use at exit: 11,204 bytes in 44 blocks.
==4873== malloc/free: 91,051 allocs, 91,007 frees, 2,895,144 bytes allocated.
==4873== For counts of detected errors, rerun with: -v
==4873== searching for pointers to 44 not-freed blocks.
==4873== checked 128,328 bytes.
==4873==
==4873== LEAK SUMMARY:
==4873==    definitely lost: 11,176 bytes in 37 blocks.
==4873==      possibly lost: 0 bytes in 0 blocks.
==4873==    still reachable: 28 bytes in 7 blocks.
==4873==         suppressed: 0 bytes in 0 blocks.
==4873== Rerun with --leak-check=full to see details of leaked memory.
```


Perhaps Michael (A) can say whether the leak is significant?  If so we could ask Michael (S) to fix it.


---

Comment by rlm created at 2009-04-29 15:59:25

John,

Since you've been using Michael Stoll's test suite, do you think you could make an `spkg-check` for this spkg which runs these?


---

Comment by rlm created at 2009-04-29 16:02:49

PS - Any leaks in "definitely lost" is never good...

Can you attach/link to the full valgrind logs?


---

Comment by cremona created at 2009-04-29 16:15:42

Replying to [comment:12 rlm]:
> PS - Any leaks in "definitely lost" is never good...
> 
> Can you attach/link to the full valgrind logs?

I will if you tell me what flags to put on the valgrind command line....


---

Comment by rlm created at 2009-05-21 15:52:32

Build works on Sage-3.4.2, but not on Sage-4.0.alpha0. Build log is attached.


---

Comment by rlm created at 2009-05-22 05:55:00

The build issues seem resolved in Sage-4.0.rc0.


---

Comment by cremona created at 2009-06-19 20:24:22

I checked that the spkg installs fine on 4.0.2 and the patch applies and tests pass.

There were some other issues raised by mabshoff, but as I am not an expert on spkgs I do not know if these are enough to stop the ticket from being merged.  So I am giving it a positive review.


---

Comment by rlm created at 2009-06-19 21:34:51

Wait, there are still memory leaks in 2.1.1. I will update the spkg to 2.1.2 (which fixes the leaks we found at Dagstuhl) in the next few days, once I get some time to do so.


---

Comment by rlm created at 2009-06-19 23:20:30

Latest version is at:

http://sage.math.washington.edu/home/rlmill/ratpoints-2.1.2.spkg

It also addresses the issues raised by mabshoff.

John-- Can you sign off on this?


---

Comment by cremona created at 2009-06-20 08:57:25

New spkg built fine for me, and the patch passed tests.


---

Comment by cremona created at 2009-06-22 14:10:18

I have been using this for real as I try to fix #6381, since this should make it very much faster to find integral points in an interval.  But for that we need to expose the parameter b_high to the sage function ratpoints().  So I am adding to the patch to allow this.


---

Comment by rlm created at 2009-07-02 22:00:28

Resolution: fixed
