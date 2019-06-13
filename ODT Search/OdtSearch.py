from odfdo import Document
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

pesquisa = input('Escolha o texto:')
filename = "test.odt"

doc = Document(filename)
text = doc.get_formatted_text()


result = fuzz.partial_ratio(str(pesquisa),str(text))
print('Porcentagem de semelhança: '+ str(result))
