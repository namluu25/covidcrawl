import scrapy
import subprocess
import json
import os


def installPackage(package):
    try:
        return __import__(str(package))
    except ImportError:
        subprocess.call(["pip3", "install", "scrapy"])


# Make a dicrectory to contain JSON file and HTML file
class makeDir():
    def JSON_dir(self):
        JSON_path = os.path.join(os.getcwd(), "JSON Image file/")

        if not os.path.exists(JSON_path):
            os.mkdir(JSON_path)

        return JSON_path

    def HTML_dir(self):
        HTML_path = os.path.join(os.getcwd(), "HTML File/")

        if not os.path.exists(HTML_path):
            os.mkdir(HTML_path)

        return HTML_path


dir = makeDir()
JSON_directory = dir.JSON_dir()
HTML_directory = dir.HTML_dir()


# For dantri.com
class covid_dantri(scrapy.Spider):
    name = "covid_dantri"

    def start_requests(self):
        urls = [
            "https://dantri.com.vn/suc-khoe/dai-dich-covid-19.htm",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1].split(".")[0].split(".")[0]
        filename = f'{HTML_directory}dantri-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

        # Writing source and caption of image into JSON file
        dantri_covid = {'img': []}

        source = []
        for i in range(1, len(response.css("img::attr(src)").extract())):
            source.append(response.css("img::attr(src)").extract()[i])

        caption = []
        for i in range(1, len(response.css("img::attr(alt)").extract())):
            caption.append(response.css("img::attr(alt)").extract()[i])

        news_source = []
        for i in range(len(response.css("a.news-item__avatar::attr(href)").extract())):
            news_source.append("dantri.com.vn" + str(response.css("a.news-item__avatar::attr(href)").extract()[i]))

        for i in range(0, len(source)):
            dantri_covid['img'].append({
                "source": source[i],
                "caption": caption[i],
                "news_source": news_source[i]
            })

        with open(f"{JSON_directory}/image_dantri.json", "w") as image_file:
            json.dump(dantri_covid, image_file)


# For tuoitre.net
class covid_tuoitre(scrapy.Spider):
    name = "covid_tuoitre"

    def start_requests(self):
        urls = [
            "https://tuoitre.vn/phong-chong-covid-19-e583.htm",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1].split(".")[0].split(".")[0]
        filename = f'{HTML_directory}tuoitre-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

        tuoitre_covid = {'img': []}

        source = []
        for i in range(5, len(response.css('img::attr(src)').extract()) - 5):
            source.append(response.css('img::attr(src)').extract()[i])

        caption = []
        for i in range(4, len(response.css('img::attr(alt)').extract()) - 5):
            caption.append(response.css('img::attr(alt)').extract()[i])

        news_source = []
        for i in range(0, len(response.css("h3.title-news a:nth-child(1)::attr(href)").extract())):
            news_source.append(
                "tuoitre.vn" + str(response.css("h3.title-news a:nth-child(1)::attr(href)").extract()[i]))

        for i in range(len(news_source)):
            tuoitre_covid['img'].append({
                "source": source[i],
                "caption": caption[i],
                "news_source": news_source[i]
            })

        """Why there is 2 loop ? Because from the 4th picture, captions and sources do not match
        source needs to be more 1 position than caption
        caption[i] => source[i+1]
        """

        # for i in range(0, 3):
        #     tuoitre_covid['img'].append({
        #         "source": source[i],
        #         "caption": caption[i],
        #     })
        #
        # for i in range(4, len(caption) - 5):
        #     tuoitre_covid['img'].append({
        #         "source": source[i + 1],
        #         "caption": caption[i],
        #     })

        with open(f"{JSON_directory}image_tuoitre.json", "w") as image_file:
            json.dump(tuoitre_covid, image_file)


####### Note: Fix vnexpressssss
# For vnexpress.net
class covid_vnexpress(scrapy.Spider):
    name = "covid_vnexpress"

    def start_requests(self):
        urls = [
            "https://vnexpress.net/covid-19/tin-tuc",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'{HTML_directory}vnexpress-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

        # Writing source and caption of image into JSON file
        vnexpress_covid = {'img': []}

        caption = []
        for i in range(0, len(response.css("p.description a:nth-child(1)::attr(title)").extract())):
            caption.append(response.css("p.description a:nth-child(1)::attr(title)").extract()[i])

        news_source = []
        for i in range(0, len(response.css("p.description a:nth-child(1)::attr(href)").extract())):
            if "#box_comment_vne" in response.css("p.description a:nth-child(1)::attr(href)").extract()[i]:
                pass
            else:
                news_source.append(response.css("p.description a:nth-child(1)::attr(href)").extract()[i])

        # Complicated stuff
        src_fake = []
        for i in range(1, len(response.css("img::attr(src)").extract())):
            src_fake.append(response.css("img::attr(src)").extract()[i])

        alt_fake = []
        for i in range(1, len(response.css("img::attr(alt)").extract())):
            alt_fake.append(response.css("img::attr(alt)").extract()[i])

        src_alt_fake = {}
        for i in range(len(alt_fake)):
            src_alt_fake[alt_fake[i]] = src_fake[i]

        source = []
        for i in range(len(news_source)):
            source.append("/")

        for i in range(len(caption)):
            for alt, src in src_alt_fake.items():
                if alt == caption[i]:
                    source[i] = src

        for i in range(0, len(source)):
            vnexpress_covid['img'].append({
                "source": source[i],
                "caption": caption[i],
                "news_source": news_source[i]
            })

        with open(f"{JSON_directory}image_vnexpress.json", "w") as image_file:
            json.dump(vnexpress_covid, image_file)


def main():
    # Install Scrapy if not have
    installPackage(scrapy)

    # Crawl image and caption about Covid19 News
    # From dantri.com
    subprocess.call(["scrapy", "crawl", "covid_dantri"])

    # From tuoitre.net
    subprocess.call(["scrapy", "crawl", "covid_tuoitre"])

    # From vnexpress.net
    subprocess.call(["scrapy", "crawl", "covid_vnexpress"])


if __name__ == "__main__":
    main()
