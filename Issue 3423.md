# Issue 3423: Make Pari error messages more informative

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2008-06-14 01:12:31

Assignee: was

CC:  craigcitro

Consider this sage session:


```
sage: pari('1.q')
---------------------------------------------------------------------------
<class 'sage.libs.pari.gen.PariError'>    Traceback (most recent call last)

/Users/ncalexan/sage-3.0.1.alpha0/devel/sage-cc/sage/rings/number_field/<ipython console> in <module>()

/Users/ncalexan/sage-3.0.1.alpha0/devel/sage-cc/sage/rings/number_field/gen.pyx in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:32332)()

<class 'sage.libs.pari.gen.PariError'>:  (7)
```


as opposed to this gp session:


```
? 1.q
  ***   unknown member function: 1.q
                                   ^-
```


It'd be nice if the error messages we generate are a bit more informative. This may be an arbitrarily large amount of work.


---

Comment by malb created at 2009-01-22 01:22:02

I think I tracked down why we can't display more information as of now:

The `pari_err` function contains the following code:


```
pari_err(long numerr, ...)
{
  char s[128], *ch1;
  PariOUT *out = pariOut;
  va_list ap;

  va_start(ap,numerr);
  if (is_warn(numerr)) pari_err(talker,"use pari_warn for warnings");

  global_err_data = NULL;
  if (err_catch_stack)
  {
    cell *trapped = NULL;
    if ( (trapped = err_seek(numerr)) )
    {
      jmp_buf *e = trapped->penv;
      if (numerr == invmoder)
      {
        (void)va_arg(ap, char*); /* junk 1st arg */
        global_err_data = (void*)va_arg(ap, GEN);
      }
      longjmp(*e, numerr);
    }
```


The difference between us and gp is that `if (err_catch_stack)` evaluates to true because all our pari calls are encapsulated in `_sig_on/_sig_off` calls.


---

Comment by jdemeyer created at 2013-11-02 12:57:20

Duplicate of #9640.


---

Comment by jdemeyer created at 2013-11-02 12:57:20

Resolution: duplicate
