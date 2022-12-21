# Issue 4893: srange docstring is misleading

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-12-30 20:28:37

Assignee: cwitty

Keywords: range

I reported

```
The docstring for srange() says:

   Return list of numbers \code{a, a+step, ..., a+k*step},
   where \code{a+k*step < b} and \code{a+(k+1)*step > b}.

   This is the best way to get an iterator over Sage integers as
   opposed to Python int's.  It also allows you to specify step sizes
   to iterate.  It is potentially much slower than the Python range
   statement, depending on your application.

The second paragraph suggests that what you get is an iterator, but in
fact you get a list.  Is there any good reason why srange does not
return an iterator?  Surely that would be more efficient in most
cases, and the user can turn the iterator into a list if needed.
```

and William replied

```
srange's docstring is wrong and should be fixed.  Please post a patch.

The function sxrange gives a proper python iterator.  The
documentation for srange should contain a remark that sxrange gives
the iterator version, and if it doesn't add that too :-)

But don't change srange to be a python iterator -- that would be like
making range a python iterator, which is a bad idea since sometimes
people use ranges not as iterators.
```

so I will post a suitable patch,


---

Attachment


---

Comment by cremona created at 2008-12-30 23:02:50

Patch attached, based on 3.2.2.  It only changes the (second paragraph of the) docstring for srange() so should not cause any problems.


---

Comment by AlexGhitza created at 2008-12-31 08:09:21

Looks good.


---

Comment by mabshoff created at 2009-01-12 02:17:56

Resolution: fixed


---

Comment by mabshoff created at 2009-01-12 02:17:56

Merged in Sage 3.3.alpha0
