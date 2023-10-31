#!/usr/bin/env python3

import uvicorn


host="0.0.0.0"
port=8080
app_name="app.main:app"


if __name__ == '__main__':
    uvicorn.run(app_name, host=host, port=port, reload=True)
