# Issue 4352: add support for weight vectors to gran/groebner_fan

Issue created by migration from https://trac.sagemath.org/ticket/4352

Original creator: mhampton

Original creation time: 2008-10-23 21:23:08

Assignee: mhampton

Keywords: gfan, groebner_fan, weight vectors

This should be pretty straightforward.

sage-support request from Ursula Whitcher:
I asked Anders Jensen, "I would like to compute the weight vectors
corresponding to each reduced Groebner basis in gfan's output.  Is
there a way to tell gfan to do this?"

He replied:

"There is a command "weightvector" that does exactly this. The command
is hidden (does not show up in the manual or the file system). To run
it type "gfan _weightvector" in your shell. MIND THE SPACE BEFORE '_'.
According to the --help text the correct thing to do would be to run
"gfan _weightvector -m" with the gfan output as input.

For example
gfan | gfan _weightvector -m
Q[x,y]
{x-y}

will produce a list of two vectors.
I hope this works out for you.
Best regards,
Anders"

Is there a way to access the weightvector command from the Sage
implementation of gfan?

Thanks!
Ursula 


---

Attachment

based on 3.1.4 but should be fine against 3.2-alpha0


---

Comment by was created at 2008-11-29 02:49:59

REVIEW:

patch applies and passes test.  Code raises major red flag!!

```
	        ans = eval(ans.replace('{','').replace('}','').replace('\n','')) 
```


If the output -- which you make into vectors over QQ ever actually has any rational numbers, then eval will do very bad things to them, e.g., 

```
sage: eval('2/3')
0
```

Oops!

Use sage_eval instead:

```
sage: sage_eval('2/3')
2/3
```



---

Attachment

supercedes previous patch, addresses review


---

Comment by mabshoff created at 2008-11-30 06:41:32

This patch no longer applies cleanly to my 3.2.1.rc1 merge tree:

```
sage-3.2.1.rc1/devel/sage$ patch -p1 --dry-run < trac_4352_2.patch 
patching file sage/rings/polynomial/groebner_fan.py
Hunk #2 FAILED at 76.
1 out of 3 hunks FAILED -- saving rejects to file sage/rings/polynomial/groebner_fan.py.rej
```

I gather from the patch description that only trac_4352_2.patch should be applied. So unless I am mistaken please rebase this. If there are unknown dependencies for this ticket please list them.

Cheers,

Michael


---

Attachment

rebased against 3.2.1.rc0


---

Comment by mabshoff created at 2008-11-30 23:11:55

Merged 4352_3.patch in Sage 3.2.1.rc1


---

Comment by mabshoff created at 2008-11-30 23:11:55

Resolution: fixed
