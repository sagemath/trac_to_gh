# Issue 384: latex formatting issues with symbolic expressions

Issue created by migration from Trac.

Original creator: jbmohler

Original creation time: 2007-06-01 15:29:03

Assignee: was

There are two latex formatting issues for the symbolic expressions.

1)  The \cdot's for implicit multiplication take up a lot of room and confuse my eyes.

2)  I have expressions which are a product of about 5 things and 
they are output with excessive parentheses, for example:
(((1+a)(1+b))(1+c))(1+d)
The parenthesis check in the code just adds parentheses if the left 
subexpression contains a minus or plus.  Of course, it should check if there 
is a minus or plus that isn't already bracketed or something like that (but, who am I 
to claim to know what should be done :) ).



---

Comment by mabshoff created at 2008-01-26 15:04:19

This is still an issue with Sage 2.10:

```
sage: var('x,y')
(x, y)
sage: f=(x+y)*(x-y)*(x^2-2)*(y^2-3)
sage: latex(f)
{\left( {\left( {\left( {x}^{2}  - 2 \right) \cdot \left( x - y \right)} \right) \cdot \left( y + x \right)} \right) \cdot \left( {y}^{2}  - 3 \right)}
```

We really ought to fix this.

Cheers,

Michael


---

Attachment

See the patch.  A few comments:

1. The parenthesis issue is, I believe, taken care of.
2. After some thinking, I decided to do away with all the \cdot's.  For a while, I thought they might still been needed in some situations, but since in the default behavior _latex_ first simplifies the expressions, all the weird cases I could think of (e.g. f=cos*(x-1)) are taken care of automatically.  I'd be happy to change my mind if anyone can prove me wrong.

Some examples:


```
sage: var('x,y')
(x, y)
sage: f=(x+y)*(x-y)*(x^2-2)*(y^2-3)
sage: latex(f)
{{{\left( {x}^{2}  - 2 \right) \left( x - y \right)} \left( y + x \right)} \left( {y}^{2}  - 3 \right)}
sage: latex(cos*(x+1))
{\left( x + 1 \right) \cos}
sage: latex(x^2*2*cos(x+1))
{{{
sage: var('x,y')
(x, y)
sage: f=(x+y)*(x-y)*(x^2-2)*(y^2-3)
sage: latex(f)
{{{\left( {x}^{2}  - 2 \right) \left( x - y \right)} \left( y + x \right)} \left( {y}^{2}  - 3 \right)}
sage: latex(cos*(x+1))
{\left( x + 1 \right) \cos}
sage: latex(x^2*2*cos(x+1))
{{2 {x}^{2} } \cos \left( x + 1 \right)}
}}}


---

Attachment


---

Comment by mhansen created at 2008-01-27 02:23:33

Added a patch to be applied after Alex's.


---

Comment by mabshoff created at 2008-01-27 03:02:25

Resolution: fixed


---

Comment by mabshoff created at 2008-01-27 03:02:25

Merged in Sage 2.10.1.rc1


---

Attachment


---

Attachment

The two doctest patches fix the issue in the documentation and the sage library. They have been merged in Sage 2.10.1.rc1.

Cheers,

Michael
