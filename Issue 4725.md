# Issue 4725: bug in number field conjugate function

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-06 18:37:26

Assignee: was

This is totally wrong!

```
sage: K.<j,b> = QQ[sqrt(-1), sqrt(2)]
sage: j.conjugate()
0
```


Much better would be either an error message (since the docs for conjugate say it isn't implemented except for cyclotomic and quadratic fields!) or an actual correct answer using a number field embedding.  But giving 0 is just crazy.


---

Comment by fwclarke created at 2009-04-21 08:43:01

This is sorted out by a minor change to `conjugate` included in the patch
with #5842.  There is a doctest at line 1456 of the patched
`number_field_element.pyx`


---

Comment by davidloeffler created at 2009-07-21 08:07:33

Changing component from number theory to number fields.


---

Comment by davidloeffler created at 2009-07-21 08:07:33

I can confirm that this is indeed fixed (although the fix has now drifted to line 1542).


---

Comment by davidloeffler created at 2009-07-21 08:07:33

Changing assignee from was to davidloeffler.


---

Comment by mvngu created at 2009-07-22 16:28:36

Resolution: fixed


---

Comment by mvngu created at 2009-07-22 16:28:36

Fixed due to #5842.
