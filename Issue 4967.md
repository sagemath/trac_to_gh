# Issue 4967: [with patch] Trouble with .gaprc file when compiling from source

Issue created by migration from https://trac.sagemath.org/ticket/4967

Original creator: mmeulien

Original creation time: 2009-01-12 16:50:51

Assignee: mabshoff

## How to reproduce the problem

 * Create a file called `~/.gaprc' containing the following line

```
ColorPrompt(true);
```

 * Compile sage from source
 * Start sage and try the following

```
sage: gap._eval_line('1+3;')
'4\n\x1b[1m\x1b[34mgap> \x1b[0m'
```


## Solution
As William Stein suggested on sage-devel (Sat, 11 Oct 2008), changing line 169 of `gap.py' from 

```
gap_cmd = "gap"
```

to 

```
gap_cmd = "gap -r"
```

solve the problem.





---

Comment by mmeulien created at 2009-01-12 16:51:28

diff -c a/sage/interfaces/gap.py b/sage/interfaces/gap.py >> ticket.patch


---

Attachment

Hi,

any chance you can post a proper mercurial patch? The attachment is "just" a diff, but I can commit it in your name.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2009-01-18 05:13:01

Positive review. I have attached a proper hg patch with check in credit given to Matthias Meulien.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-18 05:13:11

Merged in Sage 3.3.alpha0


---

Comment by mabshoff created at 2009-01-18 05:13:11

Resolution: fixed
