# Issue 6915: Getting rays from a polytope fails.

Issue created by migration from https://trac.sagemath.org/ticket/6915

Original creator: sbarthelemy

Original creation time: 2009-09-10 11:47:55

Assignee: mhampton

Keywords: polyhedra

See this example:


```
sage: p=Polyhedron([[0,0],[0,1],[1,0]])
sage: p.rays()                         
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/home/seb/.sage/temp/thinbox/5080/_home_seb__sage_init_sage_0.py in <module>()

/home/seb/.local/sage-4.1/local/lib/python2.6/site-packages/sage/geometry/polyhedra.pyc in rays(self)
    607                 return self._rays
    608         except AttributeError:
--> 609             dummy_verts = self.vertices(force_from_ieqs = True)
    610             self._checked_rays = True
    611             return self._rays

/home/seb/.local/sage-4.1/local/lib/python2.6/site-packages/sage/geometry/polyhedra.pyc in vertices(self, force_from_ieqs)
    397         """
    398         if (self._vertices == [] and self._ieqs != []) or force_from_ieqs:
--> 399             temp_poly_object = ieq_to_vert(self._ieqs, linearities = self._linearities, verbose = self._verbose)
    400             self._vertices = temp_poly_object._vertices
    401             self._vertex_incidences = temp_poly_object._vertex_incidences

/home/seb/.local/sage-4.1/local/lib/python2.6/site-packages/sage/geometry/polyhedra.pyc in ieq_to_vert(in_list, linearities, cdd_type, verbose)
   1426     """
   1427     # first we create the input for cddlib:
-> 1428     in_length = len(in_list[0])
   1429     in_str = 'H-representation\n'
   1430     if linearities != []:

IndexError: list index out of range

```



---

Comment by mhampton created at 2009-11-13 03:18:04

This will be fixed by #7109.


---

Comment by vbraun created at 2010-01-27 17:16:06

Resolution: fixed


---

Comment by vbraun created at 2010-01-27 17:16:06

fixed in 4.3.2.alpha0


---

Comment by mvngu created at 2010-01-28 04:20:14

Replying to [comment:2 vbraun]:
> fixed in 4.3.2.alpha0

Make sure you understand the procedure for closing tickets. See http://www.sagemath.org/doc/developer/trac.html#closing-tickets
