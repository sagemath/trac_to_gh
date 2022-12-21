# Issue 5810: Sage 3.4.1.rc3: Fedora 10/64 - unable to start Maxima issue in shapes.pyx

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-04-17 11:27:10

Assignee: mabshoff

The following pops up regularly on some FC10 systems:

```
sage -t -long "devel/sage/sage/plot/plot3d/shapes.pyx"      Exception exceptions.TypeError: TypeError(RuntimeError('Unable to start maxima',),) in 'sage.structure.parent_old._unregister_pair' ignored
**********************************************************************
File "/space/wstein/farm/sage-3.4.1.rc3/devel/sage/sage/plot/plot3d/shapes.pyx", line 267:
    sage: G += sum(Cylinder(.2, 1).translate(cos(2*pi*n/9), sin(2*pi*n/9), 0) for n in [1..9])Exception raised:
    Traceback (most recent call last):
      File "/space/wstein/farm/sage-3.4.1.rc3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/space/wstein/farm/sage-3.4.1.rc3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/space/wstein/farm/sage-3.4.1.rc3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[7]>", line 1, in <module>
        G += sum(Cylinder(RealNumber('.2'), Integer(1)).translate(cos(Integer(2)*pi*n/Integer(9)), sin(Integer(2)*pi*n/Integer(9)), Integer(0)) for n in (ellipsis_range(I
nteger(1),Ellipsis,Integer(9))))###line 267:
    sage: G += sum(Cylinder(.2, 1).translate(cos(2*pi*n/9), sin(2*pi*n/9), 0) for n in [1..9])
      File "<doctest __main__.example_10[7]>", line 1, in <genexpr>
        G += sum(Cylinder(RealNumber('.2'), Integer(1)).translate(cos(Integer(2)*pi*n/Integer(9)), sin(Integer(2)*pi*n/Integer(9)), Integer(0)) for n in (ellipsis_range(I
nteger(1),Ellipsis,Integer(9))))###line 267:
    sage: G += sum(Cylinder(.2, 1).translate(cos(2*pi*n/9), sin(2*pi*n/9), 0) for n in [1..9])
      File "element.pyx", line 1154, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:10558)
      File "coerce.pyx", line 706, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6543)
      File "coerce.pyx", line 1152, in sage.structure.coerce.CoercionModel_cache_maps.get_action (sage/structure/coerce.c:11646)
      File "coerce.pyx", line 1275, in sage.structure.coerce.CoercionModel_cache_maps.discover_action (sage/structure/coerce.c:12920)
      File "parent.pyx", line 1142, in sage.structure.parent.Parent.get_action (sage/structure/parent.c:11816)
      File "parent_old.pyx", line 586, in sage.structure.parent_old.Parent._get_action_ (sage/structure/parent_old.c:8141)
      File "parent_old.pyx", line 197, in sage.structure.parent_old.Parent.get_action_c (sage/structure/parent_old.c:2998)
      File "parent_old.pyx", line 209, in sage.structure.parent_old.Parent.get_action_impl (sage/structure/parent_old.c:3333)
      File "parent_old.pyx", line 268, in sage.structure.parent_old.Parent.get_action_c_impl (sage/structure/parent_old.c:4193)
      File "parent_old.pyx", line 635, in sage.structure.parent_old._register_pair (sage/structure/parent_old.c:9303)
    NotImplementedError: Infinite loop in multiplication of 
                                           0 (parent Symbolic Ring) and 1 (parent Integer Ring)!
**********************************************************************
```


One would guess that disabling mmap in Maxima might fix this.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-19 00:17:03

The disabling of mmap should happen in #5662, so hopefully that ticket will fix it.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-19 06:32:07

The updated clisp-2.47.spkg seems to fix this. I am rerunning doctests on the box to see if any other problems are popping up.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-20 03:11:46

Resolution: fixed


---

Comment by mabshoff created at 2009-04-20 03:11:46

This has been fixed by #5662 and #5823.

Cheers,

Michael
