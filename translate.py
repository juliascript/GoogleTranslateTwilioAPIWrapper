import httplib2, urllib, json 
from twilio.rest import TwilioRestClient 

# 1. Create Python wrapper function for translate 
# 2. Extend wrapper function with target language 
# 3. Extend wrapper func to translate multiple strings 
# 4. Add Twilio SMS functionality to text the translation 

# API Keyzz
# -------------------------------------------------------
# Google ----
GOOGLE_API_KEY = "------------"
# Twilio ----
ACCOUNT_SID = "-------------"
AUTH_TOKEN = "--------------"

# Translates all text elements of the array given as the first argument into the language given as the second argument
def translate(input_text_array = [], language="es") :
	# URL construction
	url = "https://www.googleapis.com/language/translate/v2?key=" + GOOGLE_API_KEY + "&target=" + language
	# Keeps connection live for translation of entire array
	http = httplib2.Http()
	array_of_translations = []
	queryString = ""

	for input_text in input_text_array:
		# Handles special characters within url
		input_text = urllib.quote(input_text, safe ='')
		queryString = queryString + "&q=" + input_text
		
	# URL construction cont. to add text to be translated
	url = url + queryString
	# HTTP GET request, returns metadata in response, translation in body
	response, body = http.request(url, "GET")

	# Check that body is string that contains JSON 
	if isinstance(body, basestring):
		try: 
			# Translate string into Python dictionary, stored in variable body
			body = json.loads(body)
			for i in range(0, len(input_text_array)):
				# Accesses the translatedText key within the body dictionary
				translatedText = body["data"]["translations"][i]["translatedText"]
				# Add translation to array, to be returned at the end of the loop
				array_of_translations.append(translatedText)
		except Exception as e:
			print "There was a problem loading translation from Google."

	return array_of_translations
			
# Takes a message as an argument and sends a message to Kenny 
def sms(message) :
	# Instantiate TwillioRestClient with ID and token 
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
	try: 
		# Calls the create method on client
		client.messages.create(  to="----------",  from_="----------",  body=message)
		# Give message receipt to terminal
		print (message + " sent.")
	except Exception as e:
		print "There was a problem sending the message with Twilio. Please try again."



array_of_messages = ["Reality is a construction of the senses", "Success is learning how to go from failure to failure without despair"]
translatedTextArray = translate(array_of_messages)
for translatedText in translatedTextArray:
	sms(translatedText)