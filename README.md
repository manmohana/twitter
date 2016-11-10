**Common Followers and Keyword in Tweets**


Requirements
	- Python 2.7.10
	- pip 
	
How to Get Started

1. clone this repo (best done inside of a virtual environment)

	```mkdir venv```

	```cd venv```

	```pip install virtualenv```

	```virtualenv venv```

	```source venv/bin/activate```

	```git clone https://github.com/manmohana/twitter.git```

	```cd twitter```

2. install all the necessary packages 

	```pip install -r requirements.txt```

3. Update key.cfg with Consumer Key, Consumer Secret, Access Token, Access Token Secret from https://apps.twitter.com/

4. run the app

	```python tweetfollowers.py common-followers MakeThunder MakeThunder```

	```python tweetfollowers.py tweet-keyword MakeThunder CEO```
 