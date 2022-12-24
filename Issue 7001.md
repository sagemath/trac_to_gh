# Issue 7001: Sage's GAP interface not properly leaving GAP's break loop

archive/issues_007001.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @wdjoyner\n\nKeywords: gap interface recursion depth trap\n\nIt seems to me that it is forgotten to quit GAP's break loop before continuing. By consequence, GAP runs into a recursion depth trap (by default, GAP throws an error if a recursion of depth 5000 occurs) if there are too many errors.\n\nExample:\n\n```\nsage: def bugtrigger(n):\n....:     a = gap(1)\n....:     for i in range(n):\n....:         try:\n....:             b = gap.eval('Name(%s)'%a.name())\n....:             a += 1\n....:         except Exception, msg:\n....:             if 'recursion depth' in str(msg):\n....:                 return i,msg\n....:\nsage: bugtrigger(10000)\n\n(4998,\n RuntimeError('Gap produced error output\\nrecursion depth trap (5000)\\n\\n\\n   executing Name($sage1);',))\n```\n\n\n__Explanation:__\n\n\"Name\" is not defined for a, so, an error occurs, that we catch and continue. If this is done 4998 times then we have 4998 break loops inside the main loop, and then call `\"Name(%s)\"%a.name()`  -- this is a total of 5000 nested loops (main loop, 4998 break loops, function call).\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7001\n\n",
    "created_at": "2009-09-23T09:41:46Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Sage's GAP interface not properly leaving GAP's break loop",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7001",
    "user": "@simon-king-jena"
}
```
Assignee: @williamstein

CC:  @wdjoyner

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



Issue created by migration from https://trac.sagemath.org/ticket/7001





---

archive/issue_comments_057881.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-09-23T11:58:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7001#issuecomment-57881",
    "user": "@simon-king-jena"
}
```

Changing status from new to assigned.



---

archive/issue_comments_057882.json:
```json
{
    "body": "Changing assignee from @williamstein to @simon-king-jena.",
    "created_at": "2009-09-23T11:58:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7001#issuecomment-57882",
    "user": "@simon-king-jena"
}
```

Changing assignee from @williamstein to @simon-king-jena.



---

archive/issue_comments_057883.json:
```json
{
    "body": "It turned out that it is a bug in GAP, not in Sage, as was pointed out by Frank L\u00fcbeck, whose message to me I post here with his permission:\n\n----\n...\n\nSecond, your previous code does actually show a bug in GAP: if a function\ncall in GAP is not properly finished (by running into an error and\nquiting the break loop) an internal counter for the recursion depth is not\nreset. Here is a short GAP session that demonstrates the effect:\n\n\n```\ngap> f := function() return 1/0; end;;\ngap> SetRecursionTrapInterval(3);\ngap> f();\nRational operations: <divisor> must not be zero at\nreturn 1 / 0;\n called from\n<function>( <arguments> ) called from read-eval-loop\nEntering break read-eval-print loop ...\nyou can 'quit;' to quit to outer loop, or\nyou can replace <divisor> via 'return <divisor>;' to continue\nbrk> quit;\ngap> f();\nRational operations: <divisor> must not be zero at\nreturn 1 / 0;\n called from\n<function>( <arguments> ) called from read-eval-loop\nEntering break read-eval-print loop ...\nyou can 'quit;' to quit to outer loop, or\nyou can replace <divisor> via 'return <divisor>;' to continue\nbrk> quit;\nrecursion depth trap (3)\n at\nreturn 1 / 0;\n called from\n<function>( <arguments> ) called from read-eval-loop\nEntering break read-eval-print loop ...\nyou can 'quit;' to quit to outer loop, or\nyou may 'return;' to continue\nbrk_02>\n```\n\n\nI will try to fix this.\n\nThanks and best regards,\n\n  Frank\n\n----\n\nSo, I label this ticket as \"reported upstream\", and think that the ticket should be closed as invalid by some administrator.\n\nCheers,\nSimon",
    "created_at": "2009-09-23T15:11:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7001#issuecomment-57883",
    "user": "@simon-king-jena"
}
```

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

archive/issue_comments_057884.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-09-24T10:36:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7001#issuecomment-57884",
    "user": "@williamstein"
}
```

Resolution: invalid



---

archive/issue_comments_057885.json:
```json
{
    "body": "Simon says \"close this\".",
    "created_at": "2009-09-24T10:36:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7001#issuecomment-57885",
    "user": "@williamstein"
}
```

Simon says "close this".
