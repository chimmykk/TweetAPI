const needle = require('needle');

const token ="$youneeda$100plan";
// Atleast save $4900

const endpointUrl = "https://api.twitter.com/2/tweets/search/recent";

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
// Data-> Data.tweets to fetch text from the twitter tweets
  if (response.body) {
    const { data, includes } = response.body;
    const tweets = [];
// If Data exist extract the details, id, public_metrics,timestamp,author_id
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
// Display a CONSOLE Log json file
    console.log(JSON.stringify(output, null, 2));
  } else {
    throw new Error("Unsuccessful request");
  }
}
// Updating to push the tweets and automatically saved it on a folder 
// Under Pulltweets folder
searchTweets().catch(console.error);
