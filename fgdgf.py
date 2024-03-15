def begin_tag(name):
	return "<"+name+">"+"\n"

def end_tag(name):
	return "</"+name+">"+"\n"

f = open("simple_page.html", "w")
f.write(begin_tag("html"))
f.write(begin_tag("title"))
f.write("Test Title\n")
f.write(end_tag("title"))
f.write("Test Content for Page\n")
f.write(end_tag("html"))
f.close()