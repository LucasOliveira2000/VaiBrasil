import logging

from sqlmodel import Session, select

from app.database.engine import engine
from app.models.fonte_model import FonteModel
from app.models.crawler_model import Crawler

logger = logging.getLogger(__name__)

SEEDS = [
    {
        "fonte": {"nome": "Câmara dos Deputados", "ativo": True},
        "crawlers": [
            {
                "nome": "Câmara Crawler",
                "url": "https://www.camara.leg.br/deputados/quem-sao/resultado",
                "caminho_modulo": "app.crawlers.camara.camara_crawler",
                "classe_nome": "CamaraCrawler",
                "ativo": True,
            }
        ],
    },
    {
        "fonte": {"nome": "Senado Federal", "ativo": True},
        "crawlers": [],
    },
]


def run():
    with Session(engine) as session:
        for seed in SEEDS:
            fonte = session.exec(
                select(FonteModel).where(FonteModel.nome == seed["fonte"]["nome"])
            ).first()

            if not fonte:
                fonte = FonteModel(**seed["fonte"])
                session.add(fonte)
                session.flush()
                logger.info("Fonte '%s' criada.", seed["fonte"]["nome"])
            else:
                logger.info("Fonte '%s' já existe, verificando crawlers.", seed["fonte"]["nome"])

            for crawler_data in seed["crawlers"]:
                existente = session.exec(
                    select(Crawler).where(
                        Crawler.fonte_id == fonte.id,
                        Crawler.nome == crawler_data["nome"],
                    )
                ).first()

                if existente:
                    for key, value in crawler_data.items():
                        setattr(existente, key, value)
                    session.add(existente)
                    logger.info("Crawler '%s' atualizado.", crawler_data["nome"])
                else:
                    crawler = Crawler(fonte_id=fonte.id, **crawler_data)
                    session.add(crawler)
                    logger.info("Crawler '%s' criado.", crawler_data["nome"])

        session.commit()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    run()
