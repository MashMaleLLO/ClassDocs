"""
testcase

*** Reading E-Book ***
Text , Highlight : My name is Male and I love to play game,e
My nam[e] is Mal[e] and I lov[e] to play gam[e]

"""

print("*** Reading E-Book ***")
Text , Highlight = input("Text , Highlight : ").split(",")
HighlightedText = ""
for i in Text:
    if i == Highlight:
        HighlightedText += "[{}]".format(i)
    else:
        HighlightedText += i
print(HighlightedText)            

