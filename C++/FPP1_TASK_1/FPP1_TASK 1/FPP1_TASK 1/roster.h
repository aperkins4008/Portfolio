/*-------------------------------------------------------------------------------------------------------*/
/*                                          Requirement E                                                */
/*-------------------------------------------------------------------------------------------------------*/
#pragma once
#define RosterHeader

#include "student.h"
#include "degree.h"
#include <string>
using namespace std;


class Roster {

public:
	void addStudent(string StudentID, string FirstName, string LastName, string EmailAddress, int Age,
		            int CourseDays1, int CourseDays2, int CourseDays3, Degree DegreeProgram);
	void removeStudent(string StudentID);
	void printAll();
	void printAverageCourseDays(string StudentID);
	void printInvalidEmails();
	void printByDegreeProgram(Degree DegreeProgram);
	Roster();
   ~Roster();

private:
	Student** classRosterArray;  // E.1 (hold the data provided in the studentData table)
	int countStudent;
};



