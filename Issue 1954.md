# Issue 1954: sage/modules/free_module_element.pyx computing abs(vector(...))

Issue created by migration from https://trac.sagemath.org/ticket/1954

Original creator: mhansen

Original creation time: 2008-01-28 00:03:21

Assignee: mhansen


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

Comment by mhansen created at 2008-01-28 00:05:05

Changing status from new to assigned.


---

Attachment


---

Comment by mhansen created at 2008-01-28 00:48:53

Changing priority from major to blocker.


---

Comment by dmharvey created at 2008-01-28 01:43:53

Looks good to me (I only ran doctests on that file, not on all files).

(If anyone has time, would be good to try doing this without the `list` call, and also I expect `x*x` is generally faster than `x**2`.)


---

Comment by mabshoff created at 2008-01-28 02:36:46

Resolution: fixed


---

Comment by mabshoff created at 2008-01-28 02:36:46

Merged in Sage 2.10.1.rc2
