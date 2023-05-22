from django.shortcuts import render
import pickle
import os
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
# Create your views here.


fk_news={
    'first':'''Google Pinterest Digg Linkedin Reddit Stumbleupon Print Delicious Pocket Tumblr 
There are two fundamental truths in this world: Paul Ryan desperately wants to be president. And Paul Ryan will never be president. Today proved it.
''',
'second':'''"Share on Twitter The Wildfire is an opinion platform and any opinions or information put forth by contributors are exclusive to them and do not represent the views of IJR. 
In a campaign ad for Donald Trump, Laura Wilkerson talks about her horrific experience of her son being doused with gasoline and set on fire by an illegal alien. In the ad called â€œLaura,â€ she explains why Hillary Clinton's policies are harmful for America. "
''',
'third':'''"Clinton Camp Desperate, Russia Trains for WWIII US media not letting the public know how tense Russia situation really is Infowars Nightly News   
Russia is training millions domestically for WWIII, the Clinton campaign has gone to drastic measures to appear as if they are still alive, the spy state is taking another step forward and the possible answer to National Anthem protests is revealed.   Download on your mobile device now for free. Today on the Show Get the latest breaking news & specials from Alex Jones and the Infowars crew. From the store Featured Videos FEATURED VIDEOS A Vote For Hillary is a Vote For World War 3 - See the rest on the Alex Jones YouTube channel . The Most Offensive Halloween EVER! - See the rest on the Alex Jones YouTube channel . ILLUSTRATION How much will your healthcare premiums rise in 2017? >25% Â© 2016 Infowars.com is a Free Speech Systems, LLC Company. All rights reserved. Digital Millennium Copyright Act Notice. 34.95 22.46 Flip the switch and supercharge your state of mind with Brain Force the next generation of neural activation from Infowars Life. 
"
''',
'show':True, 'display':True
}

real_news={'show':False, 'display':True,

'first':'''"So, that happened: This week, the early stages of the 2016 presidential election collided headlong with the phenomenon of vaccine denialism, with two candidates ending up in intensive care for foot-in-mouth disease. We'll talk about who took a hit and who managed to avoid this nonsense.

Are you a regular ""So, That Happened"" listener? Let us know! Tell us what you think of the show, what we're messing up and who we need to hear more from. Send us an electronic communication at sothathappened@huffingtonpost.com.

""It's a world in which we need sanity. And this week, we didn't get it."" -- Jason Linkins

Meanwhile, the Obama budget is out, and from the looks of it, it seems the president wants to swing for the fences on infrastructure, early childhood care and increased federal spending. But did he notice that Congress is controlled by the GOP? We'll discuss what compromises are possible.

""It's as though Democrats control both chambers of Congress. There is not an effort which he's made in previous budgets to meet them halfway, or more than halfway."" -- Sabrina Siddiqui

Finally, this was a big week for Downton Abbey-inspired congressional interior decoration scandals. We'll explain how it came to pass that we could put all those words in that previous sentence.

""Washington elites decorate their environs with track lighting, chrome appliances and granite countertops -- a very modern, spare look with open floor plans, and [Aaron] Schock is going in the other direction."" -- Arthur Delaney

We're very happy to let you know that ""So, That Happened"" is now available on iTunes. We've been working to create an eclectic and informative panel show that's constantly evolving, a show that's as in touch with the top stories of the week as it is with important stories that go underreported. We'll be here on a weekly basis, bringing you the goods.

Never miss an episode: Subscribe to ""So, That Happened"" on iTunes, and if you like what you hear, please leave a review. We also encourage you to check out other HuffPost podcasts: HuffPost Comedy's ""Too Long; Didn't Listen,"" the HuffPost Weird News podcast, HuffPost Politics' ""Drinking and Talking,"" HuffPost Live's ""Fine Print"" and HuffPost Entertainment's podcast."
'''
}


def index(request):
    return render(request, 'index.html')

def detector(request):
    return render(request, 'detector.html')

def result(req):
    text = req.POST.get('content')
    model_path = os.path.join(os.path.dirname(__file__), '..', 'static', 'models', 'model.pkl')
    vectorizer_path = os.path.join(os.path.dirname(__file__), '..', 'static', 'models', 'vectorizer.pkl')
    tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

    with open(vectorizer_path, 'rb') as f:
        loaded_vectorizer = pickle.load(f)

    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    
    tfidf_test = loaded_vectorizer.transform([text])
    predictions = model.predict(tfidf_test)
    print(predictions)

    if predictions==['REAL']:
        return render(req, 'result.html', context={'result':'REAL'})
    elif predictions==['FAKE']:
        return render(req, 'result.html', context={'result':'FAKE'})
    return render(req, 'result.html')

def dataset(request):
    return render(request, 'dataset.html')

def news(request):
    if request.method =='GET':
        op = request.GET.get('option')
        if op=='real':
            return render(request, 'news.html', context=real_news)
        elif op=='fake':
            return render(request, 'news.html', context=fk_news)
    return render(request, 'news.html',context={'show':False,'display':False})

def developer(request):
    return render(request, 'developer.html')
