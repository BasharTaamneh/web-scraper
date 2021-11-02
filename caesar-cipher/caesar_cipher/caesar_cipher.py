import nltk
from nltk.corpus import words, names

nltk.download("words", quiet=True)
nltk.download("names", quiet=True)


def encrypt(txt, key):
    def cipher(i, lower=range(97, 123), upper=range(65, 91)):
        if i in lower or i in upper:
            sheft = 65 if i in upper else 97
            i = (i - sheft + key) % 26 + sheft
        return chr(i)

    return "".join([cipher(ord(s)) for s in txt])


def decrypt(txt, k):
    return encrypt(txt, -k)


# print(encrypt("It was the best of times, it was the worst of times.", 20))
# print(decrypt("Cn qum nby vymn iz ncgym, cn qum nby qilmn iz ncgym.", 20))


def crack(encrypted_text):
    words_list = words.words()
    names_list = names.words()

    filter = []
    for i in range(26):
        filter.append(decrypt(encrypted_text, i))
    # print(filter)
    for purified_sentence in filter:
        Sentence = purified_sentence.split(" ")
        words_count = 0

        for word in Sentence:
            if word.lower() in words_list or word.lower() in names_list:
                words_count += 1

        total_words = len(purified_sentence.split(" "))
        ratio = (words_count / total_words) * 100

        if ratio >= 75:
            print(ratio)
            return (" ").join(Sentence)

    return ""


print(crack("Gr uyq rfc zcqr md rgkcq, gr uyq rfc umpqr md rgkcq."))
