from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth
from app.crawlers.base import BaseCrawler


class CamaraCrawler(BaseCrawler):
    def run(self):
        with Stealth().use_sync(sync_playwright()) as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto("https://www.camara.leg.br/deputados/quem-sao/resultado?search=&partido=&uf=&legislatura=&sexo=")

            deputados = page.locator("li.lista-resultados__item")
            total = deputados.count()

            for i in range(total):
                url_deputado = deputados.nth(i).locator("h3.lista-resultados__cabecalho a").get_attribute("href")
                nome_deputado = deputados.nth(i).locator("h3.lista-resultados__cabecalho a").inner_text()

                print(f"Nome: {nome_deputado}, URL: {url_deputado}")

            browser.close()