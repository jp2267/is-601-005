<table><tr><td> <em>Assignment: </em> IS601 Mini Project 2  Business Management</td></tr>
<tr><td> <em>Student: </em> Joy Prakashchandra Patel (jp2267)</td></tr>
<tr><td> <em>Generated: </em> 08/12/2022 00:19:56</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-mini-project-2-business-management/grade/jp2267" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>checkout dev and pull any latest changes</li><li>Create a branch called MiniProject-2</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li>Immediate add/commit/push to github</li><li>Open a pull request and keep it open until you're done adding the submission file</li><li>&nbsp;(optional) updated the deploy dev yml file and add MiniProject-2 so you can deploy to dev without needing to merge into dev</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item)<br></li><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 5</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together</li><li>Ensure all screenshots are properly captioned in the deliverable section</li></ol><li>You may save your progress when filling out this submission as often as you want</li><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from dev to prod and merge it</li><li>Navigate to the submission file under the BusinessManagement folder</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F22-MiniProject-2">https://github.com/MattToegel/IS601/tree/F22-MiniProject-2</a></div><div>May want to download branch as a zip, then copy/paste the files into your repo</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206341110-ae228a48-4bc6-442d-8fa5-f5a767f62038.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the task #1, #2 and #3<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206341300-dff94925-c87c-45cc-8e5b-f0236d0aa280.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the employee database<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206341557-d8a104a8-8633-41f2-b29c-7c7730414beb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the companies database<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206343367-dbf5b00b-538b-49d1-9649-1f2b41e96414.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the task from #1 to #4<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206343517-ca03ec35-bb67-4407-a679-4306c45dba68.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the task #5 and #6<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206343662-f1d48c83-e735-428b-bd67-78c860242399.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the task #1 and #2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206343812-e9fb544f-6879-41f7-9b73-01b3e772e7f4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Uploading a non .csv file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206343951-e0a877fd-adea-45d8-919a-456a70f5d2cf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the error msg of not a csv file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206344085-8704b2a6-af85-4b1c-bfdc-8fbf4d935dbc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the error msg when no file is uploded<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206341300-dff94925-c87c-45cc-8e5b-f0236d0aa280.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the employee data base<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206341557-d8a104a8-8633-41f2-b29c-7c7730414beb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the company data base<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206344843-a6ac4619-63c3-49fe-9f99-56bee20310aa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the task from #1 to #8<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206345235-d2d7db2c-e23c-4c8f-923a-08a9bbfe465a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the filled in valid data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206345346-9293b5c2-3bee-4213-9fe0-df6b51979158.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the success msg<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206345535-33252647-1518-4793-99be-ce2fe37fda7a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the first name error msg<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206345676-9be026ed-f316-41e5-85ec-cf844594b076.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the last name error msg<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206345826-6f43992c-4eab-4bf4-9918-bdf852d8256c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows email error msg<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206345978-5b3f0f60-d043-4ee1-824b-6606f93ca1d6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the new record added in the database<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206346211-2a542791-b236-4b96-959a-49d48132d41d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows tasks from #1 to #7<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206346503-20d1218b-b599-4f0b-aad0-ea1010454ea7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows tasks from #8 to #10<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206346664-a433d768-1552-49a2-ae4f-044a6a7981e1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>first name filter was applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206346768-50921142-5c30-48c9-977e-a38ac15b0d11.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>last name filter was applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206346852-077d94f6-811c-4b09-8a47-ff5cc81a1514.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email filter was applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206346928-5b052e38-f573-4333-9681-3e205b30fed2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>company filter was applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206347038-42f17a70-d13c-46f1-8f3c-45aaafc250db.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>asc filter applied on first name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206347086-f76bea5b-db8c-416c-8556-7d2de00ad53f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>desc filter applied on first name<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206347433-15679aa2-f80f-4256-8230-54b70acf055a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It show the task from #1 to #6<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206347545-8dcda419-bcd2-4996-8019-29c4136fd360.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It show the task from #7 to #9<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206347582-81a96df2-9f63-4b5d-a6ab-4714e7a789d3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows data before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206348022-3d2d0ea5-9368-4e18-8ae3-567eb5a94539.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the data is edited , the first name and last name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206348929-6f30e433-ee3e-4031-899f-5fe92e2a4e6a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the first name and last name is changed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206350112-ab2eb597-1024-4c73-8f8a-b027d53f109b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the updated data, in the first row you can see the<br>first name and last name is updated<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206350484-a0b7b06d-add2-47de-8600-94d3a5ad04a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the task from #1 to #8<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206350703-5fa5b405-4047-44f0-b6a2-d0b8e3ef2e6f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the task #9<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206351310-f60ee9bc-539e-4f85-9950-8409ef491aa3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the added company data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206351595-a48999fe-c4c0-4f5d-af33-0c11454f622d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the success msg<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206351955-6dd7fa68-7f50-4e30-8ea6-239082ec2665.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the task from #3 to #7<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206352153-217068fb-2ca7-4763-8771-ba4cefeac47f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The last record in the database is the newly added data <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206352754-a6036591-098e-4f2d-853a-f941efb13f8b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the task from #1 to #8<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206352793-48dd3eb9-08d1-4787-9d6e-65966bcba640.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the task #9<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206353037-742f5464-7f50-41c1-bb08-3d4c93c2fd0b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the name filtered applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206353257-42e82605-216c-4e5b-8a0e-d975da82225f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>country field applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206353371-2db53210-85ca-47af-b6cb-314f756418b3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>state filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206353546-133e1f29-02b3-483c-9bd5-f990a010626a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the asc filter with the column as first name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206353653-b1c48c7f-bfc6-4058-8edb-1e2479181d07.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the desc filter with the column as first name<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206354015-59f90b2c-80bd-459a-91ed-8c2276dc639b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the task from #1 to #9<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206354384-1cdffa66-99ad-448c-ac5c-6704f9f04e99.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the #10 task<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206354599-e74d7783-2809-4c48-81ef-b5c06e686777.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the task #1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206355176-40462741-1ea5-483e-9ccf-f87844b604be.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the data is updated, you can see in <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206355335-e0251232-e1b2-4e84-872f-afb52b811c36.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>You can see the 7th record is updated<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206355467-ef67fbdd-7321-48f7-8b25-bb952c92ebec.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Refer the 7th record, the name and address is changed in the second<br>screenshot<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206355724-c08d510e-33a5-422b-af34-03934e87bdf7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Refer the 7 record in the table <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206358937-36920a80-b85b-418d-b54b-958693fed1d9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the delete employee code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206359266-c2a3409f-8f91-4786-a8ce-308cb981ee19.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Deleting the employee record 10<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206359307-e4f5a424-0aed-4609-a882-598b1490b1cb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Deleted the record employee record 10<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206356691-039aac14-843f-4a87-a4b4-79e984891f2d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows the code of delete company code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206359731-0e3082b3-8213-4390-b7e5-b57f7af35e55.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deleting the record 8<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206362945-3a2ffd0c-5e41-476c-9d18-40dd23ec4b60.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After deleting record 8<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/206360437-f3b86361-85e8-46ce-a850-d892840fe57f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test cases are passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>I learn the crud operation during working on this project, and also learn<br>major part of flask how to get values from frontend and perform logics<br>in the backend, i faced issued in the deployment to the heroku server,<br>but finally i got the point and it was sorted with the professors<br>help.<div><br></div><div>It was a very good project to work on learned a lot of<br>stuffs&nbsp;</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-mini-project-2-business-management/grade/jp2267" target="_blank">Grading</a></td></tr></table>