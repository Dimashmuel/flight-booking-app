import React, { useEffect, useState } from 'react';

function App() {
  const [flights, setFlights] = useState([]);
  const [search, setSearch] = useState('');
  const [originFilter, setOriginFilter] = useState('');
  const [destinationFilter, setDestinationFilter] = useState('');
  const [bookingFlightId, setBookingFlightId] = useState(null);
  const [passengerName, setPassengerName] = useState('');
  const [passengerEmail, setPassengerEmail] = useState('');
  const [emailError, setEmailError] = useState('');
  const [nameError, setNameError] = useState('');
  const [message, setMessage] = useState('');
  const [view, setView] = useState('flights');
  const [bookings, setBookings] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/flights')
      .then((res) => res.json())
      .then((data) => setFlights(data))
      .catch((error) => console.error('Error fetching flights:', error));
  }, []);

  useEffect(() => {
    if (view === 'bookings') {
      fetch('http://127.0.0.1:8000/api/bookings')
        .then(res => res.json())
        .then(data => setBookings(data))
        .catch(err => console.error('Error fetching bookings:', err));
    }
  }, [view]);

  const uniqueOrigins = [...new Set(flights.map((f) => f.origin))];
  const uniqueDestinations = [...new Set(flights.map((f) => f.destination))];

  const filteredFlights = flights.filter((flight) => {
    const matchSearch = `${flight.origin} ${flight.destination} ${flight.airline}`.toLowerCase().includes(search.toLowerCase());
    const matchOrigin = originFilter === '' || flight.origin === originFilter;
    const matchDestination = destinationFilter === '' || flight.destination === destinationFilter;
    return matchSearch && matchOrigin && matchDestination;
  });

  const handleBookingSubmit = (flightId) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!passengerName.trim()) {
      setNameError('Please enter your name.');
      return;
    }
    setNameError('');

    if (!emailRegex.test(passengerEmail)) {
      setEmailError('Please enter a valid email address.');
      return;
    }
    setEmailError('');

    fetch('http://127.0.0.1:8000/api/book', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        flight: flightId,
        passenger_name: passengerName,
        passenger_email: passengerEmail
      })
    })
      .then(res => res.json())
      .then(data => {
        setMessage(data.message || 'Booking submitted!');
        setBookingFlightId(null);
        setPassengerName('');
        setPassengerEmail('');
      })
      .catch(err => {
        console.error(err);
        setMessage('Booking failed.');
      });
  };

  const handleDeleteBooking = (id) => {
    if (!window.confirm('Are you sure you want to delete this booking?')) return;

    fetch(`http://127.0.0.1:8000/api/bookings/${id}`, {
      method: 'DELETE'
    })
      .then(res => {
        if (res.ok) {
          setBookings(bookings.filter(b => b.booking_id !== id));
          setMessage('Booking deleted.');
        } else {
          throw new Error('Delete failed');
        }
      })
      .catch(err => {
        console.error(err);
        setMessage('Could not delete booking.');
      });
  };

  return (
    <div className="container py-4">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h1>{view === 'flights' ? 'Welcome to the Flight Booking System' : 'My Bookings'}</h1>
        <div>
          <button className={`btn btn-sm me-2 ${view === 'flights' ? 'btn-primary' : 'btn-outline-primary'}`} onClick={() => setView('flights')}>
            Show Flights
          </button>
          <button className={`btn btn-sm ${view === 'bookings' ? 'btn-primary' : 'btn-outline-primary'}`} onClick={() => setView('bookings')}>
            Show Bookings
          </button>
        </div>
      </div>

      {message && <div className="alert alert-info">{message}</div>}

      {view === 'flights' && (
        <>
          <div className="row align-items-end mb-4 g-2">
            <div className="col-md-3">
              <label className="form-label">Search</label>
              <input
                type="text"
                className="form-control"
                placeholder="Search flights..."
                value={search}
                onChange={(e) => setSearch(e.target.value)}
              />
            </div>
            <div className="col-md-3">
              <label className="form-label">From</label>
              <select className="form-select" value={originFilter} onChange={(e) => setOriginFilter(e.target.value)}>
                <option value="">All Origins</option>
                {uniqueOrigins.map((origin, i) => <option key={i} value={origin}>{origin}</option>)}
              </select>
            </div>
            <div className="col-md-3">
              <label className="form-label">To</label>
              <select className="form-select" value={destinationFilter} onChange={(e) => setDestinationFilter(e.target.value)}>
                <option value="">All Destinations</option>
                {uniqueDestinations.map((dest, i) => <option key={i} value={dest}>{dest}</option>)}
              </select>
            </div>
            <div className="col-md-3 d-grid">
              <button className="btn btn-outline-secondary" onClick={() => {
                setSearch('');
                setOriginFilter('');
                setDestinationFilter('');
              }}>
                Clear Filters
              </button>
            </div>
          </div>

          <div className="row">
            {filteredFlights.map((flight, index) => (
              <div className="col-md-6 col-lg-4 mb-4" key={index}>
                <div className="card shadow-sm h-100">
                  <div className="card-body d-flex flex-column justify-content-between h-100">
                    <div>
                      <h5 className="card-title">✈️ {flight.origin} → {flight.destination}</h5>
                      <p className="card-text mb-2">
                        <strong>Date:</strong> {flight.departure_date}<br />
                        <strong>Time:</strong> {flight.departure_time}<br />
                        <strong>Airline:</strong> {flight.airline}
                      </p>
                    </div>

                    {bookingFlightId === flight.id ? (
                      <div className="border-top pt-3 mt-3">
                        <input
                          type="text"
                          className={`form-control mb-2 ${nameError ? 'is-invalid' : ''}`}
                          placeholder="Your Name"
                          value={passengerName}
                          onChange={(e) => setPassengerName(e.target.value)}
                        />
                        {nameError && <div className="invalid-feedback">{nameError}</div>}

                        <input
                          type="email"
                          className={`form-control mb-2 ${emailError ? 'is-invalid' : ''}`}
                          placeholder="Your Email"
                          value={passengerEmail}
                          onChange={(e) => setPassengerEmail(e.target.value)}
                        />
                        {emailError && <div className="invalid-feedback">{emailError}</div>}

                        <button
                          className="btn btn-success w-100"
                          onClick={() => handleBookingSubmit(flight.id)}
                        >
                          Confirm Booking
                        </button>
                      </div>
                    ) : (
                      <button
                        className="btn btn-outline-primary w-100 mt-3"
                        onClick={() => setBookingFlightId(flight.id)}
                      >
                        Book This Flight
                      </button>
                    )}
                  </div>
                </div>
              </div>
            ))}
            {filteredFlights.length === 0 && (
              <div className="col-12 text-center text-muted">
                <p>No matching flights found.</p>
              </div>
            )}
          </div>
        </>
      )}

      {view === 'bookings' && (
        <div className="row">
          {bookings.length === 0 ? (
            <div className="alert alert-warning">No bookings found.</div>
          ) : (
            bookings.map((b, i) => (
              <div className="col-md-6 col-lg-4 mb-4" key={i}>
                <div className="card h-100 shadow-sm border-info">
                  <div className="card-body">
                    <h5 className="card-title">{b.name}</h5>
                    <p className="card-text mb-1">
                      <strong>Email:</strong> {b.email}<br />
                      <strong>Flight:</strong> {b.origin} → {b.destination}<br />
                      <strong>Date:</strong> {b.date} at {b.time}<br />
                      <strong>Airline:</strong> {b.airline}<br />
                      <strong>Flight ID:</strong> {b.flight_id}
                    </p>
                    <button className="btn btn-outline-danger btn-sm mt-2" onClick={() => handleDeleteBooking(b.booking_id)}>
                      Delete
                    </button>
                  </div>
                </div>
              </div>
            ))
          )}
        </div>
      )}
    </div>
  );
}

export default App;