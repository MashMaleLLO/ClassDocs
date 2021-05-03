print("*** Reading E-Book ***")
Text , Highlight = input("Text , Highlight : ").split(",")
HighlightedText = ""
for i in Text:
    if i == Highlight:
        HighlightedText += "[{}]".format(i)
    else:
        HighlightedText += i
print(HighlightedText)            
