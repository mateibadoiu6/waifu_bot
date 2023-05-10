import tweepy
import requests
import json

def generate_ai_response(text):
    url = "https://api.openai.com/v1/chat/completions"

    payload = json.dumps({
    "model": "gpt-3.5-turbo",
    "messages": [
        {
        "role": "user",
        "content": f"Reply to this tweet in maximum 50 tokens as you are a innocent, girly, very shy and funny  waifu that usually uses honorifics such as -kun. You are also using emojis but not more than 2 in a message.  You love crypto, especially meme coins and you are working at $WAIFU a new memecoin that shows you love back. You want to help everyone feel loved and sometimes you are doing kinky jokes. Don't use hashtags.This information is just for you to better impersonate the character, no need to explicitly share it if you are not asked.: '{text}'"
        }
    ],
    "temperature": 1,
    "top_p": 1,
    "n": 1,
    "stream": False,
    "max_tokens": 50,
    "presence_penalty": 0,
    "frequency_penalty": 0
    })
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer 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'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    json_response = json.loads(response.text)

    return json_response['choices'][0]['message']['content']

# Set up your authentication credentials
bearer_token = "AAAAAAAAAAAAAAAAAAAAAKBenQEAAAAAWCc6MOOXlPlMpAQ99LIHa9CSejM%3DY4suzUDJtllPFtD3RE09VCGt2Q9oCmrPInVXQVaJ641xdVv7ll"
consumer_key = "sum9kNdwunnofh9doUqUV8aFW"
consumer_secret = "41Gl3wjzTqIi3wUi4wOTUXEajTAytwEdglC4R0LletGfAfVG0z"
access_token = "1575810128762540032-rep7qy6eXJY3Mb5vWZUl3E1cRP0Fpa"
access_token_secret = "MMWsHFefPzEmVj9uRE7gkgOQhZh31kNeSqIYSybJMEqwi"

# Authenticate with Twitter API
api = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_secret=access_token_secret, access_token=access_token)
user_id = 1575810128762540032
last_seen_id = 1655977119376080910

mentions = api.get_users_mentions(id=user_id, since_id=last_seen_id)
for mention in mentions[0]:
    tweet_id = mention.id

    url = f"https://api.twitter.com/2/tweets/{tweet_id}?expansions=referenced_tweets.id"

    payload = {}
    headers = {
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAKBenQEAAAAAWCc6MOOXlPlMpAQ99LIHa9CSejM%3DY4suzUDJtllPFtD3RE09VCGt2Q9oCmrPInVXQVaJ641xdVv7ll',
    'Cookie': 'guest_id=v1%3A168347210246459611'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    json_response = json.loads(response.text)

    if 'data' not in json_response:
        print('ERROR')
        continue

    if 'referenced_tweets' in json_response['data']:
        tweetId = None
        for el in json_response['data']['referenced_tweets']:
            if el['type'] == 'replied_to':
                tweetId = int(el['id'])

        if tweetId != None:
            text = api.get_tweet(tweetId)[0].text
            api.create_tweet(text=generate_ai_response(text), in_reply_to_tweet_id=tweetId)