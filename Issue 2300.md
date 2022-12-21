# Issue 2300: A copy method for SingularElement [with patch, needs review]

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2008-02-25 09:57:08

Assignee: SimonKing

CC:  malb@informatik.uni-bremen.de

Keywords: copy SingularElement

So far, there was no method for copying a `SingularElement`. Calling `copy` on a `SingularElement` resulted in an `(invalid object -- defined in terms of closed session)`.

The patch provides a `__copy__` method. In fact, this is quite easy: For most objects `S` of type `SingularElement`, it suffices to return `singular(S.name())`. One has to make an exception when `S` is a ring, because `singular(S.name)())` would just yield another name for _the same_ ring. Therefore, `(S.ringlist()).ring()` is used for duplication of a ring. Examples:


```
sage: R=singular.ring(0,'(x,y)','dp')
sage: M=singular.matrix(3,3,'0,0,-x, 0,y,0, x*y,0,0')
sage: N=copy(M)
sage: N[1,1]=singular('x+y')
sage: N
x+y,0,-x,
0,  y,0,
x*y,0,0
sage: M
0,  0,-x,
0,  y,0,
x*y,0,0
```

Hence, N really is a copy of M. Changing N does not affect M

```
sage: S=copy(R)
sage: S.set_ring()
sage: S
//   characteristic : 0
//   number of vars : 2
//        block   1 : ordering dp
//                  : names    x y
//        block   2 : ordering C
sage: R.fetch(M)
0,  0,-x,
0,  y,0,
x*y,0,0
sage: M
`sage1`
```

Note that in the last example, `M` is unknown after making `S` active. So, `S` is a copy of `R`, but not identical to `R`.
Defining `S=singular(R.name())` would be a mistake: The matrix `M` would be known in `S`, and any change to `M` when `S` is active would persist after returning to `R`.


---

Comment by SimonKing created at 2008-02-25 10:28:25

Remark: The exception must be done both for `SingularElement` of type `ring` and of type `qring`. Done in the new patch.


---

Comment by SimonKing created at 2008-02-25 12:55:36

I observed that the words [with patch, needs review] are usually prepended and not appended to the ticket's summary.


---

Comment by malb created at 2008-02-26 11:36:56

*Referee Report*
 * `singular(self.name())` should be `self.parent()(self.name())` such that it also works if one uses a non standard instance of the Singular interface
 * I think the examples should be shifted four spaces too the right, e.g.:

```
EXAMPLE:
    sage: foo
    bar
```



---

Attachment

Sorry for being late, and sorry for accidentally adding the same patch twice.

I changed the patch according to the referee report, hence, the examples are indented, and it is `self.parent()(self.name())`. 

The patch is relative to sage-2.10.3.alpha0


---

Comment by mabshoff created at 2008-02-27 03:29:00

Resolution: fixed


---

Comment by mabshoff created at 2008-02-27 03:29:00

Merged in Sage 2.10.3.rc0


---

Comment by SimonKing created at 2008-02-28 12:01:17

Changing status from closed to reopened.


---

Attachment

Sorry, i have to re-open the ticket because i found a bug in my patch:


```
sage: R=singular.ring(0,'(x,y)','dp')
sage: L=R.ringlist()
sage: L[4]=singular.ideal('x**2-5')
sage: Q=L.ring()
sage: otherR=singular.ring(5,'(x)','dp')
sage: cpQ=copy(Q)
<snip>
<type 'exceptions.TypeError'>: Singular error:
   ? ring with polynomial data must be the base ring or compatible
   ? error occurred in STDIN line 36: `def sage12=ringlist(sage10);`
```


The problem is that `ringlist` contains polynomial data, and thus only works if the basering fits.

Solution: If `self` is a ring/qring then we first make it active `basering`, copy `self` using `ringlist`, return to the old `basering`, and return the copy of `self`.

I extended the doc tests accordingly. The new doc test would fail with the old version of `__copy__`.

The patch `bugfix__copy__.patch` is relative to `sage-2.10.3.rc0`.


---

Comment by SimonKing created at 2008-02-28 12:01:17

Resolution changed from fixed to 


---

Comment by malb created at 2008-03-03 15:45:13

Because the patches attached to this ticket were already merged, I guess it would be best to open a new ticket for the bugfixes attached after the merge.


---

Comment by malb created at 2008-03-03 15:46:53

The code looks good, I don't know a better Singular solution. I'm happy to give the bugfix a 'positive review' once it is attached to a new ticket.


---

Comment by SimonKing created at 2008-03-03 17:21:38

Replying to [comment:9 malb]:
> The code looks good, I don't know a better Singular solution. I'm happy to give the bugfix a 'positive review' once it is attached to a new ticket.

OK, it is #2377.

Sorry, i thought when a bug is found in a patch then it is still the same ticket.


---

Comment by mabshoff created at 2008-03-03 17:32:49

Replying to [comment:10 SimonKing]:
> Replying to [comment:9 malb]:
> > The code looks good, I don't know a better Singular solution. I'm happy to give the bugfix a 'positive review' once it is attached to a new ticket.
> 
> OK, it is #2377.
> 
> Sorry, i thought when a bug is found in a patch then it is still the same ticket.

Some times it is, some times it isn't, but generally you should open a new ticket if a bugfix is found post merge when an rc or alpha has been released.

I will also quote malb on the new ticket with his positive review and merge the patch then.

Cheers,

Michael


---

Comment by SimonKing created at 2008-03-04 12:11:28

I hope i am allowed to close the ticket, since it is resolved in #2377


---

Comment by SimonKing created at 2008-03-04 12:11:28

Resolution: fixed


---

Comment by mabshoff created at 2008-03-04 16:09:31

Replying to [comment:12 SimonKing]:
> I hope i am allowed to close the ticket, since it is resolved in #2377

Yeah, sorry that I didn't close this. I was an oversight on my end and it was clear that it must be closed.

Cheers,

Michael
