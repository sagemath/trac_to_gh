# Issue 308: log_html() crashes because of an undefined variable

Issue created by migration from Trac.

Original creator: dfdeshom

Original creation time: 2007-03-04 06:39:51

Assignee: was

`log_html` crashes because of an undefined variable:


```
sage: log_html ()
[..]
   245         T = self._title()
   246         inlog = os.path.split(self._input_log_name())[1]
--> 247         return '<html>%s<title>%s</title>\n<body><h1
align=center>%s</h1>\n<h2 align=center><a
href="%s">%s</a></h2><pre>'%(REFRESH,T,T, inlog, inlog)   
<type 'exceptions.NameError'>: global name 'REFRESH' is not defined
```


I'm not sure what the variable `REFRESH` is referring to, but removing
it takes care of the problem. A patch is available here:
http://sage.math.washington.edu/home/dfdeshom/custom/patches/log.py.hg



---

Comment by mabshoff created at 2007-08-24 23:18:25

Mmmh, I get the following:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.2, Release Date: 2007-08-22                       |
| Type notebook() for the GUI, and license() for information.        |
sage: log_html ()
HTML Logger
sage: 1+1
2
```

Can this be closed now? 

Cheers,

Michael


---

Comment by was created at 2007-08-29 23:59:10

Resolution: fixed
