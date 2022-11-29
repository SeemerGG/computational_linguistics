from natasha import * 

segmenter = Segmenter()
emb = NewsEmbedding()
morph_targger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)

print("Текст для анализа:")
text = input()

doc = Doc(text)

doc.segment(segmenter)
doc.tag_morph(morph_targger)
doc.parse_syntax(syntax_parser)

for i in doc.sents:
	i.syntax.print()

"""Уважаемые дамы и  господа!  Мне  неизвестно, насколько каждый из вас из литературы или понаслышке знаком  с психоанализом. Однако само название моих лекций   "Элементарное  введение в  психоанализ" -  предполагает, что  вы ничего не знаете об этом и готовы получить от меня первые сведения."""

