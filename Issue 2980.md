# Issue 2980: itanium (RHEL 5) -- weyl_group.py is broken on itanium

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-21 03:21:13

Assignee: mhansen


```
sage -t  devel/sage/sage/combinat/root_system/weyl_group.py **********************************************************************
File "/home/wstein/sage-3.0.rc0/tmp/weyl_group.py", line 235:
    sage: [WeylGroup(t).long_element().length() for t in ['A',5],['B',3],['C',3],['D',4],['G',2],['F',4],['E',6]]
Exception raised:
    Traceback (most recent call last):
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_13[1]>", line 1, in <module>
        [WeylGroup(t).long_element().length() for t in ['A',Integer(5)],['B',Integer(3)],['C',Integer(3)],['D',Integer(4)],['G',Integer(2)],['F',Integer(
4)],['E',Integer(6)]]###line 235:
    sage: [WeylGroup(t).long_element().length() for t in ['A',5],['B',3],['C',3],['D',4],['G',2],['F',4],['E',6]]
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/combinat/root_system/weyl_group.py", line 271, in long_element
        return self.__call__(m)
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/combinat/root_system/weyl_group.py", line 146, in __call__
        raise TypeError, "no way to coerce element into self."
    TypeError: no way to coerce element into self.
**********************************************************************
1 items had failures:
   1 of   2 in __main__.example_13
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wstein/sage-3.0.rc0/tmp/.doctest_weyl_group.py
         [61.1 s]
```



---

Comment by was created at 2008-04-21 03:26:46


```
20:18 < mhansen> That Weyl group issue on Itanium is weird.  The code that raises that error is from a call 
                 in GAP.
20:19 < wstein> Gap is potentially broken on itanium.
20:19 < wstein> We have to build it -O0 to get it to build at all.
20:19 < wstein> So possibly all problems originate from that.
20:20 < wstein> See #2209.
20:20 < mhansen> I'm pretty sure that's the issue since the code causing that error is very simple and works 
                 on lots of other things.

```



---

Comment by mabshoff created at 2008-04-21 04:34:37

This will be fixed by #2984.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-21 06:54:26

Resolution: fixed


---

Comment by mabshoff created at 2008-04-21 06:54:26

Fixed by merging #2984.
