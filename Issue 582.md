# Issue 582: bug in cubegroup? (syntax in RubiksCube)

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2007-09-03 16:43:37

Assignee: wdj or Robert Bradshaw

Again, a confusing error message. If group elements are allowed 
as arguments, what syntax should be used? Square bracketed list
of tuples? This element [(1,2)] is not in the Rubik's cube group, so 
shouldn't the error be something other than
`'list' object has no attribute 'strip'` ?



```
sage: C = RubiksCube().move([(1,2)])
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/mnt/hd200/sagefiles/sage-2.8.3.rc3/<ipython console> in <module>()

/home/wdj/sagefiles/sage-2.8.3.rc3/local/lib/python2.5/site-packages/sage/groups/perm_gps/cubegroup.py
in move(self, g)
  1090     def move(self, g):
  1091         if not g in self._group:
-> 1092             g = self._group.move(g)[0]
  1093         return RubiksCube(self._state * g, self._history +
[g], self.colors)
  1094

/home/wdj/sagefiles/sage-2.8.3.rc3/local/lib/python2.5/site-packages/sage/groups/perm_gps/cubegroup.py
in move(self, mv)
   730
   731         """
--> 732         mv = mv.strip().replace(" ","*").replace("**",
"*").replace("'", "^(-1)")
   733         m = mv.split("*")
   734         M = [x.split("^") for x in m]

<type 'exceptions.AttributeError'>: 'list' object has no attribute 'strip'
```




---

Comment by robertwb created at 2007-09-06 19:26:05

Resolution: fixed


---

Comment by robertwb created at 2007-09-06 19:26:05

See CubeGroup.parse() for all possible input formats, see #570
