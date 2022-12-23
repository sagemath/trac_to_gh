# Issue 4779: [with patch; not ready for review] make function for creating random rings and running automated testing on them

Issue created by migration from https://trac.sagemath.org/ticket/4779

Original creator: was

Original creation time: 2008-12-13 02:57:56

Assignee: cwitty

This will uncover numerous bugs.  It already has. 


---

Comment by mabshoff created at 2008-12-15 10:15:47

There are some bits missing here since the first hunk from the first patch does not apply. It shouldn't be too hard to rebase, but I am busy with other things today.

Cheers,

Michael


---

Comment by was created at 2008-12-31 02:03:09

I've posted a 100% doctest patch that creates lots of random rings, elements, and does arithmetic with them. 

Of course, there are numerous more rings that can be added.  But I think this is a good and very useful first step.


This patch has zero overlap with anything else, so is fairly safe to apply.   The only problem could be that the new random doctests in this patch could potentially expose some bugs, which of course would be good.


---

Attachment


---

Comment by mabshoff created at 2008-12-31 03:08:21

Looks good to me. One tiny issue probably worth fixing: The docstring says:

```
Create a random prime finite field with cardinality at most 10^20. 
```

But you create

```
GF(ZZ.random_element(x=2, y=10**20).next_prime())
```

So it is likely, but extremely unlikely that this will happen:

```
sage: ZZ.random_element(x=10**20-1, y=10**20).next_prime()
100000000000000000039
```

There is an analog issue further down in another docstring IIRC.

Thoughts?

Cheers,

Michael


---

Comment by malb created at 2008-12-31 18:31:07

*Read-Only Review*
 * I agree with mabshoff's comment on `next_prime` 
 * there is a copy'n'paste error in the docstring of rings0
 * shouldn't "RINGS" in `rings0` mention number fields and GF(p<sup>n</sup>)?
 * the docstring fro `random_rings` seems wrong ("level 0 rings")


---

Comment by ncalexan created at 2009-01-24 21:45:25

malb's comments should be addressed, but this could be applied as is.

I used this to test lots of polynomials and it was good.  Relative number fields should be added after we upgrade pari.


---

Attachment


---

Comment by mabshoff created at 2009-02-20 05:28:10

+1 - all issues raised have been addressed. The patch applies to my merge tree and passes doctests.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 05:53:07

Resolution: fixed


---

Comment by mabshoff created at 2009-02-20 05:53:07

Merged in Sage 3.3.rc3.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2009-02-20 08:27:45

The relative numeber fields still cause trouble, so disabled them for now until the pari-2.4.3svn fix should take care of it.

Cheers,

Michael
