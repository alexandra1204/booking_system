from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from models import Event
from schemas import BookingCreate, BookingResponse, EventCreate, EventResponse
import crud

# Создаем таблицы (если их нет)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Booking System API")

@app.post("/api/bookings/reserve", response_model=BookingResponse)
def reserve_booking(booking: BookingCreate, db: Session = Depends(get_db)):
    result, error = crud.create_booking(db, booking.event_id, booking.user_id)
    if error:
        raise HTTPException(status_code=400, detail=error)
    return result

@app.post("/api/events", response_model=EventResponse)
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    db_event = Event(name=event.name, total_seats=event.total_seats)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event
