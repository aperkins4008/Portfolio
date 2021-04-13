#pragma once
#define StudentHeader

#include "degree.h"
#include <string>
using namespace std;

class Student {

/*-------------------------------------------------------------------------------------------------------*/
/*                                          Requirement D.1                                              */
/*-------------------------------------------------------------------------------------------------------*/

public:
	string StudentID;
	string FirstName;
	string LastName;
	string EmailAddress;
	
	int Age;
	int* DaysToCompleteCourse;
	
	const int Courses = 3;



/*-------------------------------------------------------------------------------------------------------*/
/*                                Requirement D.2.A (accessors)                                          */
/*-------------------------------------------------------------------------------------------------------*/
// Original Default Constructor 
//    Student();

	Student(string NewStudentID, string NewFirstName, string NewLastName,
		    string newEmailAddress, int SuperNaturalist_NewAge, int* DaysToCompleteCourse);
	// D.2.C ^^^ (Constructor using all of the input parameters provided in the table)
   ~Student(); // D.2.E (Destructor)

	string GetStudentID();
	string GetFirstName();
	string GetLastName();
	string GetEmailAddress();
	int* GetDaysToCompleteCourse(int NewDays[]);
	int    GetAge();

	

/*-------------------------------------------------------------------------------------------------------*/
/*                                Requirement D.2.B (mutators)                                          */
/*-------------------------------------------------------------------------------------------------------*/


public:
	void SetStudentID(string NewStudentID);
	void SetFirstName(string NewFirstName);
	void SetLastName(string NewLastName);
	void SetEmailAddress(string newEmailAddress);
	void SetAge(int SuperNaturalist_NewAge);
	void SetDaysToCompleteCourse(int Days[]);
	
	virtual void Print() = 0;   // D.2.D ( virtual print() to print specific student data) 
	virtual Degree GetDegreeProgram() = 0; // D.2.F (virtual getDegreeProgram()) 



};

