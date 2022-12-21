# Issue 1017: [with (partial) patch] add an option to solve to return a list of dictionaries instead of a list of lists of equations.

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-10-28 04:02:22

Assignee: was

It's terribly convenient to be able to write:

```
solutions=solve([x^2+y^2 == 1, y^2 == x^3 + x + 1], x, y, solution_dict=True);
for solution in solutions: 
    print solution[x].n(digits=3), ",", solution[y].n(digits=3)
```


to print out a list of the solutions or to refer back to the solved values.  This patch implements a naive approach to solution_dict.




---

Attachment

patch is no longer a partial patch.

I just noticed one modification.


```
sol_list_dict=blah
return sol_list_dict
```

could be shortened to

```
return blah
```



---

Comment by jason created at 2007-10-28 04:10:01

I meant, in the last part of the patch:


```
sol_dict=blah
return sol_dict
```

could be shortened to

```
return blah
```



---

Comment by cwitty created at 2007-10-28 18:38:53

Resolution: fixed
