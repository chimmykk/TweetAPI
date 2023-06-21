const express = require('express');
const app = express();

const needle = require('needle');
const fs = require('fs');
const path = require('path');
const http = require('http');
const cors = require('cors'); // Import cors module

// Enable All CORS Requests
app.use(cors());

const token = "AAAAAAAAAAAAAAAAAAAAACG9oAEAAAAA0a7h3xQL2nEt%2Bo%2BJ%2BT7jKOS7o%2Fs%3Dg29BN5D1ehzxyFQvLfNmszZVbg4x9gkBSXnsDbI3paw1P3WuSl";
const endpointUrl = "https://api.twitter.com/2/tweets/search/recent";

// Function to search tweets using the Twitter API
async function searchTweets() {
  const params = {
    query: "dogepound",
    "tweet.fields": "public_metrics,created_at,text",
    "expansions": "author_id",
    "user.fields": "username,name,profile_image_url"
  };

  const response = await needle("get", endpointUrl, params, {
    headers: {
      "User-Agent": "v2RecentSearchJS",
      authorization: `Bearer ${token}`
    }
  });

  if (response.body) {
    const { data, includes } = response.body;
    const tweets = [];

    if (data && data.length > 0) {
      for (const tweet of data) {
        const {
          id,
          public_metrics,
          created_at,
          text,
          author_id
        } = tweet;

        const {
          name,
          username,
          profile_image_url
        } = includes.users.find(user => user.id === author_id);

        const tweetData = {
          id,
          public_metrics,
          created_at,
          text,
          author: {
            name,
            username,
            profile_image_url
          }
        };

        tweets.push(tweetData);
      }
    }

    const output = {
      tweets
    };

    const jsonOutput = JSON.stringify(output, null, 2);
    const filePath = path.join(__dirname, 'pulltweet', 'test.json');

    fs.writeFileSync(filePath, jsonOutput);

    console.log('Output saved to test.json');
  } else {
    throw new Error("Unsuccessful request");
  }
}

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

// Function to start the HTTP server
async function startServer() {
  const port = 8080;

  app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
  });
}

// Main function to run the code
async function run() {
  try {
    await searchTweets(); // Search tweets and save the results to test.json
    await startServer(); // Start the HTTP server to serve the JSON file
  } catch (error) {
    console.error(error);
  }
}

run(); // Run the main function
