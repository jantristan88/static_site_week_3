def main():

	top_template = open('templates/top_template.html').read()
	bottom_template = open('templates/bottom_template.html').read()

	index = open('content/index.html').read()
	index_html = top_template + index + bottom_template
	open('docs/index.html', 'w+').write(index_html)

	FeatureProject= open('content/FeatureProject.html').read()
	FeatureProject_html = top_template + FeatureProject + bottom_template
	open('docs/FeatureProject.html', 'w+').write(FeaturedProject_html)

	Publication = open('content/Publication.html').read()
	Publication_html = top_template + Publication + bottom_template
	open('docs/Publication.html', 'w+').write(Publication_html)

if __name__ == "__main__":
	main()

pages = [
	{
		"filename":"content/index.html",
		"output":"docs/index.html",
		"title":"Home"
	},
	{
		"filename":"content/FeatureProject.html",
		"output":"docs/FeatureProject.html",
		"title":"Feature Project"
	},
	{
		"filename":"content/Publication.html",
		"output":"docs/Publication.html",
		"title":"Publication"
	},

	
]
	
for page in pages
	page_title = page['title']
	print(page_title)

template = open("base.html").read()
index_content = open("content/index.html").read()
finished_index_page = template.replace("{{content}}", index_content)
open("docs/index.html", "w+").write(finished_index_page)


def main():

	pages = [
		{
			"filename":"content/index.html",
			"output":"docs/index.html",
			"title":"Home"
		},
		{
			"filename":"content/FeatureProject.html",
			"output":"docs/FeatureProject.html",
			"title":"Feature Project"
		},
		{
			"filename":"content/Publication.html",
			"output":"docs/Publication.html",
			"title":"Publication"
		},

		] 
	
	for page in pages:
		template = open("templates/base.html").read()
		index_content = open(page['filename']).read()
		finished_index_page = template.replace("{{content}}", index_content)
		open(page['output'], "w+").write(finished_index_page)

if __name__ == '__main__':
	main()


#This is my original
def main():

	#Created a list of dictionaries of the files involved, the directory to which the output should go
	#and the title which will eventually be used for the placeholder
	pages = [
		{
			"filename":"content/index.html",
			"output":"docs/index.html",
			"title":"Home"
		},
		{
			"filename":"content/FeatureProject.html",
			"output":"docs/FeatureProject.html",
			"title":"Feature Project"
		},
		{
			"filename":"content/Publication.html",
			"output":"docs/Publication.html",
			"title":"Publication"
		},

		] 

	#Used a for loop for the following commands be applied to each dictionary set
	#created a function for merging contents with the base file
	def content_base_merge():
		for page in pages:
			template = open("templates/base.html").read() #Opens base.html in the templates folder and assigned to variable template
			index_content = open(page['filename']).read() #Assign the values of the key filename to index_content
			finished_index_page = template.replace("{{content}}", index_content) #opens the variable template, replaces the placeholder content with the variable index_content
			open(page['output'], "w+").write(finished_index_page) #the values assigned to variable finished_index_page is written to the values in the output key
	content_base_merge()									  #modifying or creating the html giles in the docs folder

														
	def title():
		for page in pages:
			title_content = open(page['filename']).read()
			title_name = page['title']
			finished_title_content = title_content.replace("{{title}}", title_name)
			open(page['output'], "w+").write(finished_title_content)
	title()


if __name__ == '__main__':
	main() #invokes the main function


