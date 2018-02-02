from bs4 import BeautifulSoup
from bs4.element import Comment
import re
import urllib.request
import nltk
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

# url_ = 'http://www.nytimes.com/2009/12/21/us/21storm.html'
# url_ = 'http://medgadgets.ru/shop/katalog/gadgety-dlia-doma.html'


def tag_visible(element):
    html_tags = ['style', 'script', 'head', 'title', 'meta', '[document]']
    if element.parent.name in html_tags:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.lower().strip() for t in visible_texts)


def improve_tokenized_text(_tokens):
    if _tokens is not None:
        sr_en = stopwords.words('english')
        sr_ru = stopwords.words('russian')
        clean_tokens = []
        for token in _tokens:
            # Cleaning non-alphabetic characters
            token_cleaned = re.sub('[^A-Za-zа-яА-Я0-9]', '', token)

            if len(token_cleaned) <= 2:
                pass
            elif token_cleaned in sr_en:
                pass
            elif token_cleaned in sr_ru:
                pass
            else:
                clean_tokens.append(token_cleaned)

        return clean_tokens
    else:
        return None


def tokenize(_text):
    word_hash_map = {}
    sent_text = nltk.sent_tokenize(_text)
    for sentence in sent_text:
        tokenized_text = nltk.word_tokenize(sentence)
        tokenized_text = improve_tokenized_text(tokenized_text)
        tagged = nltk.pos_tag(tokenized_text)
        for word, tag in tagged:
            if tag.startswith('NN') or tag.startswith('VB') or tag.startswith('JJ'):
                if word in word_hash_map:
                    word_hash_map[word] = word_hash_map[word] + 1
                else:
                    word_hash_map[word] = 1
    return word_hash_map


def get_url_word_analytics(_url):
    print(_url)
    html = urllib.request.urlopen(_url).read()
    html_text = text_from_html(html)
    word_dict = tokenize(html_text)
    return word_dict
