from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


def sentiment_analysis(filename):
    myfile = open('uploads/' + filename, "r")
    text = myfile.read()
    client = language.LanguageServiceClient()
    
    document = types.Document(
           content=text,
           type=enums.Document.Type.PLAIN_TEXT)

    # Detects sentiment in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    sentiment = client.analyze_sentiment(document).document_sentiment
    return sentiment.score
    # print('Score: {}'.format(sentiment.score))
    # print('Magnitude: {}'.format(sentiment.magnitude))

# sentiment_analysis()