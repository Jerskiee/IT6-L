from fastapi import FastAPI
from employees.controller import router as employees_router
from work_schedules.controller import router as schedules_router
from admins.controller import router as admins_router
from log_history.controller import router as logs_router
from attendance_queue.controller import router as attendance_router  # <--- NEW

def register_routes(app: FastAPI):
    app.include_router(employees_router)
    app.include_router(schedules_router)
    app.include_router(admins_router)
    app.include_router(logs_router)
    app.include_router(attendance_router)  # <--- NEW