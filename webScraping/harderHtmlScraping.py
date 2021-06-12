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

soup = BeautifulSoup(HTML_SNIPPET, "html.parser")


def find_name():
    locator = "article.product_pod h3 a"
    item_link = soup.select_one(locator)
    item_name = item_link.attrs["title"]
    print(item_name)


def find_link():
    locator = "article.product_pod h3 a"
    item_link = soup.select_one(locator)
    item_link = item_link.attrs["href"]
    print(item_link)


def find_price_and_convert_to_float():
    locator = "article.product_pod p.price_color"
    price_text = soup.select_one(locator).text
    price_value = float(re.search(r"[\d]+\.[\d]+", price_text).group())
    print(price_value)


find_price_and_convert_to_float()


def find_rating():
    locator = "article.product_pod p.star-rating"
    rating_class_attr = soup.select_one(locator).attrs["class"]
    rating_value = [rating for rating in rating_class_attr if rating != "star-rating"]
    print(rating_value[0])


find_rating()