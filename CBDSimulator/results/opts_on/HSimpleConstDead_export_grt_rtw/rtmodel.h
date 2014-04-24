/*
 *  rtmodel.h:
 *
 * Code generation for model "HSimpleConstDead_export".
 *
 * Model version              : 1.5
 * Simulink Coder version : 8.2 (R2012a) 29-Dec-2011
 * C source code generated on : Thu Apr 24 13:58:27 2014
 *
 * Target selection: grt.tlc
 * Note: GRT includes extra infrastructure and instrumentation for prototyping
 * Embedded hardware selection: 32-bit Generic
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */
#ifndef RTW_HEADER_rtmodel_h_
#define RTW_HEADER_rtmodel_h_

/*
 *  Includes the appropriate headers when we are using rtModel
 */
#include "HSimpleConstDead_export.h"
#define GRTINTERFACE                   0
#define ONESTEPFCN                     1
#if MAT_FILE == 1
# define rt_StartDataLogging(S,T,U,V)  NULL
# define rt_UpdateTXYLogVars(S,T)      NULL
# define rt_UpdateSigLogVars(S,T)      ;                         /* No op */
#endif

#if defined(EXT_MODE)
# define rtExtModeUploadCheckTrigger(S)                          /* No op */
# define rtExtModeUpload(S,T)                                    /* No op */
#endif
#endif                                 /* RTW_HEADER_rtmodel_h_ */
