# Issue 4955: Magma needs write access to $SAGE_ROOT/data/excode/magma

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-01-08 17:15:56

Assignee: was

Keywords: magma

This was on [sage-devel] (2009-01-08):
>> RuntimeError: While attempting to compile /usr/local/sage-3.2.3/data/
>> extcode//magma/latex/latex.m (Data file non-existent):
>> Can't open lock file /usr/local/sage-3.2.3/data/extcode//magma/latex/
>> latex.lck for writing (Permission denied)
>>
>> While attempting to compile /usr/local/sage-3.2.3/data/extcode//magma/
>> sage/basic.m (Data file non-existent):
>> Can't open lock file /usr/local/sage-3.2.3/data/extcode//magma/sage/
>> basic.lck for writing (Permission denied
>
> It seems like you need write access to extcode (see above) at least for the
> first time you're running Magma from Sage. IIRC there was some talk about
> lifting this requirement somehow.

The only idea I have to deal with this is to copy all of extcode/magma
into .sage/extcode/magma say, and then have sage only use magma code
that's in .sage/extcode/magma/.
Whenever sage is upgraded, the .sage/extcode/magma would have to get
deleted and re-copied, using a facility similar to how the Gap
workspace always gets updated when Sage has been upgraded.


---

Comment by was created at 2009-01-23 07:39:28

dup of #5041


---

Comment by was created at 2009-01-23 07:39:28

Resolution: duplicate
