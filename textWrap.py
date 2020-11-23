# TextWrap library
'''
textwrap.wrap(text, width=50, **kwargs): This function wraps the input paragraph such that
 each line in the paragraph is at most width characters long. The wrap method returns a list 
 of output lines.The returned list is empty if the wrapped output has no content. Default width is taken as 50.

'''
import textwrap
  
mytext = """This function wraps the input paragraph such that each line 
in the paragraph is at most width characters long. The wrap method 
returns a list of output lines. The returned list 
is empty if the wrapped 
output has no content."""
  
# Wrap this text. 
wrapper = textwrap.TextWrapper(width=50)
  
sentence_list = wrapper.wrap(text=mytext) 
  
# Print each line. 
for element in sentence_list: 
    print(element)

