# Issue 7602: bug in fpLLL

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-12-04 11:13:19

Assignee: was

AndyNovo wrote on [sage-devel]:

```
We've been working on factoring polynomials in FLINT very intensively the last couple months.  So we've been making floating point LLL in FLINT.  During the process I just discovered what I thought was my bug but is actually a bug in fpLLL which means it's a bug in SAGE too.

Here's a simple lattice which triggers the bug on my 32 bit machine.
(It's the zero rows which are not handled cleanly causing it to size
reduce in very odd ways...)  For a 64 bit machine I have a much larger example which breaks it.

[[0 0 0 0 0]
[0 0 0 0 0]
[1 0 0 0 11]
[0 1 0 0 47]
[0 0 1 0 3748]]

To test the bug in SAGE just run the following code:

matrix([[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,11],[0,1,0,0,47],
[0,0,1,0,3748]]).LLL()

(This was on SAGE 4-1-1 the August 14th version.)
```



---

Comment by malb created at 2009-12-04 11:14:04

AndyNovo on [sage-devel]:
> OK found the bug.  There is a program called get_Shift which gets
> confused by zero vectors.  In any call to Babai if you just add a line
> setting n = the number of columns of B (I'm not sure his notation in
> the C++ version) then it works again.


---

Comment by malb created at 2014-06-25 00:58:39

I can't reproduce/test due to lack of 32-bit machine, anyone still got one?


---

Comment by aapitzsch created at 2014-08-13 21:26:11

The example that should fail on 64bit OS mentioned in the thread works for me.


---

Comment by aapitzsch created at 2014-08-13 21:26:11

Changing status from new to needs_review.


---

Comment by pbruin created at 2014-08-19 15:01:38

Changing status from needs_review to positive_review.


---

Comment by pbruin created at 2014-08-19 15:01:38

The example in the ticket description also works fine on 32-bit ARM, so I think we can safely assume that this has been fixed.


---

Comment by vbraun created at 2014-08-20 20:32:01

Resolution: fixed
