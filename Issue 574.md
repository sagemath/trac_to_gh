# Issue 574: bug in cubegroup

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2007-09-03 11:57:59

Assignee: wdj

Keywords: CubeGroup, RubiksCube, perm_gps


```
sage: rubik = CubeGroup()
sage: G = rubik.group()
sage: Z = G.center()
sage: superflip = Z.list()[1]
sage: superflip

(2,34)(4,10)(5,26)(7,18)(12,37)(13,20)(15,44)(21,28)(23,42)(29,36)(31,45)(39,
47)
sage: fcts = rubik.facets(superflip)
sage: faceR = [[fcts[24],fcts[25],fcts[26]],[fcts[27],0,fcts[28]],[fcts[29],fcts[30],fcts[31]]]
sage: faceL = [[fcts[8],fcts[9],fcts[10]],[fcts[11],0,fcts[12]],[fcts[13],fcts[14],fcts[15]]]
sage: faceU = [[fcts[0],fcts[1],fcts[2]],[fcts[3],0,fcts[4]],[fcts[5],fcts[6],fcts[7]]]
sage: faceD = [[fcts[40],fcts[41],fcts[42]],[fcts[43],0,fcts[44]],[fcts[45],fcts[46],fcts[47]]]
sage: faceF = [[fcts[16],fcts[17],fcts[18]],[fcts[19],0,fcts[20]],[fcts[21],fcts[22],fcts[23]]]
sage: faceB = [[fcts[32],fcts[33],fcts[34]],[fcts[35],0,fcts[36]],[fcts[37],fcts[38],fcts[39]]]
sage: superflip_state = {'right':faceR,'left':faceL,'up':faceU,'down':faceD,'front':faceF,'back':faceB}
sage: superflip_state

{'back': [[33, 2, 35], [29, 0, 12], [38, 47, 40]],
 'down': [[41, 23, 43], [15, 0, 31], [46, 39, 48]],
 'front': [[17, 7, 19], [13, 0, 28], [22, 42, 24]],
 'left': [[9, 4, 11], [37, 0, 20], [14, 44, 16]],
 'right': [[25, 5, 27], [21, 0, 36], [30, 45, 32]],
 'up': [[1, 34, 3], [10, 0, 26], [6, 18, 8]]}
sage: rubik.legal(superflip_state)
1
```

So far so good. We have created a "state" for the cube - a Python
dictionary representing the moved faces.
According to the docstring, we can now apply "solve":

```
sage: rubik.solve?
Type:           instancemethod
Base Class:     <type 'instancemethod'>
String Form:    <bound method CubeGroup.solve of The PermutationGroup of all legal moves of the Rubik's cube.>
Namespace:      Interactive
File:           /home/wdj/sagefiles/sage-2.8.3.rc3/local/lib/python2.5/site-packages/sage/groups/perm_gps/cubegroup.py
Definition:     rubik.solve(self, state)
Docstring:

            Solves the cube in the state, given as a dictionary as
            in legal.  
...
```

But doing so gives a Mysterious Error:

```
sage: rubik.solve(superflip_state)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/mnt/hd200/sagefiles/sage-2.8.3.rc3/<ipython console> in <module>()

/home/wdj/sagefiles/sage-2.8.3.rc3/local/lib/python2.5/site-packages/sage/groups/perm_gps/cubegroup.py in solve(self, state)
    997             g = state
    998         hom = G._gap_().EpimorphismFromFreeGroup()
--> 999         soln = hom.PreImagesRepresentative(gap(str(g)))
   1000         # print soln
   1001         sol1 = str(soln).replace("x1","B")

/home/wdj/sagefiles/sage-2.8.3.rc3/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, x)
    672             return x
    673         if isinstance(x, basestring):
--> 674             return cls(self, x)
    675         try:
    676             return self._coerce_impl(x)

/home/wdj/sagefiles/sage-2.8.3.rc3/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __init__(self, parent, value, is_name)
    902             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
    903                 self._session_number = -1
--> 904                 raise TypeError, x
    905         self._session_number = parent._session_number
    906

<type 'exceptions.TypeError'>: Gap produced error output
Syntax error: literal expected in /home/wdj/.sage//temp/wooster/24475//interfa\
ce//tmp line 1
$sage20:={'right': [[25, 5, 27], [21, 0, 36], [30, 45, 32]], 'up': [[1, 34, 3]\
, [10, 0, 26], [6, 18, 8]], 'back': [[33, 2, 35], [29, 0, 12], [38, 47, 40]], \
'down': [[41, 23, 43], [15, 0, 31], [46, 39, 48]], 'front': [[17, 7, 19], [13,\
 0, 28], [22, 42, 24]], 'left': [[9, 4, 11], [37, 0, 20], [14, 44, 16]]};;
         ^

   executing Read("/home/wdj/.sage//temp/wooster/24475//interface//tmp");
```

What goes wrong? The interface with GAP? To test this, we follow the
commands in "solve" and see:

```
sage: rubik.legal(superflip_state,"verbose")

(1,
 (2,34)(4,10)(5,26)(7,18)(12,37)(13,20)(15,44)(21,28)(23,42)(29,36)(31,45)(39,47))
sage: leg = rubik.legal(superflip_state,"verbose")
sage: g = leg[1]
sage: hom = G._gap_().EpimorphismFromFreeGroup()
sage: soln = hom.PreImagesRepresentative(gap(str(g)))
sage: soln

x2^-1*x1^-1*x5^-1*x1^2*x5*x2*x4*x6*x1^-1*x6^-1*x4^-1*x1*x4*x6*x1*x6^-1*x1^
-1*x4^-1*x1^-1*x2^-1*x5^-1*x1*x5*x2*x4*x6*x1^-1*x6^-1*x4^-1*x1^2*x2*x1*x2^
-1*x4^-1*x2*x1^-1*x2^-1*x1*x4*x1^2*x4^-1*x2*x4*x2^-1*x1^-1*x2^
-1*x1*x2*x4*x1*x4^-1*x1^-1*x2^-1*x1^-1*x2*x1^-1*x2^-1*x1*x4^-1*x2^
-1*x4*x2*x1*x2*x1^-1*x2^-1*x4*x1^-1*x4^-1*x2^-2*x3^-1*x2^-1*x3*x2^-1*x1^
-1*x3*x4*x3^-1*x5*x3*x5^-1*x2^-1*x6^-1*x3^-2*x6*x3*x2^-2*x1^-2*x6^-1*x1^-1*x5^
-1
sage: sol1 = str(soln).replace("x1","B")
sage:         sol2 = sol1.replace("x2","D")
sage:         sol3 = sol2.replace("x3","F")
sage:         sol4 = sol3.replace("x4","L")
sage:         sol5 = sol4.replace("x5","R")
sage:         sol6 = sol5.replace("x6","U")
sage: print sol6
D^-1*B^-1*R^-1*B^2*R*D*L*U*B^-1*U^-1*L^-1*B*L*U*B*U^-1*B^
-1*L^-1*B^-1*D^-1*R^-1*B*R*D*L*U*B^-1*U^-1*L^-1*B^2*D*B*D^
-1*L^-1*D*B^-1*D^-1*B*L*B^2*L^-1*D*L*D^-1*B^-1*D^
-1*B*D*L*B*L^-1*B^-1*D^-1*B^-1*D*B^-1*D^-1*B*L^-1*D^
-1*L*D*B*D*B^-1*D^-1*L*B^-1*L^-1*D^-2*F^-1*D^-1*F*D^-1*B^
-1*F*L*F^-1*R*F*R^-1*D^-1*U^-1*F^-2*U*F*D^-2*B^-2*U^-1*B^-1*R^
-1
```

No, the GAP interface seems to be fine. 

Also, a better mechanism for testing the group action on the "states" is 
needed. Useful for users and might help bug-checking.



---

Comment by robertwb created at 2007-09-03 16:30:54

I think this is due to confusion in the many ways of representing state. We should come up with a list of all the ways state can be represented/inputted, and make sure all functions can accept that kind of state. 

- Robert


---

Comment by robertwb created at 2007-09-03 16:30:54

Changing assignee from wdj to robertwb.


---

Comment by robertwb created at 2007-09-06 19:34:23

See #570


---

Comment by robertwb created at 2007-09-06 19:34:23

Resolution: fixed
