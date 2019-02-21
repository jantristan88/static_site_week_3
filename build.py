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
	def content_base_merge(combined):
		for page in pages:
			template = open("templates/base.html").read() #Opens base.html in the templates folder and assigned to variable template
			index_content = open(page['filename']).read() #Assign the values of the key filename to index_content
			finished_index_page = template.replace("{{content}}", index_content) #opens the variable template, replaces the placeholder content with the variable index_content
			return(finished_index_page) #goes through the list of dictionary to combine the files

	#directs the combined files to docs folder
	def output_to_folder():
		for page in pages:
			content = open(page['output']).read() #Opens the docs pages 
			final_copy = content_base_merge(content) #uses the function content_base_merge to put combined files to output folder
														
	def title():
		for page in pages:
			title_content = open(page['filename']).read()
			title_name = page['title']
			finished_title_content = title_content.replace("{{title}}", title_name)
			open(page['output'], "w+").write(finished_title_content)
	title()


if __name__ == '__main__':
	main() #invokes the main function


