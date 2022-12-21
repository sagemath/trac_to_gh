# Issue 4182: plot3d fails with 'IndexError: list index out of range'

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2008-09-23 22:52:24

Assignee: was


```
sage: def g(x,y): 
...            if y <= 0 or y >= x**2: 
...                return 0 
...           else: 
...               return 1 
sage: plot3d(g, (-3, 3), (-3, 3), adaptive=True) 
```

fails, returning

```
Traceback (most recent call last): 
  File "<stdin>", line 1, in <module> 
  File "/home/palmieri/.sage/sage_notebook/worksheets/admin/37/code/ 
7.py", line 6, in <module> 
    plot3d(g, (-Integer(3), Integer(3)), (-Integer(3), Integer(3)), 
adaptive=True) 
  File "/usr/local/share/sage/local/lib/python2.5/site-packages/ 
SQLAlchemy-0.4.6-py2.5.egg/", line 1, in <module> 
  File "/home/palmieri/Documents/sage-3.1.2/local/lib/python2.5/site- 
packages/sage/plot/plot3d/plot3d.py", line 157, in plot3d 
    P = plot3d_adaptive(f, urange, vrange, **kwds) 
  File "/home/palmieri/Documents/sage-3.1.2/local/lib/python2.5/site- 
packages/sage/plot/plot3d/plot3d.py", line 255, in plot3d_adaptive 
    G.set_texture(texture[k], opacity=opacity) 
IndexError: list index out of range
```



---

Attachment


---

Comment by jhpalmieri created at 2008-10-20 21:25:17

Here's a patch.  I was getting an index error in the last line in this code snippet:

```
                span = len(texture) / (max_z - min_z)    # max to avoid dividing by 0
            parts = P.partition(lambda x,y,z: int((z-min_z)*span))
        all = []
        for k, G in parts.iteritems():
            G.set_texture(texture[k], opacity=opacity)
```

The function g(x,y) described above is discontinuous at various places, and I think this was making the `k` in the last line of this snippet equal to 128 while `len(texture)` was also 128. Changing the definition of `span` in the first line, as this patch does, I hope should make `k` always strictly less than `len(texture)`.


---

Comment by anakha created at 2008-10-23 19:50:39

This does fix the problem and looks ok.


---

Comment by mabshoff created at 2008-10-26 03:18:30

Resolution: fixed


---

Comment by mabshoff created at 2008-10-26 03:18:30

Merged in Sage 3.2.alpha1
