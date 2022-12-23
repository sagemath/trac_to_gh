# Issue 9151: build multithreaded version of ATLAS

Issue created by migration from https://trac.sagemath.org/ticket/9151

Original creator: kilian

Original creation time: 2010-06-05 17:23:31

Assignee: GeorgSWeber

CC:  jdemeyer

Keywords: ATLAS BLAS LAPACK multi-threading pthreads

Hi,

I noted that multi-threading in ATLAS is switched off by default (switch -t 0). I was wondering if it wouldn't be better to make a multi-threaded build the default, since it results in big performance increases on most modern computers.

I attached a patch that enables threading. It works fine for me on a multi-core Linux machine. I tried to make it work for single-core machines (for which atlas might turn of threading automatically) by testing for the presence of the threaded version of the BLAS library before running the make command that builds the shared atlas library. However I haven't tested it on a single-core machine.

Kilian


---

Attachment

enables multi-threaded build in atlas-3.8.3.p12.spkg


---

Comment by kilian created at 2010-06-08 16:03:23

Hi,

It would be great if this patch would make it into the next release. I tested it on Linux 32bit and 64bit, single and multi core, Intel and AMD. On the 8 core machine, it increased the speed of e.g. a matrix dot product about 4-fold, and it didn't break the single-threaded build on the one-core machine. 

Kilian


---

Comment by jpflori created at 2013-04-05 15:42:49

Changing status from new to needs_review.


---

Comment by jpflori created at 2013-04-05 15:42:49

Superseded by #10508.


---

Comment by tscrim created at 2013-04-07 17:07:28

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-04-10 08:06:59

Resolution: duplicate
