# Issue 9464: R depends on Fortran, but has no such dependancy in spkg/standard/deps

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-07-09 12:38:51

Assignee: GeorgSWeber

CC:  rlm jhpalmieri mpatel

In the sage-4.5.alpha4 code, the $SAGE_ROOT/spkg/standard/deps file has this entry for R:


```
$(INST)/$(R): $(BASE) $(INST)/$(PYTHON) $(INST)/$(ATLAS) $(INST)/$(ICONV)
        $(INSTALL) "$(SAGE_SPKG) $(R) 2>&1" "tee -a $(SAGE_LOGS)/$(R).log"
```


Note, there is no Fortran dependency listed, yet R does have Fortran files:


```
drkirkby`@`hawk:~/sage-4.5.alpha4/spkg/standard$ find r-2.10.1.p2 -name '*.f'
r-2.10.1.p2/src/src/library/stats/src/stxwx.f
r-2.10.1.p2/src/src/library/stats/src/sgram.f
r-2.10.1.p2/src/src/library/stats/src/bsplvd.f
r-2.10.1.p2/src/src/library/stats/src/stl.f
r-2.10.1.p2/src/src/library/stats/src/hclust.f
r-2.10.1.p2/src/src/library/stats/src/sslvrg.f
r-2.10.1.p2/src/src/library/stats/src/qsbart.f
r-2.10.1.p2/src/src/library/stats/src/bvalue.f
r-2.10.1.p2/src/src/library/stats/src/loessf.f
r-2.10.1.p2/src/src/library/stats/src/lminfl.f
r-2.10.1.p2/src/src/library/stats/src/kmns.f
r-2.10.1.p2/src/src/library/stats/src/eureka.f
r-2.10.1.p2/src/src/library/stats/src/sinerp.f
r-2.10.1.p2/src/src/library/stats/src/bvalus.f
r-2.10.1.p2/src/src/library/stats/src/ppr.f
r-2.10.1.p2/src/src/library/stats/src/portsrc.f
r-2.10.1.p2/src/src/appl/dchdc.f
r-2.10.1.p2/src/src/appl/chol.f
r-2.10.1.p2/src/src/appl/dqrsl.f
r-2.10.1.p2/src/src/appl/dqrdc2.f
r-2.10.1.p2/src/src/appl/eigen.f
r-2.10.1.p2/src/src/appl/dpoco.f
r-2.10.1.p2/src/src/appl/dposl.f
r-2.10.1.p2/src/src/appl/dpbfa.f
r-2.10.1.p2/src/src/appl/dtrco.f
r-2.10.1.p2/src/src/appl/dtrsl.f
r-2.10.1.p2/src/src/appl/ch2inv.f
r-2.10.1.p2/src/src/appl/dpofa.f
r-2.10.1.p2/src/src/appl/dqrutl.f
r-2.10.1.p2/src/src/appl/dqrdc.f
r-2.10.1.p2/src/src/appl/dpbsl.f
r-2.10.1.p2/src/src/appl/dpodi.f
r-2.10.1.p2/src/src/appl/dqrls.f
r-2.10.1.p2/src/src/appl/dsvdc.f
r-2.10.1.p2/src/src/modules/lapack/dlapack4.f
r-2.10.1.p2/src/src/modules/lapack/vecLibg95f.f
r-2.10.1.p2/src/src/modules/lapack/dlapack3.f
r-2.10.1.p2/src/src/modules/lapack/dlapack2.f
etc
```


I'll upload a patch and deps file

Dave 




---

Comment by rlm created at 2010-07-09 13:01:41

This looks like the cause of #9435


---

Comment by rlm created at 2010-07-09 13:01:41

Changing priority from major to blocker.


---

Comment by drkirkby created at 2010-07-09 14:46:05

$SAGE_ROOT/spkg/standard/deps to force Fortran to build before R


---

Attachment

Diff between $SAGE_ROOT/spkg/standard/deps and that is sage-4.5.alpha4


---

Comment by jhpalmieri created at 2010-07-09 15:10:09

This change to deps seems fine -- making the dependencies explicit seems like a good idea -- but note that fortran is a dependency of lapack, lapack is a dependency of atlas, and atlas is a dependency of R.  So fortran should always get installed before R even without this change.  Have you seen otherwise?


---

Comment by drkirkby created at 2010-07-09 16:49:47

Replying to [comment:2 jhpalmieri]:
> This change to deps seems fine -- making the dependencies explicit seems like a good idea -- but note that fortran is a dependency of lapack, lapack is a dependency of atlas, and atlas is a dependency of R.  So fortran should always get installed before R even without this change.  Have you seen otherwise?

I've personally not seen a problem. 

I must admit I did not look carefully to see the Fortran/LAPACK/ATLAS/R dependency. But Robert thought it was the cause of an OS X problem (see #9435), so upgraded this ticket to blocker. I think you have rather dashed that hope however! 

Dave


---

Comment by drkirkby created at 2010-07-09 16:49:47

Changing status from new to needs_review.


---

Comment by rlm created at 2010-07-13 15:41:32

Changing priority from blocker to minor.


---

Comment by leif created at 2010-08-19 00:03:07

This change is now incorporated in #9761, which already has positive review, *so this ticket can be closed as duplicate*.

Mitesh, that's your job... ;-)


---

Comment by mpatel created at 2010-08-19 01:55:21

I'm changing the status to "positive review," so that the release mixer/masher/manager/monster will see it at report {11} or {32} and close this ticket as a "duplicate" after merging #9761.


---

Comment by mpatel created at 2010-08-19 01:55:21

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-08-24 02:52:06

Resolution: duplicate
