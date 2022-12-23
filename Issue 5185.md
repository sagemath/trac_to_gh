# Issue 5185: [with patch, needs review] is_zero is broken for sparse vectors

Issue created by migration from https://trac.sagemath.org/ticket/5185

Original creator: jhpalmieri

Original creation time: 2009-02-05 04:05:51

Assignee: tbd

Consider this:

```
sage: v = vector({1: 1, 3: -1})
sage: w = vector({1: -1, 3: 1})
sage: v+w
(0, 0, 0, 0)
sage: (v+w).is_zero()
False
```


I see two things wrong with the source code:

1. in modules/free_module_element.pyx, it says

```
    def __nonzero__(self):
        """
        EXAMPLES:
            sage: V = vector(ZZ, [0, 0, 0, 0])
            sage: bool(V)
            False
            sage: V = vector(ZZ, [1, 2, 3, 5])
            sage: bool(V)
            True
        """
        return self != 0
```

I don't understand the relevance of the doctest at all, and the actual code should probably say something like `self != self.parent()(0)`.  In fact, this is completely unnecessary, because this class inherits from ModuleElement, which has `__nonzero__` defined in precisely this way -- see structure/element.pyx.

2. in structure/element.pyx, it says

```
    def is_zero(self):
        """
        Return True if self equals self.parent()(0). The default
        implementation is to fall back to 'not self.__nonzero__'.

        NOTE: Do not re-implement this method in your subclass but
        implement __nonzero__ instead.
        """
        return not self
```

The code `return not self` looks like a typo: it should be `return not self.__nonzero__()` -- read the docstring!

The patch deals with both of these issues by fixing the code in element.pyx and by deleting the code in free_module_element.pyx.  It also adds a doctest to element.pyx, verifying that the above vector example now works.




---

Attachment


---

Comment by mabshoff created at 2009-02-08 22:10:12

Changing priority from major to critical.


---

Comment by mabshoff created at 2009-02-08 22:10:12

Changing assignee from tbd to cwitty.


---

Comment by mabshoff created at 2009-02-08 22:10:12

Oops, sounds like another 3.3 blocker or at least critical ticket to me. I don't think this is "algebra", but other than "misc" I can't come up with any better category.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-08 22:10:12

Changing component from algebra to misc.


---

Comment by mabshoff created at 2009-02-08 22:11:06

Changing assignee from cwitty to jhpalmieri.


---

Comment by mabshoff created at 2009-02-08 22:11:06

John,

please accept tickets once you post a patch since you should own all tickets you resolved. As a first step I am reassigning this to you.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-09 12:39:36

With this patch applied to my current 3.3.rc0 merge tree all doctests pass.

Cheers,

Michael


---

Comment by cwitty created at 2009-02-10 06:19:36

Actually, if `__nonzero__` is implemented for a class, then `not self` is totally equivalent to `not self.__nonzero__()`, except faster.  (Checking to see if an object is "true" calls the `__nonzero__` method using an optimized C calling convention; calling the method directly uses a slower, Python calling convention.)

So the change to the body of is_zero should be reverted.  (Maybe some comments could be added to clarify the situation.)


---

Comment by jhpalmieri created at 2009-02-10 16:13:36

Oh, I didn't know that.  Here's a new patch which just deletes the `__nonzero__` method from free_module_element.pyx, leaving element.pyx unchanged.


---

Attachment


---

Comment by jhpalmieri created at 2009-02-10 16:14:13

(Just apply 5185-new.patch.)


---

Attachment


---

Comment by cwitty created at 2009-02-11 02:29:07

Since every bug fix should have a doctest, I rescued John's doctest from his first patch, and added a tiny bit of documentation.

Positive review.  Apply 5185-new.patch, then 5185-reviewer.patch.


---

Comment by jhpalmieri created at 2009-02-11 02:36:28

Excellent.


---

Comment by mabshoff created at 2009-02-11 04:06:54

Resolution: fixed


---

Comment by mabshoff created at 2009-02-11 04:06:54

Merged 5185-new.patch and 5185-reviewer.patch in Sage 3.3.rc0.

Cheers,

Michael
