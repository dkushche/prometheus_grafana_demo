import prometheus_client
from fastapi import FastAPI

counter = prometheus_client.Counter("slash_requests", "Amount of requests to '/'")

app = FastAPI()

@app.get("/")
async def index():
   counter.inc()

   return {"message": "Hello World"}

metrics_app = prometheus_client.make_asgi_app()
app.mount("/metrics", metrics_app)

# Counter
# Gauge
# Histogram
# Summary