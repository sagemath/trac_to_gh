# Issue 4310: [with patch, needs review] simplification of the coercion api

Issue created by migration from https://trac.sagemath.org/ticket/4310

Original creator: robertwb

Original creation time: 2008-10-16 18:15:20

Assignee: robertwb

CC:  mhansen craigcitro

The `_has_coerce_map_from_` has been deleted, and the `_coerce_map_from_` now can return a boolean or callable as well as a map. 


---

Attachment

Grammar comment: "Deprecate" is spelled with an e in the middle, not an i.

Did you know that "deprecate" used to mean "to pray against" (as an evil) and comes from the latin roots de + precari (precari="to pray").  I just learned that when I looked it up.  It certainly adds emphasis to deprecation statements if people are praying against the evil of whatever is being deprecated!  See http://www.merriam-webster.com/dictionary/deprecate


---

Attachment

After a rebase and rebuild caused by parent.pxd, I think this is good.  It simplifies the coercion interface a fair amount.

Apply only trac_4310.patch


---

Comment by jason created at 2008-11-21 18:19:33

Minor nitpick from before still applies to trac_4310: Deprecate is spelled "Depricate" in the patch.  I wouldn't let that hold up the patch going in; just pointing it out.


---

Comment by robertwb created at 2008-11-21 19:10:01

I have *got* to remember how to spell that word...


---

Comment by mabshoff created at 2008-11-21 21:32:56

Merged in Sage 3.2.1.alpha0 - I also fixed the spelling problem pointed out above.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-21 21:32:56

Resolution: fixed


---

Comment by mabshoff created at 2008-11-21 21:34:14

For the record: I merged trac_4310.patch into Sage 3.2.1.alpha0.

Cheers,

Michael
