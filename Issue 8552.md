# Issue 8552: replace os.system calls in latex.py with appropriate replacements

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2010-03-17 08:35:51

Assignee: tbd

CC:  jhpalmieri

This is a followup to #8486, which uses `os.system('which xelatex')` to see if XeLaTeX is available. With #8474 now merged, we should use `have_program` to do that, and also replace other uses of `os.system` with appropriate `subprocess` replacements, since we are [supposed to use subprocess, and not os.system](http://docs.python.org/library/os.html#os.system)


---

Attachment

clean up unnecessary whitespace in latex.py


---

Comment by ddrake created at 2010-03-23 13:55:31

replace os.system with subprocess.call; apply on top of whitespace patch


---

Comment by ddrake created at 2010-03-23 14:12:20

Changing status from new to needs_review.


---

Attachment

These patches depend on the "v2" patch at #8486.
         
Please look this patch over. I think I've tested all the execution paths and have everything working, but I only tested it on one system, so it needs some review and testing.

A design decision that needs to be addressed: it's easiest to just do `subprocess.call()`, which waits for the command to finish; there are a few places where the `os.system` call ended with `&` to put the command in the background. I can reproduce that behavior with the subprocess module, but it's not as convenient, since I have to spawn the process and poll and so on. I can't detect much of a pattern or necessity to those places that possibly put the command in the background; is it okay if we just eliminate that option?

Another issue: the viewer commands from `misc.viewer` on Linux all return strings with a space in them: `'sage-native-execute xdg-open'`, which does not play nicely with subprocess; when you put that string into its call list, it tries to execute a single command with a space in it, named "sage-native-execute xdg-open" and this does not work well. It's easy enough to snag the "xdg-open" part, but if we eventually are using subprocess everywhere, we should switch the viewer commands to returning lists of strings.


---

Comment by jhpalmieri created at 2010-06-23 20:35:30

Overall, it looks good.

I think line 615, `debug=True` should be deleted.  I also think that before line 1793

```
print 'viewer: "{0}"'.format(viewer)
```

we should have `if debug:`

I notice that you don't seem to be using "base" in the switch from 

```
lt = 'cd "%s"&& sage-native-execute %s \\\\nonstopmode \\\\input{%s.tex} %s'%(base, command, filename, redirect)
```

to

```
lt = ['sage-native-execute', command, r'\nonstopmode', r'\input{' + filename + '.tex}'] 
```

But it seems to work with your patch, so I guess it's okay.

> is it okay if we just eliminate that [background] option?

I think so.  If you think it's worth asking around, you could post on sage-devel.  Anyway, I think we can eliminate it, but we should probably keep the argument there for backwards compatibility, but have it do nothing -- this is what your patch does, right?  We (meaning you) just need to document that the option no longer does anything.

> Another issue: the viewer commands from misc.viewer on Linux all return strings with a space in them

If "s" is the output of one of these commands, can we do s.split() to turn it into a list, split at spaces (if there are any)?  Oh, I guess that's what you're doing.

----------

Summary: fix the debugging issues (the print statement), and document the fact that "do_in_background" now has no effect, and I think this is ready to go.


---

Comment by jhpalmieri created at 2010-06-23 20:35:30

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2011-03-25 19:36:46

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2011-03-25 19:36:46

I'm attaching two new patches here.  One is a referee patch, present for review only: do not apply it.  The other combines all of the patches into one.  Dan, if you're happy with my changes, please give this a positive review.


---

Attachment

for review only, do not apply (diff between Dan's two patches and the all-in-one patch)


---

Comment by jhpalmieri created at 2011-03-25 19:37:59

apply only this patch


---

Attachment

Thanks for finishing this, John. Sorry I left it unfinished. Your changes look good.


---

Comment by ddrake created at 2011-03-26 07:55:07

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-04-07 08:38:01

Resolution: fixed
