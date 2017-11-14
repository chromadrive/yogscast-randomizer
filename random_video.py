import argparse	
import json
# from random import randint, choice
try:
	# For Python 3.0 and later
	from urllib.request import Request, urlopen
except ImportError:
	# Fall back to Python 2's urllib2
	from urllib2 import Request, urlopen


def parse_json(url):
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	response = urlopen(req)
	data = response.read().decode("utf-8")
	return json.loads(data)


def get_random_video_id(channel):
	url = "https://api.yogsdb.com/api/videos?channel="+ channel +"&inRandomOrder=1"
	result = parse_json(url)
	if not result['data']:
		return "Could not find channel with ID " + channel

	selected_video = result['data'][0]

	return selected_video['title'] + ": https://www.youtube.com/watch?v=" + selected_video['youtube_id']


parser = argparse.ArgumentParser(description='Selects a random video from a Yogscast channel')
parser.add_argument('channel_id', metavar='channel-id', type=str,
				   help='A Yogscast channel ID')
args = parser.parse_args()


print(get_random_video_id(args.channel_id))