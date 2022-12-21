# Issue 275: Maxtrix groups over RR don't get pushed off to GAP properly

Issue created by migration from Trac.

Original creator: moretti

Original creation time: 2007-02-21 20:34:05

Assignee: was

Keywords: matrix groups


```
sage: G = SL(2, CC)
sage: G.gens()

TypeError: Gap produced error output
Variable: 'Complex' must have a value

Syntax error: ) expected
$sage17:=SL(2, Complex Field with 53 bits of precision);;
                           ^

   executing $sage17:=SL(2, Complex Field with 53 bits of precision);;
```



---

Comment by was created at 2007-08-18 09:58:28

NOTE -- Gap doesn't have a notion of floating point numbers -- so the correct behavior here is to give a good error message.


---

Comment by was created at 2007-08-18 09:58:34

Changing component from algebraic geometry to interfaces.


---

Comment by was created at 2007-08-18 20:25:25

fixed for sage-2.8.2


---

Comment by was created at 2007-08-18 20:25:25

Resolution: fixed
