const express = require('express');
const bodyParser = require('body-parser');
const moment = require('moment');
const app = express();

// Configure middleware to parse the request body
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Serve static files (CSS, JS, etc.) from a public directory
app.use(express.static('public'));

// Define the route to handle the form submission
app.post('/submit', (req, res) => {
  const cityId = req.body.city_id;
  const pickupDate = moment(req.body.datetimes);

  // Validate city ID
  if (!isValidCityId(cityId)) {
    return res.status(400).json({ error: 'Invalid city ID' });
  }

  // Validate pickup date
  if (!isValidDate(pickupDate)) {
    return res.status(400).json({ error: 'Invalid pickup date' });
  }

  // Perform other necessary actions with the validated data
  // e.g., save booking details to a database, process payment, etc.

  // Return a success response
  return res.status(200).json({ message: 'Booking confirmed' });
});

// Utility function to validate the city ID
function isValidCityId(cityId) {
  // Implement your own validation logic here
  // Example: Check if the city ID exists in a database
  // You may also consider using a validation library like Joi or Yup
  return cityId === '4';
}

// Utility function to validate the pickup date
function isValidDate(date) {
  // Ensure the date is valid and not in the past
  return date.isValid() && date.isAfter(moment());
}

// Start the server
app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
