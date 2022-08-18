# ra_bot
RA Bot for Montgomery Hall (still being updated)


'GROUPME_BOT_ID' is a environment variable created to represent the Bot's ID



## Introduction

A simple GroupMe bot that reacts to messages sent within a group.

## Contents

  * [Quickly get our sample bot up and running in your groups](#deploy)
    * Deploy the code to heroku
    * Create a bot
    * Configure to your bot's credentials
  * [Make changes to the bot](#pull)
    * Pull the code down to your local machine
    * Configure the local environment variables to your bot's credentials

## Requirements:

  * GroupMe account
  * Heroku account
  * [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

# Get your bot up and running<a name="deploy"></a>

## Deploy to Heroku:

Be sure to log in to Heroku, using your Heroku credentials, then click the link below.

[![Deploy]
You should be taken to a page that looks like this:

![Deploy to Heroku]

Optionally, you can give your app a name, or instead leave it blank and let Heroku name it for you (you can change it later).

![Success]

## Next, create a GroupMe Bot:

Go to:
https://dev.groupme.com/session/new

Use your GroupMe credentials to log into the developer site.

![Log into dev.groupme.com]

Once you have successfully logged in, go to https://dev.groupme.com/bots/new

![Create your new bot]

Fill out the form to create your new bot:

  * Select the group where you want the bot to live
  * Give your bot a name
  * Paste in the URL of your newly deployed Heroku app
    * `http://your-app-name-here.herokuapp.com/`
  * (Optional) Give your bot an avatar by providing the URL of an image
  * Click submit!

## Find your Bot ID:<a name="get-bot-id"></a>

Go here to view all of your bots:
https://dev.groupme.com/bots

Click on the one you just created.

![Select your new bot]

On your Bot's page, copy the Bot ID

![Copy your Bot ID]

## Add your Bot ID to your Heroku app:

Go here to see all of your Heroku apps and select the one you just created before:

https://dashboard-next.heroku.com/apps

![Select your heroku app]

On your app page, click settings in the top navigation:

![Go to your app's settings]

On your app's setting page, find the Config Vars section and click the Reveal Config Vars button:

![Reveal your environment variables]

Then click edit:

![Edit your environment variables]

Fill out the form to add an environment variable to your app:

  * In the "key" field type: BOT_ID
  * In the "value" field paste your Bot ID that you copied in the previous steps
  * Click the save button

![Add the Bot ID environment variable]

## Now go test your bot!

Go to GroupMe and type "/ping" in the group where your bot lives to see it in action.

![Test your Bot]

# Make it your own<a name="pull"></a>

## Pull the code to your local machine

Within terminal, change directory to the location where you would like the files to live, then run this command:

```sh
heroku git:clone -a YOUR_APP_NAME_HERE
```

And then change directory into the new folder

```sh
cd YOUR_APP_NAME_HERE
```

## Configure your local `GROUPMEBOT_ID` environment variable

You will need to set the `GROUPMEBOT_ID` environment variable so that your bot will know where to send its messages.

If you don't know what your Bot ID is, please refer back to [this](#get-bot-id) section, where it is explained how to retrieve it.

In your terminal, run
```sh
export BOT_ID = INSERT_YOUR_BOT_ID_HERE
```
You may wish to add this to a file that runs each time you start your shell, such as `~/.bashrc`.

For Heroku, run:
```sh
heroku config:set BOT_ID = INSERT_YOUR_BOT_ID_HERE
```

## Start the server

