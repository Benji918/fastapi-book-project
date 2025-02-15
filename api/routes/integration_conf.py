from fastapi import APIRouter
from fastapi.responses import Response
from starlette.responses import JSONResponse

from core.config import settings

router = APIRouter()

integration_json = {
    {
    "data": {
        "date": {
          "created_at": "2025-02-15",
          "updated_at": "2025-02-15"
        },
        "descriptions": {
          "app_name": "TelexTest",
          "app_description": "For ci/cd pipline",
          "app_logo": "https://telex.im/dashboard/applications/generate-json",
          "app_url": "http://40.83.174.214/",
          "background_color": "#fff"
        },
        "is_active": 'true',
        "integration_type": "modifier",
        "key_features": [
          "realtime updates and develpment",
            "development"
        ],
        "author": "Benjamin",
        "settings": [
          {
            "label": "slack-channel",
            "type": "text",
            "required": True,
            "default": "defaultchannel"
          },
          {
            "label": "time interval",
            "type": "dropdown",
            "required": 'true',
            "default": "immediate",
            "options": [
              "immediate",
              "Every 5-min",
              "Every 10-min",
              "Every 1-hour"
            ]
          },
          {
            "label": "ci-pipline",
            "type": "dropdown",
            "required": True,
            "default": "ci-pipline",
            "options": [
              "ci-pipline",
              "cd-pipline",
              "deployment"
            ]
          },
          {
            "label": "message",
            "type": "text",
            "required": True,
            "default": "Basic"
          },
          {
            "label": "include-log",
            "type": "checkbox",
            "required": True,
            "default": "true"
          }
        ],
        "target_url": settings.SLACK_WEBHOOK_URL,
        "tick_url": settings.TICK_URL
        }
    }
}

@router.get('/integration-config')
async def get_integration_config():
    return JSONResponse(content=integration_json)