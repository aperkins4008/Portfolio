/*-------------------------------------------------------------------------------------------------------*/
/*                                        Requirement D.3                                                */
/*-------------------------------------------------------------------------------------------------------*/
#pragma once
#define SecurityHeader

#include "student.h"
#include "degree.h"

class ScrtyStudent : public Student {

public:
	void Print();
	Degree GetDegreeProgram(); // Contains enumerated type
	ScrtyStudent(string NewStudentID, string NewFirstName, string NewLastName,
		string NewEmailAddress, int NewSuperNaturalist_NewAge, int* NewDays);
   ~ScrtyStudent();

};




