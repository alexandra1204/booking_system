from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models import Booking, Event
from datetime import datetime


def create_booking(db: Session, event_id: int, user_id: str):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        return None, "Event not found"

    booked_count = db.query(Booking).filter(Booking.event_id == event_id).count()
    if booked_count >= event.total_seats:
        return None, "No seats available"

    booking = Booking(event_id=event_id, user_id=user_id)
    db.add(booking)
    try:
        db.commit()
        db.refresh(booking)
        return booking, None
    except IntegrityError:
        db.rollback()
        return None, "User already booked this event"
