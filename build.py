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