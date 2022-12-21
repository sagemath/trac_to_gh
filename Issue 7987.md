# Issue 7987: Most extensions don't need to be listed in module_list

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-01-19 01:49:00

Assignee: GeorgSWeber

CC:  was mhansen jason leif

Unless special libraries or C flags are needed, we can auto-generate almost this whole list, which simplifies the making of new .pyx files in the standard library.


---

Comment by robertwb created at 2010-01-19 01:51:05

Changing status from new to needs_review.


---

Comment by robertwb created at 2010-01-19 01:51:05

Eventually, the library, include, and language information should be able to be pulled out of the files themselves by Cython...


---

Attachment


---

Comment by robertwb created at 2010-02-21 02:11:20

Eventually, this should be part of Cython. Also, clang, clib, etc. should be allowed in .pxd files and be transitive (for example, everything using Pynac or NTL would automatically be C++ and get the right library).


---

Comment by robertwb created at 2010-04-25 06:32:35

I will probably implement something like this in Cython directly, though of course heavily inspired by what we want for Sage.


---

Comment by leif created at 2010-06-03 00:04:59

Changing status from needs_review to needs_work.


---

Comment by leif created at 2010-06-03 00:04:59

Not surprising (see ticket description), the patches need to be rebased.

The merged Cygwin patch involved many changes to `module_list.py`, too.

Btw, IMHO `libcsage` and `libstdcxx` should *not* be "linked" unconditionally (especially regardless of the module's `language`) to each and every module.
(I recently started sorting out which modules really directly use `libcsage`, and did add `"stdcxx"` to `libraries` only if `language=="c++"`. Currently suspended work in progress...)


---

Comment by robertwb created at 2010-06-03 00:21:43

Replying to [comment:7 leif]:

> Btw, IMHO `libcsage` and `libstdcxx` should *not* be "linked" unconditionally (especially regardless of the module's `language`) to each and every module.
> (I recently started sorting out which modules really directly use `libcsage`, and did add `"stdcxx"` to `libraries` only if `language=="c++"`. Currently suspended work in progress...)

For sure, but I figured it'd be better to refractor and clean things up in separate steps (in case one or the other has unintended consequences). 

For the record, I plan to add this functionality to Cython soon (including transitivity of library dependance), so that may make this patch invalid. Sorting what modules actually need what will be very useful though.


---

Comment by leif created at 2010-06-03 01:03:23

Replying to [comment:8 robertwb]:
> Replying to [comment:7 leif]:
> 
> > Btw, IMHO `libcsage` and `libstdcxx` should *not* be "linked" unconditionally (especially regardless of the module's `language`) to each and every module.
> > (I recently started sorting out which modules really directly use `libcsage`, and did add `"stdcxx"` to `libraries` only if `language=="c++"`. Currently suspended work in progress...)
> 
> For sure, but I figured it'd be better to refractor and clean things up in separate steps (in case one or the other has unintended consequences).

Yes. The unconditional inclusion is anyhow performed in `setup.py`. 

> For the record, I plan to add this functionality to Cython soon (including transitivity of library dependance), so that may make this patch invalid. Sorting what modules actually need what will be very useful though. 

I just wanted to decrease the number of tickets needing review. ;-)

P.S.: `s/stdcxx/stdc++/`


---

Comment by leif created at 2013-03-15 09:33:59

Changing status from needs_work to needs_info.


---

Comment by jdemeyer created at 2015-04-13 07:25:31

Changing status from needs_info to needs_work.


---

Comment by leif created at 2015-04-13 09:54:13

Replying to [ticket:7987 jdemeyer]:
> See also #15140.

Sure?


---

Comment by leif created at 2015-04-13 09:54:13

Changing type from defect to enhancement.


---

Comment by jdemeyer created at 2015-06-24 11:41:39

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2015-06-24 11:41:39

This is way too outdated to apply, it also incorrectly adds the libraries to `.pyx` files instead of `.pxd` files (see #18450) and several parts of this have already been done.


---

Comment by vbraun created at 2015-07-17 20:05:59

Resolution: fixed
