# Issue 5530: add absolute_diameter and relative_diameter to CIF (ComplexIntervalField)

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-03-16 17:31:00

Assignee: somebody

Keywords: complex interval field diameter absolute relative

RIF has the above methods; it would be nice if CIF did too, defined (like diameter()) as the max of the real and imaginary diameters.


---

Comment by cwitty created at 2009-03-16 20:27:58

Is that the right definition for relative_diameter?  Another possibility would be the absolute diameter divided by the absolute value of the center of the interval.

For example, a tiny interval centered at 1+eps*I (for tiny eps) would have a huge relative diameter under Nick's definition and a tiny relative diameter under mine.
