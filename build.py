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


