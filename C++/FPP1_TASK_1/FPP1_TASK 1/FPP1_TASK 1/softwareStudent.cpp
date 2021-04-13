/*-------------------------------------------------------------------------------------------------------*/
/*                                          Requirement D.3                                              */
/*-------------------------------------------------------------------------------------------------------*/
#include <iostream>
#include <string>

using namespace std;

#include "softwareStudent.h"


// Adjusted code to get string below by accessors previous requirements


void SftwrStudent::Print() {
	cout << "Student ID: " << GetStudentID() << ", ";
	cout << "Name: " << GetFirstName() << " " << GetLastName() << ", ";
	cout << "Email: " << GetEmailAddress() << ", ";
	cout << "Age: " << GetAge() << ", ";
	cout << "Days left in Course: ";
		for (int i = 0; i < Courses; i++) {
		cout << DaysToCompleteCourse[i] << ", ";
	}
	cout << "Degree: Software" << endl;
}

Degree SftwrStudent::GetDegreeProgram() {
	return SOFTWARE;
}

SftwrStudent::SftwrStudent(string NewStudentID, string NewFirstName, string NewLastName,
	string NewEmailAddress, int NewSuperNaturalist_NewAge, int* NewDays) :
	Student(NewStudentID, NewFirstName, NewLastName, NewEmailAddress, NewSuperNaturalist_NewAge,
		NewDays) {

}


