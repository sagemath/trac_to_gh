# Issue 9273: doctest elliptic_curves/BSD.py reports "file not found"

Issue created by migration from https://trac.sagemath.org/ticket/9273

Original creator: drkirkby

Original creation time: 2010-06-19 16:01:10

Assignee: cremona

CC:  robertwb rlm was jhpalmieri

#9127 was supposed to fix this, but it seems the fix is not complete. 

## Hardware & associated software

 * Sun Blade 1000
 * 2 x 900 MHz UltraSPARC III+ CPUs
 * 2 GB RAM
 * Solaris 10 03/2005 (first release of Solaris 10)
 * gcc 4.4.3 (uses Sun linker and assembler)

 == Sage version ==
 * 4.4.4.alpha1


 == The error ==

```
sage -t  -long devel/sage/sage/calculus/riemann.pyx
         [712.7 s]

-------------------------------------------------------------

The following tests failed:

        sage -t  -long devel/sage/sage/schemes/elliptic_curves/BSD.py # File not found
-------------------------------------------------------------
Total time for all tests: 33947.4 seconds
```



---

Comment by rlm created at 2010-06-22 16:12:19

This has nothing to do with the file `BSD.py`. It is a bug in the doctesting code, which is triggered (as William tells me) by lag times on file systems and the like. It starts testing before the doctesting file is created.

Did you try running the tests again?


---

Comment by drkirkby created at 2010-06-22 16:35:07

Replying to [comment:2 rlm]:
> This has nothing to do with the file `BSD.py`. It is a bug in the doctesting code, which is triggered (as William tells me) by lag times on file systems and the like. It starts testing before the doctesting file is created.
> 
> Did you try running the tests again?

I run that test more than once and it failed more than once. 

Note although the machine is rather old (900 MHz CPUs), the disks are local, with a 2 Gbit/s fibre channel interface and 15,000 rpm, so the disk performance is probably better than most modern PCs. If the disks were on a NFS file system, I could perhaps understand that, but it seems unlikely with local disks like this. 

I managed to mess up my build (started a 64-bit build in the same directory as the 32-bit one!), so are rebuilding now. I'll try again once complete. 

Dave


---

Comment by drkirkby created at 2010-06-22 17:35:06

I just updated the technical details of the hardware in the description. I usually put the details, but not normally the disks. But in this case I thought it prudent to add it.


---

Comment by drkirkby created at 2010-06-23 00:15:46

I've rebuilt this and tried BSD.py and it passes each time. I've no idea what the underlying problem may be, but the doc test has passed several times now. 

Dave


---

Comment by rlm created at 2010-06-23 02:55:56

Then I suggest we close this ticket.

Is there a ticket for the "file not found" issue in general? It would be nice if there were a way to reproduce the issue...


---

Comment by drkirkby created at 2010-06-25 07:03:03

There is a ticket for "file not found" - see #9316.

The assumption being made on that ticket is that the real cause of the "file not found" message is a timeout. John Cremona says 

_The reason for the timeout was simply that I suspended my laptop for a couple of hours and then woke it up._

I'm personally not convinced that is the reason this test has failed for me. When BSD.py passes, it does so in around 205 seconds. SAGE_TIMEOUT is set to 1000 seconds and SAGE_TIMEOUT_LONG is set to 10000 seconds. Since the BSD.py test is marked as long, it would need to slow down by a factor of 48 (10000/205) before causing a timeout. My SPARC is quite and old machine and does not go to sleep in the same way some computers do. 

There appears to be another test which is randomly failing in a different way - see #9310. 

I don't know what the cause(s) are but I'm less than convinced this is due to delays on file systems or processors going to sleep. 

I think the ticket should remain open until such time as it gets resolved. Being random in nature, it might not be easy to resolve.


---

Comment by zimmerma created at 2011-09-16 13:52:27

Changing keywords from "" to "ecc2011".


---

Comment by zimmerma created at 2011-09-16 13:52:27

David, does this problem still happen?

Paul


---

Comment by zimmerma created at 2011-09-16 13:52:27

Changing status from new to needs_info.


---

Comment by jdemeyer created at 2013-02-28 16:08:10

Changing status from needs_info to needs_review.


---

Comment by jdemeyer created at 2013-02-28 16:08:10

I have never seen this problem and in any case, the doctesting framework will be rewritten completely: #12415.


---

Comment by jdemeyer created at 2013-02-28 16:08:17

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-03-07 08:17:35

Resolution: invalid
