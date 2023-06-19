// Search for Tweets(For certain time-frame)

const needle = require('needle');

const token ="$youneeda$100plan";
// Atleast save $4900

const endpointUrl = "https://api.twitter.com/2/tweets/search/recent";

async function getRequest() {
    // Edit query parameters below
    // specify a search query, and any additional fields that are required
    // by default, only the Tweet ID and text fields are returned
    const params = {
        'query': 'dogepound',
        'tweet.fields': 'author_id,public_metrics'
    }

    const res = await needle('get', endpointUrl, params, {
        headers: {
            "User-Agent": "v2RecentSearchJS",
            "authorization": `Bearer ${token}`
        }
    });

    if (res.body) {
        return res.body;
    } else {
        throw new Error('Unsuccessful request');
    }
}

async function getTweetDetails(tweetId) {
    const apiUrl = `https://api.twitter.com/2/tweets/${tweetId}?tweet.fields=public_metrics`;

    const res = await needle('get', apiUrl, {
        headers: {
            "User-Agent": "v2RecentSearchJS",
            "authorization": `Bearer ${token}`
        }
    });

    if (res.body) {
        return res.body;
    } else {
        throw new Error('Unsuccessful request');
    }
}

(async () => {
    try {
        // Make request to search for tweets
        const response = await getRequest();
        console.dir(response, { depth: null });

        // Get details of public metrics for each tweet
        if (response.data && response.data.length > 0) {
            for (const tweetData of response.data) {
                const tweetDetails = await getTweetDetails(tweetData.id);
                console.log(`Tweet ${tweetData.id} - Public Metrics:`, tweetDetails.data.public_metrics);
            }
        } else {
            console.log('No tweets found.');
        }
    } catch (e) {
        console.log(e);
        process.exit(-1);
    }
    process.exit();
})();