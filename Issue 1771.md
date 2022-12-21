# Issue 1771: latex bug with symbolics [with fix]

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-14 05:08:50

Assignee: was


```
Peter.Jipsen
Hi,

with lprint() on, I calculated

diff(1/x-1/ln(x))

followed by

factor(_)

and the displayed answer is incorrect because prefix negation is not
handled correctly in the _latex_ method.

The same error in a simpler setting can be observed with:

(-(x-1)/2)._latex_(simplify=False)

output:

'\\frac{-x - 1}{2}'

(The error is usually masked by the fact that symbolic expressions are
normalized to avoid prefix negation.)

I think the last two lines of the _latex_ method should probably
change from

       elif op is operator.neg:
           return '-%s' % s[0]

to something like:

       elif op is operator.neg:
           if ops[0]._has_op(operator.add) or
ops[0]._has_op(operator.sub):
               s[0] = r'\left( %s \right)' %s[0]
           return '-%s' % s[0]

Sorry, I haven't figured out how to turn this into a hg patch (if the
solution is even appropriate).

--Peter
```



---

Attachment

This looks good to me.  Thanks for turning it into a patch Mike!


---

Comment by mabshoff created at 2008-01-14 05:52:24

Merged in Sage 2.10.alpha3.


---

Comment by mabshoff created at 2008-01-14 05:52:24

Resolution: fixed
