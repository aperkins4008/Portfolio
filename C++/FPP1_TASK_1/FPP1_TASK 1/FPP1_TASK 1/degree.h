/*-------------------------------------------------------------------------------------------------------*/
/*                                          Requirement C                                                */
/*-------------------------------------------------------------------------------------------------------*/
#pragma once
#define DegreeHeader

#include <string>
#include <map>
using namespace std;


enum Degree { SECURITY, NETWORKING, SOFTWARE };
const map<string, Degree> OutPut_StringAsDegree {
		{"SECURITY",   SECURITY},
		{"NETWORK", NETWORKING},
		{"SOFTWARE",   SOFTWARE}
};
