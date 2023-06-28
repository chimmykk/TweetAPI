const express = require('express');
const app = express();
const fs = require('fs');
const path = require('path');

// Function to serve the JSON file through HTTP
app.get('/pulltweet/test.json', (req, res) => {
  const filePath = path.join(__dirname, 'pulltweet', 'test.json');

  fs.readFile(filePath, (err, data) => {
    if (err) {
      res.status(500).send('Internal Server Error');
    } else {
      res.status(200).json(JSON.parse(data));
    }
  });
});

// Start the server
const port = 8080;
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
