from odfdo import Document
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

input_to_compare = input('Escolha o texto:')
file_name = "test.odt"

open_document = Document(filename)
text_formatted = open_document.get_formatted_text()


result = fuzz.partial_ratio(str(input_to_compare),str(text_formatted))
print('Porcentagem de semelhança: '+ str(result))
