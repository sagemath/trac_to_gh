# Issue 2548: more flexible syntax for defining callable function ring elements

Issue created by migration from Trac.

Original creator: edrex

Original creation time: 2008-03-16 17:01:26

Assignee: cwitty

I like the object resulting from 
`f(x,y)=x<sup>2+y</sup>2`
better than that from
`var('x,y');g=x<sup>2+y</sup>2`
However, (as I can attest) it's not at all clear to a new user that these are different objects (since what's to the right of the equals sign is the same, which is usually all you need to check -- except in this case)

Anyhow, I'm not sure if that's fixable. What I would like is a syntax for defining callable functions inline. I'm thinking 
`some_python_function(f(x,y)=blah)`
Except that the 'f' is immediately thrown away. Also, it is somewhat confusing since this is meant to be a positional, not keyword argument (how would you pass this as a keyword? key=f(x,y)=x^2 looks a bit strange). Any other ideas? Or is this already possible using some other syntax?


---

Comment by mabshoff created at 2008-03-16 18:00:10

Replying to [ticket:2548 edrex]:
> I like the object resulting from 
> `f(x,y)=x<sup>2+y</sup>2`
> better than that from
> `var('x,y');g=x<sup>2+y</sup>2`
> However, (as I can attest) it's not at all clear to a new user that these are different objects (since what's to the right of the equals sign is the same, which is usually all you need to check -- except in this case)
> 
> Anyhow, I'm not sure if that's fixable. What I would like is a syntax for defining callable functions inline. I'm thinking 
> `some_python_function(f(x,y)=blah)`
> Except that the 'f' is immediately thrown away. Also, it is somewhat confusing since this is meant to be a positional, not keyword argument (how would you pass this as a keyword? `key=f(x,y)=x^2` looks a bit strange). Any other ideas? Or is this already possible using some other syntax?

Please do not open tickets like this. It is vague and could certainly benefit from some discussion in GG:sage-devel. Trac is no substitute for a discussion in GG:sage-devel and not meant as a vector for support queries.

Cheers,

Michael

Michael


---

Comment by gfurnish created at 2008-03-16 20:08:40

Changing assignee from cwitty to gfurnish.


---

Comment by gfurnish created at 2008-03-16 20:08:40

Changing status from new to assigned.


---

Comment by was created at 2008-03-16 20:47:06

I think the answer to the posters's question is -- use the "function" function:

```
sage: var('x,y')
(x, y)
sage: f = (x^2 + y^2).function(x,y)
sage: f
(x, y) |--> y^2 + x^2
```



---

Comment by was created at 2008-03-16 20:47:06

Resolution: fixed
