import matplotlib.pyplot as pyp
import seaborn as sns

sns.distplot([0,1,2,3,4,5])
pyp.show()
'''
# Create a TextBlob object
text = "TextBlob is a great library for processing textual data."
blob = TextBlob(text)

# Perform some simple analysis
print("Original text:", blob)
print("Word count:", len(blob.words))
print("Sentence count:", len(blob.sentences))
print("Sentiment:", blob.sentiment)
'''