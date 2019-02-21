

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
	#def content_base_merge():
	#	for page in pages:
	#		template = open("templates/base.html").read() #Opens base.html in the templates folder and assigned to variable template
	#		index_content = open(page['filename']).read() #Assign the values of the key filename to index_content
	#		finished_index_page = template.replace("{{content}}", index_content) #opens the variable template, replaces the placeholder content with the variable index_content
	#		return(finished_index_page) #goes through the list of dictionary to combine the files 
	#content_base_merge()

	#directs the combined files to docs folder
	#def output_to_folder():
	#	for page in pages:
	#		final_step = content_base_merge
	#		open(page['output'], "w+").write(final_step) #uses the function content_base_merge to put combined files to output folder
	#output_to_folder()

	#def title():
	#	for page in pages:
	#		title_content = open(page['filename']).read()
	#		title_name = page['title']
	#		finished_title_content = title_content.replace("{{title}}", title_name)
	#		open(page['output'], "w+").write(finished_title_content)
	#title()
#for page in pages:

#	def apply_template():
#		template = open("templates/base.html").read() 
#		index_content = open(page['filename']).read()
#		finished_index_page = template.replace("{{content}}", index_content)
#		finished_index_page = finished_index_page.replace("{{title}}", title_name)
#		open(page['output'], "w+").write(finished_index_page)
#	apply_template()
#	def title():
#		title_content = open(page['filename']).read()
#		title_name = page['title']
#		finished_title_content = title_content.replace("{{title}}", title_name)
#		open(page['output'], "w+").write(finished_title_content)
#	title()

#	def main():
#		return()
    
#def print_page(template, page):
#    file_name = page['filename']
#    page_output = page['output']
#    page_title = page['title']
    
#    page_html = apply_template(template, page_title, file_name)
#    open(page_output, "w+").write(page_html)

#def apply_template(template, page_title, file_name):
#    index_content = open(file_name).read()
#    finished_index_page = template.replace("{{content}}", index_content)
#    finished_index_page = finished_index_page.replace("{{title}}", page_title)
#    return finished_index_page

    
#def main():
#    template = open("templates/base.html").read()
#    for page in pages:
#        print_page(template, page)


def apply_template(template,filename,title):
	index_content = open(filename).read()
	finished_index_page = template.replace("{{content}}", index_content)
	finished_index_page = finished_index_page.replace("{{title}}", title)
	return (finished_index_page)

def docs_output(template,page):
	filename = page['filename'] 
	output = page['output']
	title = page['title']
	final_step = apply_template(template,filename,title)
	open(output, "w+").write(final_step)

def main():
	template = open("templates/base.html").read()
	for page in pages:
		docs_output(template,page)


	

if __name__ == '__main__':
	main() #invokes the main function


