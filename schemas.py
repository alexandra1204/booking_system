from pydantic import BaseModel

class BookingCreate(BaseModel):
    event_id: int
    user_id: str

class BookingResponse(BaseModel):
    id: int
    event_id: int
    user_id: str
    created_at: str

    class Config:
        orm_mode = True

class EventCreate(BaseModel):
    name: str
    total_seats: int

class EventResponse(BaseModel):
    id: int
    name: str
    total_seats: int

    class Config:
        orm_mode = True
