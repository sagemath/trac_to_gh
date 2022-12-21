# Issue 4524: interact : incomplete default string in the input box

Issue created by migration from Trac.

Original creator: slabbe

Original creation time: 2008-11-14 17:04:23

Assignee: itolkov

Keywords: input_box

Using interact in sage 3.1.4, the default string doesn't print completly in the input box. It looks like it prints up to the first character ' found.
The folowing example works well 


```
`@`interact
def _(a=input_box(default='interact is "cool"',type=str,label='Name:')):
    print a
```


and it puts *interact is "cool"* in the input box. But in the next one, 


```
`@`interact
def _(a=input_box(default="interact is 'cool'",type=str,label='Name:')):
    print a
```


the default string in the input box is incomplete, it puts only *interact is *. So, we don't know if interact is cool or not !


---

Attachment


---

Comment by mhansen created at 2009-01-23 08:11:21

Changing assignee from itolkov to mhansen.


---

Comment by mhansen created at 2009-01-23 08:11:21

Changing status from new to assigned.


---

Comment by slabbe created at 2009-01-23 18:18:01

First, that is the first time I review a patch. So if you have comment on the way I review, tell me. I also have some questions that I write below as I have them. Moreover, I am not familiar with notebook code at all....so should I let the job to somebody else?

However, I applied the patch and I can at least say that the problem I submitted is now fixed which is cool!

There is a small issue here (double that) :


```
Note that any HTML that that uses quotes around this should use double quotes and not single quotes. 
```


Also, I don't know if you agreee, but I suggest to add the second example below :


```
EXAMPLES: 
    sage: from sage.server.notebook.interact import InteractControl 
    sage: InteractControl('x', '"cool"').html_escaped_default_value() 
    '&quot;cool&quot;' 
    sage: InteractControl('x',"'cool'").html_escaped_default_value()
    "'cool'"
```


My last question is : I could have posted a patch for both issues (double that, and the 2nd example). What is commonly done? Do we leave the changes to the patcher?

My statement is Positive review pending fixes on at least the first of my two doc-suggestions.

Thanks for the fix,


---

Comment by mhansen created at 2009-01-24 15:15:01

I've posted a patch which addresses the issues.

You could have posted a patch and then asked me to review your portion of the patch.


---

Attachment

Positive review.


---

Comment by slabbe created at 2009-01-24 16:59:35

I think it can be merged in sage 3.3.


---

Comment by mabshoff created at 2009-01-24 18:42:10

Merged in Sage 3.3.alpha2


---

Comment by mabshoff created at 2009-01-24 18:42:10

Resolution: fixed
