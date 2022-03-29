import arxivpy
from fpdf import FPDF
from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape



# articles = arxivpy.query(search_query='',
#                          start_index=0, max_index=20, results_per_iteration=100,
#                          wait_time=5.0, sort_by='lastUpdatedDate')    

query='all:Quantum+AND+all:Cryptography+AND+all:key+AND+distribution+AND+cat:quant-ph'
print(query)
articles = arxivpy.query(search_query=query, start_index=0,max_index=10,results_per_iteration=100,wait_time=5.0, sort_by='lastUpdatedDate')

# articles = arxivpy.query(search_query=['quant-ph'],
#                          start_index=0, max_index=10, results_per_iteration=100,
#                          wait_time=5.0, sort_by='lastUpdatedDate') # grab 200 articles


doc = Document()
doc.preamble.append(Command('title', 'Daily Quantum Cryptography Snacks'))
doc.preamble.append(Command('author', 'Everyone'))
doc.preamble.append(Command('date', NoEscape(r'\today')))
doc.append(NoEscape(r'\maketitle'))

# fill_document(doc)
# doc.generate_pdf('basic_maketitle', clean_tex=False)
# Add stuff to the document
for article in articles:
	try:
		with doc.create(Subsection(NoEscape(article['title']))):
				doc.append(NoEscape(r'\paragraph{}'))
				doc.append(article['authors'])
				doc.append(NoEscape(article['abstract']))
	except Exception as e:
		print(e)
		pass


doc.generate_pdf('snacks', clean_tex=False)
tex = doc.dumps()  # The document as string in LaTeX syntax
