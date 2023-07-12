const { exec } = require('child_process');
const robot = require('robotjs');
const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

async function automateChatbot() {
  // Open the chatbot application
  exec('start "" "C:\\Users\\paperspace\\Downloads\\AllCharactersAI_v0.18\\AllCharactersAI_v0.18\\Windows\\Chatbot_Characters.exe"');

  await sleep(2000);

  // Press "Tab" key three times to navigate to the Doge option
  robot.keyTap('tab');
  robot.keyTap('tab');
  robot.keyTap('tab');

  // Press "Enter" key to select the Doge option
  robot.keyTap('enter');

  await sleep(2000);

  // Press "Tab" key three times to trigger three tabs again
  robot.keyTap('tab');
  robot.keyTap('tab');
  robot.keyTap('tab');

  await sleep(2000);

  // Type "what is your name"
  robot.typeString("what is your name");

  // Press "Enter" key to send the message
  robot.keyTap('enter');

  // Add a 2-second delay
  await sleep(2000);

  // Enable screen recording
  robot.keyToggle('alt', 'down');
  robot.keyTap('f9');
  robot.keyToggle('alt', 'up');

  // Wait for 1 minute
  await sleep(60000);

  // Close the application
  robot.keyToggle('alt', 'down');
  robot.keyTap('f4');
  robot.keyToggle('alt', 'up');
}

automateChatbot();
