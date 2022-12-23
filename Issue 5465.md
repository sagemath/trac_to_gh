# Issue 5465: render3d for groebner fans is totally broken

Issue created by migration from https://trac.sagemath.org/ticket/5465

Original creator: was

Original creation time: 2009-03-10 08:03:00

Assignee: mhampton


```
teragon:~ wstein$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: P.<a,b,c> = PolynomialRing(QQ,3, order='lex')
sage: sage.rings.ideal.Katsura(P,3).groebner_fan().render3d()
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)
| Sage Version 3.4.alpha0, Release Date: 2009-02-24                  |
| Type notebook() for the GUI, and license() for information.        |
/Users/wstein/.sage/temp/teragon.local/68617/_Users_wstein__sage_init_sage_0.py in <module>()

/Users/wstein/build/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.pyc in render3d(self, verbose)
   1067         g_cones_ieqs = [self._cone_to_ieq(q) for q in g_cones_facets]
   1068         # Now the cones are intersected with a plane:
-> 1069         cone_info = [ieq_to_vert(q,linearities=[[1,-1,-1,-1,-1]]) for q in g_cones_ieqs]
   1070 	if verbose:
   1071 	    for x in cone_info:

/Users/wstein/build/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/geometry/polyhedra.pyc in ieq_to_vert(in_list, linearities, cdd_type, verbose)
   1268             adj_index = index
   1269     # read the vertices and rays:
-> 1270     for index in range(vert_index,len(ans_lines)):
   1271         a_line = ans_lines[index]
   1272         if a_line.find('end') != -1: break

UnboundLocalError: local variable 'vert_index' referenced before assignment
```



---

Comment by mhampton created at 2009-03-14 15:42:54

This needs to have a better error message - the example here is trying to render a 2D fan with render3d, which doesn't make sense.  So the code should check the dimension first, which I will do this week (I am currently traveling until Tuesday which makes development a bit harder).
-Marshall


---

Attachment

Adds some more informative error messages


---

Comment by mvngu created at 2009-03-26 08:01:20

REFEREE REPORT



The patch *trac_5465_1.patch* applies OK against Sage 3.4, all doctests pass with the `-long` option as well. Since the purpose of the patch is to add more meaningful error messages, I tried to get those two more meaningful messages. First, for the case where the number of generators is < 3:

```
sage: # first for the case of S.ngens() < 3...
sage: R.<x,y> = PolynomialRing(QQ,2)
sage: G = R.ideal([y^3 - x^2, y^2 - 13*x]).groebner_fan()
sage: G.render()
For 2-D fan rendering the polynomial ring must have 3 variables (or more, which are ignored).
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (118, 0))

---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/home/mvngu/.sage/temp/sage.math.washington.edu/16843/_home_mvngu__sage_init_sage_0.py in <module>()

/home/mvngu/scratch/sage-3.4/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.pyc in render(self, file, larger, shift, rgbcolor, polyfill, scale_colors)
    902         if S.ngens() < 3:
    903             print "For 2-D fan rendering the polynomial ring must have 3 variables (or more, which are ignored)."
--> 904             raise NotImplementedError
    905         cmd = 'render'
    906         if shift:

NotImplementedError:
```

Yep, the error message is certainly now more comprehensible than something like `UnboundLocalError` which misses the main point that the number of generators is not of the required size.  Now, for the case where the number of generators is not 4:

```
sage: # second, for the case of S.ngens() != 4...
sage: P.<a,b,c> = PolynomialRing(QQ, 3, order="lex")
sage: sage.rings.ideal.Katsura(P,3).groebner_fan().render3d()
For 3-D fan rendering the polynomial ring must have 4 variables
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/home/mvngu/.sage/temp/sage.math.washington.edu/16843/_home_mvngu__sage_init_sage_0.py in <module>()

/home/mvngu/scratch/sage-3.4/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.pyc in render3d(self, verbose)
   1070         if S.ngens() != 4:
   1071             print "For 3-D fan rendering the polynomial ring must have 4 variables"
-> 1072             raise NotImplementedError
   1073         g_cones = [q.groebner_cone() for q in self.reduced_groebner_bases()]
   1074         g_cones_facets = [q.facets() for q in g_cones]

NotImplementedError:
```

Again, I see a `NotImplementedError` which is certainly more comprehensible than the error message reported above by William Stein. And finally, given the correct number of generators, we have a nice Groebner fan :-) Positive review for the problem that the patch fixes.


---

Comment by mabshoff created at 2009-03-26 23:14:22

Well, to be absolutely pedantic: Shouldn't we add doctests that check the error messages being raised?

I am happy to merge the patch "as is", but if someone wanted to submit such a patch I would not be unhappy ;)

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-26 23:20:25

Resolution: fixed


---

Comment by mabshoff created at 2009-03-26 23:20:25

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael


---

Comment by mvngu created at 2009-03-27 03:41:55

Replying to [comment:5 mabshoff]:
> Well, to be absolutely pedantic: Shouldn't we add doctests that check the error messages being raised?
> 
> I am happy to merge the patch "as is", but if someone wanted to submit such a patch I would not be unhappy ;)


Some happiness is available at #5619 :-)
