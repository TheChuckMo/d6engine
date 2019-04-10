from d6engine.attribute import D6Attribute

# single attribute unit tests

# Creation
wisdom = D6Attribute(label='Wisedom', value=4, min=2, max=7)

assert wisdom.value == 4
assert wisdom.min == 2
assert wisdom.max == 7
assert wisdom.label is 'Wisedom'

# Assignment
wisdom.value = 5
wisdom.label = 'Wisdom'

assert wisdom.value == 5
assert wisdom.label is 'Wisdom'

# Add
wisdom = wisdom + 1

assert wisdom.value == 6

# Subtract
wisdom = wisdom - 1

assert wisdom.value == 5

# Simple creation
strength = D6Attribute(label='Strength')

assert strength.value == 3
assert strength.min == 1
assert strength.max == 6
assert strength.label is 'Strength'

# increment
strength += 2

assert strength.value == 5

# decrement
strength -= 4

assert strength.value == 1


