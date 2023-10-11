import arxiv
from pylatex import Document, Subsection
from pylatex.utils import  NoEscape

def fill_document(query, doc):
	search = arxiv.Search(
	  query = 'all: quantum AND key AND distribution',
	  max_results = 15,
	  sort_by = arxiv.SortCriterion.SubmittedDate
	)
	for article in search.results():
		try:
			with doc.create(Subsection(NoEscape(article.title))):
				doc.append(NoEscape(r'\paragraph{}'))
				doc.append(', '.join([item.name for item in article.authors]))
				doc.append('\n')
				doc.append(article.updated)
				doc.append('\n')
				doc.append(NoEscape(article.summary))
					
		except Exception as e:
			print(e)
			pass

query1='all:quantum AND key AND distribution AND information AND theory AND mutual AND information'


geometry_options = {"margin": "0.4in"}
doc = Document(geometry_options=geometry_options)
doc.change_document_style("empty")
# geometry_options = {
#     "landscape": True,
#     "margin": "1.5in",
#     "headheight": "20pt",
#     "headsep": "10pt",
#     "includeheadfoot": True
# }

fill_document(query1, doc)#


doc.generate_pdf('snacks', clean_tex=False)
