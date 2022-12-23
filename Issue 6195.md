# Issue 6195: [with patch, needs review] in symbolic Expression.math() return a dictionary with matched values of wildcards

Issue created by migration from https://trac.sagemath.org/ticket/6195

Original creator: burcin

Original creation time: 2009-06-03 15:24:16

Assignee: burcin

CC:  mhansen

While matching patterns containing wildcards in symbolic expressions, GiNaC supports returning the sub expressions that match the given wildcards.

Attached patch wraps this interface.

The current interface for .match() on sage.symbolic.expression.Expression is to return False if there was a match, and True otherwise. The patch changes this to return a dictionary with the wildcards in the pattern as keys. This might result in an empty dictionary being returned. See the doctests in the patch for examples.

I am open to suggestions for improvements on this interface. 



---

Attachment

I don't understand this.

Why does the first match but the second not?  

```
sage: ((x+y)).match(w0+w1)
{$1: x, $0: y}
sage: ((x+x)).match(w0+w1)
```



Can you explain the difference in these behaviours?

```
sage: ((x+y)^a).match((x+y)^a)
{}
sage: print ((x+y)^a).match((x+y)^b)
None
```



---

Comment by burcin created at 2009-06-23 21:50:47

Replying to [comment:1 ncalexan]:
> Why does the first match but the second not?  
 {{{
 sage: ((x+y)).match(w0+w1)
 {$1: x, $0: y}
 sage: ((x+x)).match(w0+w1)
 }}}


```
sage: t = (x+x); t
2*x
sage: t.operator()
<built-in function mul>
```


You're looking for an add object, matching doesn't work algebraically in this case. We could start a "pitfalls of pattern matching in symbolics" wiki page to document these.

> Can you explain the difference in these behaviours?
 {{{
 sage: ((x+y)<sup>a).match((x+y)</sup>a)
 {}
 sage: print ((x+y)<sup>a).match((x+y)</sup>b)
 None
 }}}

The first example doesn't have any wildcards. It is a match, so it returns a dictionary, but without any keys. There is no match in the second example, so we return None. As I say in the description, I'm open to suggestions to improve the interface.


---

Comment by burcin created at 2009-06-23 21:50:47

Changing status from new to assigned.


---

Attachment

apply after the first patch


---

Comment by AlexGhitza created at 2009-07-17 09:30:31

Changing keywords from "" to "symbolic expression match".


---

Comment by AlexGhitza created at 2009-07-17 09:30:31

The patch looks good to me.  Nick's questions above were very good, and it's good to have the answers in a visible place so I've added these two to the docstring of `match()`.


---

Comment by mvngu created at 2009-07-19 13:48:03

Resolution: fixed
