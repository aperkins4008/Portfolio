/*-------------------------------------------------------------------------------------------------------*/
/*                                          Requirement D.2                                              */
/*-------------------------------------------------------------------------------------------------------*/
#pragma once
#include "student.h"
#include <iostream>
#include <string>
using namespace std;


// These functions call the appropriate accessors and mutators


	/// Change to "get" for accessor revision
Student::Student(string NewStudentID, string NewFirstName, string NewLastName,
	string NewEmailAddress, int NewSuperNaturalist_NewAge, int* NewDays) {
	DaysToCompleteCourse = NewDays;
	StudentID = NewStudentID;
	FirstName = NewFirstName;
	LastName = NewLastName;
	EmailAddress = NewEmailAddress;
	Age = NewSuperNaturalist_NewAge;
}


Student :: ~Student() {

}

string Student::GetStudentID() {
	return StudentID;
}

string Student::GetFirstName() {
	return FirstName;
}

string Student::GetLastName() {
	return LastName;
}

string Student::GetEmailAddress() {
	return EmailAddress;
}


int Student::GetAge() {
	return Age;
}

int* Student::GetDaysToCompleteCourse(int NewDays[]) {
	return DaysToCompleteCourse;
}



// Mutators


void Student::SetStudentID(string NewStudentID) {
	StudentID = NewStudentID;
}

void Student::SetFirstName(string NewFirstName) {
	FirstName = NewFirstName;
}

void Student::SetLastName(string NewLastName) {
	LastName = NewLastName;
}

void Student::SetEmailAddress(string newEmailAddress) {
	EmailAddress = newEmailAddress;
}

void Student::SetAge(int SuperNaturalist_NewAge) {
	Age = SuperNaturalist_NewAge;
}

void Student::SetDaysToCompleteCourse(int Days[]) {
	DaysToCompleteCourse = Days;
}