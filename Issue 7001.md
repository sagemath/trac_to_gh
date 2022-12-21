# Issue 7001: Sage's GAP interface not properly leaving GAP's break loop

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2009-09-23 09:41:46

Assignee: was

CC:  wdj

Keywords: gap interface recursion depth trap

It seems to me that it is forgotten to quit GAP's break loop before continuing. By consequence, GAP runs into a recursion depth trap (by default, GAP throws an error if a recursion of depth 5000 occurs) if there are too many errors.

Example:

```
sage: def bugtrigger(n):
....:     a = gap(1)
....:     for i in range(n):
....:         try:
....:             b = gap.eval('Name(%s)'%a.name())
....:             a += 1
....:         except Exception, msg:
....:             if 'recursion depth' in str(msg):
....:                 return i,msg
....:
sage: bugtrigger(10000)

(4998,
 RuntimeError('Gap produced error output\nrecursion depth trap (5000)\n\n\n   executing Name($sage1);',))
```


__Explanation:__

"Name" is not defined for a, so, an error occurs, that we catch and continue. If this is done 4998 times then we have 4998 break loops inside the main loop, and then call `"Name(%s)"%a.name()`  -- this is a total of 5000 nested loops (main loop, 4998 break loops, function call).




---

Comment by SimonKing created at 2009-09-23 11:58:41

Changing status from new to assigned.


---

Comment by SimonKing created at 2009-09-23 11:58:41

Changing assignee from was to SimonKing.


---

Comment by SimonKing created at 2009-09-23 15:11:32

It turned out that it is a bug in GAP, not in Sage, as was pointed out by Frank Lübeck, whose message to me I post here with his permission:

----
...

Second, your previous code does actually show a bug in GAP: if a function
call in GAP is not properly finished (by running into an error and
quiting the break loop) an internal counter for the recursion depth is not
reset. Here is a short GAP session that demonstrates the effect:


```
gap> f := function() return 1/0; end;;
gap> SetRecursionTrapInterval(3);
gap> f();
Rational operations: <divisor> must not be zero at
return 1 / 0;
 called from
<function>( <arguments> ) called from read-eval-loop
Entering break read-eval-print loop ...
you can 'quit;' to quit to outer loop, or
you can replace <divisor> via 'return <divisor>;' to continue
brk> quit;
gap> f();
Rational operations: <divisor> must not be zero at
return 1 / 0;
 called from
<function>( <arguments> ) called from read-eval-loop
Entering break read-eval-print loop ...
you can 'quit;' to quit to outer loop, or
you can replace <divisor> via 'return <divisor>;' to continue
brk> quit;
recursion depth trap (3)
 at
return 1 / 0;
 called from
<function>( <arguments> ) called from read-eval-loop
Entering break read-eval-print loop ...
you can 'quit;' to quit to outer loop, or
you may 'return;' to continue
brk_02>
```


I will try to fix this.

Thanks and best regards,

  Frank

----

So, I label this ticket as "reported upstream", and think that the ticket should be closed as invalid by some administrator.

Cheers,
Simon


---

Comment by was created at 2009-09-24 10:36:07

Resolution: invalid


---

Comment by was created at 2009-09-24 10:36:07

Simon says "close this".
