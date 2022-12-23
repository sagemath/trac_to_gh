# Issue 5125: Ideal.basis_is_groebner() may return wrong results

Issue created by migration from https://trac.sagemath.org/ticket/5125

Original creator: malb

Original creation time: 2009-01-29 00:02:15

Assignee: malb

CC:  john_perry

For the attached list, `Ideal(gb).basis_is_groebner()` returns `True` but the basis is not a Gröbner basis!

The code in question:


```
    def basis_is_groebner(self, singular=singular_default):
        self.ring()._singular_().set_ring()

        F = singular( self.gens(), "module" )
        LTF = singular( [f.lt() for f in self.gens()] , "module" )

        M = (F * LTF.syz()).reduce(self._singular_())

        for i in range(M.nrows()):
            if int(singular.eval("%s[1][%s+1]!=0"%(M.name(),i))):
                return False

        self._singular_().attrib('isSB',1)
        return True
```



---

Attachment

load("B.sobj") this file to test if the bug is fixed.


---

Comment by john_perry created at 2009-01-30 23:09:05

Wait-- sorry, that doesn't work either. Now things that *are* Groebner bases are considered not to be.


---

Attachment

now it works on `B.sobj` as well as on its groebner basis


---

Comment by john_perry created at 2009-01-30 23:27:40

There were two subtle bugs.
 * The first was that `M` only had one row. Thus, `i` would check only the first element of `M`. Hence unpredictable behavior: sometimes the correct answer, sometimes not.
 * The second was that Singular (for whatever reason) expects the arrays to be indexed by `[row,col]` and not by `[row][col]`.


---

Comment by malb created at 2009-01-31 15:29:15

apply after basis_is_groebner.patch


---

Attachment

The attached patch fixes the issue for me. I've added a second patch which documents that the bug is indeed fixed. mabshoff, this patch should definitely go in for 3.3 because right now Sage gives wrong answers!


---

Comment by mabshoff created at 2009-02-02 02:46:16

Resolution: fixed


---

Comment by mabshoff created at 2009-02-02 02:46:16

Merged both patches in Sage 3.3.alpha4.

Cheers,

Michael
