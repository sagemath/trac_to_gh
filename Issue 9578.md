# Issue 9578: Add even more customization of ticks in plots

Issue created by migration from https://trac.sagemath.org/ticket/9578

Original creator: kcrisman

Original creation time: 2010-07-23 01:55:04

Assignee: jason, was

Such as arbitrary ticks, color... Here are some hints for this from [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/64aee5700d4f7ff4/34a82a725be9e2a5?show_docid=34a82a725be9e2a5)

```
> I figure with some polishing it could go into Sage. Part of that 
> polishing would require to figure out how one can make 
> sage: pylab.clf() 
> sage: _ = pylab.pcolor(pylab.rand(2,2)) 
> sage: pylab.savefig('foo.png',dpi=96) 
> not print out indices for x and y from 0 to n but from a to b. I 
> couldn't figure this out. Maybe someone on this list knows from the 
> top of the head? 


Here's one way to do it, just by changing the tick labels.  There are 
other more flexible ways too: 
sage: import pylab 
sage: pylab.clf() 
sage: p = pylab.pcolor(pylab.rand(2,2)) 
sage: p.axes.get_xticks() # see what ticks are in the plot 
array([ 0. ,  0.5,  1. ,  1.5,  2. ]) 
sage: _=p.axes.set_xticklabels(['0','1000','2000','3000','4000']) 
sage: pylab.savefig('foo.png',dpi=96) 
Or if you just want to multiply each tick label by a certain amount: 
sage: _=p.axes.set_xticklabels([str(i) for i in 1000*p.axes.get_xticks()]) 
sage: pylab.savefig('foo.png',dpi=96) 
Thanks, 
Jason 
```

and

```
Yes, I think it would be pretty easy.  Note that matplotlib just added 
some nice convenience functions for dealing with changing the styles of 
ticks too, so we could easy change the colors or weights or whatever as 
well. 
```



---

Comment by kcrisman created at 2010-07-23 01:55:38

#1431 and #2189 are also relevant.


---

Comment by kcrisman created at 2012-07-07 03:26:45

We have arbitrary ticks now, and some formatting.  Since this is a little vague, I'm making it be about color.

See also #13078.
