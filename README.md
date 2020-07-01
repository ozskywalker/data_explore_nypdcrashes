# Data Exploration - NYPD Car Crashes

Excuse the hackiness.  This is a 1am job :)

## Step 1 - base environment

1. ``git clone`` this repo
2. __DON'T UNZIP the data yet.__
3. Run ``docker-compose up -d``
4. Open browser to http://localhost:5601/
5. Click __Explore on my own__ in the Kibana console
6. Click on __Console__ under _Manage and Administer the Elastic Stack_
7. Copy and paste the contents of ``crashes_pipeline.txt`` into the console and hit the PLAY button

## Step 2 - Loading in data

8. Run ``docker ps -a``, and stop the filebeat container
9. Extract the ``data/crashes.csv.gz`` - the file should now become ``data/crashes.csv``
10. Re-run ``docker-compose up -d``

Data will now start loading in as the filebeat container starts up.

We had to do it this way, because we needed the pipeline inserted first, and I haven't scripted loading that /before/ the filebeat container comes online to start loading data.

## Step 3 - Create Kibana Index & Start exploring your data

To begin exploring an index (whether partially or fully loaded), you will always need to define a Kibana index pattern.

1. Click on Discover (first icon in sidebar)
2. Set the index pattern to _filebeat*_ and click __Next Step__
3. Set the time filter field name to _@timestamp_ and click __Create Index Pattern__
4. Click on Discover again.

Please note that by default Kibana sets its time range back to 15min ago from now, and for first timers this makes you think there is no data.

Make sure you click on "Last 15 minutes" in the top-right, and change it to an appropriate selection (ie 15 years ago).

## Destroying your environment

Run ``docker-compose down``

## Stopping the environment

Don't want to be destructive?  Run ``docker-compose stop`` !