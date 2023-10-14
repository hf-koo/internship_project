# Created by ahdoy at 10/11/23
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: User can open and verify application
   Given Open Main page
   When Log in to the page
   And Click on Get a free Subscription
   And Switch the new tab
   And Enter some test information in the form at the right side of the page
   Then Verify the right information is present
   #And Switch back to original