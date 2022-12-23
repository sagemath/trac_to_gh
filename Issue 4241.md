# Issue 4241: magma -- memory is never freed in the interface when MagmaElement's are deleted

Issue created by migration from https://trac.sagemath.org/ticket/4241

Original creator: was

Original creation time: 2008-10-04 05:01:55

Assignee: was

Observe:

```
sage: a = magma('10000')
sage: a.name()
'_sage_[1]'
sage: del a
sage: magma.eval('_sage_[1]')
'10000'
```


Whenever anybody ever creates a MagmaElement via the Magma interface, it doesn't get deleted.  This is because possible (1) the clear method in magma.py is commented out, and/or (2) the _available_var list that gets appended to in (1) isn't actually used by magma.py, so e.g., _sage_[1] in the example above never gets re-used. 



---

Comment by was created at 2008-10-04 05:02:06

Changing status from new to assigned.


---

Comment by was created at 2008-10-23 22:01:25

Here's a vivid illustration of the memory leakage, which of course we know is there by reading the code:

```
sage: a = [magma('3^100000') for _ in range(1000)]
sage: magma.GetMemoryUsage()
42917912
sage: del a
sage: magma.GetMemoryUsage()
42917912
sage: a = [magma('3^100000') for _ in range(1000)]
sage: magma.GetMemoryUsage()
69103640
sage: del a
sage: magma.GetMemoryUsage()
69103640
```



---

Comment by was created at 2008-10-23 23:26:50

Without patch:

```
sage: a = [magma('3^100000') for _ in range(1000)]; del a;magma.GetMemoryUsage() 
42917912
sage: a = [magma('3^100000') for _ in range(1000)]; del a;magma.GetMemoryUsage() 
94192176
sage: a = [magma('3^100000') for _ in range(1000)]; del a;magma.GetMemoryUsage()
121287216
```

With patch:

```
sage: a = [magma('3^100000') for _ in range(1000)]; del a;magma.GetMemoryUsage()
40817200
sage: a = [magma('3^100000') for _ in range(1000)]; del a;magma.GetMemoryUsage()
41820720
sage: a = [magma('3^100000') for _ in range(1000)]; del a;magma.GetMemoryUsage()
41820720
sage: a = [magma('3^100000') for _ in range(1000)]; del a;magma.GetMemoryUsage()
41820720
sage: a = [magma('3^100000') for _ in range(1000)]; del a;magma.GetMemoryUsage()
41820720
```

}}}


---

Attachment


---

Comment by mabshoff created at 2008-10-27 02:53:21

Patch looks good to me. There is a spelling error in the new docstring: "clearlying" _ i will fix it in the patch I will apply.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-27 04:19:14

Merged in Sage 3.2.alpha1


---

Comment by mabshoff created at 2008-10-27 04:19:14

Resolution: fixed
