# Issue 9341: K.S_units doesn't check for repeated entries

Issue created by migration from Trac.

Original creator: syazdani

Original creation time: 2010-06-25 20:54:29

Assignee: davidloeffler

CC:  rlm robertwb

Keywords: S_units

Here is a stupid example:

```
sage: _.<t>=QQ[]
sage: K.<T>=NumberField(t-1)
sage: I = K.ideal(2)
sage: K.S_units([I])
[2, -1]
sage: K.S_units([I, I])
[2, 2, -1]
```

Looking at the code, this seems to be an upstream issue with gp as well.


---

Comment by AlexGhitza created at 2014-04-18 00:39:04

New commits:


---

Comment by AlexGhitza created at 2014-04-18 00:39:04

Changing status from new to needs_review.


---

Comment by pbruin created at 2014-04-18 12:39:38

It doesn't seem very robust to rely on a duplicate in the list of prime ideals yielding the _same_ _S_-unit twice, rather than two (or more) different but linearly dependent _S_-units.  PARI's algorithm probably assumes that the input is a list of pairwise distinct prime ideals, so I would guess it is safer to apply `uniq()` to the input instead of the output.

[Edit: it may even be wise to do this in `_S_class_group_and_units()`.]


---

Comment by git created at 2014-04-18 22:25:14

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-04-18 22:28:50

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by AlexGhitza created at 2014-04-18 22:31:50

Peter is of course right.  I have modified the fix so that it uniq-fies the input list of primes instead, and I have put it into the helper function.

Sorry about this minor fix now being spread across 3 git commits, still getting the hang of the "new" workflow.  Is there a way to flatten the commits into one?  (After having pushed to the trac server?)


---

Comment by chapoton created at 2014-04-20 09:00:20

It is not necessary to flatten the commits, imho. If you prefer less commits, you should rather flatten them before pushing to trac (for example using `git rebase -i develop`).


---

Comment by pbruin created at 2014-04-21 10:23:27

OK, looks good and all tests pass.  The only comment I have is that `TEST:` should only have a single colon, since there is no doctest directly following it.

If you want to flatten the commits into one, the easiest way is `git reset develop` (this forgets that you have made the commits, but keeps the edits) followed by `git commit -a` and then do a forced push.  I agree that you shouldn't do this in general, but in this case I think it is fine; I don't expect people have already started to base new work on this.

When you have done one or both of these things, feel free to set this to positive review.


---

Comment by git created at 2014-04-22 22:12:54

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by AlexGhitza created at 2014-04-22 22:13:52

I fixed the docstring issue.


---

Comment by AlexGhitza created at 2014-04-22 22:13:52

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-04-25 14:20:50

Resolution: fixed
