# Issue 5152: order of abelian group element is a rational number, but should be an integer

Issue created by migration from https://trac.sagemath.org/ticket/5152

Original creator: was

Original creation time: 2009-02-01 22:02:43

Assignee: somebody

The line commented with "error here???" below is frightening:

```
File: /sage/groups/abelian_gps/abelian_group_element.py
Source Code (starting at line 268):
    def order(self):
        """
        Returns the (finite) order of this element or Infinity if this element
        does not have finite order.
 
        EXAMPLES:
            sage: F = AbelianGroup(3,[7,8,9]); F
            Multiplicative Abelian Group isomorphic to C7 x C8 x C9
            sage: F.gens()[2].order()
            9
            sage: a,b,c = F.gens()
            sage: (b*c).order()
            72
        """
        M = self.parent()
        if self == M(1):
            return Integer(1)
        invs = M.invariants()
        if self in M.gens():
            o = invs[list(M.gens()).index(self)]
            if o == 0:
                return infinity
            return o
        L = list(self.list())
        N = LCM([invs[i]/GCD(invs[i],L[i]) for i in range(len(invs)) if L[i]!=0])   ####### error here????
        if N == 0:
            return infinity
        else:
            return N
```



But what bugs me about it is:

```
sage: G = AbelianGroup(3,[7,8,9])
sage: type((G.0 * G.1).order())
<type 'sage.rings.rational.Rational'>
```


a simple coercion to Integer at the end of the function would fix this, or using // instead of /.   And add a doctest that has a type check so this doesn't get re-introduced. 




---

Comment by wdj created at 2009-02-01 23:09:29

to be applied to 3.3.alpha3


---

Attachment

Please *ignore* trac-5152-abelian-gp-order.2.patch (2.8 kB). I don't know how that got there; hg_sage.export was not working the way I expected.


---

Comment by wdj created at 2009-02-01 23:13:25

The patch trac-5152-abelian-gp-order.patch (1.6 kB) does exactly as instructed.


---

Comment by mabshoff created at 2009-02-02 18:20:16

Resolution: fixed


---

Comment by mabshoff created at 2009-02-02 18:20:16

Merged in Sage 3.3.alpha4.

Cheers,

Michael
