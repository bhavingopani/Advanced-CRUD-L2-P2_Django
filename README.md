# Advanced-CRUD-L2-P2_Django
Create Advanced CRUD App in Django Level 2 - Project 2 (Refer Simple-CRUD-L1-P1_Django)



Add few more fields in user add/edit form 

  - Date of birth
  - Hobbies
  - Profile picture
  - Address line 1
  - Address line 2
  - City
  - State
  - Country dropdown with list of all country

Functionalities and Conditions:
  - Address fields need to be stored in different table called "user_addresses". So that users and user_addresses tables have one to one relationship.
  - Hobbies need to be stored in different table called "user_hobbies". So that users and user_hobbies tables have one to many realtionship.
  - DOB(age) should not  be less than 21 years.
  - Hobbies selection should have checkbox.
  - At least 2 hobbies must be selected.
  - Profile pictures should only be image ( PNG and JPG ) and size must be less than 1 MB.
  - In list users page add profile picture with Full name column, new column for DOB and Hobbies.
  - Add/Edit form should be via ajax.
  - If is there is any validation error arrise in ajax than it should be filled in form for each field
  - Profile pictire needs to be stored in the public directory of project with this location uploads/<user_id>
