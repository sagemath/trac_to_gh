# Issue 4149: [with patch, needs review] make every field a fraction field

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2008-09-19 01:20:22

Assignee: tbd

CC:  mhansen

Keywords: fraction field, fractionfield

Currently in Sage:

```
sage: is_FractionField(FractionField(ZZ))
False
sage: is_FractionField(QQ)
False
```

These bother me.  Since every field is its own fraction field, this patch makes `is_FractionField` return True when the argument is a field.

I've tried to test this for incompatibilities with other parts of Sage -- I searched for `is_FractionField`, and this led to the change to jack.py. (This change is why mhansen is cc'ed on this, since he wrote jack.py.)  I also ran `sage -testall` after committing the change. Have I missed things?




---

Attachment


---

Comment by mhansen created at 2008-09-19 01:27:40

Hmm... it's kind of weird since _every_ other is_Something method is really a check on a data-type and only "coincidentally" corresponds to the mathematical thing.


---

Comment by mhansen created at 2008-09-19 02:43:05

More specifically, I'd be happier with a is_fraction_field() method that returns what you want.


---

Comment by jhpalmieri created at 2008-09-19 03:46:42

Your responses are reasonable from a computing point of view, but since Sage is mathematical software, I think it _should_ make sense from a mathematical point of view. If you ask someone, "What's a simple example of a fraction field?", the answer will be *Q*, so I would argue that most users would expect `is_FractionField(QQ)` to return True. People who need a data-type check can do `is_instance(x, FractionField_generic)`.

There is a lot about Sage that I don't know. Are there many cases in which you have something like `FractionField` which is supposed to construct an object in a particular class (like `FractionField_generic`), but which in special cases (like ZZ) returns objects which are not instances of that class? I mean, 

```
sage: is_FractionField(FractionField(ZZ))
False
}}} 
really bothers me.


---

Comment by mhansen created at 2008-09-19 03:54:07

I would say that none of the is_Something functions should be imported at the top level.  One reason why they're there is to make things easy to refactor / change over time.  If they aren't doing that, then they should probably be removed all together.

I consider both of those situations better than not being able to predict what an is_Something method does.

Additionally, almost every other mathematical property is queried by an .is_* method on the object itself.


---

Comment by jhpalmieri created at 2008-09-19 04:35:19

Replying to [comment:4 mhansen]:
> I would say that none of the is_Something functions should be imported at the top level.  

But they are! That affects the argument: if they weren't imported at the top level, I wouldn't have any objections at all, but as it stands, casual users can easily run into the sorts of issues I'm bringing up, and they will be confused. So there is a clash here between casual users and (I think) developers.  I would suggest that developers can handle confusion better than casual users. I would also suggest that since is_FractionField (for example) is imported at the top level, it is intended for use by casual users, not just developers, and so its output should make mathematical sense.

Finally, if is_Something functions should strictly be checks on data-types, then this should be mentioned in the developer's guide. Is this documented anywhere?


---

Comment by mhansen created at 2008-09-19 04:43:34

Replying to [comment:5 jhpalmieri]:
> But they are! That affects the argument: if they weren't imported at the top level, I wouldn't have any objections at all, but as it stands, casual users can easily run into the sorts of issues I'm bringing up, and they will be confused. 

Right, so I think the fix should be to deprecate and then remove them from the top level, and make an is_fraction_field method on rings in Sage.  I'd be willing to do this work.

>So there is a clash here between casual users and (I think) developers.  I would suggest that developers can handle confusion better than casual users. I would also suggest that since is_FractionField (for example) is imported at the top level, it is intended for use by casual users, not just developers, and so its output should make mathematical sense.

> Finally, if is_Something functions should strictly be checks on data-types, then this should be mentioned in the developer's guide. Is this documented anywhere? 

I forget if there's a central source.  But, every docstring that I've seen on these functions reflects this.  Even the docstring for is_FractionField states that it "Tests whether or not x inherits from FractionField_generic."


---

Comment by nbruin created at 2008-09-19 05:22:01

Replying to [comment:6 mhansen]:

> Right, so I think the fix should be to deprecate and then remove them from the top level, and make an is_fraction_field method on rings in Sage.  I'd be willing to do this work.

But as the original report points out, every field is a fraction field, so how would is_fraction_field be different from is_field? Do you want them to be synonymous?


---

Comment by mhansen created at 2008-09-19 06:03:01

I had thought that you wanted it for a particular reason.  I'm definitely fine with not having it at all.


---

Comment by robertwb created at 2008-09-19 07:34:15

I don't think the `is_Something` methods belong in the top level import, at least not as they are implemented now. They are all (explicitly, as pointed out by the documentation, and as used) type checks.


---

Comment by cremona created at 2008-09-20 19:45:39

My 2 cents:  I agree that is_* functions are not needed at the top level, as people can import them if needed in code, while users can use an object's own .is_*() functions.

The only problem with that is that there will surely be many places where the answer is clear but not currently implemented, such as
sage: ZZ.is_integrally_closed()
NotImplementedError  

This is bound to happen.  There is no algorithm which can be applied to arbitrary rings and determine whether they are integrally closed;  but a lot of special classes are known to be so, and these really should define the relevant functions to return True.


---

Comment by robertwb created at 2008-09-20 22:02:54

There is currently a distinction between the is_Xxx methods and the is_Xxx functions. For example, the is_Xxx functions determine if the given object is a subclass of the right thing. The is_Xxx method determines whether or not the object in question is (mathematically) of the given type. We should keep the latter, and it should raise a NotImplementedError if it cannot be decided. 

I just noticed is_Field has been changed to call is_Field on its argument. If we keep the top level functions (which some people may be more comfortable with), perhaps this is what we should do for all of them.


---

Comment by jhpalmieri created at 2008-09-24 17:06:34

I've created a ticket for the removal of is_Blah functions from top-level imports: #4192.  I hope my summary there is accurate. 

Perhaps this ticket should be closed now?


---

Comment by cremona created at 2008-09-24 17:26:59

I agree that this could now be closed in favour of the new one.  (Maybe renaming this one would have been easier, but I'm not sure if that is allowed.)

I bet someone is looking forward to seeing how many things fail when all the is_* functions are removed from top-level imports!


---

Comment by mabshoff created at 2008-09-24 20:51:52

Resolution: wontfix


---

Comment by mabshoff created at 2008-09-24 20:51:52

Closed as wontfix as suggested. The issue is now being dealt with at #4192.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-24 20:53:02

Replying to [comment:13 cremona]:
> I agree that this could now be closed in favour of the new one.  (Maybe renaming this one would have been easier, but I'm not sure if that is allowed.)

It is allowed for admins in trac and I attempted to grant that right to every logged in user in trac, but the permission model seems to not allow this or I did not read the documentation correctly.

> I bet someone is looking forward to seeing how many things fail when all the is_* functions are removed from top-level imports!

:)

Cheers,

Michael
