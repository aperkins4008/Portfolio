/*-------------------------------------------------------------------------------------------------------*/
/*                                          Requirement D.3                                              */
/*-------------------------------------------------------------------------------------------------------*/
#include "networkStudent.h"
#include <iostream>
#include <string>
using namespace std;



// Adjusted code to get string below by accessors previous requirements

void NtwkStudent::Print() {
	cout << "Student ID: " << GetStudentID() << ", ";
	cout << "Name: " << GetFirstName() << " " << GetLastName() << ", ";
	cout << "Email: " << GetEmailAddress() << ", ";
	cout << "Age: " << GetAge() << ", ";
	cout << "Days left in Course: ";
	for (int i = 0; i < Courses; i++) {
		cout << DaysToCompleteCourse[i] << ", ";
	}
	cout << "Degree: Networking" << endl;

}

Degree NtwkStudent::GetDegreeProgram() {
	return NETWORKING;
}

NtwkStudent::NtwkStudent(string NewStudentID, string NewFirstName, string NewLastName,
	string NewEmailAddress, int NewSuperNaturalist_NewAge, int* NewtDays) :
	Student(NewStudentID, NewFirstName, NewLastName, NewEmailAddress, NewSuperNaturalist_NewAge,
		NewtDays) {

}