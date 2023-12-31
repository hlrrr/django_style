from fastapi    import FastAPI
from fastapi.middleware.cors    import CORSMiddleware


app = FastAPI(
    swagger_ui_parameters={"defaultModelsExpandDepth": 0}       # shrink schema section
    )      

origins = [""]

# 리퀘스트는 정의한 미들웨어들을 역순으로 타고 들어옴.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
)


'''
for database
'''


'''
for starlette_admin
'''
from starlette_admin.contrib.sqla.admin import Admin
from starlette_admin.contrib.sqla.view  import ModelView

# admin = Admin(engine)
# # admin.add_view(ModelView(m.User))
# admin.mount_to(app)

@app.get(path="/")
async def root():
    pass

