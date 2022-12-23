# Issue 4325: CC() fails on Mathematica output

Issue created by migration from https://trac.sagemath.org/ticket/4325

Original creator: ddrake

Original creation time: 2008-10-20 02:17:29

Assignee: was

Keywords: mathematica

Using 3.1.2 on sage.math:

```
sage: mathematica.eval('N[BesselK[1+I, 2+ 3*I], 20]')
         -0.105203133241753451256 + 0.017589014615189905553 I
```

Now say I want to get a CC element out of that:

```
sage: CC(mathematica.eval('N[BesselK[1+I, 2+ 3*I], 20]'))
------------------------------------------------------------
   File "<string>", line 1
     -RealNumber('0.105203133241753451256')+RealNumber('0.017589014615189905553')I
                                                                                 ^
SyntaxError: unexpected EOF while parsing

```

It's confused because Mathematica uses a space between the number and I; a workaround is to put in an asterisk:

```
sage: CC(mathematica.eval('N[BesselK[1+I, 2+ 3*I], 20]').replace(' I', '*I'))
-0.105203133241753 + 0.0175890146151899*I
```

I understand that this kind of parsing can get difficult and complicated, but it seems like something we should aim for.


---

Comment by ddrake created at 2008-10-20 05:42:19

Here's another problem:

```
sage: mathematica.eval('N[BesselK[I-1, I], 30]')

         -0.190193056011529041190471623406 - 
 
>    0.470313413807477232703205350275 I
```

Trying to `CC()` that fails because of the newlines and the `>` in the middle. This may be another ticket entirely, so let me know if I should open another.


---

Comment by jason created at 2008-10-20 10:46:41

In Mathematica, we can set the output to automatically be wrapped in a certain function.  We ought to just write a function that first calls InputForm.


```
sage: CC(mathematica.eval('N[BesselK[1+I, 2+ 3*I], 20]//InputForm[#,NumberMarks->False]&'))
-0.105203133241753 + 0.0175890146151899*I
sage: CC(mathematica.eval('N[BesselK[I-1, I], 30]//InputForm[#,NumberMarks->False]&'))
-0.190193056011529 - 0.470313413807477*I
```


I put the NumberMarks->False option since Sage doesn't know how to deal with the precision information returned from Mathematica.  It would be nice if there was a way to use that in constructing Sage objects.  My guess is it would be fairly easy in Mathematica to write a function that generates Sage output, given that you easily have access to the full parse tree of the function in Mathematica.


Another way to get rid of the precision information is to set $NumberMarks = False:


```
sage: mathematica.eval('$NumberMarks=False')
         False
sage: CC(mathematica.eval('N[BesselK[I-1, I], 30]//InputForm'))-0.190193056011529 - 0.470313413807477*I
```


We can automatically apply the InputForm to any printed output by setting the $PrePrint hook:


```
sage: mathematica.eval('$NumberMarks=False')
         False
sage: mathematica.eval('$PrePrint = InputForm')
         InputForm
sage: CC(mathematica.eval('N[BesselK[I-1, I], 30]'))
-0.190193056011529 - 0.470313413807477*I
sage: CC(mathematica.eval('N[BesselK[1+I, 2+ 3*I], 20]'))
-0.105203133241753 + 0.0175890146151899*I
```



---

Comment by was created at 2008-10-20 15:40:29

The output of mathematica.eval (or in general FOO.eval) must be the string that *system* outputs. There is absolutely no reason any coercion, e.g., CC(FOO.eval(...)) should ever work.  This ticket as is is definitely invalid.

However, it is fair game to want to make something like CC(FOO(...)) work. Note that there is no eval.  So this is the only thing that should work:

```
sage: CC(mathematica('N[BesselK[1+I, 2+ 3*I], 20]'))
```

Unfortunately, due to stuff not being implemented, this doesn't work either.
Another thing that should work is 

```
sage: a = mathematica('N[BesselK[1+I, 2+ 3*I], 20]')
sage: CC((a.Re(), a.Im()))
```

It doesn't, because of #4330.


---

Comment by ddrake created at 2008-10-21 00:19:34

Replying to [comment:2 jason]:
> In Mathematica, we can set the output to automatically be wrapped in a certain function.  We ought to just write a function that first calls InputForm.

Those are good ideas. I wish I had known that when I was using Mathematica a lot more! I spent a *lot* of time manually editing wonky output from Mathematica's primitive command line interface.

Replying to [comment:3 was]:
> The output of mathematica.eval (or in general FOO.eval) must be the string that *system* outputs. There is absolutely no reason any coercion, e.g., CC(FOO.eval(...)) should ever work. This ticket as is is definitely invalid. 

Okay, it's no problem if this is an invalid ticket. Looks like #4330 will fix the true problem here.


---

Comment by ddrake created at 2009-04-22 07:24:06

With #4330 being fixed I'm closing this ticket as fixed. The suggestion given above ([comment:3 was]) works now with 3.4.1.rc4:

```
sage: a = mathematica('N[BesselK[1+I, 2+ 3*I], 30]')
sage: CC((a.Re(), a.Im()))
-0.105203133241753 + 0.0175890146151899*I
```

You lose a bit of precision, there, so you can use RealField and so on:

```
sage: a.Re()
-0.10520313324175345125609254499068
sage: RealField(100)(a.Re())
-0.10520313324175345125609254499
sage: RealField(110)(a.Re())
-0.10520313324175345125609254499070
```


Since this works now, and my original usage of `mathematica.eval` isn't supposed to work, I say this is fixed.


---

Comment by ddrake created at 2009-04-22 07:24:06

Resolution: fixed


---

Comment by mabshoff created at 2009-04-22 07:33:17

Changing status from closed to reopened.


---

Comment by mabshoff created at 2009-04-22 07:33:17

Resolution changed from fixed to 


---

Comment by mabshoff created at 2009-04-22 07:33:17

This ticket should only be closed when a proper doctest has been added. I skimmed #4330 and did not see such a doctest.

Thoughts?

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-22 07:34:52

Resolution: wontfix


---

Comment by mabshoff created at 2009-04-22 07:34:52

And to close this it should be "wontfix" or "invalid" depending on taste. I think that since this is bogus/an abuse of eval we don't need a doctest in this case :).

Cheers,

Michael
