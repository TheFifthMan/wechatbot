from app import create_app,db
app = create_app('default')

from app.index.models import *
@app.shell_context_processor
def shell_context_processor():
    return {"db":db}