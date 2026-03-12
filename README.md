# 🎬 Magic Movies

A full-stack movie ticket booking web app — BookMyShow style.

## Tech Stack
- **Backend**: Python Flask
- **Database**: SQLite (auto-created on first run)
- **Frontend**: HTML + CSS + Vanilla JavaScript

## Quick Start

```bash
pip install flask
cd magic-movies
python app.py
```

Open **http://localhost:5000**

## Features
- ✅ SQLite database with 12 real movies
- ✅ Live search (type to search movies instantly)
- ✅ Account creation + login with session
- ✅ Recommended & Recent movie sections
- ✅ Movie detail page with cast, reviews, ratings
- ✅ Booking flow: Date → Showtime → Seat map
- ✅ Payment page: UPI / Card / Wallet with PIN entry
- ✅ Countdown timer during payment (10 mins)
- ✅ Ticket page with QR code + barcode
- ✅ Download button (triggers print/save as PDF)
- ✅ Complete booking details (BookMyShow style)

## User Flow
```
/ → /signup → /login → /movies
→ /movie/<id> → /booking/<id> → /payment → /confirm-payment → /ticket
```

## Project Structure
```
magic-movies/
├── app.py              ← Flask routes + SQLite DB init
├── movies.db           ← Auto-created SQLite database
├── templates/
│   ├── signup.html
│   ├── login.html
│   ├── movies.html
│   ├── movie_details.html
│   ├── booking.html
│   ├── payment.html
│   └── ticket.html
├── static/
│   ├── css/style.css
│   └── js/script.js
└── README.md
```

watch the demo link here:
https://1drv.ms/v/c/1de26de4f90092cb/IQBH-CrTMqm4R78oBzwobzazAf-dc5sDbr1LV8OHYAqjGzQ?e=QWMbrR
