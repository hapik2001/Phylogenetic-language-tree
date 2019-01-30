import json
import wikipediaapi

def parse_page(w):
#докстринггде?#непопепу!!!
    return len(w.text)

articles = open('articles.txt', encoding='utf-8').read().splitlines()
#некрасиво #неэкономно
langs = open('langs.txt', encoding='utf-8').read().splitlines()
#ещехуже
res = {lang:([-100] * len(articles)) for lang in langs}
#спорно
wiki = wikipediaapi.Wikipedia('en')
for ind, article in enumerate(articles):
    page = wiki.page(article)
    langlinks = page.langlinks
    langlinks['en'] = page
    article_info = []
    for l in langs:
        if l in langlinks:
            res[l][ind] = parse_page(langlinks[l])
    print(ind + 1, '/', len(articles))


out = open("wikiData.txt", "w", encoding='utf-8')
for key, value in res.items():
    out.write(key + ' ' + ' '.join([str(i) for i in value]) + '\n')
out.close()
#ивообщеестьконструкцияwith
