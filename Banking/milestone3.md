<table><tr><td> <em>Assignment: </em> IS601 Milestone 3 Bank Project</td></tr>
<tr><td> <em>Student: </em> Joy Prakashchandra Patel (jp2267)</td></tr>
<tr><td> <em>Generated: </em> 22/12/2022 19:45:15</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone-3-bank-project/grade/jp2267" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone3 branch</li><li>Create a new markdown file called milestone3.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone3.md</li><li>Add/commit/push the changes to Milestone3</li><li>PR Milestone3 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 4</li><li>Submit the direct link to this new milestone3.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on GitHub and everywhere else. Images are only accepted from dev or prod, not localhost. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> User will be able to transfer between their accounts </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of transfer page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/209240052-5ea75dee-fa76-4cbd-8ed2-0c5be330d669.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Internal Transfer Heading Displayed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot showing dropdown values</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/209240618-496a3975-6c89-4410-be70-c954c58a8075.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>account source<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/209240700-3f1ddaae-2d34-4664-8629-e066ec5d3bb0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>account destination<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot showing user can't transfer more funds than they have</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/209240784-f8986137-e689-4712-ad8b-529236e3cfd2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing user can&#39;t transfer more funds than they have<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot showing user can't transfer to the same account</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/209240866-d1caa787-aab9-4180-b653-8678d23dd176.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing user can&#39;t transfer to the same account<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/209241033-16b662a6-f274-455e-8b19-99915d7d7284.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code snippet that prevents the internal same account transfer<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshot showing you can't transfer an negative balance</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/209241141-0516726f-1ead-4fcd-a589-9ce1c8e4ecab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing you can&#39;t transfer an negative balance<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/209241275-e1f97cf9-d1ed-41c0-a79b-5886e2aac24a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code snippet<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshot of the generated transaction history from the db</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/209241778-6c1f57ef-e358-4383-95e7-88140d028d07.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>see record 15th row to 18th row<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a screenshot of the Accounts table showing both affected accounts</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/209242075-f096103b-bac7-4f70-8d65-787b25eddfdc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>see record from 5th row to 9th row<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Briefly explain the code process/flow of a transfer including how the accounts are fetched for the dropdowns</td></tr>
<tr><td> <em>Response:</em> <ul><br><li>Initial balance is fetched by using the accounts id from all the<br>number of accounts and their expected values or total balance is displayed<div>- two<br>transaction are calculated by when a user transfer the money from src to<br>dest account the money will be deducted from the src account and it<br>will be credited in the dest account, this all process will be done<br>after the final commit.<br><div>- src account is deducted and dest account is credited</div></div><br></li><br></ul><br></td></tr>
<tr><td> <em>Sub-Task 9: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/jp2267/is-601-005/pull/31">https://github.com/jp2267/is-601-005/pull/31</a> </td></tr>
<tr><td> <em>Sub-Task 10: </em> Add link to transfer page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is-601-jp2267-fp-prod.herokuapp.com/accounts/transfer">https://is-601-jp2267-fp-prod.herokuapp.com/accounts/transfer</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Transaction History Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of transaction history page showing the new transfer transaction</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/209243224-535abf09-2075-444c-af31-f27b350a81d2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>look at 2nd and 3rd record<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots demonstrating the filters and pagination</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/209243343-7a346a55-b5fc-4153-8080-ef6e1de2033b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>transaction type : deposite filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/209243440-edf3aa03-f099-4a3a-9a91-b2554161a9c2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>transaction type : transfer filter applied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how the filters/pagination work</td></tr>
<tr><td> <em>Response:</em> <p>Pagination Tried but not working<div>Logic applied is that one page will have max<br>10 rows to display, if the no of rows exceeds above 10 then<br>it will create a page 1 same thing for the remaining pagination.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/jp2267/is-601-005/pull/31">https://github.com/jp2267/is-601-005/pull/31</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add link to Transaction History page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is-601-jp2267-fp-prod.herokuapp.com/accounts/transactions?acc_number=000000000003">https://is-601-jp2267-fp-prod.herokuapp.com/accounts/transactions?acc_number=000000000003</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> User's profile First name and Last name </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the user's profile with the new fields</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/209244204-8313c8b6-f1b1-42d6-b0bc-f3c379728da7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing the first name and last name <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/jp2267/is-601-005/pull/31">https://github.com/jp2267/is-601-005/pull/31</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Add link to profile page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is-601-jp2267-fp-prod.herokuapp.com/profile">https://is-601-jp2267-fp-prod.herokuapp.com/profile</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> User will be able to transfer funds to another user </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the external transfer page with filled in data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/209244705-11d21ba7-8f7e-4221-bd83-874c1cad4ecd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>External Transfer Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot showing user can't send more than they have</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/209245009-cc75ff93-2740-4159-aaee-037871e1036f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing user can&#39;t send more than they have<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/209245118-b96231f7-0b8f-4a71-b376-b7902c668174.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code snippet<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot showing they can't send a negative amount</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/209245205-29db16ce-4ac9-4321-a7a9-4cfe63d163ff.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing they can&#39;t send a negative amount<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/209245280-1293141d-a382-47b0-974e-cf29ce27b9dc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code snippet<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot(s) showing message if a user doesn't exist and/or a destination account wasn't found</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshot of the transactions table showing the recorded transfer</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/209246142-1d5b29be-0d7f-47cb-a286-d2ace5d1c97c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>see the last 2 records<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshot(s) showing the updated account balances</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113148416/209246290-5a9f3fb5-e6d9-4e53-a7d7-4224be516749.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>see row 3rd and 5th<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Briefly explain the process of looking up the target user's account and the validation logic</td></tr>
<tr><td> <em>Response:</em> <ul><br><li>Account is fetched using the account id plus the user id<div>- The<br>destination account is fetched using the input given by user as a last<br>name and the account number ending 4 digits.</div><div>- Then it will perform the<br>two transaction one will be deduction of amount from src account and the<br>same amount will be transferred to the src account&nbsp;<br><div><div><br></div></div></div><br></li><br></ul><br></td></tr>
<tr><td> <em>Sub-Task 8: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/jp2267/is-601-005/pull/31">https://github.com/jp2267/is-601-005/pull/31</a> </td></tr>
<tr><td> <em>Sub-Task 9: </em> Add link to external transfer page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is-601-jp2267-fp-prod.herokuapp.com/accounts/ext_transfer">https://is-601-jp2267-fp-prod.herokuapp.com/accounts/ext_transfer</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Learned about the transaction between two internal accounts and transfering the funds to<br>external accounts through the db executions.<div><br></div><div>Pagination part is not done it is challenging</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone-3-bank-project/grade/jp2267" target="_blank">Grading</a></td></tr></table>