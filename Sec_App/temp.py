import textwrap
'''
value = """This function wraps the input paragraph \n such that each line 
in the paragraph is at most width \n characters long. The wrap method 
returns a list of output lines. \nThe returned list 
is empty if the wrapped 
output has no content."""

# Wrap this text. 
wrapper = textwrap.TextWrapper(width=40)

word_list = wrapper.wrap(text=value)
#print(word_list)

# Print each line. 
#for element in word_list:
#	print(element)

import textwrap

sample_text = """This function wraps the input paragraph such that each line 
n the paragraph is at most width characters long. The wrap method 
returns a list of output lines. The returned list 
is empty if the wrapped 
output has no content."""

print(sample_text)
wrapper = textwrap.TextWrapper(width=50)
dedented_text = textwrap.dedent(text=sample_text)
original = wrapper.fill(text=dedented_text)

print('Original:\n')
print(original)



shortened = textwrap.shorten(text=original, width=100)
shortened_wrapped = wrapper.fill(text=shortened)

print('\nShortened:\n')
print(shortened_wrapped)'''


