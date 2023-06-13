// Sample data for booking history and current bookings
const bookingHistory = [
  { id: 1, car: 'Toyota Camry', startDate: '2023-05-20', endDate: '2023-05-25', status: 'Completed' },
  { id: 2, car: 'Honda Civic', startDate: '2023-06-01', endDate: '2023-06-05', status: 'Upcoming' },
  { id: 3, car: 'Ford Mustang', startDate: '2023-05-15', endDate: '2023-05-18', status: 'Completed' }
];

const currentBookings = [
  { id: 4, car: 'Tesla Model S', startDate: '2023-06-02', endDate: '2023-06-10', status: 'Ongoing' },
  { id: 5, car: 'BMW X5', startDate: '2023-06-03', endDate: '2023-06-07', status: 'Upcoming' }
];

// Function to create table rows for the booking history
function populateBookingHistory() {
  const bookingHistoryTable = document.querySelector('#booking-history-table tbody');

  bookingHistory.forEach(booking => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${booking.id}</td>
      <td>${booking.car}</td>
      <td>${booking.startDate}</td>
      <td>${booking.endDate}</td>
      <td>${booking.status}</td>
    `;
    bookingHistoryTable.appendChild(row);
  });
}

// Function to create table rows for the current bookings
function populateCurrentBookings() {
  const currentBookingsTable = document.querySelector('#current-bookings-table tbody');

  currentBookings.forEach(booking => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${booking.id}</td>
      <td>${booking.car}</td>
      <td>${booking.startDate}</td>
      <td>${booking.endDate}</td>
      <td>${booking.status}</td>
    `;
    currentBookingsTable.appendChild(row);
  });
}

// Call the functions to populate the tables
populateBookingHistory();
populateCurrentBookings();
