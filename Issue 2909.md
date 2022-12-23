# Issue 2909: notebook -- implement a way of parsing script tags in output as they appear (but none that already appeared)

Issue created by migration from https://trac.sagemath.org/ticket/2909

Original creator: was

Original creation time: 2008-04-13 18:04:03

Assignee: boothby

CC:  mpatel

The canonical example to get to work is the following (submitted by Jason Grout):


```
for i in range(5):
    print html('<script>alert(%s)</script>'%i)
    sleep(1)
```


would pop up a dialog box about every second.


This feature was requested by `gerhard <ge01705`@`yahoo.de>`.


---

Comment by schilly created at 2008-04-14 08:55:11

I don't know the details of the notebook source code, but one possible way to run javascript code out of javascript is writing it dynamically into the source, because it get's evaluated. The hack: unescape escaped characters!


```
<html>
<head>
<script type="text/javascript">
function run() {
   eval(cmd);
}
</script>
</head>
<body>

<script type="text/javascript">
cmd = 'alert("I am an alert")';
</script>

<script type="text/javascript">
document.write(unescape("%3Cscript type='text/javascript'%3E" + "run('" + cmd + "');" + "%3C/script%3E"));
</script>

</body>
</html>
```


the generated source code, after running everything, relevant part:


```
<script type="text/javascript">
document.write(unescape("%3Cscript type='text/javascript'%3E" + "run('" + cmd + "');" + "%3C/script%3E"));
</script><script type="text/javascript">run('alert("I am an alert")');</script>
```



---

Comment by schilly created at 2008-04-14 09:25:41

ok, i'm confused, maybe my last comment is helpful for something else - just tested the cannonical exmaple, and it works for me.


---

Comment by timdumol created at 2010-01-17 00:13:12

Changing type from defect to enhancement.


---

Comment by kcrisman created at 2014-09-18 02:38:17

> ok, i'm confused, maybe my last comment is helpful for something else - just tested the cannonical exmaple, and it works for me.

Ah, but _does_ it?  For me, it first prints out the (empty) lines every second, and only then all the alerts come up (in order) at once.


---

Comment by boothby created at 2020-03-29 02:03:43

Closing deprecated notebook tickets


---

Comment by boothby created at 2020-03-29 02:03:43

Resolution: invalid
