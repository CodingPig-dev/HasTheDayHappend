# HasTheDayHappened

This repository is completly useless. Every day since the year 1900 gets added to the days json file after it has happened. The file is like a list of all the days that have already happened with each date marked as true.

## How it works

A Raspberry Pi is set up to run a job every day at midnight. This job updates the days json file. When a day is over the date gets added to the JSON file.

## API
The repository has a JSON API at https://epi.etme.tech/HasTheDayHappend/. This API returns the complete days json file, which has all the days that have already happened.
Anyone can use this API to check if a specific day has already happened.

## Rate Limiting

To stop people from using the API much and to prevent the server from getting overloaded there is a limit on how many requests you can make. Each computer is allowed to make one request per second. If you make requests in one second the API will say 429 Too Many Requests. This limit is, for each computer so each user has their limit.

## Technical Details

This project uses a Raspberry Pi and has the following parts:

- PHP is used to serve the API

- Cloudflare is used for HTTPS and to protect the server

- A JSON file called the days json is used as the database

- A job called a cron job is used to update the days json file every day

So it works like this: the cron job updates the days json file then the PHP API uses this file and Cloudflare adds HTTPS and protection and then users can access it.

## Why

Why not?
