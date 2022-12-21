# Issue 4659: remove an extra 'cdef class Integer' line from integer.pyx

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2008-11-30 00:44:16

Assignee: somebody

CC:  robertwb

Keywords: integer

In the file sage/rings/integer.pyx, line 288 says 

```
    cdef class Integer (sage.structure.element.EuclideanDomainElement): 
```

followed by documentation and the various methods for this class.  But earlier in the file, line 137 says 

```
    cdef class Integer(sage.structure.element.EuclideanDomainElement) 
```

The attached patch removes line 137.


---

Attachment

Looks good to me. As RobertWB said in http://groups.google.com/group/sage-devel/t/3d76203eeed29ec5 this can go in.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-30 05:39:02

Resolution: fixed


---

Comment by mabshoff created at 2008-11-30 05:39:02

Merged in Sage 3.2.1.rc1. Reviewer credit goes to RobertWB
