Note:  This is a considerably long, but hopefully interesting assignment. Please start early so that you can complete it on time. We will open EMR access for those who want to use it, but it is not required to use it.

The assignment can be done in groups of two. For increasing diversity, the two members need to be from different sets where set A and B are defined here: https://docs.google.com/spreadsheets/d/1kM5ah1TSDqhVMm-UMpbhD1YsHYvxg_eiyWK3dzUyiYo/edit#gid=0 (Links to an external site.) 

Introduction

A detailed dump of Stack Exchange user activity logs are available at: https://archive.org/details/stackexchange (Links to an external site.)

StackOverflow, for example has about 50 GB of compressed data which uncompressed may be 500 GB. Considering the large size of this dataset, we will work with a smaller dataset from datascience forum (https://datascience.stackexchange.com/ (Links to an external site.)).

Data Preparation

Download link for the dataset: datascience.stackexchange.com.7z (Links to an external site.)

https://www.7-zip.org/ (Links to an external site.)    --- To extract the files.

Uncompressed size should be around 355 MB

A cursory look at the data tells me that the content is from May 2014 to Sep 2021. Can you guess how I may have done that?

Example rows for some table.

Posts:

  <row Id="17" PostTypeId="5" CreationDate="2014-05-14T02:49:14.580" Score="0" Body="Chih-Chung .." OwnerUserId="63" LastEditorUserId="63" LastEditDate="2014-05-16T13:44:53.470" LastActivityDate="2014-05-16T13:44:53.470" CommentCount="0" ContentLicense="CC BY-SA 3.0" />

Post History:

<posthistory>
  <row Id="7" PostHistoryTypeId="2" PostId="5" RevisionGUID="009bca93-fce2-44ed-a277-a8452650a627" CreationDate="2014-05-13T23:58:30.457" UserId="5" Text="I've always ...  I do this?" ContentLicense="CC BY-SA 3.0" />

When you extract, you will see the following .xml files.

Badges.xml  ---
Comments.xml -- 
PostHistory.xml ---
PostLinks.xml ---
Posts.xml ---
Tags.xml ---
Users.xml ---
Votes.xml ---

Part 1 <10 Points> Please document the fields in each file to create a "schema". Do you find common fields across files? What may be the purpose in doing so? Present your analysis as a nice table. Organize fields so that the common fields come first.

File Name	Field 1	Field 2	Field 3
Part 2 <10 points> Using simple shell commands, (grep, wc, sort, uniq, awk etc.) count the number of different Badges and the number of users per badge in the Badges.xml file. Prepare the script to run in parallel using Hadoop streaming.

Part 3 <15 points per part> Using the Posts.xml file, write Map-Reduce Jobs to create summary tables (plot wherever possible) for the following:

a. Analyze the popularity of tags (how many posts used each of the tags). Note that a post may have multiple tags. Which theoretical distribution does it look like? 

b. Calculate the View Count Distribution (How many posts were viewed a given number of times). Which theoretical distribution does it look like? Can you identify the top 10 most viewed posts on DataScienceExchange? You can also use their website to verify your answers. Please summarize the posts briefly, i.e. what were they about. 

c. Calculate the number of Posts per Hour of the day, for each of the 24 hours. (Tells us how the user activity varies.) What is the ratio of the peak to lowest user activity per hour? Is there an opportunity for Cloud deployment for Stack Exchange? How much can they save by going to cloud? <Hint: remember the example of Rackspace's mail servers discussed in the class>

Part 4 <15 points> Using the Comments.xml file, write Map-Reduce Jobs to create summary tables (plot wherever possible) for the total Number of Comments and Median of Comment Length by Month from May 2014 to Sep 2021.

Part 5 <20 points> Using the Users.xml file and PostsHistory.xml, calculate the correlation coefficient of the reputation of the user in Users.xml to the total answers (hint: use post History type id) given by the user in PostsHistory.xml file.  Hint [Users.??=PostsHistory.Userid]

Deliverables:

a.  Document with all the answers and explanations of how you designed the code for each part.

b. Shell scripts for Part 2, Map-Reduce (must) and Combine (optional) scripts Parts 3-5.

c. For a Bonus of 20 points, you can submit the time taken by each of your scripts (for every part) to process the data on 1 node vs 5 node EMR cluster. 

For those who have a difficulty with Hadoop, the following solution based on the shell script pattern is also acceptable.

cat file | map | sort | reduce

d. For simplicity of managing grades, every student should submit the assignment. If you did it in groups of 2, one member can submit the full assignment and second student can just describe what each member did in the assignment.
