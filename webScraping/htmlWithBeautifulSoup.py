from bs4 import BeautifulSoup

SIMPLE_HTML = """<html>
<head></head>
<body>
<h1>This is a title</h1>
<p>Some paragraph 0 text</p>
<p class="subtitle">Some paragraph 1 text</p>
<p>Some paragraph 2 text</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
<h1>This is another title</h1>
</body>
</html>
"""

simple_soup = BeautifulSoup(SIMPLE_HTML, "html.parser")

h1_tag = simple_soup.find("h1")  # finds 1 item findAll() finds all suitable elements
print(h1_tag)
print(h1_tag.text)
print(h1_tag.string)


def find_list_items():
    list_items = [item.string for item in simple_soup.findAll("li")]
    print(list_items)


find_list_items()


def find_subtitle():
    paragraph = simple_soup.find("p", {"class": "subtitle"})  # find element by specific attribute
    print(paragraph)


find_subtitle()


def find_other_paragraphs():
    paragraphs = simple_soup.findAll("p")
    other_paragraphs = [p for p in paragraphs if "subtitle" not in p.attrs.get("class", [])]  # get all p elements without class attribute = "subtitle"
    """
    p.attrs.get("class") returns None if no "class" attribute found and <"subtitle" not in p.attrs> throws an error when iterating over None 
    TypeError: argument of type 'NoneType' is not iterable
    to avoid this instead of None we return [] if no "class" attribute is found (p.attrs.get("class", [])) as a result - no error is thrown
    """
    #other_paragraphs = [p for p in paragraphs if "class" not in p.attrs] #  to filter by class attribute in general, not by its' "subclass" value
    print(other_paragraphs)


find_other_paragraphs()