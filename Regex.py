import re
print(re.match("Science","Science is experimental!").group())
print(re.search("world","Hello world!").group())
print(re.findall("world","hello world"))            #group() is not possible
print(re.sub("Dog","Cat","Dog is cute!"))           #group() is not possible
