from lxml import html


class Parser:

    def __init__(self, html):
        self.html = html

    def get_sku(self):
        sku = None
        try:
            (sku,) = self.html.xpath("//div[@class='p-type-wrapper']/span[@class='p-type']/text()")
            sku = sku.strip()
        except ValueError:
            pass
        return sku

    def get_dimensions(self):
        dimensions = {}
        try:
            (dl,) = self.html.xpath("//li[@class='p-col-child p-chapter-to-toggle']/p[@class='p-heading-03 p-spec-title'][text()='Dimensions']")[0].getparent().xpath('./dl')
            dimensions_size = len(dl.xpath('./dt'))
            for i in range(1, dimensions_size + 1):
                try:
                    key = dl.xpath(f'./dt[position()={i}]')[0].text.strip()
                    value = dl.xpath(f'./dd[position()={i}]/div/span')[0].text.strip()
                    dimensions[key] = value
                except:
                    pass
            pass
        except Exception:
            pass
        return dimensions

    def parse(self):
        self.html = html.fromstring(self.html)
        sku = self.get_sku()
        dim = self.get_dimensions()
        print(f'SKU: {sku}')
        print(f'Dimensions: {len(dim)}')
