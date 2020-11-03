import wikipedia
wikipedia.set_lang("tr")
page=wikipedia.page("Su Kefiri")
print(page.url)
print(page.title)
print(page.content[0:200])
page2=wikipedia.summary("Facebook", sentences=1)
print(page2)