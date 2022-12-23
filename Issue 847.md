# Issue 847: rewrite the symbolic calculus package to do evaluation / simplification without recursion

Issue created by migration from https://trac.sagemath.org/ticket/847

Original creator: was

Original creation time: 2007-10-10 22:51:26

Assignee: was

I very much agree with Mike Hansen's conclusion below, which is basically that
we have to rewrite the calculus package (at some point) to not use recursion
in the way it currently does. 


```
Answer: apparently SAGE/Python can't handle numbers bigger than it.

If I type:

z=5/994;y=0;count=0
for j in range(994):
   y+=z
   count+=y^2
print(float(count*z))

I get 41.7295650158 as expected.

However, if I define

def right(f,a,b,n):
   Deltax=(b-a)/n;c=a;est=0
   for i in range(n):
       c+=Deltax
       est+=f(c)
   return(float(est*Deltax))

and then use

right(x^2,0,5,994)

I get a horrible endless loop of error messages identical (!) to

 File "/Applications/.../python2.5/site-packages/sage/calculus/
calculus.py", line 2739, in __float__
   fops = [float(op) for op in self._operands]

But if I do

right(x^2,0,5,993)

Then all is well and I get

41.729628378846591

as desired.

Does this make any sense to anybody?  It's not just 994 - any larger
number creates the same behavior, while the script without definition
works fine.  I'm baffled.  I tried the same experiment on sagenb.org
and got the normal answer where expected, but once again got this
message when I defined the function once I let n>993, while n=993
worked fine after about 5 seconds.  I was using 2.7.3 at home,
presumably the latest release on sagenb.org.  What is up with line
2739?  It's in the constructor for symbolic arithmetic.

Thanks for any insight - hopefully also helping make the software
better.


--~--~---------~--~----~------------~-------~--~----~
To post to this group, send email to sage-support@googlegroups.com
To unsubscribe from this group, send email to sage-support-unsubscribe@googlegroups.com
For more options, visit this group at http://groups.google.com/group/sage-support
URLs: http://sage.math.washington.edu/sage/ and http://sage.scipy.org/sage/
-~----------~----~----~----~------~----~------~--~---


	
Reply	Forward	Invite kcrisman to chat
	
	
		
		
	 Reply 		
Reply to all Reply to allForward Forward Print Add Mike to Contacts list Delete this message Report phishing Show original Message text garbled?
	Mike Hansen 	
to sage-support
	
show details
	 3:04 pm (38 minutes ago) 

Hello,

The issue is that you are passing in x^2 as a function.  Since x is
defined by default to be a symbolic expression, then x^2 is also a
symbolic expression.  Furthermore, when you apply it to a value, you
also get a symbolic expression.  See this:

sage: g = x^2
sage: type(g)
<class 'sage.calculus.calculus.SymbolicArithmetic'>
sage: g._operator
<built-in function pow>
sage: g._operands
[x, 2]
sage: a = g(2)
sage: a
4
sage: type(a)
<class 'sage.calculus.calculus.SymbolicArithmetic'>
sage: a._operator
<built-in function pow>
sage: a._operands
[2, 2]

In your loop, when you do est += f(c), you build up a huge symbolic
expression.  When you try to convert it to a float, it goes down this
tower and tries to convert everything to floats, but it will only go
so far down before hitting a maximum recursion error.  That is why you
are seeing the cutoff around 994.

Symbolic arithmetic is very slow so I personally don't recommend using
it where you don't need to.  Here is a much better solution which
doesn't rely on symbolic expressions.

sage: f = lambda x: x^2
sage: right(f,0,5, 993)
41.72962837884662
sage: right(f,0,5, 1000)
41.729187499999995
sage: right(f,0,5, 10000)
41.672916874999999
sage: time right(f,0,5, 100000)
CPU times: user 0.40 s, sys: 0.02 s, total: 0.42 s
Wall time: 0.43
41.667291668749996

That being said, some thought should be given to simplifying symbolic
expressions after substitution (i.e., f(c)) so that the error you got
doesn't happen.

Hope that helps,
Mike
- Hide quoted text -


On 10/10/07, kcrisman <kcrisman@gmail.com> wrote:
>
> Answer: apparently SAGE/Python can't handle numbers bigger than it.
>
> If I type:
>
> z=5/994;y=0;count=0
> for j in range(994):
>     y+=z
>     count+=y^2
> print(float(count*z))
>
> I get 41.7295650158 as expected.
>
> However, if I define
>
> def right(f,a,b,n):
>     Deltax=(b-a)/n;c=a;est=0
>     for i in range(n):
>         c+=Deltax
>         est+=f(c)
>     return(float(est*Deltax))
>
> and then use
>
> right(x^2,0,5,994)
>
> I get a horrible endless loop of error messages identical (!) to
>
>  File "/Applications/.../python2.5/site-packages/sage/calculus/
> calculus.py", line 2739, in __float__
>     fops = [float(op) for op in self._operands]
>
> But if I do
>
> right(x^2,0,5,993)
>
> Then all is well and I get
>
> 41.729628378846591
>
> as desired.
>
> Does this make any sense to anybody?  It's not just 994 - any larger
> number creates the same behavior, while the script without definition
> works fine.  I'm baffled.  I tried the same experiment on sagenb.org
> and got the normal answer where expected, but once again got this
> message when I defined the function once I let n>993, while n=993
> worked fine after about 5 seconds.  I was using 2.7.3 at home,
> presumably the latest release on sagenb.org.  What is up with line
> 2739?  It's in the constructor for symbolic arithmetic.
>
> Thanks for any insight - hopefully also helping make the software
> better.
>
>
> >
>

--~--~---------~--~----~------------~-------~--~----~
To post to this group, send email to sage-support@googlegroups.com
To unsubscribe from this group, send email to sage-support-unsubscribe@googlegroups.com
For more options, visit this group at http://groups.google.com/group/sage-support
URLs: http://sage.math.washington.edu/sage/ and http://sage.scipy.org/sage/
-~----------~----~----~----~------~----~------~--~---


	
Reply	Forward	Mike is not available to chat
	
	
	
	
#  Choose Language
#   Auto
#   English (US)
#   English (UK)
#   Deutsch
#   Español
#   Português
#   Português (Portugal)
#   Français
#   Italiano
#   Nederlands
#   Polski
#   Svenska
#   Norsk
#   Suomi
#   Dansk
#   Български
#   Hrvatski
#   Magyar
#   Slovenský
#   Slovenščina
#   Українська
#   Tiếng Việt
#   Ελληνικά
#   Íslenska
#   Bahasa Indonesia
#   Català
#   Český
#   Eesti keel
#   हिन्दी
#   Lietuvių
#   Română
#   Русский
#   Tagalog
#   Hebrew
#   Arabic
#   Malay
#   Latin
	
	
	
	
		
New window
Print all
Collapse all
Forward all
 
« Back to Inbox
ArchiveReport SpamDelete
‹ Newer 3 of 4 Older ›
Compose a message in a new window by pressing "Shift" while clicking Compose Mail or Reply.
You are currently using 1301 MB (44%) of your 2911 MB.
Gmail view: standard with chat | standard without chat | basic HTML  Learn more
©2007 Google - Terms of Use - Privacy Policy - Program Policies - Google Home
```



---

Comment by was created at 2007-11-30 22:01:24

[Referee remark] Very good -- just add some more doctests to illustrate what is being fixed.  Great work!


---

Comment by mabshoff created at 2007-11-30 22:03:49

And a short 2 line summary of what was fixed would also be very nice.

Cheers,

Michael


---

Comment by was created at 2007-11-30 22:06:47

Officially refereed -- it works.  And it also fixes another bug reported on sage-support day by John Perry.  Nice!

All it needs now is that spelling error fixed and a doctest to illustrate the recursion.


---

Attachment


---

Comment by mhansen created at 2007-11-30 22:59:37

Basically, the following things were changed:
  1) Arithmetic with SymbolicConstants should produce SymbolicConstants (where it makes sense)
  2) When performing substitution with a SymbolicArithmetic object, the result should be a SymbolicConstant if all the operands are.


---

Comment by mhansen created at 2007-11-30 22:59:37

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2007-11-30 22:59:37

Changing status from new to assigned.


---

Comment by cwitty created at 2007-12-01 02:01:57

The revised patch looks good to me.


---

Comment by mabshoff created at 2007-12-01 11:13:25

Resolution: fixed


---

Comment by mabshoff created at 2007-12-01 11:13:25

Merged in 2.8.15.alpha0.

Applied with slight offset:

```
sage$ hg import 847.patch
applying 847.patch
patching file sage/calculus/calculus.py
Hunk #5 succeeded at 2877 with fuzz 2 (offset 35 lines).
```

