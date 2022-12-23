# Issue 4694: ?? for decorated functions shows the source of the decorator

Issue created by migration from https://trac.sagemath.org/ticket/4694

Original creator: whuss

Original creation time: 2008-12-04 10:28:11

Assignee: was


```
sage: plot??
Type:           function
Base Class:     <type 'function'>
String Form:    <function plot at 0xb6f1f454>
Namespace:      Interactive
File:           /.../site-packages/sage/plot/misc.py
Definition:     plot(*args, **kwds)
Source:
        @wraps(func)
        def wrapper(*args, **kwds):
            for old_name, new_name in self.renames.items():
                if kwds.has_key(old_name) and not kwds.has_key(new_name):
                    kwds[new_name] = kwds[old_name]
                    del kwds[old_name]
            return func(*args, **kwds)
```




---

Comment by mabshoff created at 2008-12-04 10:35:42

Resolution: duplicate


---

Comment by mabshoff created at 2008-12-04 10:35:42

Hi,

this is a dupe of #4672. There is a patch over there that needs one doctest fixed to be merged, so feel free to look into it.

Cheers,

Michael
