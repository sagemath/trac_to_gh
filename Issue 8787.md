# Issue 8787: upgrade the openssl optional spkg to version 1.0

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-04-27 23:02:19

Assignee: tbd

CC:  schilly

Amazingly, openssl released version *1.0*! Let's upgrade to this.


---

Comment by was created at 2010-04-27 23:14:52

Here is the spkg:

http://wstein.org/home/wstein/patches/openssl-1.0.0.spkg

I fixed things to be "modern" and up to snuff -- a formatted SPKG.txt file, a .hg directory, error messages not all messed up in spkg-install, a src/ directory, etc.


---

Comment by was created at 2010-04-27 23:14:52

Changing status from new to needs_review.


---

Comment by mariah created at 2010-05-05 15:32:25

Changing status from needs_review to needs_work.


---

Comment by mariah created at 2010-05-05 15:32:25

Sadly, building sage-4.3.5 with gcc-4.4.3 and openssl-1.0.0.spkg 
did NOT work on one of my company's computers (not connected to
the Internet).  The machine is similar hardware to Skynet/taurus, 
but running Red Hat Enterprise Linux Server.

First I installed openssl-1.0.0.spkg.  Then I did 'make testlong'.
The build failed while trying to build python-2.6.4.p7 with the
message
  
  import _md5
Import Error: No module named _md5
hashlib module failed to import


---

Comment by was created at 2010-05-05 15:42:36

Replying to [comment:3 mariah]:
> Sadly, building sage-4.3.5 with gcc-4.4.3 and openssl-1.0.0.spkg 
> did NOT work on one of my company's computers (not connected to
> the Internet).  The machine is similar hardware to Skynet/taurus, 
> but running Red Hat Enterprise Linux Server.
> 
> First I installed openssl-1.0.0.spkg.  Then I did 'make testlong'.
> The build failed while trying to build python-2.6.4.p7 with the
> message

Can you post the log that results from doing

  sage -f openssl-1.0.0

and also the log that results from building python, e.g.,

  sage -f python-2.6.4.p7


Also, did you get this failure on taurus?  If so, I can just test there.


---

Comment by mariah created at 2010-05-05 15:56:11

> Can you post the log that results from doing
> 
>   sage -f openssl-1.0.0
> 
> and also the log that results from building python, e.g.,
> 
>   sage -f python-2.6.4.p7

I do not believe I am allowed to export the logs.
This problem is happening on one of our internal 
company machines.

> Also, did you get this failure on taurus?  If so, I can just test there.

I tried to reproduce the problem on taurus, but sadly the 
problem does NOT seem to be reproducible on taurus.


---

Comment by mariah created at 2010-05-27 14:23:29


```
I have investigated the problem and found that 
the reason for the failure is that openssl-1.0.0
puts libraries in $SAGE_ROOT/local/lib64 on 64-bit 
machines. Sage does not add $SAGE_ROOT/local/lib64
to the LD_LIBRARY_PATH.

If you add

  --libdir=lib

to the ./config line in spkg-install, then sage
builds with openssl-1.0.0 and all tests pass.
```



---

Comment by was created at 2010-06-04 05:29:54

I've posted a new spkg with the fix you suggest here:

   http://wstein.org/home/wstein/patches/openssl-1.0.0.p0.spkg


---

Comment by was created at 2010-06-04 05:29:54

Changing status from needs_work to needs_review.


---

Comment by mariah created at 2010-06-09 14:23:36

Changing status from needs_review to positive_review.


---

Comment by mariah created at 2010-06-09 14:23:36

On the machine where I previously was having problems, 
openssl-1.0.0.p0.spkg builds and 'make testlong' on
sage-4.4.3 passes all tests.

Thus I give this package a positive review!


---

Comment by rlm created at 2010-07-08 18:57:45

Resolution: fixed
