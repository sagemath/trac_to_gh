# Issue 4604: Graphics() should work in 3d as a valid empty object

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2008-11-24 17:37:26

Assignee: was

Keywords: graphics, 3d

From sage-support (and this has bugged me too):


I'm not sure if this is a bug or just something I'm misunderstanding,
but for 2D graphics I can write code like this.

```
g = Graphics()
g += line( [ [-1,-1], [1,1] ] )
g.show()
```

But in 3D if I do either

```
g = Graphics()
g += sphere( (1,1,1), 2 )
g.show()
```

or

```
g = sage.plot.plot3d.base.Graphics3dGroup()
g += sphere( (1,1,1), 2 )
g.show()
```

I get the error: 

```
ValueError: min() arg is an empty sequence
```


Is there something I'm missing on how to create a graphics object and
add 3D graphics to it like the way it's done in 2D? 




---

Attachment

based on sage 4.3.1.alpha1


---

Comment by wcauchois created at 2010-01-16 23:51:33

Changing status from new to needs_review.


---

Comment by wcauchois created at 2010-01-16 23:51:33

Robert and I confirmed this bug has been fixed in Sage 4.3. The attached patch implements a doctest for Graphics that implements this.


---

Comment by timdumol created at 2010-01-17 01:56:36

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-01-17 01:56:36

LGTM.


---

Comment by rlm created at 2010-01-19 00:40:56

Resolution: fixed
