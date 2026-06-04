import importlib
import logging

from sqlmodel import Session, select

from app.database.engine import engine
from app.models.crawler_model import Crawler
from app.models.fonte_model import FonteModel

logger = logging.getLogger(__name__)


def crawler_run():
    statement = (
        select(Crawler)
        .join(FonteModel)
        .where(Crawler.ativo == True)
        .where(FonteModel.ativo == True)
    )

    with Session(engine) as session:
        crawlers = session.exec(statement).all()

    if not crawlers:
        logger.info("Nenhum crawler ativo encontrado.")
        return

    for crawler in crawlers:
        try:
            module = importlib.import_module(crawler.caminho_modulo)
            cls = getattr(module, crawler.classe_nome)
            instance = cls(crawler_id=crawler.id, fonte_id=crawler.fonte_id)
            logger.info("Executando crawler %s (id=%s, fonte_id=%s)", crawler.nome, crawler.id, crawler.fonte_id)
            instance.run()
        except Exception as e:
            logger.exception("Erro ao executar crawler %s: %s", crawler.nome, e)


if __name__ == "__main__":
    crawler_run()
