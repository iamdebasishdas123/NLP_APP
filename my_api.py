import paralleldots

class api:
    def __init__(self):
        paralleldots.set_api_key('nij30PI1HzQGNSyY1DZBFNhyKi0aAQ8bcshyDS51wos')
    
    def sentiment_analysis(self,text):
        response=paralleldots.sentiment(text)
        return response
    
    def abuse_analysis(self,text):
        response=paralleldots.batch_abuse(text)
        return response
    
    def ner_analysis(self,text):
        response=paralleldots.batch_ner(text)
        return response