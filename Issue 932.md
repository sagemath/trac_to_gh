# Issue 932: upgrade lcalc in sage

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-10-19 18:58:49

Assignee: was


```

Hi William. Before you go ahead and make a big official table like that,
you should upgrade to the latest lcalc. I'll be releasing that in a few
days. It has a more efficient zero finding routine and also gets rid of
annoying warning message that sometimes appears when it ought not to...
the message might interfere with the preparation of your table. Also,
currently not all digits outputed are guaranteed. For low conductor I
don't think that will be an issue, but as the conductor increases
that will be a bit relevant.

I'm currently implementing something to verify the precision and adjust the
output accordingly.

It also has other improvements, though not relevant for the table you
mention.

Mike}}}


---

Comment by mabshoff created at 2007-10-19 19:23:51

I am not sure if this is going to make it for 2.8.8, but we ca at least try.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-27 17:26:38

Mike Rubinstein says:

```
Dear Colleagues,

I've released a new version of lcalc.

This release fixes some bugs (so please update), has improvements to
some of the key
routines, especially for higher degree L-functions (i.e. deg >=3, and
also for Maass forms),
and better handling of output precision.

The code can be downloaded from:
http://pmmac03.math.uwaterloo.ca/~mrubinst/L_function_public/CODE/

Please email me any bugs you notice.

Thanks,
Mike
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-01-27 17:27:27

Hmm, see also #1626 and #449.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-27 17:28:20

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-01-27 17:28:20

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2008-03-26 00:10:29

Resolution: duplicate


---

Comment by mabshoff created at 2008-03-26 00:10:29

This is a dupe of #1626
