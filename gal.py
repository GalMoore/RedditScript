import nltk, webbrowser, requests, json, random
from nltk import pos_tag, word_tokenize

############################ Classes #######################
class NewsItem:
    def __init__(self, headline, newsImage, newsSource):
        self.headline = headline
        self.newsImage = newsImage
        self.newsSource = newsSource
    def headline(self, text):
        return self.headline
    def newsImage(self, newsImage):
    	return self.newsImage
    def newsSource(self, newsSource):
    	return self.newsSource

class Joke:
    def __init__(self, text, selfText, url, jokeSource):
        self.text = text
        self.selfText = selfText
        self.url = url
        self.jokeSource = jokeSource
    def text(self, text):
        return self.text
    def selfText(self, selfText):
        return self.selfText
    def url(self, url):
        return self.url
    def jokeSource(self, jokeSource):
    	return self.jokeSource

        
############################ End Classes #######################

def main():
	r = requests.get('https://www.reddit.com/r/UpliftingNews/top/.json', headers = {'User-agent': 'Chrome'})
	theJSON = json.loads(r.text)
	newschildren = theJSON["data"]["children"]
	newsItemList = [NewsItem('Future of Farming: Replacing Human Farmers with Robots', 
		'https://i.redditmedia.com/ChxRQ40Yd7xgH3Uy-Rr0xN2rSQ5Mks5e-FioRh94Idw.jpg?s=c167a339424085d9d8c06dff4f025e10',
		'https://medium.com/@austinmunday/future-of-farming-replacing-human-farmers-with-robots-6e899cff1a8f#.nswozymyy'),
        ]
        
# Preloaded one story.
    
####################### For loop uplifting #######################
	
	for post in newschildren:
		if "data" in post and post["data"]["over_18"]==False:
			if 'preview' in post["data"]: 
				headline = post["data"]["title"]
				newsImage = post["data"]["preview"]["images"][0]["source"]["url"]
				newsSource = post["data"]["url"]
				newsInstance = NewsItem(headline, newsImage, newsSource)
				newsItemList.append(newsInstance)
			else:
				pass

	newsItemOne = random.choice(newsItemList)

###################### check for nouns ################
	


####################### NLP #######################

	nouns = [token for token, pos in pos_tag(word_tokenize(newsItemOne.headline))
	if pos.startswith('N')]
	
# 	if not nouns:
# 		pass

		

# 	nouns might be an empty list, if so, %(nouns[0]) will fail because nouns[0] doesnt exist
	Link = 'https://www.reddit.com/r/funny/search.json?q=%25s&sort=top&restrict_sr=on&t=year' % (nouns[0])
	r = requests.get(Link, headers = {'User-agent': 'Chrome'})
	JokeJSON = json.loads(r.text)
	jokeList = newsItemList = [Joke('* NO JOKES FOUND or API GLITCH * SORRY!',
                                '',
                                'https://i.redditmedia.com/ChxRQ40Yd7xgH3Uy-Rr0xN2rSQ5Mks5e-FioRh94Idw.jpg?s=c167a339424085d9d8c06dff4f025e10',
                                'http://i.imgur.com/Ng0I5UA.gif'),
                        		]

####################### for loop jokes #######################
	if 'data' in JokeJSON:
		JokeChildren = JokeJSON["data"]["children"]
		for post in JokeChildren:
			if 'preview' in post["data"] and post["data"]["over_18"]==False:
				title = post["data"]["title"]
				selfText = post["data"]["selftext"]
				url = post["data"]["preview"]["images"][0]["source"]["url"]
				jokeSource = post["data"]["url"]
				jokeInstance = Joke(title, selfText, url, jokeSource)
				jokeList.append(jokeInstance)
			else:
				pass
			
# 	if preview in post data -> 
# else : pass doesn't do anything. 
# if statement is enough - it will only do something if the 'if' statement is TRUE
# delete self text
				
# if over_18 tag true take out of loop
	jokeOne=random.choice(jokeList)
	
	

####################### dict for passing to html #######################
    
#     Anything that you want to have displayed should go in the dict
	vars = {'headline':newsItemOne.headline,
    		'newsImage':newsItemOne.newsImage,
    		'newsSource':newsItemOne.newsSource,
            'noun':nouns[0],
			'joketitle':jokeOne.text,
            'joketext':jokeOne.selfText,
			'jokeurl':jokeOne.url,
			'jokeSource':jokeOne.jokeSource}
			
	return vars


