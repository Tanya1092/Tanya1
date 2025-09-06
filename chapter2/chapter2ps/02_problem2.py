letter = ''' Dear <|name|>
you are selected!
<|Date|>
'''
print(letter.replace("<|name|>", "Tanya").replace("<|Date|>" , "2 september 2025"))