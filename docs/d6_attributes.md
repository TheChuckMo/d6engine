# d6Engine Attribute System

### D6Attribute object

```pythonstub
from d6engine.attribute import D6Attribute, D6AttributeList
strength = D6Attribute(label='Strength')
wisdom = D6Attribute(label='Wisdom', value=2)
strength.label
'Strength'
strength.value
3
str(wisdom)
'Wisdom'
int(wisdom)
2
strength = strength + 1
strength.value
4
wisdom += 2
int(wisdom)
4
```

### D6AttributeList object

```pythonstub
from d6engine.attribute import D6Attribute, D6AttributeList
attributes = D6AttributeList()
attributes.strength.label
'Strength'
attributes.strength.value
3
str(attributes.willpower)
'Willpower'
int(attributes.willpower)
3
attributes.strength.value = 2
attributes.strength.value
2
```