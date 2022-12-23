# Issue 4117: number_field_* leaks caused by gen.pyx's type(gen self)

Issue created by migration from https://trac.sagemath.org/ticket/4117

Original creator: mabshoff

Original creation time: 2008-09-14 09:54:26

Assignee: mabshoff

We leak medium to massive amount of memory in a lot of number field related code. This is caused by

```
     def type(gen self):
        return str(type_name(typ(self.g)))
```

in gen.pyx. The regular and obvious fix causes segfualts in other places (i.e. due to integer.pyx), so I am attaching a workaround fix that has some performance penalty.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-14 09:54:30

Changing status from new to assigned.


---

Attachment

This is a diff with some work around code


---

Comment by craigcitro created at 2008-09-14 10:34:09

Different fix for the same problem


---

Comment by mabshoff created at 2008-09-14 11:02:46

Resolution: fixed


---

Attachment

Merged trac-4117.patch in Sage 3.1.2.rc3


---

Comment by jdemeyer created at 2017-09-19 13:47:37

I wonder why this was a memleak. The original code looks correct, so either there was a bug in PARI/GP, a bug in Cython or a mis-identified memleak.

After 9 years, I am reverting this is in https://github.com/defeo/cypari2/commit/8f8ec558fd2864ea72f10068ed4f11843731199d
