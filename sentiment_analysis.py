from textblob import TextBlob

text = input("Enter a sentence: ")

analysis = TextBlob(text)

if analysis.sentiment.polarity > 0:
    print("Positive Sentiment 😊")
elif analysis.sentiment.polarity < 0:
    print("Negative Sentiment 😔")
else:
    print("Neutral Sentiment 😐")