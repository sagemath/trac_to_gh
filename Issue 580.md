# Issue 580: bug in cubegroup (group action)

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2007-09-03 16:37:33

Assignee: was

It seems from the cubegroup.py code that RubiksCube().move
accepts a group element as an argument. Even if it doesn't the
error below seems confusing.


```
sage: rubik = CubeGroup()
sage: G = rubik.group()
sage: Z = G.center()
sage: superflip = Z.list()[1]
sage: superflip

(2,34)(4,10)(5,26)(7,18)(12,37)(13,20)(15,44)(21,28)(23,42)(29,36)(31,45)(39,
47)
sage: r = rubik.R(); l = rubik.L(); f = rubik.F()
sage: b = rubik.B(); u = rubik.U(); d = rubik.D()
sage: superflip in G
True
sage: C = RubiksCube().move(superflip)
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

<type 'exceptions.AttributeError'>: 'PermutationGroupElement' object
has no attribute 'strip'
```



---

Comment by wdj created at 2007-09-03 16:40:11

Robert Bradshaw or I can try to work on this when we get time.
The ticket was automatically assigned to was (William).

Replying to [ticket:580 wdj]:
> It seems from the cubegroup.py code that RubiksCube().move
> accepts a group element as an argument. Even if it doesn't the
> error below seems confusing.
> 
> {{{
> sage: rubik = CubeGroup()
> sage: G = rubik.group()
> sage: Z = G.center()
> sage: superflip = Z.list()[1]
> sage: superflip
> 
> (2,34)(4,10)(5,26)(7,18)(12,37)(13,20)(15,44)(21,28)(23,42)(29,36)(31,45)(39,
> 47)
> sage: r = rubik.R(); l = rubik.L(); f = rubik.F()
> sage: b = rubik.B(); u = rubik.U(); d = rubik.D()
> sage: superflip in G
> True
> sage: C = RubiksCube().move(superflip)
> ---------------------------------------------------------------------------
> <type 'exceptions.AttributeError'>        Traceback (most recent call last)
> 
> /mnt/hd200/sagefiles/sage-2.8.3.rc3/<ipython console> in <module>()
> 
> /home/wdj/sagefiles/sage-2.8.3.rc3/local/lib/python2.5/site-packages/sage/groups/perm_gps/cubegroup.py
> in move(self, g)
>   1090     def move(self, g):
>   1091         if not g in self._group:
> -> 1092             g = self._group.move(g)[0]
>   1093         return RubiksCube(self._state * g, self._history +
> [g], self.colors)
>   1094
> 
> /home/wdj/sagefiles/sage-2.8.3.rc3/local/lib/python2.5/site-packages/sage/groups/perm_gps/cubegroup.py
> in move(self, mv)
>    730
>    731         """
> --> 732         mv = mv.strip().replace(" ","*").replace("**",
> "*").replace("'", "^(-1)")
>    733         m = mv.split("*")
>    734         M = [x.split("^") for x in m]
> 
> <type 'exceptions.AttributeError'>: 'PermutationGroupElement' object
> has no attribute 'strip'
> }}}


---

Comment by wdj created at 2007-09-03 16:40:11

Changing assignee from was to wdj.


---

Comment by robertwb created at 2007-09-06 19:28:40

Resolution: fixed


---

Comment by robertwb created at 2007-09-06 19:28:40

This code now works, see #570.
