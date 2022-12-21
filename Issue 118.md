# Issue 118: Tab completion is too noisy

Issue created by migration from Trac.

Original creator: justin

Original creation time: 2006-10-07 20:38:24

Assignee: was

I'd like to see TAB completion work more like 'bash': if I type "foo[TAB]", the system should complete up to ambiguity:

```
foo[TAB]b
```

for example (assuming 'foobar' and 'fooble' are both known).  If I hit tab twice (with no completion), I get the display of the alternatives:

```
sage: foo[TAB]b[TAB][TAB]
foobar  fooble  
sage: foob
```

As it is now, an inadvertent TAB will blow unwanted bits all over my screen.

Is this under SAGE control, or is it an iPython thing?



---

Comment by was created at 2006-10-14 20:34:19

In the notebook we can do anything we want.  In the command line this is entirely
an IPYthon thing.  It would, of course, be good to keep the behavior of the notebook
and of Ipython in sync.    I'm not sure I agree with the change you want, since so
far I rather like IPython's behavior.   -- William


---

Comment by was created at 2006-10-14 20:34:26

Changing priority from major to minor.


---

Comment by was created at 2006-10-16 05:00:41

Resolution: fixed


---

Comment by was created at 2006-10-16 05:00:41


```
Justin,

See below, regarding tab completion.  

------- Forwarded message -------
From: "Fernando Perez" <Fernando.Perez`@`colorado.edu>
To: "William Stein" <wstein`@`gmail.com>
Cc:
Subject: Re: ipython huge traceback
Date: Sun, 15 Oct 2006 19:16:32 -0700

Justin Walker suggested changing the tab behavior in ipython to be like
in bash, which it currently isn't.  Any thoughts about that?
    http://sage.math.washington.edu:9002/sage_trac/ticket/118
 I like IPython's tab completion behavior and hadn't thought much about
it differing from bash's until now.

That's entirely a user customization, and it has nothing to do with Bash: it's purely the behavior of the readline library.  IPython happens to tweak readline one way and bash does it in a different way, but readline is very customizable.

Justin is free to set the readline behavior to his heart's content via the settings in the sage ipythonrc file.  Just look for those called readline_parse_and_bind, which will make calls to the function with that name in Python's readline library.  The meaning of those settings is defined in the readline documentation.

So this is something users can set as they like it, it's not really a bug.

In particular, what Justin wants requires changing

readline_parse_and_bind set show-all-if-ambiguous on

to:

readline_parse_and_bind set show-all-if-ambiguous off

in his personal config file.

Cheers,

f


```

