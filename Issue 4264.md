# Issue 4264: change E.a_invariants() for an elliptic curve to return a tuple

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-10-11 09:46:11

Assignee: was

For consistency with b_invariants, etc., and to emphasize immutability, it would be
good for E.a_invariants() to return a tuple.  Changing this could change lots of doctests, etc., so this isn't trivial.

See trac #4262 for a related ticket


---

Comment by cremona created at 2008-10-13 11:51:15

Quick comment:  the cached `self.__ainvs` should actually *be* a tuple.  So the only code to change is in line 142 in `ell_generic.py`, from this

```
        self.__ainvs = ainvs
```

to this

```
        self.__aincs = tuple(ainvs)
```

as well as the doctests.


---

Comment by cremona created at 2008-10-13 16:12:38

I have made a patch (not yet attached) which implements this.   It was easy to do what was suggested (and make the consequent cosmetic changes in doctests from [...] to (...) ) but there were two similar but distinct other issues:

    * Several Sage functions (the `__init__` function in the EllipticCurve classes) expect the a-invs input parameters to be a list and not a tuple.  I tried changing them to accept tuples but it caused too many difficulites with parsing different input possibilities so I reverted that.
    * In several places where elliptic curves in other systems are initialised (e.g. mwrank, gp) lists are required for the parsing done by the wrappers.

In all the above I sorted everything out by inserting list(...) around `blah.ainvs()` or `blah.a_invariants()`, which works but is ugly.   Is there a better way?  Even just having a new function a_list() to be list(self.ainvs()) would be a bit cleaner.  We already have the unnecessary synonyms a_invariants() and ainvs().

I'll wait for reaction before going further.  In particular, I have not yet tested anything outside the elliptic_curves directory, e.g. the tutorial.


---

Comment by cremona created at 2008-10-13 16:12:38

Changing priority from major to minor.


---

Comment by davidloeffler created at 2009-07-20 19:48:48

Changing assignee from was to davidloeffler.


---

Comment by davidloeffler created at 2009-07-20 19:48:48

Changing component from number theory to elliptic curves.


---

Comment by cremona created at 2009-07-20 19:58:39

Doesn't 9 months go quickly?  I thought this had been fixed long ago.  No time now though...


---

Comment by davidloeffler created at 2009-10-09 09:13:41

Remove assignee davidloeffler.


---

Comment by wuthrich created at 2009-10-20 21:56:42

I think we won't need a a_list. I'd prefer having list() everywhere, even if it is ugly.

Could you post your first draft of a patch here ? I will try to work on it.

Chris.


---

Comment by cremona created at 2009-10-21 08:17:38

Replying to [comment:6 wuthrich]:
> I think we won't need a a_list. I'd prefer having list() everywhere, even if it is ugly.
> 
> Could you post your first draft of a patch here ? I will try to work on it.
> 
> Chris.

Sorry, but after a year I am sure that it is lost for ever.  I should have uploaded it anyway with a "needs more work" tag.  Anyway, after a year of version changes it would never have merged without a lot of work.


---

Comment by wuthrich created at 2009-10-21 09:35:47

That is alright. If I get to do it, I will start from scratch, then.


---

Comment by wuthrich created at 2009-11-02 13:11:02

exported against 4.2.


---

Attachment

I hope I did not miss any a_invs or a_invariants.


---

Comment by wuthrich created at 2009-11-02 13:12:24

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-11-05 02:39:48

Looks good to me.  Passes all tests with -long.


---

Comment by mhansen created at 2009-11-05 02:39:48

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-05 02:40:01

Resolution: fixed
