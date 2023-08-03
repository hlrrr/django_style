import uvicorn
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors    import CORSMiddleware
from dataclasses    import asdict
from fastapi    import Depends, FastAPI

from app.routers    import contact, index, user
from app.database.database   import db
from app.common.configs     import config

API_KEY_HEADER = APIKeyHeader(name="Authorization", 
                              auto_error=False)

def init_app():
    ''' application initailizer '''
    app = FastAPI(swagger_ui_parameters={"defaultModelsExpandDepth": 0})       # shrink schema section
    cfg = config()
    cfg_dict = asdict(cfg)
    db.init_database(app, **cfg_dict)

    # 리퀘스트는 정의한 미들웨어들을 역순으로 타고 들어옴.
    app.add_middleware(CORSMiddleware,
                       allow_origins=cfg.ALLOW_SITE,
                       allow_credentials=True,
                       allow_methods=["*"],
                       allow_headers=["*"])

    # routnig
    app.include_router(index.router)
    if cfg.DEBUG:
        app.include_router(router=contact.router,
                           tags=['Contact'],
                           prefix='/api',
                           dependencies=[Depends(APIKeyHeader)])
        app.include_router(router=user.router,
                           tags=['User'],
                           prefix='/api',
                           dependencies=[Depends(APIKeyHeader)])
    else:
        app.include_router(router=contact.router,
                            tags=['infomation'],
                            prefix='/api')
        app.include_router(router=user.router,
                           tags=['User'],
                           prefix='/api')

    return app

app = init_app()

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=config().DEBUG)
