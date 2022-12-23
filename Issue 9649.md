# Issue 9649: c_lib/include/interrupt.h: rename FOO_H

Issue created by migration from https://trac.sagemath.org/ticket/9649

Original creator: jdemeyer

Original creation time: 2010-07-31 08:23:54

Assignee: jason

In c_lib/include/interrupt.h, there is

```
#ifndef FOO_H
#define FOO_H
```

to protect the header.  This FOO_H should be changed.


---

Comment by jdemeyer created at 2010-07-31 08:24:53

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2010-07-31 08:25:43

Rename FOO_H to C_LIB_INCLUDE_INTERRUPT_H


---

Comment by robertwb created at 2010-07-31 19:00:35

Changing status from needs_review to positive_review.


---

Attachment

This is obviously code that went in before the referee process :).


---

Comment by mpatel created at 2010-08-09 09:41:41

Resolution: fixed
