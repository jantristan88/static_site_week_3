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
	for page in pages:
		template = open("templates/base.html").read() #Opens and assigns base.html in the templates folder to variable template
		index_content = open(page['filename']).read() #Opens and assigns the values of the key filename to index_content
		finished_index_page = template.replace("{{content}}", index_content) #opens the the variable template, replaces the placeholder content with the variable index_content
		open(page['output'], "w+").write(finished_index_page) #the values assigned to variable finished_index_page is written to the values in the output key
															  #modifying or creating the html giles in the docs folder

	#created another function to address the title placeholders													
	def title():
		for page in pages:
			title_content = open(page['filename']).read()
			title_name = page['title']
			finished_title_content = title_content.replace("{{title}}", title_name)
			open(page['output'], "w+").write(finished_title_content)
	title()


if __name__ == '__main__':
	main() #invokes the main function


