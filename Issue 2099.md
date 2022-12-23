# Issue 2099: Make sage-test execute multiple doctests in parallel

Issue created by migration from https://trac.sagemath.org/ticket/2099

Original creator: ncalexan

Original creation time: 2008-02-08 04:40:23

Assignee: ncalexan

CC:  ncalexander@gmail.com

Keywords: sage test doctest multiple parallel

It would greatly speed testing if `sage-test` doctested multiple files in parallel.


---

Comment by ncalexan created at 2008-02-08 04:41:44

Mike Abshoff suggested a short document explaining how the current doctesting system is organized.  I have attached a preliminary version of this document.


---

Attachment


---

Attachment


---

Comment by ncalexan created at 2008-02-09 02:36:51

The patch `ncalexan-parallel-testing-1.hg` applies to `hg_scripts` in `local/bin`.


---

Attachment


---

Comment by ncalexan created at 2008-02-10 11:07:53

`2099-ncalexan-parallel-testing-2.hg` should not depend on the earlier bundle.

This is a work in progress bundle that improves option parsing and makes 'test via make' the only option.  It improves `sage-doctest` slightly and tries to write a `Makefile.doctest` that can be run via command-line `make`.

Use two dashes (`--`) for options.

Output is not yet collated.  Timeouts are not yet implemented.


---

Attachment

`2099-ncalexan-parallel-testing-3.hg` should not depend on earlier bundles.

This is a work in progress bundle that adds
 * working per-test timeouts
 * parsing SAGE_DOCTEST_OPTIONAL, _LONG, _TIMEOUT from the environment
 * output via -o OUTFILE
 * improves handling of sage-doctest crashing


```
[5:25pm] ncalexan: mabshoff: I have parallel testing with output and timeout working, or mostly working.
[5:25pm] mabshoff: ncalexan: cool
[5:26pm] ncalexan: mabshoff: I can't think of a way to get partial output correct.  You can display it while it comes, but if you don't wait until the entire test is done, you won't get the sorted output.
[5:26pm] ncalexan: I'll post another bundle.
[5:26pm] ncalexan: Use -v for verbose, -q for quiet, -o OUTFILE.
[5:26pm] ncalexan: (All to sage-test or sage -t)
```



---

Comment by gfurnish created at 2008-03-02 23:05:25

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-03-02 23:05:25

Changing assignee from ncalexan to gfurnish.


---

Comment by gfurnish created at 2008-03-03 02:13:15

This creates sage-ptest for parallel test.  The first argument is equivalent to -j (the number of parallel tests to run).  The rest of the arguments are as normal.


---

Comment by gfurnish created at 2008-03-03 02:14:35

sage-ptest


---

Attachment

trac_2999.patch replaces all the other patches (with the exception of a minimal fix to `sage -test`. I give it a positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-03 04:55:40

Resolution: fixed


---

Comment by mabshoff created at 2008-03-03 04:55:40

Merged in Sage 2.10.3.rc1
