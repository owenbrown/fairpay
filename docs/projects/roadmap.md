This document describes each stage of developing this application.
The numbering system matching each document to the detailed markdown file in docs/projects/

0010 Create Django application with landing page
0011 Document how Django app is structured
0020 Allow user to sign into landing page
0025 Create mock frontend application, without uplaoding real images
 - To aid visualization, use stub images
0030 Allow user to scan price tags
 - Decide if async upload of the file is possible
 - Decide where to store file - s3, render storage, or other file system
 - Create Django model to store data
 - For proof of concept, storing the file in local file system is acceptable
 - Create huey task
0040 Configure Veryfi AnyDocs template. Complete task processor.
0050 Allow user to upload receipt
 - Create Django model to store receipt
 - Call create task to upload recept to Veryfi
0060 Process call to Veryfi's recepts API endpoint
0070 Design page that displays the results
 - There are many ways on how to dispaly this data
0080 
- Implement page that dispalys the results
0090 Write blog post and press release
