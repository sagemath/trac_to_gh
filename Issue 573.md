# Issue 573: word_problem bug in permgroup_element

Issue created by migration from https://trac.sagemath.org/ticket/573

Original creator: wdj

Original creation time: 2007-09-03 11:40:55

Assignee: wdj

CC:  sage-combinat

Keywords: EpimorphismFromFreeGroup, PreImagesRepresentative, RubiksCube, CubeGroup


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
sage: superflip.word_problem([b,d,f,l,r,u])
          x1^-1
          [['(33,35,40,38)(34,37,39,36)(3,9,46,32)(2,12,47,29)(1,14,48,27)', -1]]
'(33,35,40,38)(34,37,39,36)(3,9,46,32)(2,12,47,29)(1,14,48,27)^-1'
sage: ########## wrong #############
```



---

Comment by robertwb created at 2007-09-06 20:18:08

Resolution: fixed


---

Attachment

This was due to superflip being viewed as an element of Z (with one generator). Obviously the solution was trivial. 

I've updated it so it now casts the element into the parent of words.


---

Comment by robertwb created at 2007-09-06 20:20:18

Resolution changed from fixed to 


---

Comment by robertwb created at 2007-09-06 20:20:18

Changing status from closed to reopened.


---

Comment by was created at 2007-09-07 04:37:05

Resolution: fixed
