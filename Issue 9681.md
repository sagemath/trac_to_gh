# Issue 9681: Missing dependancy in spkg/standard/deps for zn_poly.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-08-04 00:32:03

Assignee: GeorgSWeber

CC:  ddrake mpatel leif jhpalmieri

The zn_poly package lists in `SPKG.txt` the only dependencies are GMP, but this is not true, as zn_poly's configure script has in it:


```
/configure --gmp-prefix="$SAGE_LOCAL" --ntl-prefix="$SAGE_LOCAL" \
            --prefix="$SAGE_LOCAL" --cflags="$CFLAGS" --ldflags="$LDFLAGS"
```


Looking at $SAGE_ROOT/spkg/standard/deps, I see: 


```
$(INST)/$(ZNPOLY): $(BASE) $(INST)/$(MPIR)
        $(INSTALL) "$(SAGE_SPKG) $(ZNPOLY) 2>&1" "tee -a $(SAGE_LOGS)/$(ZNPOLY).log"
```


then looking at MPIR I see the dependencies are only BASE and ICONV. But ICONV only depends on BASE, so there is nothing to force ntl to build before zn_poly.

I am aware of two other changes that are desirable in the 'deps' file too, as they add clarity. 

 * #9464 
 * #9637 

These might as well be fixed at the same time. 

Dave


---

Attachment

Updated deps file, which solves this major problem and corrects two minor ones in #9464 and #9637


---

Attachment

Unifier diff file for $SAGE_ROOT/spkg/standard/deps


---

Comment by drkirkby created at 2010-08-04 00:49:06

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-08-04 00:51:46

I've attached an updated 'deps' file, which fixed this major problem and two minor ones - #9464 and #9637. If this ticket is merged, then  #9464 and #9637 can be closed as fixed. 

Dave


---

Comment by drkirkby created at 2010-08-04 01:09:48

It was only by chance I found this, while trying to resolve a 64-bit Solaris issue, which is #9358. 

I'm adding the two release managers to the ticket, as I believe this should be a blocker. 

Dave


---

Comment by robertwb created at 2010-08-04 07:16:32

Unless it's actually causing problems for builds, or giving incorrect results, I wouldn't classify this a as a blocker (though I'd say it is a bug for sure).


---

Comment by drkirkby created at 2010-08-04 08:58:47

Replying to [comment:7 robertwb]:
> Unless it's actually causing problems for builds, or giving incorrect results, I wouldn't classify this a as a blocker (though I'd say it is a bug for sure). 

Some rather subtle problems have been caused by dependencies which have not been correct - I'm thinking in particular of William's failure on OS X to compile some Fortran code, when in fact it was due to the fortran package being dependent on python for a very simple script. The strange thing about that was everyone else had no problems, including me, using William's script on bsd.math. 

I would have thought anything that had the potential to mis-compile would be a blocker personally, but that's a personal opinion of course. 

Dave


---

Comment by drkirkby created at 2010-08-04 23:50:57

Resolution: wontfix


---

Comment by drkirkby created at 2010-08-04 23:50:57

Changing priority from blocker to minor.


---

Comment by drkirkby created at 2010-08-04 23:50:57

Apparently NTL is not needed unless one makes those targets, so this is a non-issue.
