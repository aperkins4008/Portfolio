/*-------------------------------------------------------------------------------------------------------*/
/*                                          Requirement D                                                */
/*-------------------------------------------------------------------------------------------------------*/
#define RosterCapacity 100
#include "roster.h"
#include "securityStudent.h"
#include "networkStudent.h"
#include "softwareStudent.h"
#include <sstream>
#include <iostream>
#include <string>
#include <array>
using namespace std;


// Constructor call from D.2.C

Roster::Roster() {
	countStudent = 0;
	classRosterArray = new Student * [RosterCapacity];
}

// Destructor call from D.2.E

Roster::~Roster() {
	delete classRosterArray;
}
/*-------------------------------------------------------------------------------------------------------*/
/*                                          Requirement E                                                */
/*-------------------------------------------------------------------------------------------------------*/

// E.3.A (Creates add function)
void Roster::addStudent(string StudentID, string FirstName, string LastName, string EmailAddress, int Age,
	                    int CourseDays1, int CourseDays2, int CourseDays3, Degree DegreeProgram) {

	int* CourseDays = new int[3];
	CourseDays[0] = CourseDays1;
	CourseDays[1] = CourseDays2;
	CourseDays[2] = CourseDays3;
	Student* student = NULL;
	
	
	switch (DegreeProgram) {

	case NETWORKING:
		student = new NtwkStudent(StudentID, FirstName, LastName, EmailAddress, Age, CourseDays);
		break;
	case SOFTWARE:
		student = new SftwrStudent(StudentID, FirstName, LastName, EmailAddress, Age, CourseDays);
		break;
	case SECURITY:
		student = new ScrtyStudent(StudentID, FirstName, LastName, EmailAddress, Age, CourseDays);
		break;

	}
	// E.2.A/B (Applied pointer operations when parsing each set of data)
	if (student != NULL) {
		if (countStudent < RosterCapacity) {
			classRosterArray[countStudent] = student;
			countStudent++;
		}
	}
}

// E.3.B (Creates remove function)
void Roster::removeStudent(string StudentID) {
	bool studentFound = false;
	for (int i = 0; i < countStudent; i++) {
		if (classRosterArray[i] -> GetStudentID().compare(StudentID) == 0) { // Using Pointer
			studentFound = true;
			for (int j = i; j < countStudent; j++) {
				 classRosterArray[j] = classRosterArray[j + 1];
			}
			countStudent--;
		}
		else if (studentFound == true) {

		}
	}
	if (studentFound == true) {
		cout << "Student ID " << StudentID << " doesn't exist." << endl;
	}
}

// E.3.C (Creates print function)
void Roster::printAll() {
	for (int i = 0; i < countStudent; i++) {
		 classRosterArray[i] -> Print(); // Using Pointer
	}
	cout << endl;
}

// E.3.D (Creates printaveragecoursedays function)
void Roster::printAverageCourseDays(string StudentID) {
	int AverageCourseDays = 0;
	int sumCourseDayss = 0;
	const int NUM_Courses = 3;
	
		for (int i = 0; i < countStudent; i++) {
		if (classRosterArray[i] -> GetStudentID().compare(StudentID) == 0) { // Using Pointer
			int* DaysOfCourses = classRosterArray[i] -> DaysToCompleteCourse; // Using Pointer
			for (int j = 0; j < NUM_Courses; j++) {
				sumCourseDayss += DaysOfCourses[j];
			}
			AverageCourseDays = sumCourseDayss / NUM_Courses;
			cout << classRosterArray[i] -> GetFirstName() << " " << classRosterArray[i] -> GetLastName() // Using Pointer
				<< "'s average days in courses: " << AverageCourseDays << endl;
		}
	}
	cout << endl;
}

// E.3.E (Creates invalid email(s) function)
void Roster::printInvalidEmails() {
	for (int i = 0; i < countStudent; i++) {
		string EmailAddress = classRosterArray[i] -> GetEmailAddress(); // Using Pointer
		if (EmailAddress.find('@') == string::npos || EmailAddress.find('.') == string::npos ||
			EmailAddress.find(' ') != string::npos) {
			cout << "Email " << EmailAddress << " is invalid for student " << classRosterArray[i] -> GetFirstName(); // Using Pointer
			cout << " " << classRosterArray[i] -> GetLastName() << ". Admin please correct." << endl; // Using Pointer
		}
	}
	cout << endl;
}

// E.3.F (Creates degree by program function, specifically enum-ed)
void Roster::printByDegreeProgram(Degree DegreeProgram) {
	for (int i = 0; i < countStudent; i++) {
		if (classRosterArray[i] -> GetDegreeProgram() == DegreeProgram) { // Using Pointer
			classRosterArray[i] -> Print(); // Using Pointer
		}
	}
	cout << endl;
}




/*-------------------------------------------------------------------------------------------------------*/
/*                                   Requirement A & F                                                   */
/*-------------------------------------------------------------------------------------------------------*/
int main() {

	// F.1 (Creates demographic and class information)
	cout << "Class: SCRIPTING AND PROGRAMMING APPLICATIONS — C867" << endl;
	cout << "Programming Language: C++" << endl;
	cout << "Student ID: 000591708" << endl;
	cout << "Name: Carl (Andrew) Perkins" << endl << endl;


	// F.2 (Creates instance of classRoster)

	Roster* classRoster = new Roster;

	const string StudentData[] = { "A1,John,Smith,John1989@gm ail.com,20,30,35,40,SECURITY",
								  "A2,Suzan,Erickson,Erickson_1990@gmailcom,19,50,30,40,NETWORK",
								  "A3,Jack,Napoli,The_lawyer99yahoo.com,19,20,40,33,SOFTWARE",
								  "A4,Erin,Black,Erin.black@comcast.net,22,50,58,40,SECURITY",
								  "A5,Carl (Andrew),Perkins,cperk26@wgu.edu,32,45,22,36,SOFTWARE",
		// (A.) Modified the StudentData table above ^^^ to include my personal information as the last item
								  "" };

	// F.3 (Adds each student to the class roster)

	for (int i = 0; !StudentData[i].empty(); i++) {
		istringstream data(StudentData[i]);
		string ID, FirstName, LastName, Email, AgeString, Day1String, Day2String, Day3String, ProgramString;
		getline(data, ID, ',');
		getline(data, FirstName, ',');
		getline(data, LastName, ',');
		getline(data, Email, ',');
		getline(data, AgeString, ',');
		getline(data, Day1String, ',');
		getline(data, Day2String, ',');
		getline(data, Day3String, ',');
		getline(data, ProgramString, ',');
		
		int Age, Day1, Day2, Day3;
		Age = stoi(AgeString);
		Day1 = stoi(Day1String);
		Day2 = stoi(Day2String);
		Day3 = stoi(Day3String);
		
		Degree Program;
		Program = OutPut_StringAsDegree.at(ProgramString);
		classRoster -> addStudent(ID, FirstName, LastName, Email, Age, Day1, Day2, Day3, Program); // Using Pointer
	}

	
	// F.4 (Converted pseudo code)
	classRoster -> printAll(); // Using Pointer
	classRoster -> printInvalidEmails(); // Using Pointer
	//loops through classRosterArray and for each element:
	classRoster -> printAverageCourseDays("A5"); // Using Pointer
	classRoster -> printByDegreeProgram(SOFTWARE); // Using Pointer
	classRoster -> removeStudent("A3"); // Using Pointer
	classRoster -> removeStudent("A3"); // Using Pointer
	
	// F.5 (Calls destructor  to wipe out roster)
	delete classRoster;
}