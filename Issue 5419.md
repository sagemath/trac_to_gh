# Issue 5419: moving fraction field to new coercion broke old pickles

Issue created by migration from https://trac.sagemath.org/ticket/5419

Original creator: craigcitro

Original creation time: 2009-03-02 06:40:28

Assignee: craigcitro

CC:  burcin

At some point, fraction fields were moved over to the new coercion model, which is good -- except that it broke all the old pickles. This thread on `sage-support` is about someone having a problem with them: http://groups.google.com/group/sage-support/browse_thread/thread/b5519db45a141819

The problem is that the old pickles don't have `_element_class` or `_element_constructor` fields, and there was no factory function in place -- so unpickling tries to directly create the object, which totally fails. Putting the old `__call__` method back in place is an ugly hack to get these to load, but it's not a good permanent solution. 




---

Comment by mabshoff created at 2009-03-02 07:00:10

Hmm,

how did this escape the pickle jar doctest?

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-02 07:00:10

Changing component from algebra to misc.
