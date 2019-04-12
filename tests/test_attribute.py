# todo needs to be converted to actual pytest code.
from d6engine.resource.attribute import D6CharacterAttributeEntry

wisattr = D6CharacterAttributeEntry(label='Wisdom')
strattr = D6CharacterAttributeEntry(label='Strength', value=4)
dexattr = D6CharacterAttributeEntry(label='Dexterity', value=2)
chnattr = D6CharacterAttributeEntry(label='Chance', value=4, die=6)

# properties
print(wisattr)
print(int(wisattr))
print(wisattr.name)
print(wisattr.label)
print(wisattr.die)
print(wisattr.value)

# change value
print(wisattr.value)
wisattr += 2
print(wisattr.value)
wisattr -= 4
print(wisattr.value)
wisattr.value = 5
print(wisattr.value)
wisattr.value = wisattr.value - 4
print(wisattr.value)

# .value + int will output an int
print(type(wisattr))
wisattr = wisattr.value + 4
print(type(wisattr))
wisattr = D6CharacterAttributeEntry(label='Wisdom')
print(type(wisattr))

# adding attributes will output an int
health = wisattr + strattr + chnattr
print(type(health))
print(health)


from d6engine.resource.attribute import D6CharacterAttributeComponent

attr_component = D6CharacterAttributeComponent([wisattr, strattr, dexattr, chnattr])


from d6engine.resource.character import D6CharacterSheet

d6_char = D6CharacterSheet([attr_component])

d6_char.name





