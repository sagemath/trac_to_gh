# Issue 4407: magma -- painful scalability issue with parser and interface

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-10-31 00:01:27

Assignee: was


```
sage: a = magma('"%s"'%('n'*1000000))
[This is the Trac macro *works instantly, uses almost no memeory* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#works instantly, uses almost no memeory-macro)
sage: magma.GetMemoryUsage()
15728664
```

Now do the same, but with just 10 times as much input (be ready to kill magma processes).  This will uses several GIGABYTES.

```
sage: a = magma('"%s"'%('n'*10000000))
^C^Z
```


This is probably some major magma parser issue.  We should nail down the bound, then either:
   (1) find some clever way to program around it,
   (2) report it as a bug to Allan Steel,
   (3) give an error message instead of blowing up people's computers


---

Comment by was created at 2008-10-31 00:20:41


```
17:11 < wstein-4399> so this happens on OS X in magma 2.14
17:12 < wstein-4399> it does *not* happen on magma 2.13 on linux
17:12 < mhansen> If only you had a control group :-)
17:13 < mabshoff> Interesting
17:13 < mhansen> I'd guess it's probably the OS X vs. Linux as opposed to the 
                 version though.
17:13 < mabshoff> Well, the issue has also popped up on Linux boxen IIRC.
17:13 < mabshoff> mhansen: can you review #2462?
17:13 < wstein-4399> On magma 2.14 on my linux laptop (that tiny acer) it 
                     doesn't happen.
17:14 < wstein-4399> so I'm thinking it is yet another bug in magma on osx.

17:15 < wstein-4399> and definitely just a bug in magma.
17:15 < wstein-4399> Let's close the ticket as invalid.  There's nothing to be 
                     done
17:15 < mabshoff> I am surprised their OSX version is so buggy.
17:15 < mabshoff> ok
17:15 < wstein-4399> from the point of sage, and magma isn't (yet) a component 
                     of sage.
17:15 < mabshoff> :)
```



---

Comment by was created at 2008-10-31 00:20:53

Resolution: wontfix


---

Comment by mabshoff created at 2008-10-31 00:22:28

cantfix :)
