"""main
"""
import uvicorn

from app import config, server

if __name__ == "__main__":
    uvicorn.run(app=server.APP, host=config.SETTINGS.app_host,
                port=config.SETTINGS.app_port, log_level=config.SETTINGS.LOG_LEVEL,)
