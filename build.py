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
