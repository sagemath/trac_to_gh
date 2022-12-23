# Issue 4073: disable colors in sage0

Issue created by migration from https://trac.sagemath.org/ticket/4073

Original creator: malb

Original creation time: 2008-09-07 19:51:57

Assignee: was

CC:  mhansen

This is related to #4072


```
[20:42] <mhansen> malb: How do you have your ipython colors set up?
[20:43] <malb> I had: colors LightBG 
[20:43] <malb> now I have colors NoColor
[20:43] <mhansen> And it sage0 fails with them and passes without them?
[20:44] <malb> yep
[20:44] <malb> I think the child process should be started with some option not to use colors
[20:44] <mhansen> Yep
[20:44] <malb> maybe by passing in an alternative ipythonrc
[20:45] <mhansen> I think you can also do it by just evaluating something at the command line.
[20:46] <malb> %colors NoColor
[20:47] <malb> I'll open a ticket
```



---

Attachment


---

Comment by mhansen created at 2008-09-07 22:40:53

Looks good to me.


---

Comment by mabshoff created at 2008-09-07 23:01:26

Merged in Sage 3.1.2.rc1


---

Comment by mabshoff created at 2008-09-07 23:01:26

Resolution: fixed


---

Comment by ddrake created at 2009-05-26 08:11:31

Resolution changed from fixed to 


---

Comment by ddrake created at 2009-05-26 08:11:31

I hate to reopen this, but...the problem has returned in 4.0.alpha0 and 4.0.rc0 (and possibly earlier; I haven't checked). I have exactly the same problem that malb did, but the `'%colors NoColor'` bit isn't working. I had Expect make a logfile, and here's what I get in the logfile when colors are enabled:

```
Loading Sage library.
sage: import cPickle
%colors NoColor
import cPickle
sage: sage0=cPickle.load(open("/home/drake/.sage//temp/klee/24661//interface//tmp24661"))
print sage0
%colors NoColor
```

Both "`sage: `" prompts are colored. Without color in my ipythonrc file, I get this logfile:

```
Loading Sage library.
sage: import cPickle
import cPickle
sage: %colors NoColor
%colors NoColor
sage: sage0=cPickle.load(open("/home/drake/.sage//temp/klee/25347//interface//tmp25347"))
<en("/home/drake/.sage//temp/klee/25347//interface//tmp25347"))              
sage: print sage0
print sage0
3
```

In both cases, I did "`s = Sage()`" and "`a = s(3)`" in my Sage session. It looks like with color, Expect isn't correctly detecting the prompt.


---

Comment by ddrake created at 2009-05-26 08:11:31

Changing status from closed to reopened.


---

Comment by mabshoff created at 2009-05-26 14:19:27

Please don't reopen fixed tickets if the bug has reappeared, even if it seems to be the same bug. Instead open a new ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-26 14:19:27

Resolution: fixed


---

Comment by ddrake created at 2009-05-26 23:54:13

Replying to [comment:5 mabshoff]:
> Please don't reopen fixed tickets if the bug has reappeared, even if it seems to be the same bug. Instead open a new ticket.

The new ticket is #6135.
