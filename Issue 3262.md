# Issue 3262: interact selector breaks if there are too many options

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2008-05-20 21:07:09

Assignee: somebody

Keywords: interact, notebook

When the lists of values of multiple selectors are too long, the output is truncated, causing nasty bugs.  Here's an example:


```
`@`interact
def test(q1 = selector(range(100)), q2 = selector(range(1000)+['None'], default ='None'), q3 = selector(['hi']+range(1000)+['None'], default=127)):
    show([q1,q2,q3])
```



---

Comment by mhampton created at 2008-05-20 23:38:23

only truncates if `@`interact is not input


---

Attachment

This might be considered a hack: output is only truncated if "`@`interact" is not in a cell's input, which prevents mangling of long html/javascript output.


---

Comment by was created at 2008-05-21 13:00:36

REFEREE REPORT:

1. good idea

2. This line

```
if self.__in.find('`@`interact') == -1: 
```

would read better as

```
if '`@`interact' not in self.__in
```


3. There should be a big comment right before or next to the loop that
we are being *VERY HACKISH* doing this, since e.g. it will cause us to
think that

```
 print "`@`interact"
```

is an interact cell, even though it isn't, and this could must be rewritten
to more intelligently determine whether a cell is an interact cell. 
ACTUALLY, *much* better would be for you to just replace that if by
a cell to `self.is_interactive_cell()`, which I wrote, and which
does things right(er).


---

Comment by mhampton created at 2008-05-21 16:57:38

addressed review comments


---

Attachment

The new patch uses self.is_interactive_cell().  Someone just needs to double-check that this works and it can be merged.


---

Comment by craigcitro created at 2008-06-15 21:47:10

Changing keywords from "interact, notebook" to "interact, notebook, editor_wstein".


---

Comment by was created at 2008-06-15 23:09:28

apply *only* this patch


---

Attachment


---

Comment by mabshoff created at 2008-06-23 11:06:28

Resolution: fixed


---

Comment by mabshoff created at 2008-06-23 11:06:28

Merged in Sage 3.0.4.alpha0


---

Comment by was created at 2008-07-10 08:04:04

Resolution changed from fixed to 


---

Comment by was created at 2008-07-10 08:04:04

1. The patch sage-3262-final.patch  I attached has nothing to do with this tick and simply introduces a bug that totally breaks using interact in sage.

2. The patches by mhampton on this ticket never got applied in sage.

so I'm re-opening this.


---

Comment by was created at 2008-07-10 08:04:04

Changing status from closed to reopened.


---

Attachment

So, for the record: which patch(es) should be applied in which order?

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-11 04:14:05

Ok, sage-3262-undo.patch has already been applied to the official 3.0.4 repo.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-25 00:12:12

This ticket is always showing up at report 11, so let's change the title :)

Cheers,

Michael


---

Comment by itolkov created at 2008-08-30 02:06:55

Why is this still open? Since #3854, it shouldn't be a problem.


---

Comment by itolkov created at 2008-08-30 02:06:55

Changing component from notebook to interact.


---

Comment by mabshoff created at 2008-08-30 02:15:26

Resolution: fixed


---

Comment by mabshoff created at 2008-08-30 02:15:26

You are right. Fixed via #3854.

Cheers,

Michael
