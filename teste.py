import wikipedia
from wikipedia import summary
wikipedia.set_lang("pt")
print(summary("Wikipedia"))
