# Issue 5251: preparser bug in parsing the backslash "solve right" notation

Issue created by migration from https://trac.sagemath.org/ticket/5251

Original creator: was

Original creation time: 2009-02-13 00:06:12

Assignee: cwitty


```
sage: A = matrix(QQ,2,2,[1..4])
sage: A \ matrix(QQ,2,1,[1,2])

[  0]
[1/2]
sage: A \ matrix(QQ,2,1,[1/3,2/3])
------------------------------------------------------------
   File "<ipython console>", line 1
     A ._backslash_( matrix(QQ,Integer(2),Integer(1),[Integer(1))/Integer(3),Integer(2)/Integer(3)])
                                                                ^
SyntaxError: invalid syntax

```



---

Comment by mhansen created at 2009-02-15 03:23:50

Changing status from new to assigned.


---

Comment by mhansen created at 2009-02-15 03:23:50

Changing assignee from cwitty to mhansen.


---

Attachment

I posted a patch which fixes this, but I don't completely understand the intention behind the stopping condition in question.  I'm not sure what the '/' in the list of characters was meant to prevent.


---

Comment by was created at 2009-02-15 07:01:49

I read the stopping condition code, and realized it is easy to make up many other examples that break the \ notation, even after the above patch is applied:

```
sage: A = matrix(QQ,2,2,[1..4])
sage: matrix(QQ,2,1,[1/3,"2/3"])  # valid notation

[1/3]
[2/3]
sage: A \ matrix(QQ,2,1,[1/3,"2/3"])
------------------------------------------------------------
   File "<ipython console>", line 1
     A ._backslash_( matrix(QQ,Integer(2),Integer(1),[Integer(1)/Integer(3),)"2/3"])
                                                                            ^
SyntaxError: invalid syntax

sage: A \ matrix(QQ,2,1,[1/3,'2/3'])
------------------------------------------------------------
   File "<ipython console>", line 1
     A ._backslash_( matrix(QQ,Integer(2),Integer(1),[Integer(1)/Integer(3),)'2/3'])
                                                                            ^
SyntaxError: invalid syntax

sage: A \ matrix(QQ,2,1,[1/3,2*3])
------------------------------------------------------------
   File "<ipython console>", line 1
     A ._backslash_( matrix(QQ,Integer(2),Integer(1),[Integer(1)/Integer(3),Integer(2))*Integer(3)])
                                                                                      ^
SyntaxError: invalid syntax
```


The point of the stopping condition is that one should be able to do, e.g.,

```
A \ stuff # this does something, 
```

and get

```
A._backslash_(stuff)  # this does something
```

instead of

```
A._backslash_(stuff  # this does something)
```

Another example:

```
A \ B + C
```

should become

```
A._backslash_(B) + C
```


Now that is *not* correctly parsed:

```
sage: preparse('A \ B + C')
'A ._backslash_( B + C)'
```

It should be parsed to

```
A._backslash_(B) + C
```


Here is another that isn't correctly parsed:

```
sage: preparse( 'A\eval("C+D")' )
'A._backslash_(eval()"C+D")'
```


It should be

```
A._backslash_(eval("C+D"))
```


Finally, the / was there before because of precedence.  I.e., the following
is now wrong after the patch:

```
sage: preparse('A \\ x  / 5')
'A ._backslash_( x  / Integer(5))'
```

but we should get

```
sage: preparse('A \\ x  / 5')
'A ._backslash_( x ) / Integer(5)'
```

since precedence of backslash should be left to right (just like that of /).


----

Comments:

1. I find the backslash notation -- which is from Matlab -- very useful and do use it all the time. Otherwise, I wouldn't have noticed the bug I reported in this ticket.

2. Clearly whoever (=me, of course!) implemented this in preparser.py did a very bad job, and this is an extremely buggy feature with the potential to lead to serious confusion and wrong answers.  It's not the sort of thing that should be implemented without using a more sophisticated parsing technique.  

3. I almost think it would be better that this feature didn't exist given the bugs I listed above.


---

Comment by was created at 2009-02-15 07:20:33


```
22:57 < wstein> mhansen -- Hi -- I posted some remarks on #5251
22:58 < mhansen> I'm reading them now.
22:58 < wstein> I'm ashamed of how bad the preparser is on \.
22:58 < wstein> It's all my fault, of course.
22:58 < wstein> I also just wrote Robertwb to ask him to comment on the ticket... even though that
                might mean waiting for his
22:58 < wstein> feedback until Monday.
23:02 < mhansen> One quick fix on the safe side would be to eliminate the stopping condition.  That's
                 how I figured it was implemented anyway.  I only thought a simple "A \ x" syntax was
                 supported.
23:02 < wstein> A\x + B\y would be a disaster.
23:02 < wstein> Of course, it already is :-)
23:02 < mabs> :)
23:02 < wstein> sage: preparse(r'A\x + B\y')
23:02 < wstein> 'A._backslash_(x + B)._backslash_(y)'
23:03 < mhansen> Obviously no one has used it for anything too involved :-)
23:03 < wstein> without the stopping, we would have
23:03 < wstein> sage: preparse(r'v = A\x  # find the solution')
23:03 < wstein> 'v = A._backslash_(x  )# find the solution'
23:03 < wstein> oops
23:03 < wstein> that's now
23:03 < wstein> we would have
23:03 < wstein> 'v = A._backslash_(x  # find the solution)'
23:04 < wstein> I wonder if we should deprecate it?
23:04 < wstein> I like the feature, but the implementation is so bad.
23:04 < wstein> And doing it right might be quite hard.
23:04 < wstein> Also, it clearly can't be used that much...
23:05 < mhansen> I would probably throw in a deprecation warning until we do a proper fix.
23:05 < wstein> Use, I definitely mean by deprecate that there would be a deprecation warning.
23:05 < mhansen> Just so anyone who uses it knows there are "issues".
23:05 < wstein> Yep.
23:05 < wstein> How to do it -- ?
23:05 < wstein> One way would be to add something to A._backslash_
23:05 < wstein> The other would be to actually make the preparser itself emit a warning as it preparses.
23:05 < wstein> The latter would be more robust.
23:06 < mhansen> That was what I was envisioning.
23:06 < wstein> It's possible other code already in preparser.py can be used though to quickly fix this
                problem well.
23:06 < wstein> Robertwb wrote is particularly good at this sort of thing, being a "compiler guy".
23:06 < mhansen> Agreed.  He has some other improvements to the preparser at #5106.
```



---

Comment by robertwb created at 2009-02-15 08:06:52

Yeah, this is horribly broken. I completely rewrote the preparser in #5106, but I don't think I changed the behavior of the backslash operator much. I've got an idea and will post a new patch as soon as I rebase #5106.


---

Comment by robertwb created at 2009-02-15 09:11:22

I introduced a new class called "BackslashOperator" which has a __mul__ and __rmul__ and gives the \ operator the same precedence as multiplication. 

This patch depends on #5106 (which has been rebased).


---

Comment by mhampton created at 2009-02-17 11:47:32

This looks good to me, apart from the issues mentioned on 5106, which I also applied.


---

Comment by mhampton created at 2009-02-17 13:05:24

I did a test-run, and this seems to break a few doctests, so I am withdrawing my fully positive review.  

schemes/elliptic_curves/padics.py 

is one example, where a wrap-around \ character is parsed incorrectly.  I think this is the only issue but this ticket does deserve a "testall" I think.


---

Comment by robertwb created at 2009-02-17 23:35:16

I thought I had taken care of this case, but I guess not. I'll look into this after eating and feeding the babies.


---

Attachment

OK, a better patch is attached. I see what the error was now--it's worked on all the examples and files I've tested, but I'm doing a -testall now, but things look good so far.


---

Comment by robertwb created at 2009-02-18 03:23:43

All tests pass.


---

Comment by mhansen created at 2009-02-18 04:33:32

Looks good to me.  Nice work on this Robert!


---

Comment by mabshoff created at 2009-02-20 07:37:00

Resolution: fixed


---

Comment by mabshoff created at 2009-02-20 07:37:00

Merged 5251-backslash.patch only in Sage 3.3.rc3.

Cheers,

Michael
