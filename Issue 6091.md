# Issue 6091: [with patch, needs review] syntax extended for subfields of number fields

Issue created by migration from Trac.

Original creator: fwclarke

Original creation time: 2009-05-20 06:41:06

Assignee: tbd

At present

```
sage: C.<z> = CyclotomicField(20)
sage: D.<w>, phi = C.subfield(z^4)
```

fails.

This is simply because the code uses the name `name` instead of the name `names`.  The patch fixes this, and does the same for `change_generator` (with doctests).


---

Attachment

Positive review. Patch applies fine to 4.0.rc1, all tests in sage/rings/number_field and doc/en/bordeaux_2008 pass; and the new syntax is a very useful thing to have.

David


---

Comment by davidloeffler created at 2009-05-29 10:46:30

Changing component from algebra to number theory.


---

Comment by davidloeffler created at 2009-05-29 10:46:30

Changing assignee from tbd to was.


---

Comment by mhansen created at 2009-06-01 00:14:03

This will break all old code that uses the name= syntax.

There is a decorator at sage.plot.misc.rename_keyword that could be use to rename a 'name' keyword argument to 'names'.  A useful thing to do would be to add a flag to that decorator so that a deprecation warning would be thrown whenever a rename is done.


---

Comment by fwclarke created at 2009-06-01 21:40:39

Replying to [comment:2 mhansen]:
> This will break all old code that uses the name= syntax.
Point taken.

> There is a decorator at sage.plot.misc.rename_keyword that could be use to rename a 'name' keyword argument to 'names'.  A useful thing to do would be to add a flag to that decorator so that a deprecation warning would be thrown whenever a rename is done.

I think in this case there's a simpler solution,  already used in the `NumberField`function, which allows either `name` or `names`; see the replacement patch.


---

Attachment

replaces previous


---

Comment by mhansen created at 2009-06-04 19:08:10

While it is a solution, I think it's a bit more hackish.  We should really clean these things up a bit.  But, I'm okay with this going in.

Merged in 4.0.1.rc1.


---

Comment by mhansen created at 2009-06-04 19:08:10

Resolution: fixed
