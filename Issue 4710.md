# Issue 4710: fix docstring for divisors

Issue created by migration from https://trac.sagemath.org/ticket/4710

Original creator: robertwb

Original creation time: 2008-12-05 06:09:06

Assignee: tba


```
On Dec 4, 2008, at 9:35 PM, pong wrote:

In SAGE 3.2.1 , the docstring of divisors says:

Definition:	divisors(n)
Docstring:

        Returns a list of all positive integer divisors
        of the nonzero integer n.

        A second parameter may be passed to surpress sorting
        of the list (as ordering the list can be more time
        consuming then creating it).

        INPUT:
            n -- the element
            sorted -- whether or not to sort the output (default True)

My question is how to get an unsorted output?

I tried divisors(300, sorted=False) but SAGE complaints that divisors
only takes 1 argument. In fact, the source codes seem to suggest that
it will always return a sorted list.
```


Now the divisors are always returned sorted (as we have resolved the issue of sorting taking the majority of the time). The documentation needs to be fixed.


---

Comment by jhpalmieri created at 2009-02-26 17:08:18

Here's a trivial patch.  Is this good enough?


---

Attachment


---

Comment by robertwb created at 2009-02-26 20:01:28

Yep, looks good to me.


---

Comment by mabshoff created at 2009-02-28 17:07:34

Merged in Sage 3.4.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-28 17:07:34

Resolution: fixed
