# Issue 1926: [with patch, needs review] fixes for the maple interface

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2008-01-25 13:53:08

Assignee: burcin

Attached patch includes the following fixes:

 * Maple uses = as the equality test operator
 * Use . as multiplication operator
 * Print using printf("%q",var)
 * Add code to convert Sage matrices to Maple
 * Add code to convert Sage vectors to Maple



---

Comment by burcin created at 2008-01-25 13:53:33

fixes to the maple interface


---

Attachment

This patch is very good except I don't like:

```
 	581	        # everything is supposed to be comparable in Python, so we define 
 	582	        # the comparison thus when no comparable in interfaced system. 
 	583	        return -1   
```


It would be better to compare something deterministic instead of always return -1, since you want that if a < b then it isn't the case that b < a; however your code will return that a < b *and* b < a, when the two aren't comparable.  Better would be to compare a hash of the string reps of the objects (can maple do that?!) or _something_ deterministic and easy.


---

Comment by burcin created at 2008-01-25 16:18:50

fixes to the maple interface (new version, fixing __cmp__ problem)


---

Attachment

Replying to [comment:1 was]:
> This patch is very good except I don't like:
 {{{
  	581	        # everything is supposed to be comparable in Python, so we define 
  	582	        # the comparison thus when no comparable in interfaced system. 
 	583	        return -1   
 }}}

I copied the body of the `__cmp__` function from `sage/interfaces/expect.py`, and this comment came with it. 

> It would be better to compare something deterministic instead of always return -1, since you want that if a < b then it isn't the case that b < a; however your code will return that a < b *and* b < a, when the two aren't comparable.  Better would be to compare a hash of the string reps of the objects (can maple do that?!) or _something_ deterministic and easy.   

You're right. This was also a problem with `expect.py`. attachment:sage-maple_interface_fixes.2.patch  changes the offending lines with

{{{ 
if hash(str(self)) < hash(str(other):
    return -1
else:
    return 1
}}}

Hopefully making `__cmp__` behave more like an order relation.


---

Comment by was created at 2008-01-25 17:01:24

> I copied the body of the __cmp__ function from sage/interfaces/expect.py, 
> and this comment came with it.

I've certainly made the mistake of defining cmp to return -1 always, which 
is very stupid.  If __cmp__ currently does that in expect.py, please open
a ticket about it!

> if hash(str(self)) < hash(str(other):
>     return -1
> else:
>    return 1

> Hopefully making __cmp__ behave more like an order relation. 

I do not like the above cmp (even though I used to write code
like that).  Imagine that self or orther is a 1000x1000 matrix,
say, which is completely reasonable.  Then the above would
literally take a very long time, since it would have to pull that matrix
back to Sage, etc.   Much better would be to do a comparison
that involves a Maple hash function. 

William


---

Comment by mhansen created at 2008-01-28 01:15:16

I've added a patch which changes the hashing of expect elements and adds a special hash method for MapleElements.


---

Attachment


---

Comment by mabshoff created at 2008-01-28 02:45:02

Resolution: fixed


---

Comment by mabshoff created at 2008-01-28 02:45:02

Merged sage-maple_interface_fixes.2.patch and 1926.patch in Sage 2.10.1.rc2


---

Comment by burcin created at 2008-01-29 09:14:17

make the doctests optional in sage/interfaces/maple.py


---

Comment by burcin created at 2008-01-29 09:16:41

Resolution changed from fixed to 


---

Comment by burcin created at 2008-01-29 09:16:41

Changing status from closed to reopened.


---

Attachment

attachment:1926-make_doctests_optional.patch needs to be applied to make the new doctests in the maple interface optional.


---

Comment by mhansen created at 2008-02-01 03:42:30

New patch looks good to me.


---

Comment by mabshoff created at 2008-02-01 03:48:36

Merged 1926-make_doctests_optional.patch in Sahe 2.10.1.rc4


---

Comment by mabshoff created at 2008-02-01 03:48:36

Resolution: fixed
