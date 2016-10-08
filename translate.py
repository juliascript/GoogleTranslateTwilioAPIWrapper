import httplib2, urllib, json 
from twilio.rest import TwilioRestClient 

# 1. Create Python wrapper function for translate 
# 2. Extend wrapper function with target language 
# 3. Extend wrapper func to translate multiple strings 
# 4. Add Twilio SMS functionality to text the translation 

# API Keyzz
# -------------------------------------------------------
# Google ----
GOOGLE_API_KEY = "-----REPLACE-------"
# Twilio ----
ACCOUNT_SID = "------REPLACE-------"
AUTH_TOKEN = "-------REPLACE-------"

# Translates all text elements of the array given as the first argument into the language given as the second argument
def translate(input_text_array = [], language="es") :
	# URL construction
	url = "https://www.googleapis.com/language/translate/v2?key=" + GOOGLE_API_KEY + "&target=" + language
	# Opens connection for web API calls
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
			# Iterate for length of input_text_array and access the translatedText key for each
			for i in range(0, len(input_text_array)):
				# Accesses the translatedText key within the body dictionary
				translatedText = body["data"]["translations"][i]["translatedText"]
				# Add translation to array, to be returned at the end of the loop
				array_of_translations.append(translatedText)
		except Exception as e:
			print "There was a problem loading translation from Google."

	return array_of_translations
			
# Takes a message as an argument and sends a message to Kenny 
def sms(message, toNumber) :
	# If toNumber is not a string, throw it into a string
	if !(isinstance(toNumber, basestring)):
		toNumber = "+" + toNumber

	# Instantiate TwillioRestClient with ID and token 
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
	try: 
		# Calls the create method on client
		client.messages.create(  to = toNumber,  from_ = "---REPLACE WITH YOUR TWILIO NUMBER---",  body=message)
		# Give message receipt to terminal
		print (message + " sent.")
	except Exception as e:
		print "There was a problem sending the message with Twilio. Please try again."
