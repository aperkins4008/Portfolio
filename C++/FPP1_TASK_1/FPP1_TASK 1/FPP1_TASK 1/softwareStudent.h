/*-------------------------------------------------------------------------------------------------------*/
/*                                        Requirement D.3                                                */
/*-------------------------------------------------------------------------------------------------------*/
#pragma once
#define SoftwareHeader

#include "student.h"

class SftwrStudent : public Student {

public:
	void Print();
	Degree GetDegreeProgram(); // Contains enumerated type
	SftwrStudent(string NewStudentID, string NewFirstName, string NewLastName,
		string NewEmailAddress, int NewSuperNaturalist_NewAge, int* NewDays);
	~SftwrStudent();

};

