# Issue 391: Bundle adding apropos to SAGE -- try `conductor**?' for an example.

Issue created by migration from https://trac.sagemath.org/ticket/391

Original creator: ncalexan

Original creation time: 2007-06-27 05:31:26

Assignee: was

Keywords: apropos ipython search

This bundle adds an apropos command to SAGE -- try `conductor**?' for an example.

The implementation is in sage.misc.apropos.  Some code that needs to be fast is in sage.misc.apropos_internals, a Pyrex module.

This bundle addresses some annoyances with IPython's introspection module.

See the hg log for details.


---

Attachment

Summary of bundle, in a nutshell:

sage: conductor**?
sage.all.mwrank_EllipticCurve.conductor Command: Return the conductor of this curve, computed using Cremona's implementation of Tate's algorithm.
sage.databases.cremona.LargeCremonaDatabase.conductor_range Command: Return the range of conductors that are covered by the database.
sage.databases.cremona.LargeCremonaDatabase.largest_conductor Command: The largest conductor for which the database is complete. OUTPUT: int -- largest conductor
sage.databases.cremona.LargeCremonaDatabase.smallest_conductor Command: The smallest conductor for which the database is complete. (Always 1.)
sage.databases.cremona.MiniCremonaDatabase.conductor_range Command: Return the range of conductors that are covered by the database.
sage.databases.cremona.MiniCremonaDatabase.largest_conductor Command: The largest conductor for which the database is complete. OUTPUT: int -- largest conductor
sage.databases.cremona.MiniCremonaDatabase.smallest_conductor Command: The smallest conductor for which the database is complete. (Always 1.)
sage.modular.dirichlet.DirichletCharacter.conductor Command: Computes and returns the conductor of this character.
sage.schemes.elliptic_curves.ell_rational_field.EllipticCurve_rational_field.conductor Command: Returns the conductor of the elliptic curve.

Lists all callable things (classes, functions, etc) that have
conductor in the last part of their dotted name.

The bundle also contains several enhancements to IPython's
introspection.  For example:

sage: ?y
Parent:		Symbolic Ring :: <class 'sage.calculus.calculus.SymbolicExpressionRing_class'>
Type:		SymbolicVariable
Base Class:	<class 'sage.calculus.calculus.SymbolicVariable'>
String Form:	y
Namespace:	Interactive
Docstring:
    <no docstring>

Displays y's parent, which is very helpful.

sage: ?2
Parent:		Integer Ring :: <type 'sage.rings.integer_ring.IntegerRing_class'>
Type:		Integer
Base Class:	<type 'sage.rings.integer.Integer'>
String Form:	2
Docstring:
    <no docstring>

Interrogating literals works, more or less.

sage: ?factor(6)
Type:		Factorization
Base Class:	<class 'sage.structure.factorization.Factorization'>
String Form:	2 * 3
Length:		2
Docstring:
    <no docstring>

Does what you'd expect, even if it will mangle iterators in strange
corner cases.


---

Comment by was created at 2007-06-30 04:52:03

Hi Nick,

(1) I applied the patch and when I do 

   conductor**?

I get a segfault that results from an infinite loop; at least
for me, this happens in the function given below, which recursively calls
itself and gets in an infinite loop.   This happens for me on 
32-bit Linux on both SAGE-2.6 vanilla and my latest SAGE-2.7
devel tree. 



```
  cdef propos_name(object obj, object hist, object names, object matches):
     objid = <int>(<void*> obj) # id(obj)
     if PyDict_Contains(names, objid):
         return <object>PyDict_GetItem(names, objid)
     hist_record = <object>PyDict_GetItem(hist, objid)
     parent_name = apropos_name(<object>PyTuple_GetItem(hist_record, 1), hist, names, matches)
     name = parent_name + '.' + <object>PyTuple_GetItem(hist_record, 2)
     PyList_Append(matches, (name, obj))
     PyDict_SetItem(names, objid, name)
     return name
```



2. The style of the above code surprises me.  The whole point of 
Pyrex (and me choosing Pyrex for SAGE) is so that one never ever has
to write code like that.  Do you really think it is actually 
significantly more readable or faster?   I personally find the 
following, which is equivalent, more readable:

  cdef propos_name(obj, hist, names, matches):
     objid = <int>(<void*> obj) # id(obj)
     if objid in names:
         return names[objid]
     hist_record = hist[objid]
     parent_name = apropos_name(hist_record[1], hist, names, matches)
     name = parent_name + '.' + hist_record[2]
     matches.append((name, obj))
     names[objid] = name
     return name


 -- William


---

Comment by was created at 2007-11-18 04:02:00

NOT ready -- Nick never addressed my comments from "06/29/2007 09:52:03 PM".  The code is unpleasant (in many ways) since it directly is written against the python/c api instead of using Cython as it should be used.  Also, I got that segfault (though I haven't retested this).


---

Comment by mabshoff created at 2007-11-19 23:01:45

Nick said:

```
At some point I will resubmit -- I'm just too busy right now.  I  
don't know what invalidate means but I'd appreciate it if the ticket  
(and the patch!) stayed in TRAC. 
```


Cheers,

Michael


---

Comment by ncalexan created at 2007-11-19 23:06:40

Sorry William,

Your comments are all valid.  Segfaults of course can't be applied :)

The unorthodox style (calling the C Python API directly) decreases the runtime by a large constant factor -- more than 10 times on my old machine.  I'll rewrite against Cython and not worry about that last constant factor.

Soon :)

Nick


---

Comment by cwitty created at 2007-11-27 04:54:34

Changing assignee from was to ncalexan.


---

Comment by mhansen created at 2013-07-21 22:31:21

I think we can mark this as invalid / wontfix since I can't access the bundle.  For something similar, see the Python package "grasp".


---

Comment by chapoton created at 2018-04-02 12:54:36

Changing status from needs_work to positive_review.


---

Comment by chapoton created at 2018-04-02 12:54:36

Let us get rid of this very old ticket.


---

Comment by vdelecroix created at 2018-05-18 17:16:26

Resolution: wontfix


---

Comment by vdelecroix created at 2018-05-18 17:16:26

closing positively reviewed duplicates
