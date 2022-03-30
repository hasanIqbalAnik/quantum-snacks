import arxivpy
from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape

def fill_document(query, doc):
	articles = arxivpy.query(search_query=query, start_index=0,max_index=12,results_per_iteration=100,wait_time=5.0, sort_by='lastUpdatedDate')
	for article in articles:
		try:
			with doc.create(Subsection(NoEscape(article['title']))):
					doc.append(NoEscape(r'\paragraph{}'))
					doc.append(article['authors'])
					doc.append('\n')
					doc.append(article['update_date'])
					doc.append('\n')
					doc.append(NoEscape(article['abstract']))
					
		except Exception as e:
			print(e)
			pass

query1='all:Quantum+AND+all:Cryptography+AND+abs:%22quantum+key+distribution%22'
query2 = 'abs:%22quantum+information+theory%22'
query3 = 'abs:%22entropic+uncertainty+relation%22'

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

fill_document(query1, doc)
fill_document(query2, doc)
fill_document(query3, doc)

doc.generate_pdf('snacks', clean_tex=False)
