/*
 * ErrorValue.h: interface for the CErrorValue class.
 * Copyright (c) 1996-2000 Erwin Coumans <coockie@acm.org>
 *
 * Permission to use, copy, modify, distribute and sell this software
 * and its documentation for any purpose is hereby granted without fee,
 * provided that the above copyright notice appear in all copies and
 * that both that copyright notice and this permission notice appear
 * in supporting documentation.  Erwin Coumans makes no
 * representations about the suitability of this software for any
 * purpose.  It is provided "as is" without express or implied warranty.
 *
 */

/** \file ErrorValue.h
 *  \ingroup expressions
 */

#ifndef __ERRORVALUE_H__
#define __ERRORVALUE_H__

#include "Value.h"

class CErrorValue : public CPropValue  
{

public:
	virtual const STR_String & GetText();
	virtual double GetNumber();
	CErrorValue();
	CErrorValue(const char *errmsg);
	virtual ~CErrorValue();
	virtual CValue* Calc(VALUE_OPERATOR op, CValue* val);
	virtual CValue* CalcFinal(VALUE_DATA_TYPE dtype, VALUE_OPERATOR op, CValue *val);
	virtual CValue* GetReplica();

private:
	STR_String m_strErrorText;


#ifdef WITH_CXX_GUARDEDALLOC
	MEM_CXX_CLASS_ALLOC_FUNCS("GE:CErrorValue")
#endif
};

#endif  /* __ERRORVALUE_H__ */
