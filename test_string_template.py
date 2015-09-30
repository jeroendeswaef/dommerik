import stringtemplate
 
hello = stringtemplate.ST("Hello, <name>")
hello["name"] = "World"
print(str(hello.render()))