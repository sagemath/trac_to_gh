# Issue 395: flatten command for nested lists

Issue created by migration from https://trac.sagemath.org/ticket/395

Original creator: mhampton

Original creation time: 2007-06-28 16:06:22

Assignee: mhampton

Keywords: lists, flatten

The attached file has a candidate function for a flatten command. The default types to flatten are lists and tuples, but more can be added.


```
def flatten(in_list, ltypes=(list, tuple)):
    """
    Flattens a nested list.

    INPUT:
        in_list -- a list or tuple
        ltypes -- optional list of particular types to flatten

    OUTPUT:
        a flat list of the entries of in_list

    EXAMPLES:
        sage: flatten([[1,1],[1],2])
        [1, 1, 1, 2]
        sage: flatten((['Hi',2,vector(QQ,[1,2,3])],(4,5,6)))
        ['Hi', 2, (1, 2, 3), 4, 5, 6]
        sage: flatten((['Hi',2,vector(QQ,[1,2,3])],(4,5,6)),ltypes=(list, tuple, sage.modules.vector_rational_dense.Vector_rational_dense))
        ['Hi', 2, 1, 2, 3, 4, 5, 6]
    """
    index = 0
    new_list = [x for x in in_list]
    while index < len(new_list):
        if not new_list[index]:
            new_list.pop(index)
            continue
        while isinstance(new_list[index], ltypes):
            new_list[index : index + 1] = list(new_list[index])
        index += 1
    return new_list
```




---

Comment by mhampton created at 2007-06-28 16:06:39

Changing status from new to assigned.


---

Comment by mhampton created at 2007-07-05 15:57:34

New version:

def flatten(in_list, ltypes=(list, tuple)):
    """
    Flattens a nested list.

    INPUT:
        in_list -- a list or tuple
        ltypes -- optional list of particular types to flatten

    OUTPUT:
        a flat list of the entries of in_list

    EXAMPLES:
        sage: flatten([[1,1],[1],2])
        [1, 1, 1, 2]
        sage: flatten([[1,2,3], (4,5), [[[1],[2]]]])
        [1, 2, 3, 4, 5, 1, 2]

    In the following example, the vector isn't flattened because
    it is not given in the ltypes input.
        sage: flatten((['Hi',2,vector(QQ,[1,2,3])],(4,5,6)))
        ['Hi', 2, (1, 2, 3), 4, 5, 6]

    We give the vector type and then even the vector gets flattened:
        sage: flatten((['Hi',2,vector(QQ,[1,2,3])], (4,5,6)),
ltypes=(list,
tuple,sage.modules.vector_rational_dense.Vector_rational_dense))
        ['Hi', 2, 1, 2, 3, 4, 5, 6]

    We flatten a finite field.
        sage: flatten(GF(5))
        [0, 1, 2, 3, 4]
        sage: flatten([GF(5)])
        [Finite Field of size 5]
        sage: flatten([GF(5)], ltypes = (list, tuple,
sage.rings.finite_field.FiniteField_prime_modn))
        [0, 1, 2, 3, 4]

    """
    index = 0
    new_list = [x for x in in_list]
    while index < len(new_list):
        while isinstance(new_list[index], ltypes):
            if len(new_list[index]) != 0:
                new_list[index : index + 1] = list(new_list[index])
            else:
                new_list.pop(index)
                break
        index += 1
    return new_list


---

Comment by mabshoff created at 2007-08-23 12:50:50

Sage 2.8.2 has a flatten command. It also seems to work on nested lists:

```
sage: L
[[1, 2], [1, 2]]
sage: flatten(L)
[1, 2, 1, 2]
sage: L=[L,[L,[L,[L]]]]
sage: L
[[[1, 2], [1, 2]], [[[1, 2], [1, 2]], [[[1, 2], [1, 2]], [[[1, 2], [1, 2]]]]]]
sage: flatten(L)
[1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
```

So am I correct to assume that this ticket can be closed? 

Cheers,

Michael


---

Comment by was created at 2007-08-29 02:39:43

Resolution: fixed


---

Comment by was created at 2007-08-29 02:39:43

Yep, this has been in SAGE a while.


---

Comment by mhampton created at 2007-09-11 16:48:26

This still has some problems on empty lists, which I (Marshall Hampton) will try to fix soon.  the simplest example of the problem for the current (2.8.4.1) behavior is:
flatten([[],[]])
[[]]

It should return [].


---

Comment by mhampton created at 2007-09-11 16:48:26

Changing type from enhancement to defect.


---

Comment by mhampton created at 2007-09-11 16:48:26

Resolution changed from fixed to 


---

Comment by mhampton created at 2007-09-11 16:48:26

Changing status from closed to reopened.


---

Comment by mhampton created at 2007-09-11 16:48:58

Changing status from reopened to new.


---

Comment by mhampton created at 2007-09-11 16:50:32

Replying to [comment:6 mhampton]:

Sorry, I am not used to this formatting.  My example should be:

flatten([[],[]])

[[]]



---

Comment by mhampton created at 2007-09-11 20:31:33

Changing status from new to assigned.


---

Comment by mhampton created at 2007-09-11 20:33:24

Here is a new version that I believe fixes the problem.


```
def flatten(in_list, ltypes=(list, tuple)):
   """
   Flattens a nested list.

   INPUT:
       in_list -- a list or tuple
       ltypes -- optional list of particular types to flatten

   OUTPUT:
       a flat list of the entries of in_list

   EXAMPLES:
       sage: flatten([[1,1],[1],2])
       [1, 1, 1, 2]
       sage: flatten([[1,2,3], (4,5), [[[1],[2]]]])
       [1, 2, 3, 4, 5, 1, 2]

   In the following example, the vector isn't flattened because
   it is not given in the ltypes input. 
       sage: flatten((['Hi',2,vector(QQ,[1,2,3])],(4,5,6)))
       ['Hi', 2, (1, 2, 3), 4, 5, 6]

   We give the vector type and then even the vector gets flattened:
       sage: flatten((['Hi',2,vector(QQ,[1,2,3])], (4,5,6)), ltypes=(list, tuple,sage.modules.vector_rational_dense.Vector_rational_dense))
       ['Hi', 2, 1, 2, 3, 4, 5, 6]

   We flatten a finite field. 
       sage: flatten(GF(5))
       [0, 1, 2, 3, 4]
       sage: flatten([GF(5)])
       [Finite Field of size 5]
       sage: flatten([GF(5)], ltypes = (list, tuple, sage.rings.finite_field.FiniteField_prime_modn))
       [0, 1, 2, 3, 4]

   Degenerate cases:
      sage: flatten([[],[]])
      []
      sage: flatten([[[]]])
      []
   """
   index = 0
   new_list = [x for x in in_list]
   while index < len(new_list):
      while isinstance(new_list[index], ltypes):
         v = list(new_list[index])
         if len(v) != 0:
            new_list[index : index + 1] = v
         else:
            new_list.pop(index)
            index += -1
            break
      index += 1
   return new_list

```



---

Comment by mhampton created at 2007-09-11 20:33:24

Changing type from defect to task.


---

Comment by was created at 2007-09-11 23:00:21

Changing priority from minor to major.


---

Comment by was created at 2007-09-13 15:03:45

applied for sage-2.8.4.2.


---

Comment by was created at 2007-09-13 15:03:45

Resolution: fixed
