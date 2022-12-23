# Issue 2054: prun is not preparsed -- potentially very confusing

Issue created by migration from https://trac.sagemath.org/ticket/2054

Original creator: was

Original creation time: 2008-02-05 14:31:08

Assignee: was

If one uses the Python profiler through Sage's Ipython command line, the input line is not preparsed, which is potentially very confusing.  E.g., this should print 256:


```
sage: %prun print 2^8
10
         2 function calls in 0.000 CPU seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

sage: 
```



---

Comment by was created at 2008-02-08 05:37:46


```
Fernando Perez to me
	
show details 9:15 PM (18 minutes ago)
	
	
	
Reply
	
	
Hi William,

On Feb 5, 2008 7:46 AM, William Stein <wstein@gmail.com> wrote:
> Fernando,
>
> Any hints about how I could make the argument to %prun get preparsed?

sorry for the delay, I just wanted to let you know that I don't have a
quick solution to this right now, and I'm swamped with moving/home
sale issues, so for a couple of weeks my coding time is reduced to
exactly zero.

I'll keep this in my inbox, starred, so once I get to Berkeley I can
fix it.  It's not difficult, I just don't have a spare hour right now
to code it and test it, sorry.

Cheers,

f
```



---

Attachment


---

Comment by mhansen created at 2010-02-02 19:53:53

Changing status from new to needs_review.


---

Comment by rossk created at 2010-02-09 10:36:39

Is this an error on my part?


```
/scratch/rossk/sage-4.3.2/devel/sage$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/2054/scripts_2054.patch
adding scripts_2054.patch to series file

/scratch/rossk/sage-4.3.2/devel/sage$ hg qpush
applying scripts_2054.patch
unable to find 'ipy_profile_sage.py' for patching
1 out of 1 hunks FAILED -- saving rejects to file ipy_profile_sage.py.rej
patch failed, unable to continue (try -v)
ipy_profile_sage.py: No such file or directory
patch failed, rejects left in working dir
errors during apply, please fix and refresh scripts_2054.patch
```



---

Comment by mhansen created at 2010-02-09 10:39:47

Hello,

You need to be in /scratch/rossk/sage-4.3.2/local/bin in order to be in the repository which the patch applies to.


---

Comment by rossk created at 2010-02-09 10:53:44

Replying to [comment:4 mhansen]:
> Hello,
> 
> You need to be in /scratch/rossk/sage-4.3.2/local/bin in order to be in the repository which the patch applies to.

Thanks - it installed and built ok :-) 

(I suppose look in the patch next time to know which folder I should be in?) 

Will run a few tests, do the doctests and hopefully we'll knock this one over soon.


---

Comment by rossk created at 2010-02-09 11:51:29

Tested the patch with a few statements that exercised the preparser. e.g.

```
sage: %prun 123456789123456789123456789123456789123456789123456789.factor()

sage: %prun print integrate(log(x)^(2^3),x)
```

Pre-patch statements like these crashed or gave incorrect answers if prefixed with "%prun ". 
Post-patch the statements give the same answers with or without "%prun" (and all doctests passed).
Positive review


---

Comment by rossk created at 2010-02-09 11:51:29

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-10 10:58:21

For the record: Applying the patch to Sage 4.3.2's scripts repository, I get

```
patching file ipy_profile_sage.py
Hunk #1 succeeded at 29 with fuzz 2 (offset 0 lines).
now at: scripts_2054.patch
```



---

Comment by mpatel created at 2010-02-11 15:12:25

Resolution: fixed
