# Issue 1985: is_pseudoprime docstring doesn't wrap

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-01-30 15:01:28

Assignee: mabshoff

Reported by Steve Vonn in https://groups.google.com/group/sage-support/t/ea050f051600e792

```
is_pseudoprime?
The help entry for (is_pseudoprime) has a nonwrapping text bug

INPUT:
        flag -- int
                0 (default): checks whether x is a Baillie-Pomerance-Selfridge-Wagstaff pseudo prime (strong Rabin-Miller pseudo prime for base 2, followed by strong Lucas test for the sequence (P,-1), P smallest positive integer such that P^2 - 4 is not a square mod x).
                > 0: checks whether x is a strong Miller-Rabin pseudo prime for flag randomly chosen bases (with end-matching to catch
square roots of -1). 
```



---

Attachment


---

Comment by AlexGhitza created at 2008-01-30 15:25:15

Looks good to me.


---

Comment by mabshoff created at 2008-01-30 15:27:53

Merged in Sage 2.10.1.rc4


---

Comment by mabshoff created at 2008-01-30 15:27:53

Resolution: fixed
