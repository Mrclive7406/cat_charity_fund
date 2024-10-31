from fastapi import APIRouter

from app.api.endpoints import (charity_project_router,
                               donation_router, user_router)


CHARITY_PROJECT = '/charity_project'
DONATION = '/donation'
TAG_DONATION = ['Donation']
TAG_PROJECT = ['Charity Project']

main_router = APIRouter()
main_router.include_router(charity_project_router,
                           prefix=CHARITY_PROJECT,
                           tags=TAG_PROJECT)
main_router.include_router(donation_router,
                           prefix=DONATION,
                           tags=TAG_DONATION)
main_router.include_router(user_router)
