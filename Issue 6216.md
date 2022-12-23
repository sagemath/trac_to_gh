# Issue 6216: make a sage.misc.profile module that makes hotshot and grof2dot and line_profiler easily used

archive/issues_006216.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  craigcitro mhansen\n\nKeywords: misc profile hotshot gprof2dot timing\n\n\n```\n[5:12pm] ncalexan: It's a script that takes profile output and writes a .dot file of the callgraph.\n[5:12pm] ncalexan: It's incredibly useful for understanding where your time is going.\n[5:13pm] ddrake: sounds nice.\n[5:13pm] ncalexan: It is.  So I'd like to include it \n[5:13pm] mhansen: ncalexan: Have you used Robert Kern's line profiler?\n[5:13pm] ncalexan: mhansen: no.\n[5:13pm] ncalexan: link\n[5:14pm] mhansen: http://packages.python.org/line_profiler/\n[5:14pm] cwitty left the chat room. (Read error: 113 (No route to host))\n[5:17pm] ncalexan: They look complimentary.\n[5:18pm] mhansen: Yes.  But, I often find the line_profiler more useful.  I just thought I'd mention it since people were talking about profiling.\n[5:18pm] ncalexan: We need to make this stuff easier to use from the prompt.\n[5:18pm] mhansen: Definitely\n[5:18pm] ncalexan: Maybe a sage.misc.profile module is in order.\n[5:19pm] ncalexan: I will make a ticket.\n[5:19pm] mhansen: It'd be cool if we could integrate it with craigcitro's time capsule\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6216\n\n",
    "created_at": "2009-06-05T00:20:36Z",
    "labels": [
        "distribution",
        "minor",
        "enhancement"
    ],
    "title": "make a sage.misc.profile module that makes hotshot and grof2dot and line_profiler easily used",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6216",
    "user": "ncalexan"
}
```
Assignee: tbd

CC:  craigcitro mhansen

Keywords: misc profile hotshot gprof2dot timing


```
[5:12pm] ncalexan: It's a script that takes profile output and writes a .dot file of the callgraph.
[5:12pm] ncalexan: It's incredibly useful for understanding where your time is going.
[5:13pm] ddrake: sounds nice.
[5:13pm] ncalexan: It is.  So I'd like to include it 
[5:13pm] mhansen: ncalexan: Have you used Robert Kern's line profiler?
[5:13pm] ncalexan: mhansen: no.
[5:13pm] ncalexan: link
[5:14pm] mhansen: http://packages.python.org/line_profiler/
[5:14pm] cwitty left the chat room. (Read error: 113 (No route to host))
[5:17pm] ncalexan: They look complimentary.
[5:18pm] mhansen: Yes.  But, I often find the line_profiler more useful.  I just thought I'd mention it since people were talking about profiling.
[5:18pm] ncalexan: We need to make this stuff easier to use from the prompt.
[5:18pm] mhansen: Definitely
[5:18pm] ncalexan: Maybe a sage.misc.profile module is in order.
[5:19pm] ncalexan: I will make a ticket.
[5:19pm] mhansen: It'd be cool if we could integrate it with craigcitro's time capsule
```


Issue created by migration from https://trac.sagemath.org/ticket/6216





---

archive/issue_comments_049662.json:
```json
{
    "body": "#17689 makes `line_profiler` easy to access",
    "created_at": "2015-04-14T08:31:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6216",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6216#issuecomment-49662",
    "user": "mmezzarobba"
}
```

#17689 makes `line_profiler` easy to access
