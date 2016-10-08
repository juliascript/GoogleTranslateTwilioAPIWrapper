# GoogleTranslateTwilioAPIWrapper 

`translate` takes two arguments. The first argument is an array of strings that are to be translated into the language specified in the second argument. The default value for the language is Spanish. An array of translated strings is returned. 

`sms` takes one argument, the string to send to the number which is specified in the function body. This should probably be edited in the future so we're not only texting one person. :P 

And now a code sample: 

```

# Define an array of strings that you want translated 
array_of_messages = ["Reality is a construction of the senses", "Success is learning how to go from failure to failure without despair"]

# Call the translate function, passing in the array as the first argument. This text will be translated to Spanish. The array of translated text is captured in the translatedTextArray variable. 
translatedTextArray = translate(array_of_messages)

# Alternatively, you can specify another language by passing it in as the second argument. This text will be translated into French. 
# translatedTextArray = translate(array_of_messages, 'fr')

# For every element in the translatedTextArray, send it via sms. 
for translatedText in translatedTextArray:
	sms(translatedText)

```
