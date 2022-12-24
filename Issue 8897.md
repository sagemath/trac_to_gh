# Issue 8897: units.mass.pound to units.mass.drachma broken

archive/issues_008897.json:
```json
{
    "body": "Assignee: @burcin\n\n\n```\nsage: a = 170*units.mass.pound\nsage: a.convert(units.mass.drachma)\n```\n\ngives\n\n```\nTypeError: unable to convert x (=kilogram) to an integer\n```\n\ndespite 1 drachma is 0.00429234 kilograms.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8897\n\n",
    "created_at": "2010-05-05T21:27:48Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "units.mass.pound to units.mass.drachma broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8897",
    "user": "@haraldschilly"
}
```
Assignee: @burcin


```
sage: a = 170*units.mass.pound
sage: a.convert(units.mass.drachma)
```

gives

```
TypeError: unable to convert x (=kilogram) to an integer
```

despite 1 drachma is 0.00429234 kilograms.

Issue created by migration from https://trac.sagemath.org/ticket/8897





---

archive/issue_comments_081823.json:
```json
{
    "body": "Same is true for other units of mass or time, that contains tuples in unitdict:\n\n\n```\nsage: sage.symbolic.units.unitdict['mass']['obol']\n\"(0.000715380000000000,{'greek':1/6})\"\nsage: sage.symbolic.units.unitdict['mass']['drachma']\n\"(0.00429234000000000, {'greek':1})\"\nsage: sage.symbolic.units.unitdict['mass']['mina']   \n\"(0.429234000000000, {'greek':100})\"\nsage: sage.symbolic.units.unitdict['mass']['talent']\n\"(25.7540400000000, {'greek':6000})\"\nsage: sage.symbolic.units.unitdict['time']['sidereal_second']\n\"(0.997269566329086, {'sidereal':1})\"\nsage: sage.symbolic.units.unitdict['time']['sidereal_day']\n\"(86164.0905308330, {'sidereal':86400})\"\n```\n\nall those result in same \"unable to convert x to an integer\", coming from:\n\n```\nsage: sage.symbolic.units.base_units(units.time.sidereal_second)\n```\n",
    "created_at": "2012-08-09T11:28:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8897#issuecomment-81823",
    "user": "aginiewicz"
}
```

Same is true for other units of mass or time, that contains tuples in unitdict:


```
sage: sage.symbolic.units.unitdict['mass']['obol']
"(0.000715380000000000,{'greek':1/6})"
sage: sage.symbolic.units.unitdict['mass']['drachma']
"(0.00429234000000000, {'greek':1})"
sage: sage.symbolic.units.unitdict['mass']['mina']   
"(0.429234000000000, {'greek':100})"
sage: sage.symbolic.units.unitdict['mass']['talent']
"(25.7540400000000, {'greek':6000})"
sage: sage.symbolic.units.unitdict['time']['sidereal_second']
"(0.997269566329086, {'sidereal':1})"
sage: sage.symbolic.units.unitdict['time']['sidereal_day']
"(86164.0905308330, {'sidereal':86400})"
```

all those result in same "unable to convert x to an integer", coming from:

```
sage: sage.symbolic.units.base_units(units.time.sidereal_second)
```

