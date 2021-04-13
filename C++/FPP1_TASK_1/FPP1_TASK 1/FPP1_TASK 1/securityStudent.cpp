/*-------------------------------------------------------------------------------------------------------*/
/*                                          Requirement D.3                                              */
/*-------------------------------------------------------------------------------------------------------*/
#include <iostream>
#include <string>

using namespace std;

#include "securityStudent.h"

// Adjusted code to get string below by accessors previous requirements


void ScrtyStudent::Print() {
	cout << "Student ID: " << GetStudentID() << ", ";
	cout << "Name: " << GetFirstName() << " " << GetLastName() << ", ";
	cout << "Email: " << GetEmailAddress() << ", ";
	cout << "Age: " << GetAge() << ", ";
	cout << "Days left in Course: ";
	for (int i = 0; i < Courses; i++) {
		cout << DaysToCompleteCourse[i] << ", ";
	}
	cout << "Degree: Security" << endl;
}

Degree ScrtyStudent::GetDegreeProgram() {
	return SECURITY;
}

ScrtyStudent::ScrtyStudent(string NewStudentID, string NewFirstName, string NewLastName,
	string NewEmailAddress, int NewSuperNaturalist_NewAge, int* NewDays) :
	Student(NewStudentID, NewFirstName, NewLastName, NewEmailAddress, NewSuperNaturalist_NewAge,
		NewDays) {

}