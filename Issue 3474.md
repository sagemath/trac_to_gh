# Issue 3474: Request for improvement in plotting

Issue created by migration from https://trac.sagemath.org/ticket/3474

Original creator: craigcitro

Original creation time: 2008-06-19 21:44:51

Assignee: robertwb

Robert Bradshaw made some nice p-adic plotting code in #3210. David Joyner requested an additional feature that wasn't suppported. Here's the discussing from that ticket:

David:

My suggestion, and it really a very minor one, is that the "radius" where the points are plotted should be a parameter the user can reset. For example, if you graph a p=3 and a p=7 then they overlap maybe more that some would like. Not that I see this as important for teaching but might be a fun option for making cool pictures. Just an idea.

Robert: 

The "radius" can be changed with the pointsize parameter. Also, you could plot it with fewer points (as for p=3 or 7, the "points" you're seeing are probably a cluster of even smaller ones).

David:

I am talking about a different radius I think. To me

```
sage: P1 = Zp(3).plot(pointsize=1,rgbcolor=(0,1,0))
sage: P2 = Zp(7).plot(pointsize=2,rgbcolor=(1,0,0))
```

and

```
sage: P1 = Zp(3).plot(pointsize=1,rgbcolor=(0,1,0))
sage: P2 = Zp(7).plot(pointsize=3,rgbcolor=(1,0,0))
```

Look the same. I was wondering about a scaling parameter "distance", say, where

```
sage: P1 = Zp(3).plot(distance=1,rgbcolor=(0,1,0))
```

would plot the 3 triangles at (say) a circle of radius 1 from (0,0) as it does now, and

```
sage: P1 = Zp(3).plot(distance=2,rgbcolor=(0,1,0))
```

would plot the 3 triangles at (say) a circle of radius 2 from (0,0).

Is this possible without introducing a new parameter?

