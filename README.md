# GoogleTranslateTwilioAPIWrapper 

**Remember to update the code with your own API keys, IDs, and tokens from Google Cloud Platform and Twilio, as well as your Twilio phone number.**


`translate` takes two arguments. The first argument is an array of strings that are to be translated into the language specified in the second argument. The default value for the language is Spanish. An array of translated strings is returned. 

`sms` takes two arguments. The first argument is the string to send. The second argument is the number to which the message will be sent. 

And now a code sample: 

```
# Define an array of strings that you want translated 
array_of_messages = ["Reality is a construction by the senses", "Success is learning how to go from failure to failure without despair"]

# Call the translate function, passing in the array as the first argument. This text will be translated to Spanish. The array of translated text is captured in the translatedTextArray variable. 
translatedTextArray = translate(array_of_messages)

# Alternatively, you can specify another language by passing it in as the second argument. This text will be translated into French. 
# translatedTextArray = translate(array_of_messages, 'fr')

# For every element in the translatedTextArray, send it via sms. 
for translatedText in translatedTextArray:
	sms(translatedText, 19998887777)
	# Or, if you want to pass the string value of the number..
	# sms(translatedText, "+19998887777")
```
