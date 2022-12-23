# Issue 5232: [with patch; needs review] interact -- major bug in interact ranges due to str versus repr

Issue created by migration from https://trac.sagemath.org/ticket/5232

Original creator: was

Original creation time: 2009-02-11 05:43:05

Assignee: itolkov

This is related a little to #5220, but tangentially.

In sage-3.3.alphpha5 the following is now COMPLETELY BROKEN:

```
@interact
def f(s=(0,pi,1)):
    print s
```


Basically anything involving symbolics in ranges is broken. If you try this in the console you'll see the reason:


```
sage: @interact
....: def f(s=(0,pi,1)):
....:         print s
....: 
<html><!--notruncate--><div padding=6 id='div-interact-0'> <table width=800px height=20px bgcolor='#c5c5c5'
                 cellpadding=15><tr><td bgcolor='#f9f9f9' valign=top align=left><table><tr><td align=right><font color="black">s&nbsp;</font></td><td><table><tr><td>
    	<div id='slider-s-0' class='ui-slider ui-slider-3' style='margin:0px;'><span class='ui-slider-handle'></span></div>
    	</td><td><font color='black' id='slider-s-0-lbl'></font></td></tr></table><script>(function(){ var values = ["
                                       0","
                                       1","
                                       2","
                                       3","pi"]; setTimeout(function() {
```


Notice that the range values -- 0, 1, 2,3, etc., are symbolic and printed via ascii art. This is thus a similar problem.  It is I think a massive bug -- it causes mysterious hangs in numerous natural situations.


---

Comment by was created at 2009-02-11 05:47:26

Changing priority from major to critical.


---

Attachment

Looks good.


---

Comment by mabshoff created at 2009-02-11 06:32:08

Merged in Sage 3.3.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-11 06:32:08

Resolution: fixed
