# Issue 1064: applying permutation is coded in a way that behaves badly when input isn't an "expected type"

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-11-02 02:04:43

Assignee: somebody


```
19:00 < wstein> that permuation application code in #750 is (and has always been) lame.
19:00 < wstein> watch:
19:00 < wstein> g = PermutationGroup(['(1,2,3)(4,5)']).gen(0)
19:00 < wstein> g(x)
19:00 < wstein> Get a big traceback from Gap.
19:00 < wstein> It would be trivial to code things to give a much more sensible error.
19:01 < wstein> This isn't a criticism of #750; just that looking at #750 immediately
19:01 < wstein> makes me see that there are bad features to the code.
19:02 < wstein> Even worse:
19:02 < wstein> sage: g(3/2)
19:02 < wstein> 1
19:02 < wstein> That makes no sense!
}}]

The problem is this line of code in sage/groups/perm_gps/permgroup_element.py:

{{{
            return int(gap.eval('%s^%s'%(i, self._gap_().name())))
}}}

Instead that should be

{{{
            return int(gap.eval('%s^%s'%(Integer(i), self._gap_().name())))
}}}

since then we'll get a sensible error message if i doesn't have a natural
interpretation as an integer.

Of course, one must import Integer. 

I'm not attaching a patch, since ticket #750 and a text patch would be
too confusing to apply.


---

Comment by rlm created at 2007-12-19 06:37:41

Now the stupid traceback is different, but equally stupid. Amusingly:

```
sage: g(3/2)
2
```

Now we're starting to make some sense!?


---

Attachment


---

Comment by rlm created at 2007-12-21 00:28:45

Resolution: fixed


---

Comment by rlm created at 2007-12-21 00:28:45

Merged in 2.9.1 alpha2
