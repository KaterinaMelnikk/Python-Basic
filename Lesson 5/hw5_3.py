def create_hashtag(text):
    cleaned_text = text
    for char in text:
        if not char.isalnum():
            cleaned_text = cleaned_text.replace(char, ' ')

    words = cleaned_text.split()

    for i in range(len(words)):
        words[i] = words[i].title()

    hashtag = '#' + ''.join(words)

    if len(hashtag) > 140:
        hashtag = hashtag[:140]

    return hashtag

print(create_hashtag("I love Python"))
print(create_hashtag("i like python community!"))
print(create_hashtag("Should, I. subscribe? Yes!"))
