import re

from bs4 import BeautifulSoup

HTML_SNIPPET = """<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>
        In stock
</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>            
            </div>
    </article>
</li>
</body></html>
"""


class ParsedItemLocators:
    """
    Locators for an item in the HTML page.

    This allows us to easily see what our code will be looking at as well as change it quickly if we notice it is now
    different.
    """
    NAME_LOCATOR = "article.product_pod h3 a"
    LINK_LOCATOR = "article.product_pod h3 a"
    PRICE_LOCATOR = "article.product_pod p.price_color"
    RATING_LOCATOR = "article.product_pod p.star-rating"


class ParsedItem:
    """
    A class to take in an HTML page (or part of it) and find properties of an item in it.
    """

    def __init__(self, page):
        self.soup = BeautifulSoup(page, "html.parser")

    @property
    def name(self) -> str:
        locator = ParsedItemLocators.NAME_LOCATOR
        item_link = self.soup.select_one(locator)
        return item_link.attrs["title"]

    @property
    def link(self) -> str:
        locator = ParsedItemLocators.LINK_LOCATOR
        item_link = self.soup.select_one(locator)
        return item_link.attrs["href"]

    @property
    def price_converted_to_float(self) -> float:
        locator = ParsedItemLocators.PRICE_LOCATOR
        price_text = self.soup.select_one(locator).text
        return float(re.search(r"[\d]+\.[\d]+", price_text).group())

    @property
    def rating(self) -> str:
        locator = ParsedItemLocators.RATING_LOCATOR
        classes = self.soup.select_one(locator).attrs["class"]  # ['star-rating', 'Three']
        rating_value = [r for r in classes if r != "star-rating"]
        return rating_value[0]


item = ParsedItem(HTML_SNIPPET)
print(item.name)
print(item.link)
print(item.price_converted_to_float)
print(item.rating)
