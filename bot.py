
import os
from decouple import config
import twitter

# Initialize client
api_client = twitter.Api(
	consumer_key=config('CONSUMER_KEY'),
	consumer_secret=config('CONSUMER_SECRET'),
	access_token_key=config('ACCESS_TOKEN_KEY'),
	access_token_secret=config('ACCESS_TOKEN_SECRET')
)



# Checking credentials out
# print(api_client.VerifyCredentials())

# posting a twit
# result = api_client.GetFollowers()
# first_ten = result[:10]

# print(result[0])
# for f in first_ten:
# 	print(f)

image_path = os.path.abspath('image.jpg')

result = api_client.PostUpdate(
	"Stop trolling me"
)

print(result)

