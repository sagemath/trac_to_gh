# Issue 2001: --long doctests -- seven files have doctst failures in sage-2.10.rc3

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-31 06:37:42

Assignee: failure


```
        sage -t -long devel/sage-main/sage/groups/perm_gps/cubegroup.py
        sage -t -long devel/sage-main/sage/groups/group.pyx
        sage -t -long devel/sage-main/sage/groups/matrix_gps/matrix_group.py
        sage -t -long devel/sage-main/sage/crypto/mq/sr.py
        sage -t -long devel/sage-main/sage/libs/pari/gen.pyx
        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/sha.py
        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_number_field.py
```


I've attached the full test log for this run.  (I'm too tired to do more right now.)  This ticket might get busted up into several smaller ones or something...


---

Attachment


---

Comment by was created at 2008-01-31 06:40:01

(I think the preview of the attached file is broken and only shows the second half.  So you should download the file and view it locally.)


---

Comment by mabshoff created at 2008-01-31 08:06:00

From the above log:

```
sage -t -long devel/sage-main/sage/groups/perm_gps/cubegroup.py
sage -t -long devel/sage-main/sage/groups/group.pyx
sage -t -long devel/sage-main/sage/groups/matrix_gps/matrix_group.py
sage -t -long devel/sage-main/sage/crypto/mq/sr.py
sage -t -long devel/sage-main/sage/libs/pari/gen.pyx
sage -t -long devel/sage-main/sage/schemes/elliptic_curves/sha.py
sage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_number_field.py
```

`devel/sage-main/sage/crypto/mq/sr.py` works fine, it just times out. I am working on patches for some of the other issues.

Cheers,

Michael


---

Attachment

`schemes/elliptic_curves/sha.py` also works fine, it just timed out with the 3 minute default timeout value. There is also a patch up for the `groups/matrix_gps/matrix_group.py` doctest failure.

Cheers,

Michael


---

Attachment

The fix might be needed due to the pari 2.3.3 update.


---

Comment by mabshoff created at 2008-01-31 08:34:01

Four down, three to go. I am wandering if we shouldn't remove the two remaining `#long` from  gen.pyx since doctesting with the long option needs 12 seconds versus 5 seconds without.


---

Comment by mabshoff created at 2008-01-31 08:37:42

The remaining issues:

```
sage -t -long devel/sage-main/sage/groups/perm_gps/cubegroup.py
**********************************************************************
File "cubegroup.py", line 918:
    sage: C.solve(algorithm='gap')  # long time
Expected:
    'L*R'
Got:
    'L R'
**********************************************************************
```

And:

```
sage -t -long devel/sage-main/sage/groups/group.pyx
**********************************************************************
File "group.pyx", line 146:
    sage: G.show3d(vertex_size=0.03, edge_size=0.01, edge_size2=0.02, vertex_colors={(1,1,1):x.vertices()}, bgcolor=(0,0,0), color_by_label=True, xres=700, yres=700, iterations=200) # long time
Exception raised:
    Traceback (most recent call last):
      File "/home/was/build/sage-2.10.1.rc3/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_17[6]>", line 1, in <module>
        G.show3d(vertex_size=RealNumber('0.03'), edge_size=RealNumber('0.01'), edge_size2=RealNumber('0.02'), vertex_colors={(Integer(1),Integer(1),Integer(1)):x.vertices()}, bgcolor=(Integer(0),Integer(0),Integer(0)), color_by_label=True, xres=Integer(700), yres=Integer(700), iterations=Integer(200)) # long time###line 146:
    sage: G.show3d(vertex_size=0.03, edge_size=0.01, edge_size2=0.02, vertex_colors={(1,1,1):x.vertices()}, bgcolor=(0,0,0), color_by_label=True, xres=700, yres=700, iterations=200) # long time
    AttributeError: 'SymbolicVariable' object has no attribute 'vertices'
**********************************************************************
```

Finally:

```
sage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_number_field.py
**********************************************************************
File "ell_number_field.py", line 137:
    sage: v = E.simon_two_descent(); v  # long time
Expected:
    (1, -1, [])
Got:
    (1, 3, [(-4 : -3/2*a + 3/2 : 1), (8 : 18 : 1), (15/32*a - 59/32 : -75/128*a + 519/128 : 1), (-286/361 : -7215/13718*a - 75/722 : 1), (15/8*a + 19/8 : -105/16*a + 3/16 : 1), (-2 : 3 : 1)])
**********************************************************************
```


Cheers,

Michael


---

Comment by was created at 2008-02-02 09:34:16

this fixes all remaining problems (I claim, and have tested fairly carefully)


---

Attachment

All three patches look good, i.e. was reviewed mine and the other way around.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-02 09:52:03

Resolution: fixed


---

Comment by mabshoff created at 2008-02-02 09:52:03

Merged all three patches in Sage 2.10.1.rc5
