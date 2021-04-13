/*-------------------------------------------------------------------------------------------------------*/
/*                                        Requirement D.3                                                */
/*-------------------------------------------------------------------------------------------------------*/
#pragma once
#define NetworkHeader

#include "networkStudent.h"
#include "student.h"
#include <iostream>
#include <string>
using namespace std;



	class NtwkStudent : public Student {

	public:
		void Print();
		Degree GetDegreeProgram(); // Contains enumerated type
		NtwkStudent(string NewStudentID, string NewFirstName, string NewLastName,
			string NewEmailAddress, int NewSuperNaturalist_NewAge, int* NewDays);
		~NtwkStudent();

};

