# Issue 4149: [with patch, needs review] make every field a fraction field

archive/issues_004149.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @mwhansen\n\nKeywords: fraction field, fractionfield\n\nCurrently in Sage:\n\n```\nsage: is_FractionField(FractionField(ZZ))\nFalse\nsage: is_FractionField(QQ)\nFalse\n```\n\nThese bother me.  Since every field is its own fraction field, this patch makes `is_FractionField` return True when the argument is a field.\n\nI've tried to test this for incompatibilities with other parts of Sage -- I searched for `is_FractionField`, and this led to the change to jack.py. (This change is why mhansen is cc'ed on this, since he wrote jack.py.)  I also ran `sage -testall` after committing the change. Have I missed things?\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4149\n\n",
    "created_at": "2008-09-19T01:20:22Z",
    "labels": [
        "component: algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch, needs review] make every field a fraction field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4149",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: tbd

CC:  @mwhansen

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



Issue created by migration from https://trac.sagemath.org/ticket/4149





---

archive/issue_comments_030052.json:
```json
{
    "body": "Attachment [4149.patch](tarball://root/attachments/some-uuid/ticket4149/4149.patch) by @jhpalmieri created at 2008-09-19 01:20:54",
    "created_at": "2008-09-19T01:20:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4149#issuecomment-30052",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [4149.patch](tarball://root/attachments/some-uuid/ticket4149/4149.patch) by @jhpalmieri created at 2008-09-19 01:20:54



---

archive/issue_comments_030053.json:
```json
{
    "body": "Hmm... it's kind of weird since _every_ other is_Something method is really a check on a data-type and only \"coincidentally\" corresponds to the mathematical thing.",
    "created_at": "2008-09-19T01:27:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4149#issuecomment-30053",
    "user": "https://github.com/mwhansen"
}
```

Hmm... it's kind of weird since _every_ other is_Something method is really a check on a data-type and only "coincidentally" corresponds to the mathematical thing.



---

archive/issue_comments_030054.json:
```json
{
    "body": "More specifically, I'd be happier with a is_fraction_field() method that returns what you want.",
    "created_at": "2008-09-19T02:43:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4149#issuecomment-30054",
    "user": "https://github.com/mwhansen"
}
```

More specifically, I'd be happier with a is_fraction_field() method that returns what you want.



---

archive/issue_comments_030055.json:
```json
{
    "body": "Your responses are reasonable from a computing point of view, but since Sage is mathematical software, I think it *should* make sense from a mathematical point of view. If you ask someone, \"What's a simple example of a fraction field?\", the answer will be **Q**, so I would argue that most users would expect `is_FractionField(QQ)` to return True. People who need a data-type check can do `is_instance(x, FractionField_generic)`.\n\nThere is a lot about Sage that I don't know. Are there many cases in which you have something like `FractionField` which is supposed to construct an object in a particular class (like `FractionField_generic`), but which in special cases (like ZZ) returns objects which are not instances of that class? I mean, \n\n```\nsage: is_FractionField(FractionField(ZZ))\nFalse\n```\n \nreally bothers me.",
    "created_at": "2008-09-19T03:46:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4149#issuecomment-30055",
    "user": "https://github.com/jhpalmieri"
}
```

Your responses are reasonable from a computing point of view, but since Sage is mathematical software, I think it *should* make sense from a mathematical point of view. If you ask someone, "What's a simple example of a fraction field?", the answer will be **Q**, so I would argue that most users would expect `is_FractionField(QQ)` to return True. People who need a data-type check can do `is_instance(x, FractionField_generic)`.

There is a lot about Sage that I don't know. Are there many cases in which you have something like `FractionField` which is supposed to construct an object in a particular class (like `FractionField_generic`), but which in special cases (like ZZ) returns objects which are not instances of that class? I mean, 

```
sage: is_FractionField(FractionField(ZZ))
False
```
 
really bothers me.



---

archive/issue_comments_030056.json:
```json
{
    "body": "I would say that none of the is_Something functions should be imported at the top level.  One reason why they're there is to make things easy to refactor / change over time.  If they aren't doing that, then they should probably be removed all together.\n\nI consider both of those situations better than not being able to predict what an is_Something method does.\n\nAdditionally, almost every other mathematical property is queried by an .is_* method on the object itself.",
    "created_at": "2008-09-19T03:54:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4149#issuecomment-30056",
    "user": "https://github.com/mwhansen"
}
```

I would say that none of the is_Something functions should be imported at the top level.  One reason why they're there is to make things easy to refactor / change over time.  If they aren't doing that, then they should probably be removed all together.

I consider both of those situations better than not being able to predict what an is_Something method does.

Additionally, almost every other mathematical property is queried by an .is_* method on the object itself.



---

archive/issue_comments_030057.json:
```json
{
    "body": "Replying to [comment:4 mhansen]:\n> I would say that none of the is_Something functions should be imported at the top level.  \n\nBut they are! That affects the argument: if they weren't imported at the top level, I wouldn't have any objections at all, but as it stands, casual users can easily run into the sorts of issues I'm bringing up, and they will be confused. So there is a clash here between casual users and (I think) developers.  I would suggest that developers can handle confusion better than casual users. I would also suggest that since is_FractionField (for example) is imported at the top level, it is intended for use by casual users, not just developers, and so its output should make mathematical sense.\n\nFinally, if is_Something functions should strictly be checks on data-types, then this should be mentioned in the developer's guide. Is this documented anywhere?",
    "created_at": "2008-09-19T04:35:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4149#issuecomment-30057",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:4 mhansen]:
> I would say that none of the is_Something functions should be imported at the top level.  

But they are! That affects the argument: if they weren't imported at the top level, I wouldn't have any objections at all, but as it stands, casual users can easily run into the sorts of issues I'm bringing up, and they will be confused. So there is a clash here between casual users and (I think) developers.  I would suggest that developers can handle confusion better than casual users. I would also suggest that since is_FractionField (for example) is imported at the top level, it is intended for use by casual users, not just developers, and so its output should make mathematical sense.

Finally, if is_Something functions should strictly be checks on data-types, then this should be mentioned in the developer's guide. Is this documented anywhere?



---

archive/issue_comments_030058.json:
```json
{
    "body": "Replying to [comment:5 jhpalmieri]:\n> But they are! That affects the argument: if they weren't imported at the top level, I wouldn't have any objections at all, but as it stands, casual users can easily run into the sorts of issues I'm bringing up, and they will be confused. \n\nRight, so I think the fix should be to deprecate and then remove them from the top level, and make an is_fraction_field method on rings in Sage.  I'd be willing to do this work.\n\n>So there is a clash here between casual users and (I think) developers.  I would suggest that developers can handle confusion better than casual users. I would also suggest that since is_FractionField (for example) is imported at the top level, it is intended for use by casual users, not just developers, and so its output should make mathematical sense.\n\n> Finally, if is_Something functions should strictly be checks on data-types, then this should be mentioned in the developer's guide. Is this documented anywhere? \n\nI forget if there's a central source.  But, every docstring that I've seen on these functions reflects this.  Even the docstring for is_FractionField states that it \"Tests whether or not x inherits from FractionField_generic.\"",
    "created_at": "2008-09-19T04:43:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4149#issuecomment-30058",
    "user": "https://github.com/mwhansen"
}
```

Replying to [comment:5 jhpalmieri]:
> But they are! That affects the argument: if they weren't imported at the top level, I wouldn't have any objections at all, but as it stands, casual users can easily run into the sorts of issues I'm bringing up, and they will be confused. 

Right, so I think the fix should be to deprecate and then remove them from the top level, and make an is_fraction_field method on rings in Sage.  I'd be willing to do this work.

>So there is a clash here between casual users and (I think) developers.  I would suggest that developers can handle confusion better than casual users. I would also suggest that since is_FractionField (for example) is imported at the top level, it is intended for use by casual users, not just developers, and so its output should make mathematical sense.

> Finally, if is_Something functions should strictly be checks on data-types, then this should be mentioned in the developer's guide. Is this documented anywhere? 

I forget if there's a central source.  But, every docstring that I've seen on these functions reflects this.  Even the docstring for is_FractionField states that it "Tests whether or not x inherits from FractionField_generic."



---

archive/issue_comments_030059.json:
```json
{
    "body": "Replying to [comment:6 mhansen]:\n\n> Right, so I think the fix should be to deprecate and then remove them from the top level, and make an is_fraction_field method on rings in Sage.  I'd be willing to do this work.\n\nBut as the original report points out, every field is a fraction field, so how would is_fraction_field be different from is_field? Do you want them to be synonymous?",
    "created_at": "2008-09-19T05:22:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4149#issuecomment-30059",
    "user": "https://github.com/nbruin"
}
```

Replying to [comment:6 mhansen]:

> Right, so I think the fix should be to deprecate and then remove them from the top level, and make an is_fraction_field method on rings in Sage.  I'd be willing to do this work.

But as the original report points out, every field is a fraction field, so how would is_fraction_field be different from is_field? Do you want them to be synonymous?



---

archive/issue_comments_030060.json:
```json
{
    "body": "I had thought that you wanted it for a particular reason.  I'm definitely fine with not having it at all.",
    "created_at": "2008-09-19T06:03:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4149#issuecomment-30060",
    "user": "https://github.com/mwhansen"
}
```

I had thought that you wanted it for a particular reason.  I'm definitely fine with not having it at all.



---

archive/issue_comments_030061.json:
```json
{
    "body": "I don't think the `is_Something` methods belong in the top level import, at least not as they are implemented now. They are all (explicitly, as pointed out by the documentation, and as used) type checks.",
    "created_at": "2008-09-19T07:34:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4149#issuecomment-30061",
    "user": "https://github.com/robertwb"
}
```

I don't think the `is_Something` methods belong in the top level import, at least not as they are implemented now. They are all (explicitly, as pointed out by the documentation, and as used) type checks.



---

archive/issue_comments_030062.json:
```json
{
    "body": "My 2 cents:  I agree that is_* functions are not needed at the top level, as people can import them if needed in code, while users can use an object's own .is_*() functions.\n\nThe only problem with that is that there will surely be many places where the answer is clear but not currently implemented, such as\nsage: ZZ.is_integrally_closed()\nNotImplementedError  \n\nThis is bound to happen.  There is no algorithm which can be applied to arbitrary rings and determine whether they are integrally closed;  but a lot of special classes are known to be so, and these really should define the relevant functions to return True.",
    "created_at": "2008-09-20T19:45:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4149#issuecomment-30062",
    "user": "https://github.com/JohnCremona"
}
```

My 2 cents:  I agree that is_* functions are not needed at the top level, as people can import them if needed in code, while users can use an object's own .is_*() functions.

The only problem with that is that there will surely be many places where the answer is clear but not currently implemented, such as
sage: ZZ.is_integrally_closed()
NotImplementedError  

This is bound to happen.  There is no algorithm which can be applied to arbitrary rings and determine whether they are integrally closed;  but a lot of special classes are known to be so, and these really should define the relevant functions to return True.



---

archive/issue_comments_030063.json:
```json
{
    "body": "There is currently a distinction between the is_Xxx methods and the is_Xxx functions. For example, the is_Xxx functions determine if the given object is a subclass of the right thing. The is_Xxx method determines whether or not the object in question is (mathematically) of the given type. We should keep the latter, and it should raise a NotImplementedError if it cannot be decided. \n\nI just noticed is_Field has been changed to call is_Field on its argument. If we keep the top level functions (which some people may be more comfortable with), perhaps this is what we should do for all of them.",
    "created_at": "2008-09-20T22:02:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4149#issuecomment-30063",
    "user": "https://github.com/robertwb"
}
```

There is currently a distinction between the is_Xxx methods and the is_Xxx functions. For example, the is_Xxx functions determine if the given object is a subclass of the right thing. The is_Xxx method determines whether or not the object in question is (mathematically) of the given type. We should keep the latter, and it should raise a NotImplementedError if it cannot be decided. 

I just noticed is_Field has been changed to call is_Field on its argument. If we keep the top level functions (which some people may be more comfortable with), perhaps this is what we should do for all of them.



---

archive/issue_comments_030064.json:
```json
{
    "body": "I've created a ticket for the removal of is_Blah functions from top-level imports: #4192.  I hope my summary there is accurate. \n\nPerhaps this ticket should be closed now?",
    "created_at": "2008-09-24T17:06:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4149#issuecomment-30064",
    "user": "https://github.com/jhpalmieri"
}
```

I've created a ticket for the removal of is_Blah functions from top-level imports: #4192.  I hope my summary there is accurate. 

Perhaps this ticket should be closed now?



---

archive/issue_comments_030065.json:
```json
{
    "body": "I agree that this could now be closed in favour of the new one.  (Maybe renaming this one would have been easier, but I'm not sure if that is allowed.)\n\nI bet someone is looking forward to seeing how many things fail when all the is_* functions are removed from top-level imports!",
    "created_at": "2008-09-24T17:26:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4149#issuecomment-30065",
    "user": "https://github.com/JohnCremona"
}
```

I agree that this could now be closed in favour of the new one.  (Maybe renaming this one would have been easier, but I'm not sure if that is allowed.)

I bet someone is looking forward to seeing how many things fail when all the is_* functions are removed from top-level imports!



---

archive/issue_events_004387.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-24T20:51:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4149",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4149#event-4387"
}
```



---

archive/issue_comments_030066.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-09-24T20:51:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4149#issuecomment-30066",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: wontfix



---

archive/issue_comments_030067.json:
```json
{
    "body": "Closed as wontfix as suggested. The issue is now being dealt with at #4192.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-24T20:51:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4149#issuecomment-30067",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Closed as wontfix as suggested. The issue is now being dealt with at #4192.

Cheers,

Michael



---

archive/issue_comments_030068.json:
```json
{
    "body": "Replying to [comment:13 cremona]:\n> I agree that this could now be closed in favour of the new one.  (Maybe renaming this one would have been easier, but I'm not sure if that is allowed.)\n\nIt is allowed for admins in trac and I attempted to grant that right to every logged in user in trac, but the permission model seems to not allow this or I did not read the documentation correctly.\n\n> I bet someone is looking forward to seeing how many things fail when all the is_* functions are removed from top-level imports!\n\n:)\n\nCheers,\n\nMichael",
    "created_at": "2008-09-24T20:53:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4149#issuecomment-30068",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:13 cremona]:
> I agree that this could now be closed in favour of the new one.  (Maybe renaming this one would have been easier, but I'm not sure if that is allowed.)

It is allowed for admins in trac and I attempted to grant that right to every logged in user in trac, but the permission model seems to not allow this or I did not read the documentation correctly.

> I bet someone is looking forward to seeing how many things fail when all the is_* functions are removed from top-level imports!

:)

Cheers,

Michael
