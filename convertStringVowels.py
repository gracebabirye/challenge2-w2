def countVowels(stringInput):
    vowels = ['a', 'e', 'i', 'o', 'u']
    listFoundVowels = []
    setUniqueStringChars = set()
    setDuplicatedStringChars = set()

    try:
        # Remove spaces from the string
        stringInput = stringInput.replace(' ', '')

        for each in stringInput:
            # check if string character is a vowel 
            # and if yes, add it to list of found string vowels if not yet added
            if (each in vowels and each not in listFoundVowels):
                listFoundVowels.append(each)
            #if you encouter any character of our string,
            #check in the set "setUniqueStringChars" to see if we had encountered it before
            #if yes, then add it to our set "setDuplicatedStringChars" that is storing duplicates.
            #if we have not encountered it before, then add it to set "setUniqueStringChars"
            # so that next time we encounter it we shall be aware.
            if(each in setUniqueStringChars):
                setDuplicatedStringChars.add(each)
            else:
                setUniqueStringChars.add(each)

            # Convert the list into a tuple
            # then join it into one string by removing the '', spaces and commas
            stringvoweltuple = ''.join(tuple(listFoundVowels))
        return (stringvoweltuple, len(setDuplicatedStringChars))
    except TypeError:
        return("Invalid input")

print(countVowels('dahdah'))
print(countVowels('drink water'))