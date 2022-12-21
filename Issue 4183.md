# Issue 4183: ?? can't always find the source for new style classes

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-09-24 01:25:02

Assignee: was

I think one needs to check bit 9 (Py_TPFLAGS_HEAPTYPE) of the __class__.__flags__ attribute to see if one should do the same trick as in #2777 or something like that.


---

Comment by aginiewicz created at 2008-09-24 02:40:50

I didn't though about if for #2777, but based on [http://psyco.sourceforge.net/psycoguide/metaclass.html](http://psyco.sourceforge.net/psycoguide/metaclass.html), i.e. part "... if `x` contains an instance of ... a new-style class, then `type(x)` will be `x.__class__` instead of `types.InstanceType`." - I think that test like:

`hasattr(arg, __class__) and type(arg) == arg.__class__`

could do the thing, maybe not best way but it works for example with instances of `sage.rings.rational_field.RationalField`... no code to attach yet (just in-place tests in console, it's 4:30 am here) - will try to do some small patch soon


---

Comment by robertwb created at 2008-09-24 05:10:38

Ah, that sounds like a much nicer way to detect it.


---

Comment by aginiewicz created at 2008-09-24 22:16:03

Used other approach, above with type equal class is true for too much, for example:


```
sage: type(arg)
<type 'function'>
sage: arg.__class__
<type 'function'>
```


Check like:

`obj.__class__.__module__ not in ('__builtin__', 'exceptions')`

seems to work both old and new style classes, the problem seems to be that everything is object, so best we can do is check if something is object of non built-in class


---

Comment by aginiewicz created at 2008-09-25 00:43:01

second try


---

Attachment

in previous patch I trusted the "everything is object" too much... so not everything have `__class__`, that's why I added back the check for `__class__` and also `__module__`, though every class should have one... better safe than sorry


---

Comment by robertwb created at 2008-10-14 19:44:10

Applies cleanly and works well. This is very nice.


---

Comment by robertwb created at 2008-10-14 19:44:27

Note: apply only the second patch.


---

Comment by mabshoff created at 2008-10-18 12:03:30

Resolution: fixed


---

Comment by mabshoff created at 2008-10-18 12:03:30

Merged 4183-2.patch in Sage 3.2.alpha0
