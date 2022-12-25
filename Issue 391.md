# Issue 391: Bundle adding apropos to SAGE -- try `conductor**?' for an example.

archive/issues_000391.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: apropos ipython search\n\nThis bundle adds an apropos command to SAGE -- try `conductor**?' for an example.\n\nThe implementation is in sage.misc.apropos.  Some code that needs to be fast is in sage.misc.apropos_internals, a Pyrex module.\n\nThis bundle addresses some annoyances with IPython's introspection module.\n\nSee the hg log for details.\n\nIssue created by migration from https://trac.sagemath.org/ticket/391\n\n",
    "created_at": "2007-06-27T05:31:26Z",
    "labels": [
        "component: user interface",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Bundle adding apropos to SAGE -- try `conductor**?' for an example.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/391",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @williamstein

Keywords: apropos ipython search

This bundle adds an apropos command to SAGE -- try `conductor**?' for an example.

The implementation is in sage.misc.apropos.  Some code that needs to be fast is in sage.misc.apropos_internals, a Pyrex module.

This bundle addresses some annoyances with IPython's introspection module.

See the hg log for details.

Issue created by migration from https://trac.sagemath.org/ticket/391





---

archive/issue_comments_001907.json:
```json
{
    "body": "Attachment [ncalexan-apropos.hg](tarball://root/attachments/some-uuid/ticket391/ncalexan-apropos.hg) by @ncalexan created at 2007-06-27 05:42:07\n\nSummary of bundle, in a nutshell:\n\nsage: conductor**?\nsage.all.mwrank_EllipticCurve.conductor Command: Return the conductor of this curve, computed using Cremona's implementation of Tate's algorithm.\nsage.databases.cremona.LargeCremonaDatabase.conductor_range Command: Return the range of conductors that are covered by the database.\nsage.databases.cremona.LargeCremonaDatabase.largest_conductor Command: The largest conductor for which the database is complete. OUTPUT: int -- largest conductor\nsage.databases.cremona.LargeCremonaDatabase.smallest_conductor Command: The smallest conductor for which the database is complete. (Always 1.)\nsage.databases.cremona.MiniCremonaDatabase.conductor_range Command: Return the range of conductors that are covered by the database.\nsage.databases.cremona.MiniCremonaDatabase.largest_conductor Command: The largest conductor for which the database is complete. OUTPUT: int -- largest conductor\nsage.databases.cremona.MiniCremonaDatabase.smallest_conductor Command: The smallest conductor for which the database is complete. (Always 1.)\nsage.modular.dirichlet.DirichletCharacter.conductor Command: Computes and returns the conductor of this character.\nsage.schemes.elliptic_curves.ell_rational_field.EllipticCurve_rational_field.conductor Command: Returns the conductor of the elliptic curve.\n\nLists all callable things (classes, functions, etc) that have\nconductor in the last part of their dotted name.\n\nThe bundle also contains several enhancements to IPython's\nintrospection.  For example:\n\nsage: ?y\nParent:\t\tSymbolic Ring :: <class 'sage.calculus.calculus.SymbolicExpressionRing_class'>\nType:\t\tSymbolicVariable\nBase Class:\t<class 'sage.calculus.calculus.SymbolicVariable'>\nString Form:\ty\nNamespace:\tInteractive\nDocstring:\n    <no docstring>\n\nDisplays y's parent, which is very helpful.\n\nsage: ?2\nParent:\t\tInteger Ring :: <type 'sage.rings.integer_ring.IntegerRing_class'>\nType:\t\tInteger\nBase Class:\t<type 'sage.rings.integer.Integer'>\nString Form:\t2\nDocstring:\n    <no docstring>\n\nInterrogating literals works, more or less.\n\nsage: ?factor(6)\nType:\t\tFactorization\nBase Class:\t<class 'sage.structure.factorization.Factorization'>\nString Form:\t2 * 3\nLength:\t\t2\nDocstring:\n    <no docstring>\n\nDoes what you'd expect, even if it will mangle iterators in strange\ncorner cases.",
    "created_at": "2007-06-27T05:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/391#issuecomment-1907",
    "user": "https://github.com/ncalexan"
}
```

Attachment [ncalexan-apropos.hg](tarball://root/attachments/some-uuid/ticket391/ncalexan-apropos.hg) by @ncalexan created at 2007-06-27 05:42:07

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

archive/issue_comments_001908.json:
```json
{
    "body": "Hi Nick,\n\n(1) I applied the patch and when I do \n\n   conductor**?\n\nI get a segfault that results from an infinite loop; at least\nfor me, this happens in the function given below, which recursively calls\nitself and gets in an infinite loop.   This happens for me on \n32-bit Linux on both SAGE-2.6 vanilla and my latest SAGE-2.7\ndevel tree. \n\n\n\n```\n  cdef propos_name(object obj, object hist, object names, object matches):\n     objid = <int>(<void*> obj) # id(obj)\n     if PyDict_Contains(names, objid):\n         return <object>PyDict_GetItem(names, objid)\n     hist_record = <object>PyDict_GetItem(hist, objid)\n     parent_name = apropos_name(<object>PyTuple_GetItem(hist_record, 1), hist, names, matches)\n     name = parent_name + '.' + <object>PyTuple_GetItem(hist_record, 2)\n     PyList_Append(matches, (name, obj))\n     PyDict_SetItem(names, objid, name)\n     return name\n```\n\n\n\n2. The style of the above code surprises me.  The whole point of \nPyrex (and me choosing Pyrex for SAGE) is so that one never ever has\nto write code like that.  Do you really think it is actually \nsignificantly more readable or faster?   I personally find the \nfollowing, which is equivalent, more readable:\n\n  cdef propos_name(obj, hist, names, matches):\n     objid = <int>(<void*> obj) # id(obj)\n     if objid in names:\n         return names[objid]\n     hist_record = hist[objid]\n     parent_name = apropos_name(hist_record[1], hist, names, matches)\n     name = parent_name + '.' + hist_record[2]\n     matches.append((name, obj))\n     names[objid] = name\n     return name\n\n\n -- William",
    "created_at": "2007-06-30T04:52:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/391#issuecomment-1908",
    "user": "https://github.com/williamstein"
}
```

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

archive/issue_comments_001909.json:
```json
{
    "body": "NOT ready -- Nick never addressed my comments from \"06/29/2007 09:52:03 PM\".  The code is unpleasant (in many ways) since it directly is written against the python/c api instead of using Cython as it should be used.  Also, I got that segfault (though I haven't retested this).",
    "created_at": "2007-11-18T04:02:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/391#issuecomment-1909",
    "user": "https://github.com/williamstein"
}
```

NOT ready -- Nick never addressed my comments from "06/29/2007 09:52:03 PM".  The code is unpleasant (in many ways) since it directly is written against the python/c api instead of using Cython as it should be used.  Also, I got that segfault (though I haven't retested this).



---

archive/issue_comments_001910.json:
```json
{
    "body": "Nick said:\n\n```\nAt some point I will resubmit -- I'm just too busy right now.  I  \ndon't know what invalidate means but I'd appreciate it if the ticket  \n(and the patch!) stayed in TRAC. \n```\n\n\nCheers,\n\nMichael",
    "created_at": "2007-11-19T23:01:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/391#issuecomment-1910",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Nick said:

```
At some point I will resubmit -- I'm just too busy right now.  I  
don't know what invalidate means but I'd appreciate it if the ticket  
(and the patch!) stayed in TRAC. 
```


Cheers,

Michael



---

archive/issue_comments_001911.json:
```json
{
    "body": "Sorry William,\n\nYour comments are all valid.  Segfaults of course can't be applied :)\n\nThe unorthodox style (calling the C Python API directly) decreases the runtime by a large constant factor -- more than 10 times on my old machine.  I'll rewrite against Cython and not worry about that last constant factor.\n\nSoon :)\n\nNick",
    "created_at": "2007-11-19T23:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/391#issuecomment-1911",
    "user": "https://github.com/ncalexan"
}
```

Sorry William,

Your comments are all valid.  Segfaults of course can't be applied :)

The unorthodox style (calling the C Python API directly) decreases the runtime by a large constant factor -- more than 10 times on my old machine.  I'll rewrite against Cython and not worry about that last constant factor.

Soon :)

Nick



---

archive/issue_comments_001912.json:
```json
{
    "body": "Changing assignee from @williamstein to @ncalexan.",
    "created_at": "2007-11-27T04:54:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/391#issuecomment-1912",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Changing assignee from @williamstein to @ncalexan.



---

archive/issue_comments_001913.json:
```json
{
    "body": "I think we can mark this as invalid / wontfix since I can't access the bundle.  For something similar, see the Python package \"grasp\".",
    "created_at": "2013-07-21T22:31:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/391#issuecomment-1913",
    "user": "https://github.com/mwhansen"
}
```

I think we can mark this as invalid / wontfix since I can't access the bundle.  For something similar, see the Python package "grasp".



---

archive/issue_comments_001914.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2018-04-02T12:54:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/391#issuecomment-1914",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_001915.json:
```json
{
    "body": "Let us get rid of this very old ticket.",
    "created_at": "2018-04-02T12:54:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/391#issuecomment-1915",
    "user": "https://github.com/fchapoton"
}
```

Let us get rid of this very old ticket.



---

archive/issue_comments_001916.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2018-05-18T17:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/391#issuecomment-1916",
    "user": "https://github.com/videlec"
}
```

Resolution: wontfix



---

archive/issue_comments_001917.json:
```json
{
    "body": "closing positively reviewed duplicates",
    "created_at": "2018-05-18T17:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/391#issuecomment-1917",
    "user": "https://github.com/videlec"
}
```

closing positively reviewed duplicates



---

archive/issue_events_000413.json:
```json
{
    "actor": "https://github.com/videlec",
    "created_at": "2018-05-18T17:16:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/391",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/391#event-413"
}
```
