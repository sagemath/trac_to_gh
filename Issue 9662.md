# Issue 9662: gp(string) always returns a value, even when it should not

Issue created by migration from Trac.

Original creator: jdemeyer

Original creation time: 2010-08-01 17:37:29

Assignee: was

When executing a GP command using the Sage interface, a value of 0 is returned when None would be expected.  For example, in a gp shell (started with sage -gp for example):


```
gp> kill(x)   /* No output */
```


But in Sage:

```
sage: gp('kill(x)')
0
```



---

Comment by jdemeyer created at 2010-08-01 17:44:10

This is not easily fixed, it is due to the way how Expect assigns variables.  In fact, one could argue that the observed behaviour is as expected, because in gp, we get

```
gp> a = kill(x)
0
```

So, assigning a nil value makes it into a zero.


---

Comment by jdemeyer created at 2010-08-03 07:13:27

Changing keywords from "" to "pari".


---

Comment by mhansen created at 2013-07-24 12:23:34

Resolution: invalid


---

Comment by mhansen created at 2013-07-24 12:23:34

I agree that this is invalid.  Doing `gp('kill(x)')` means to create an object "kill(x)" in gp, assign it to a variable, and return a object pointing to that variable.


```
sage: type(gp('kill(x)'))
<class 'sage.interfaces.gp.GpElement'>
```


This is how it works for all the interfaces.  If you just want to evaluate a command, then you can do


```
sage: gp.eval('kill(x)')
''
```


which appropriately returns an empty string.
