# Issue 1955: bug in vector

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-28 00:25:26

Assignee: somebody


```

Hi,

It seems the __abs__ method for vectors is missing the part that is
supposed to square the components before they are added.

[e.g. abs(vector([1..5])) should really be
sqrt(1+4+9+16+25)=sqrt(55) ]

The code of the current version is included below.

   def __abs__(self):
       """
       Return the square root of the sum of the squares of the
entries of this vector.

       EXAMPLES:
           sage: v = vector([1..5]); abs(v)
           sqrt(15)
           sage: v = vector(RDF, [1..5]); abs(v)
           3.87298334621
       """
       return sum(self.list()).sqrt()

The last line should be something like

       return sum([x*x for x in self.list()]).sqrt()

(not sure if that is the most efficient way).

--Peter
```



---

Comment by mabshoff created at 2008-01-28 00:28:02

Resolution: duplicate


---

Comment by mabshoff created at 2008-01-28 00:28:02

This is a dupe of #1954, which already has a patch for review.
